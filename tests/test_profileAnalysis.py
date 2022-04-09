from src.profileAnalysis import find_author, collect_tweets
from exemple_tweet import tweet   
### /!\ tweet est un exemple de tweet sauvegardé en local. Il est nécessaire d'exécuter exemple_tweet.py pour lancer les tests


def test_find_author():
    try:
        assert find_author() == ("", "")
    except Exception as exc:
        print("exception of type", type(exc).__name__)
        print("message", exc)


def test_collect_tweets():
    try:
        assert type(collect_tweets(tweet)) == list
    except Exception as exc:
        print("exception of type", type(exc).__name__)
        print("message", exc)
