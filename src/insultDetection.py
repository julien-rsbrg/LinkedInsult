from src.data import dico_insultes


def is_insult(word):
    """
    Évalue si le mot word est une insulte.
    MVP1: compare ce mots aux listes d'insultes rentrées à la main

    Args:
        word: mot à analyser (str)
    
    Returns:
        True si le mot est une insulte
        False sinon
    """
    # MVP1: comparaison mot à mot
    return word in dico_insultes