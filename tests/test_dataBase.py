from src.dataBase import add_insulter, init_db, remove_insulter, update_profile


def test_init_db():

	# La db est crée si elle n'existe pas
	assert init_db() == (True, None)


def test_add_new_insulter():

	# Un nouvel utilisateur peut être ajouté:
	assert add_insulter('jeanmidu92', 'Jean-mi') == (True, None)


def test_add_existing_insulter():

	# Un utilisateur déjà listé ne peut être ajouté une seconde fois:
	assert add_insulter('jeanmidu92', 'Jean-mi')[0] == False


def test_update_existing_profile():

	# Le profil d'un utilisateur peut être mis à jour:
	assert update_profile('jeanmidu92', 5, 12, 20, 2, 4, 5, 2, 0, 0, 1) == (True, None)


def test_remove_insulter():

	# Un utilisateur listé peut être supprimé:
	assert remove_insulter('jeanmidu92') == (True, None)