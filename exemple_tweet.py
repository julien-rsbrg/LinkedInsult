##### Ce module sert à avoir un exemple de tweet insultant pour les fonctions tests
##### Il est utilisé dans test_profileAnalysis et test_tweetAnalysis

import sys
import tweepy
from filepath_perso import filepath
from src.findTweet import find_tweet_with
from main import twitter_setup

sys.path.append(filepath) # Adds path to find credentials.py

from credentials import CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET
API_credentials = CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET



connexion = twitter_setup(API_credentials)
tweet = find_tweet_with('bitch AND bastard AND idiot AND fucking', connexion)
print(tweet.text)