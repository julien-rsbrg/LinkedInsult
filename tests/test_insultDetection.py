from src.insultDetection import is_insult
from src.data import dico_insultes


def test_is_insult():
    try:
        assert is_insult("bitch") == True
        assert is_insult("Macron") == False
    except Exception as exc:
        print("exception of type", type(exc).__name__)
        print("message", exc)
