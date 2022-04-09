from src.dataBase import add_insulter, init_db, remove_insulter, update_profile
from src.getStats import get_name, insult_classification, insult_rate, profile_type



def test_insult_classification():

    init_db()
    add_insulter('jeanmidu92', 'Jean-mi')
    update_profile('jeanmidu92', 5, 12, 20, 2, 4, 5, 2, 0, 0, 1)

    # Les fréquences d'apparition des insultes sont correctement évaluées
    res = insult_classification('jeanmidu92')
    expected = {'toxic':int(100*4/12), 'severe_toxic': int(100*5/12), 'obscene': int(100*2/12), 'threat': int(0), 'insult': 0, 'identity_hate': int(100*1/12)}
    for cat in res.keys():
        assert int(res[cat]*100) == expected[cat] # On compare en pourcentage car 2 flottants ne sont jamais égaux

    remove_insulter('jeanmidu92')



def test_insult_rate():

    init_db()
    add_insulter('jeanmidu92', 'Jean-mi')
    update_profile('jeanmidu92', 5, 12, 20, 2, 4, 5, 2, 0, 0, 1)

    # Le taux de tweets insultants est correctement évalué
    assert int(100*insult_rate('jeanmidu92')) == int(100*5/20)

    remove_insulter('jeanmidu92')



def test_profile_type():

    init_db()
    add_insulter('jeanmidu92', 'Jean-mi')
    update_profile('jeanmidu92', 5, 12, 20, 2, 4, 5, 2, 0, 0, 1)
    
    # Le type de profil est correctement évalué
    assert profile_type('jeanmidu92') == 'severe_toxic'

    remove_insulter('jeanmidu92')



def test_get_name():

    init_db()
    add_insulter('jeanmidu92', 'Jean-mi')
    update_profile('jeanmidu92', 5, 12, 20, 2, 4, 5, 2, 0, 0, 1)

    # Le nom du profil est bien retrouvé à partir de son identifiant
    assert get_name('jeanmidu92') == 'Jean-mi'

    remove_insulter('jeanmidu92')