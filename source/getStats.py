import sqlite3



def insult_classification(ID):
    """
    Renvoie les proportions de chaque catégorie d'insulte dans les tweets de ID
    sous forme de dictionnaire.

    Args:
        ID: identifiant Twitter (str)
    
    Returns:
        freq: dictionnaire python {'cat1':freq, 'cat2':..., ...}
            Attention: les valeurs sont entre 0 et 1
    """

    # connexion à la base de donnée
    conn = sqlite3.connect('db_insulter.db')
    cursor = conn.cursor()

    # requête SQL
    cursor.execute("""SELECT nb_insultes_total, toxic, severe_toxic, obscene, threat, insult, identity_hate FROM Insulteurs WHERE ID=?""",(ID,))
    nb_insultes_total, toxic, severe_toxic, obscene, threat, insult, identity_hate = cursor.fetchone()
    cursor.close()
    conn.close()
    
    # on créé le dictionnaire avec les valeurs récupérées dans la base de donnée
    dico = {
        'toxic': toxic/nb_insultes_total,
        'severe_toxic': severe_toxic/nb_insultes_total,
        'obscene': obscene/nb_insultes_total,
        'threat': threat/nb_insultes_total,
        'insult': insult/nb_insultes_total,
        'identity_hate': identity_hate/nb_insultes_total
    }

    return dico
    




def insult_rate(ID):
    """
    Renvoie la fréquence de tweets insultants de ID.

    Args:
        ID: identifiant Twitter (str)
    
    Returns:
        freq: fréquence (entre 0 et 1) des tweets insultants (float)
    """
    # connexion à la base de donnée
    conn = sqlite3.connect('db_insulter.db')
    cursor = conn.cursor()

    # requête SQL 
    cursor.execute("""SELECT nb_tweets_total, nb_tweets_insultants FROM Insulteurs WHERE ID=?""",(ID,))
    nb_tweets_total, nb_tweets_insultants = cursor.fetchone()
    cursor.close()
    conn.close()
    return nb_tweets_insultants/nb_tweets_total





def profile_type(ID):
    """
    Renvoie le nom de la catégorie la plus fréquente.

    Args:
        ID: identifiant Twitter (str)
    
    Returns:
        cat_max: catégorie de plus haute fréquence (str)
    """
    # on utilise le dictionnaire des insultes du tweet donné par la fonction insult_classification
    dico = insult_classification(ID)
    max = 0
    cat_max = None
    for key in dico:
        # if key[1] == 1:
        if dico[key] > max:
            max = dico[key]
            cat_max = key
    return cat_max




def get_name(ID):
    """
    Permet de trouver le nom à partir de la base de donnée

    Args:
        ID: identifiant Twitter (str)
    
    Return:
        name: le nom du profil Twitter (str)
    """
    # connexion à la base de donnée
    conn = sqlite3.connect('db_insulter.db')
    cursor = conn.cursor()

    # requête SQL 
    cursor.execute("""SELECT name FROM Insulteurs WHERE ID=?""",(ID,))
    name = cursor.fetchone()
    cursor.close()
    conn.close()
    return name[0]




def get_insulters():
    """
    Permet d'accéder à l'ensemble des identifiants des insulteurs de la base de donnée

    Args:
        None

    Return:
        insulter_list: la liste des identifiants des insulteurs (list)
    """
    # connexion à la base de donnée
    conn = sqlite3.connect('db_insulter.db')
    cursor = conn.cursor()

    # initialisation de la variable
    # requête SQL 
    cursor.execute("""SELECT ID FROM Insulteurs""")
    insulter_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return [user[0] for user in insulter_list]