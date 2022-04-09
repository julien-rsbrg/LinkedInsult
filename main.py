import sys
import tweepy
from filepath_perso import filepath
from src.gui_main_window import start_gui
from src.getStats import get_insulters
from src.dataBase import init_db
from src.cli import init_interface


#==============================================#
################# PREFERENCES ##################


# Choisir le type d'interface entre 'graphic' et 'command' :
INTERFACE = 'graphic'

# Choisir le nombre maximal de tweets récupérés :z
NB_MAX = 1000


################################################
#==============================================#




sys.path.append(filepath) # Adds path to find credentials.py

# L'erreur indiqué ici n'engendre pas de problème, elle est seulement lié à VSCode
# qui n'est pas capable de lire ce qui se trouve dans 'filepath' avant l'exécution
from credentials import CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET
API_credentials = CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET



def twitter_setup(API_credentials):
    """
    Établit une instance de connection à l'API Twitter.

    Args:
        API_credentials: tuple à 4 éléments (str) contenant les informations nécessaires à la connection
    
    Returns:
        None
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(API_credentials[0], API_credentials[1])
    auth.set_access_token(API_credentials[2], API_credentials[3])

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


if __name__ == '__main__':

    init_db()

    connexion = twitter_setup(API_credentials)

    insulter_list = get_insulters()


    # Démarrage de l'appli

    if INTERFACE == 'graphic':
        start_gui(insulter_list, connexion, NB_MAX)

    elif INTERFACE == 'command':
        init_interface(connexion)