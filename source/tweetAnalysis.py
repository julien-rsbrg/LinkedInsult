from src.insultDetection import is_insult
from src.data import dico_insultes, categories

## pour la seconde méthode ##
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from src.IA_supervised_learning.toxic_classifier_generate import df, stop, max_features
from src.IA_supervised_learning.str_info import str_file_save_toxic
from src.IA_supervised_learning.common_functions import load_model, apply_model, preprocess_text


def is_insulting(tweet):
    """
    Détecte si un tweet est insultant.
    MVP1: cherche si un des mots de tweet est une insulte (en utilisant is_insult())

    Args:
        tweet: (status object)

    Returns:
        True si le tweet est insultant
        False sinon
    """

    # MVP1: comparaison mot-à-mot
    for word in tweet.text.split(sep=' '):
        if is_insult(word):
            return True
    return False


def insult_list(tweet):
    """
    Renvoie la liste des insultes présentes dans le tweet.

    Args:
        tweet: (status object)

    Returns:
        list_insults: liste des insultes présentes dans le tweet (list of str)
    """
    list_insults = []

    # MVP1: les insultes sont des mots isolés (et non des groupes de mots)
    for word in tweet.text.split(sep=' '):
        if is_insult(word):
            list_insults.append(word)
    return list_insults


def classify_insults(list_insults):
    """
    Renvoie le nombre d'insultes par catégorie sous forme de dictionnaire.

    Args:
        list_insults: liste des insultes présentes dans le tweet (list of str)

    Returns:
        scores: dictionnaire python {'cat1':score, 'cat2':..., ...}
    """
    # Initialisation du dictionnaire renvoyé
    scores = {}
    for cat in categories:
        scores[cat] = 0

    # Remplissage
    for insult in list_insults:
        scores[dico_insultes[insult][0]] += 1

    return scores


def violence(list_insults):
    """
    Évalue la violence d'une liste d'insultes, ie la somme des scores des insultes de la liste.
    (Plus une insulte est forte, plus son score est élevé)

    Args:
        list_insults: liste d'insultes (list of str)

    Returns:
        violence: somme des scores des insultes de la liste (int)
    """
    violence = 0
    for insult in list_insults:
        violence += dico_insultes[insult][1]

    return violence


##############################################################################################################
########################################### Méthode IA #######################################################
##############################################################################################################

classifier = load_model(str_file_save_toxic)




def analyse_tweets_AI(tweets):
    '''
    Analyse les tweets grâce à une IA de classification
    Les classes utilisées sont celles dans categories (liste issue de src.data)

    Args : 
        tweets : liste de tweets (tweepy.models.ResultSet)

    Returns :
        y_pred : array des prédictions, à chaque tweet est associé une ligne de 
                type liste de longueur 6 remplie de 0 et 1 indiquant l'appartenance 
                à la catégorie de categorie de même indice (np.array [[0,...],[0,]])
    '''
    l_text = []

    N = len(tweets)

    for i in range(N):
        text = tweets[i].text
        # Ajouter le texte au dataset d'entraînement et de test non vectorialisé
        l_text.append([text])
    new_data = pd.DataFrame(data=l_text, columns=['comment_text'])

    preprocess_text(new_data, "comment_text", stop)

    df2 = df.append(new_data)

    X = df2["comment_text"]

    # Vectorialiser
    tf_vec = TfidfVectorizer(
        max_features=max_features, stop_words=stop, min_df=10, max_df=0.7)
    X_vec = tf_vec.fit_transform(X).toarray()

    # Appliquer
    y_pred = apply_model(classifier, X_vec[-N:])
    return y_pred





def is_insulting_AI(tweets):
    """
    Détecte les twwets insultants d'une liste tweets.
    Via IA de classification

    Args:
        tweets: liste de tweets (tweepy.models.ResultSet)

    Returns:
        l : liste de booléen :
                True si le tweet est insultant
                False sinon
    
    Remark : 
        N'est pas utilisée mais le principe compte
    """
    l = []
    y_pred = analyse_tweets_AI(tweets)
    for y_tweet in y_pred:
        l.append(sum(y_tweet)>0)
    return l
