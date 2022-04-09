import sys
from src.findTweet import find_tweet_with
from main import twitter_setup

from filepath_perso import filepath


# Setup de l'API Twitter

sys.path.append(filepath) # Adds path to find credentials.py

from credentials import CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET
API_credentials = CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET

connexion = twitter_setup(API_credentials)



# Tests


def test_find_tweet_with():

    # Le tweet correspond à la recherche
    assert 'motherfucker' in find_tweet_with('motherfucker', connexion).text