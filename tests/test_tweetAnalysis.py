from src.tweetAnalysis import classify_insults, insult_list, is_insulting, violence
from exemple_tweet import tweet
### /!\ tweet est un exemple de tweet sauvegardé en local. Il est nécessaire d'exécuter exemple_tweet.py pour lancer les tests

def test_is_insulting():
    assert is_insulting(tweet)


def test_insult_list():
    assert insult_list(tweet) == ['fucking','bastard', 'idiot', 'bitch']


def test_classify_insult():

    # Les insultes sont bien classées
    assert classify_insults(['idiot', 'bastard', 'coward']) == {'severe_toxic': 1, 'obscene': 0, 'threat': 0, 'identity_hate': 0, 'toxic': 1, 'insult': 1}


def test_violence():

    # La violence est bien évaluée
    assert violence(['idiot', 'bastard', 'coward']) == 19