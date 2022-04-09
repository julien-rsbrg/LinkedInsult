import tweepy

def stream_until_insult(query):
    global S

    """
    Collecte des tweets en continue selon la requête query jusqu'à trouver un tweet insultant.

    Args:
        query: requête servant à cibler les recherches (str)
            Ex: nom d'utilisateur, mots clés, etc...

    Returns:
        premier tweet insultant correspondant à la requête (status object)
    """
    class textPrinter(tweepy.Stream):

        def on_status(self, status):
            global S
            S=status
            tweepy.Stream.disconnect(self)


# Initialize instance of the subclass
    printer = textPrinter(CONSUMER_KEY, CONSUMER_SECRET,
                       ACCESS_TOKEN, ACCESS_SECRET)


# Filter realtime Tweets by keyword
    printer.filter(track=[query])

    return S





def find_tweet_with(insult, connexion, query=""):
    """
    Trouve un tweet contenant l'insulte insult.

    Args:
        insult: insulte(s) à rechercher (str)
            Ex: "connard" ou "connard idiot imbécile"
        query: éléments optionnels de requêtes supplémentaires (str)

    Returns:
        tweet correspondant à la requête
    """
    tweet = connexion.search_tweets("( " + insult + " ) AND ( " + query +" )",include_entities=True,count=1)

    if len(tweet) > 0: # Vérifie que la liste des tweets récupérés n'est pas vide (donnait lieu à une erreur)
        return tweet[0], True

    else:
        return None, False


def find_tweet_author(screen_name, connexion):
    """
    Trouve un tweet d'un utilisateur de Twitter correspondant à screen_name.

    Args:
        screen_name: identifiant de l'utilisateur (@...)
        connexion: l'api de connexion Twitter

    Returns:
        tweet correspondant à la requête
    """
    tweet = connexion.user_timeline(screen_name=screen_name,include_entities=True,count=1)
    return tweet[0]