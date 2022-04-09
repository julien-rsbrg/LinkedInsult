from src.dataBase import add_insulter, update_profile
from src.findTweet import find_tweet_with, stream_until_insult
from src.profileAnalysis import collect_tweets, find_author
from src.tweetAnalysis import classify_insults, insult_list, is_insulting, violence


def from_twitter_to_database_stream(query):
    """
    Permet de trouver les tweets postés en direct correspondant à un ensemble d'insultes, 
    et à mettre à jour la base de donnée concernant l'insulteur.

    Args :
        query: les insultes à repérer dans les tweets (str)
    
    Returns :
        (True, ID)
    """
    tweet = stream_until_insult(query)
    (ID, name) = find_author(tweet)
    return (add_insulter(ID, name)[0], ID)





def from_twitter_to_database_search(connexion, insult, query=""):
    """
    Permet de trouver les tweets postés durant la semaine précédente correspondant à un ensemble d'insultes, 
    et à mettre à jour la base de donnée concernant l'insulteur.

    Args :
        insult: les insultes à repérer dans les tweets (str)
        query: des ajouts sur le thème pour polariser la recherche (str)
    
    Returns :
        (True,ID)
    """

    tweet = find_tweet_with(insult, connexion, query)[0]
    (ID, name) = find_author(tweet)
    return (add_insulter(ID, name)[0], ID)





def add_to_database(connexion, ID, nb_max=10):
    """
    Mets à jour toutes les informations de ID.

    Args :
        ID: l'identifiant Twitter d'un insulteur
        connexion: api tweeter
        nb_max: nombre maximal de tweets collectés, vaut 10 par défaut (int)

    Returns:
        None
    """
    statuses = collect_tweets(connexion, ID, nb_max) # on récupère les différents tweets de l'insulteur
    
    # on initialise les différentes variables
    name = statuses[0].user.name 
    nb_tweets_total = 0
    nb_tweets_insultants = 0 
    violence_totale = 0 
    nb_insultes_totales = 0
    toxic = 0
    severe_toxic = 0
    obscene = 0
    threat = 0
    insult = 0
    identity_hate = 0
    # on parcoure les différents tweets pour pouvoir mettre à jour les variables
    for status in statuses:
        nb_tweets_total += 1
        
        if is_insulting(status):
            nb_tweets_insultants += 1
            list_insults = insult_list(status)
            scores_tweet = classify_insults(list_insults)
            toxic += scores_tweet['toxic']
            severe_toxic += scores_tweet['severe_toxic']
            obscene += scores_tweet['obscene']
            threat += scores_tweet['threat']
            insult += scores_tweet['insult']
            identity_hate += scores_tweet['identity_hate']
    
    nb_insultes_totales = toxic + severe_toxic + obscene + threat + insult + identity_hate
    
    return update_profile(ID, nb_tweets_insultants, nb_insultes_totales, nb_tweets_total, 
        violence_totale, toxic, severe_toxic, obscene, threat, insult, identity_hate)

        
