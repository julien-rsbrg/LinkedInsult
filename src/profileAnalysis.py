
def find_author(tweet):
    """
    Renvoie l'ID et le nom de l'auteur de tweet.

    Args:
        tweet: (status object)

    Returns:
        (ID, name): ("@screen_name, name) (str, str)
    """
    return tweet.user.screen_name, tweet.user.name


def collect_tweets(connexion, ID, nb_max):
    """
    Renvoie une liste de tweets de l'utilisateur ID.

    Args:
        connexion : api tweeter
        ID: identifiant Twitter (str)
        nb_max: nombre maximal de tweets collectés (int)

    Returns:
        tweets: liste de tweets de l'utilisateur (tweepy.models.ResultSet)
    """
    statuses = connexion.user_timeline(screen_name=ID, count=nb_max)
    return statuses
