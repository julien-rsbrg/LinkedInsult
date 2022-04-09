import sqlite3


def init_db():
    """
    Crée la database stockant les insulteurs si elle n'existe pas déjà.
    La db contient les colonnes:
        ID (@screen_name), name, nb_tweets_total, nb_tweets_insultants,
        violence_moyenne, nb_insultes_total, cat1, cat2, ...

    Returns:
        (True, None) si la db est créée
        (False, Error) sinon
    """
    print("Création de la database...")

    try:
        conn = sqlite3.connect('db_insulter.db')
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Insulteurs (
        "ID" TEXT PRIMARY KEY,
        "name" TEXT,
        "nb_tweets_total" INTEGER,
        "nb_tweets_insultants" INTEGER,
        "violence_moyenne" FLOAT,
        "nb_insultes_total" INTEGER,
        "toxic" INTEGER,
        "severe_toxic" INTEGER,
        "obscene" INTEGER,
        "threat"	INTEGER,
        "insult" INTEGER,
        "identity_hate" INTEGER
        )
        """)

    except sqlite3.Error as error:
        conn.rollback()
        # Return False to indicate that something went wrong.
        print("Une erreur s'est produite lors de la création...")
        return (False, error)

    print("La database a bien été créée ou l'était déjà.")
    conn.commit()
    return (True, None)



def add_insulter(ID, name):
    """
    Ajoute l'insulteur name d'identifiant (@...) ID à la database s'il n'y est pas déjà.
    Les colonnes autres que ID et name sont null

    Args:
        ID: identifiant Twitter (@...) (str)
        name: pseudo du compte associé à ID (str)

    Returns:
        (True, None) s'il est ajouté
        (False, Error) sinon
    """
    conn = sqlite3.connect('db_insulter.db')
    cur = conn.cursor()
    print("Connexion réussie à SQLite (add_insulter)")

    try:
        sql = "INSERT INTO Insulteurs (ID, name, nb_tweets_insultants, nb_insultes_total, nb_tweets_total,  violence_moyenne, toxic, severe_toxic, obscene, threat, insult, identity_hate ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        value = (ID, name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        cur.execute(sql, value)
        
    except sqlite3.Error as error:
        conn.rollback()
        cur.close()
        conn.close()
        return (False, error)
    
    conn.commit()
    print("Enregistrement inséré avec succès dans la table Insulteur")
    cur.close()
    conn.close()
    return (True, None)



def update_profile(ID, nb_tweets_insultants, nb_insultes_total, nb_tweets_total,  violence_totale, toxic, severe_toxic, obscene, threat, insult, identity_hate):
    """
    Rentre dans la database les résultats de l'analyse du profil ID:
        nb_tweets_total
        nb_tweets_insultants
        violence_totale
        nb_insultes_total
        cat1
        cat2
        ...

    Args:
        ID: identifiant (screen_name) Twitter (str)
        name : name Twitter (str)
        nb_tweets_total: nombre de tweets dans l'échantillon (int)
        nb_tweets_insultants: nombre de tweets insultants dans l'échantillon (int)
        violence_totale: violence cumulée de toute les insultes (int)
        scores: dictionnaire python {'cat1':nb_insultes_cat1, 'cat2':..., ...}

    Returns:
        (True, None) si l'opération est effectuée
        (False, Error) en cas d'erreur
    """
    conn = sqlite3.connect('db_insulter.db')
    cur = conn.cursor()

    try:
        cur.execute("""UPDATE Insulteurs
                    SET (nb_tweets_insultants, nb_insultes_total, nb_tweets_total, violence_moyenne, toxic, severe_toxic, obscene, threat, insult, identity_hate) = (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    WHERE ID = ?""", (nb_tweets_insultants, nb_insultes_total, nb_tweets_total, violence_totale, toxic, severe_toxic, obscene, threat, insult, identity_hate, ID))

    except sqlite3.Error as error:
        conn.rollback()
        cur.close()
        conn.close()
        print("Erreur lors de l'update du profil: ", error)
        return (False, error)

    conn.commit()
    cur.close()
    conn.close()
    return (True, None)



def remove_insulter(IDdelete):
    """
    Supprime la ligne correspondant à l'insulteur ID.

    Args:
        ID: identifiant Twitter (str)

    Returns:
        (True, None) s'il est supprimé
        (False, Error) sinon
    """
    conn = sqlite3.connect('db_insulter.db')
    cur = conn.cursor()
    print("Connexion réussie à SQLite (remove_insulter)")
    
    try:
        sql = "DELETE FROM Insulteurs WHERE ID=?"
        cur.execute(sql, (IDdelete,))
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
        cur.close()
        conn.close()
        return (False, error)
    
    conn.commit()
    cur.close()
    conn.close()
    print("Enregistrement supprimé avec succès")
    return (True, None)
