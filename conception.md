Voir fichier Plan du projet.png pour la conception de l'interface graphique contenant:<br/>
• Liste cliquable de profil ayant déjà insulté sur Twitter<br/>
• Profil de chaque insulteur affichant:<br/>
\- Photo de profil<br/>
\- Nom d'utilisateur<br/>
\- Type de profil (catégorie principale de ses insultes)<br/>
\- Camembert des types d'insultes employées<br/>
\- Barre de pourcentage de tweets insultants<br/>


## MVPs:

MVP 1 : Détecteur d’insulte et profilage (un profil = une liste). Les queries tweepy mènent à compléter la base de donnée<br/>
MVP 2 : MVP1 + Interface graphique avec Dash<br/>
MVP 3 : MVP2 + Niveau de créativité, originalité ou répétitions ? vocabulaire réduit ?<br/>
MVP 4 :  MVP3 + Apprendre à une IA à reconnaître les insultes<br/>



## DataBase:

ID (PRIMARY KEY)<br/>
@user<br/>
nb_tweets_total<br/>
nb_tweets_insultants<br/>
nb_insultes_total<br/>
nb_insultes_category1<br/>
nb_insultes_category2<br/>
...


## TODO LIST


Base de données<br/>
- init_db() --> (True, None) ou (False, Error)<br/>
- add_insulter(ID, name) --> (True, None) ou (False, Error)<br/>
- update_profile(author) --> (True, None) ou (False, Error)<br/>
- remove_insulter(author) --> (True, None) ou (False, Error)<br/>

--> la db est prête<br/><br/>


Detection insulte<br/>
- is_insult(string) --> bool<br/>

--> insulte détectée<br/><br/>


Trouver un tweet insultant<br/>
- stream_until_insult(filter)<br/>
- find_tweet_with(insult)<br/>

--> on a un tweet<br/><br/>


Analyser le profil de l'auteur de tweet<br/>
- find_author(tweet) --> (ID, name)<br/>
- collect_tweet(author) --> liste de tweets<br/>

--> on a les tweets (liste)<br/><br/>


Analyser les tweets<br/>
- insulting(tweet) --> bool<br/>
- violence(tweet) --> [0,1]<br/>
- insult_list(tweet) --> liste des insultes<br/>
- classify_insults(list) --> Dico {category: score} (y compris catégorie "Points")<br/>

--> données à rentrer dans la db<br/><br/>


Obtenir Stats<br/>
- insult_classification(author) --> dico {category: frequency}<br/>
- insult_rate(author) --> frequency<br/>
- profile_type(dico{category:frequency})<br/>

--> les infos peuvent être consultées<br/><br/>


Interface terminal<br/>
- init_interface() --> None<br/>
- display_interface(ID) --> None<br/>
- get_random_insulter() --> ID<br/>
- get_specific_insulter_by_score(score) --> ID<br/>
- get_specific_insulter_by_name(name) --> ID<br/>

--> l'application est utilisable simplement<br/><br/>


Interface graphique<br/>
- start_gui() --> lance l'interface<br/>
- open_profile() --> ouvre la fenêtre du profil choisi<br/>
- open_add_menu() --> ouvre le menu permettant d'ajouter un insulteur<br/>

--> l'application est agréable visuellement et d'utilisation intuitive
