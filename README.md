# Projet des Rageux pour les Coding Weeks 2021

## LinkedInsult ou le Twitter des rageux

Ce projet est un projet d'analyse de tweets mené durant les Coding Weeks de CentraleSupelec

Le but du projet est de détecter les rageux.ses qui sévissent sur Twitter par une détection d'insultes au hasard sur le réseau social puis une analyse du profil de l'insultant (fréquence des insultes, violence des insultes, créativité des insultes, catégorie des insultes...). Les tweets analysés sont en anglais car le français n'est pas pris en charge par les datasets utilisés. Les statistiques sur les insultes d'un utilisateur sont stockés dans une base de donnée et les profils sont consultables via une interface graphique.


## Rageux

• Amiaud--Plachy Ilann : contributor who wants to do the perfect insult censor. <br/>
• Bidard Pauline : contributor & Twitter developer <br/>
• Caillot Alexandre : contributor<br/>
• Dumas Robin : contributor & Twitter developer<br/>
• Martin Gabriel : Host and contributor <br/>
• Rosenberger Julien : Grammatical mistakes sensitive<br/>


## Utilisation

Modules utilisés:<br/>
• sys<br/>
• tweepy<br/>
• sqlite3<br/>
• pandas<br/>
• random<br/>
• tkinter <br/>
• matplotlib.pyplot<br/>
• matplotlib.figure<br/>
• matplotlib.backends_tkagg<br/>
• json<br/>

Pour la partie IA : <br/>
• sklearn<br/>
• numpy<br/>
• pickle<br/>

## Prérequis et déploiement 

Avoir un **compte Twitter Developer** est indispensable.

Avant toute utilisation, **créer un fichier _filepath_perso.py_** en parallèle de _main.py_ et y coller la ligne suivante:<br/>
\>\>\> filepath = "chemin_d'accès_absolu_vers_dossier_CONTENANT_credentials"<br/>
Avec _credentials.py_ un fichier contenant les informations nécessaires à la connection à l'API Twitter 
(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)


Pour lancer l'application, il suffit d'**exécuter _main.py_**. Il est possible de choisir le type d'interface entre :<br/>
terminal (INTERFACE = 'command') et Tkinter (INTERFACE = 'graphic') directement dans _main.py_.<br/>
L'utilisateur peut aussi fixer le nombre maximal de tweets récupéré par compte Twitter avec la variable NB_MAX.

```python
################# PREFERENCES ##################

# Choisir le type d'interface entre 'graphic' et 'command' :
INTERFACE = 'graphic'

# Choisir le nombre maximal de tweets récupérés :
NB_MAX = 1000

################################################
```


## Avertissement fonctions défaillantes

Certaines fonctionnalités ne sont pas encore opérationnelles : <br/>
    - faire des recherches de tweets en direct<br/>
    - certaines insultes peuvent ne retourner aucun tweet. Cela créer une erreur *IndexError: list index out of range*<br/>
(Update: problème normalement résolu)
# LinkedInsult
# LinkedInsult
# LinkedInsult
