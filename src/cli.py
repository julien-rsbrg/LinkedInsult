import random
import sqlite3
from src.from_twitter_to_database import add_to_database, from_twitter_to_database_search, from_twitter_to_database_stream
from src.getStats import insult_classification, insult_rate, profile_type, get_insulters


def init_interface(connexion):
    """
    Permet d'initier l'interface terminal

    Args:
        None
    
    Returns:
        ID: l'identifiant ou une liste d'identifiants Twitter d'insulteurs (@...) (str)
    """

    # message d'accueil
    print("\n")
    print("Bienvenue dans LinkedInsultes. Ici vous pouvez trouver des informations") 
    print("sur les plus grands insulteurs de Twitter.")
    print("")
    print("Vous pouvez arrêter le programme à tout moment en appuyant sur 'Ctrl+C' sur Windows ou 'Cmd+C' sur Mac \n \n \n")
    
    # on fait une boucle pour pouvoir revenir au début en cas d'erreur 
    boucle = True # la variable boucle permet de revenir au début s'il y a une erreur de saisie
    
    while boucle == True:
        answer = input("Voulez vous le profil d'un utilisateur en particulier ? (oui/non) ")
        print("")

        if answer == 'non':
            print("Vous pouvez rechercher des utilisateurs par insultes ou au hasard.")
            demande = input ("Faire une recherche par : insultes ou hasard ? ")
            print("")
            
            if demande == 'insultes':
                boucle = False
                insult = input("Rentrez une ou plusieurs insultes : ")
                print("")
                print("Rentrez des mots-clés pouvant aiguiller la recherche")
                query = input("(vous pouvez ne rien mettre en appuyant sur Entrée) : ")
                print("")
                ID = get_insulter_by_query(connexion, insult, query) 
                display_interface(ID, connexion)

            if demande == 'hasard':
                boucle = False
                get_random_insulter()
                ID = get_random_insulter()
                display_interface(ID, connexion)
            
            else :
                print("Veuillez rentrer les mots 'insultes' ou 'hasard'")
                print("")
                boucle = True
            

        if answer == 'oui':
            print("Connaissez vous l'ID de la personne recherchée ? ")
            ID_or_not = input("La recherche sera plus précise si vous donnez l'ID de la personne (@...) : ")
            print("")
            
            if ID_or_not == 'oui':
                boucle = False
                ID = input("Rentrez l'arobase de la personne recherchée : ")
                print("")
                display_interface(ID, connexion)
            
            if ID_or_not == 'non':
                boucle = False
                name = input("Rentrez le nom de la personne recherchée : ")
                print("")
                ID = get_specific_insulter_by_name(name)
                display_interface(ID, connexion)
            
            else :
                print("Veuillez répondre par 'oui' ou par 'non'")
                print("")
                boucle = True
    
        else:
            print("Répondez par 'oui' ou par 'non'")
            print("")
    





def display_interface(ID, connexion):
    """
    Permet d'afficher les données spécifiques d'une personne associée 
    à ID dans la base de donnée.

    Args: 
        ID: identifiant Twitter (@...) (str)
    
    Returns:
        None
    """

    # on affiche les données en utilisant les fonctions du module getStats (insult_rate, profile_type et insult_classification)
    print("Vous avez choisi de regarder le profil de " + ID)
    print("\n")
    freq = insult_rate(ID)
    taux = freq*100
    print("Le taux d'insultes de " + ID + " est de " + str(taux) + "%")
    print("")
    cat_max = profile_type(ID)
    print("Son profil insulteur est '" + str(cat_max) + "'")
    print("")
    plus = input("Voir plus ? (oui ou non) ")
    print("")
    if plus == 'oui':
        frequence = insult_classification(ID)
        print("Voici le profil complet de " + ID + " : ")
        print(frequence)
    print("")
    fin = input("Voulez vous revenir au début ou quitter le programme ? (revenir ou quitter) ")
    
    if fin == 'quitter':
        print("Merci de votre visite, à bientôt ;)")
        return None
    
    if fin == 'revenir':
        init_interface(connexion)
    
    else:
        print("En écrivant n'importe quoi vous avez décidé de quitter le programme, à bientôt ;)")
        return None





def get_random_insulter():
    """
    Recherche un insulteur au hasard dans la base de donnée.

    Args:
        None

    Returns:
        ID: identifiant Twitter (@...) (str)
    """
    insulter_list = get_insulters()
    length = len(insulter_list)
    return insulter_list[random.randint(0, length - 1)]





def get_specific_insulter_by_name(name):
    """
    Recherche une personne dans la base de donnée à partir d'un pseudo spécifique 
    s'il correspond à un insulteur.

    Args:
        score: le pseudo d'un insulteur (str)
    
    Returns:
        liste_ID: liste des identifiants Twitter (@...) (str)
    """
    # connexion à la base de donnée
    conn = sqlite3.connect('db_insulter.db')
    cursor = conn.cursor()

    # commande SQL
    cursor.execute("""SELECT ID FROM Insulteurs WHERE name=?""", (name,))
    ID = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return ID



def get_insulter_by_query(connexion, insult, query):
    """
    Permet de lancer un stream ou une recherche sur des tweets déjà postés 
    à partir de certaines insultes, et renvoie le nom de l'insulteur.

    Args:
        insult: une ou plusieurs insultes (str)
        query: un ensemble de requêtes pouvant aiguiller la recherch (str) 
    
    Returns:
        ID: l'identifiant Twitter de l'insulteur (@...) (str)
    """
    print("Voulez-vous lancer une recherche sur des tweets postés en direct ou")
    print("sur des tweets postés la semaine passée ?")
    Stream_or_not = input("Veuillez rentrer 'direct' ou 'existant' : ")
    
    # on utilise les fonctions du module from_twitter_to_database (stream et search) 
    if Stream_or_not == "direct":
        (res, ID) = from_twitter_to_database_stream(insult)
        add_to_database(connexion, ID, nb_max=10)

    if Stream_or_not == "existant":
        (res, ID) = from_twitter_to_database_search(connexion, insult, query)
        add_to_database(connexion, ID, nb_max=10)
    
    return ID

