import tkinter as tk
from tkinter import messagebox

from src.dataBase import add_insulter, update_profile
from src.findTweet import find_tweet_with
from src.profileAnalysis import collect_tweets, find_author
from src.tweetAnalysis import classify_insults, insult_list, analyse_tweets_AI
from src.gui_profile_window import open_profile

from src.data import dico_insultes, categories



def open_add_menu(connexion, nb_max, profile_buttons, scrollable_frame):
    """
    Ouvre le menu pour ajouter un insulteur.

    Args:
        connexion: instance de l'API Twitter
        nb_max: nombre maximal de tweets récoltés (int)
        profile_buttons: boutons de la fenêtre principale (dict)
        scrollable_frame: frame tkinter contenant ces boutons
    
    Results:
        None
    """
    add_menu = tk.Toplevel()
    add_menu.title("Menu d'ajout")



    bottom_frame = tk.Frame(add_menu, padx=10, pady=10)
    
    info_var = tk.StringVar()
    info_var.set("Seléctionner le type de recherche")
    info_line = tk.Label(bottom_frame,textvariable=info_var,pady=10, width=30)
    info_line.grid(row=0)

    cancel_button = tk.Button(bottom_frame, text="Annuler", command=add_menu.destroy, padx=10, pady=5)
    cancel_button.grid(row=1)



    radio_frame = tk.Frame(add_menu, padx=10, pady=30)

    # Choix du mode de recherche

    search_kind = tk.LabelFrame(radio_frame, text='Mode de recherche', pady=10, padx=10, borderwidth=1, relief=tk.SUNKEN, width=50)

    search_type = tk.StringVar()
    search_type.set('search')

    input_field = tk.Entry(search_kind, width=15)
    input_field.grid(row=2)

    # Radio Buttons:
    by_search = tk.Radiobutton(search_kind, text='Chercher une insulte', variable=search_type, value='search', command=lambda: input_field.configure(state=tk.NORMAL))
    by_search.grid(row=1, sticky='w')
    by_stream = tk.Radiobutton(search_kind, text='Streamer une insulte', variable=search_type, value='stream', pady=10, command=lambda: input_field.configure(state=tk.DISABLED))
    by_stream.grid(row=3, sticky='w')

    search_kind.pack(fill=tk.X)


    # Choix du mode d'analyse

    analysis_kind = tk.LabelFrame(radio_frame, text="Mode d'analyse", pady=10, padx=10, borderwidth=1, relief=tk.SUNKEN, width=50)

    analysis_type = tk.StringVar()
    analysis_type.set('comparaison')

    # Radio Buttons:
    by_search = tk.Radiobutton(analysis_kind, text='Mot à mot', variable=analysis_type, value='comparaison')
    by_search.grid(row=1, sticky='w')
    by_stream = tk.Radiobutton(analysis_kind, text='IA', variable=analysis_type, value='ai', pady=10)
    by_stream.grid(row=3, sticky='w')

    analysis_kind.pack(fill=tk.X)



    def gui_add(search_type, analysis_type, connexion, nb_max, profile_buttons, scrollable_frame):
        """
        Ajoute un utilisateur selon le mode de recherche search_type.

        Args:
            search_type: 'search' ou 'stream' (str)
            analysis_type: 'comparaison' ou 'ai' (str)
            connexion: instance d'API Twitter
            nb_max: nombre maximal de tweets récoltés (int)
            profile_buttons: boutons de la fenêtre principale (dict)
            scrollable_frame: frame tkinter contenant ces boutons
        
        Returns:
            None
        """
        if search_type=='search':

            info_var.set('Ajout en cours...')

            insult = input_field.get()
            tweet, check = find_tweet_with(insult, connexion=connexion)
            if not check:
                messagebox.showerror('Info LinkedInsult', "Une erreur est survenue lors de la recherche d'un tweet...")
                return None

            (ID, name) = find_author(tweet)

            # Crée le dictionnaire des scores par catégorie et ajoute l'insulte entrée
            score_tot = {}
            
            if analysis_type =='comparaison':
                for cat in categories:
                    score_tot[cat] = 0
                if insult in dico_insultes:
                    score_tot[dico_insultes[insult][0]] += 1

            if analysis_type =='ai':
                y_pred = analyse_tweets_AI([tweet]) # sortie prédite par l'IA
                print(tweet.text)
                for i,cat in enumerate(categories):
                    print(y_pred[0][i])
                    score_tot[cat]=int(y_pred[0][i])

            if add_insulter(ID, name)[0]: # if dataBase.add_insulter()[0]:
                info_var.set('Analyse du profil...')
            
                tweets = collect_tweets(connexion, ID, nb_max)
                
                # Calcul des scores

                nb_tweets_insultants = 1
                nb_insultes_total = 1
                nb_tweets_total = len(tweets)
                violence_moyenne = 0

                if analysis_type=='comparaison':

                    for tw in tweets:
                        classification = classify_insults(insult_list(tw))
                        insultes_avant_maj = nb_insultes_total
                        for key, val in classification.items():
                            score_tot[key] += val
                            nb_insultes_total += val
                        if nb_insultes_total - insultes_avant_maj > 0:
                            nb_tweets_insultants += 1
                
                elif analysis_type=='ai':

                    y_pred = analyse_tweets_AI(tweets)

                    for i,y_tweet in enumerate(y_pred):
                        if sum(y_tweet)>0:
                            nb_tweets_insultants+=1

                        for j,cat in enumerate(categories):
                            score_tot[cat]+=int(y_pred[i][j])

                if update_profile(ID, nb_tweets_insultants, nb_insultes_total, nb_tweets_total, violence_moyenne, score_tot["toxic"], score_tot["severe_toxic"], score_tot["obscene"], score_tot["threat"], score_tot["insult"], score_tot["identity_hate"])[0]:
                    messagebox.showinfo("Info LinkedInsult", "Un nouvel insulteur a bien été ajouté ! \nID : @" + ID)
                else:
                    messagebox.showerror("Une erreur s'est produite lors de l'analyse du profil")
                    return None
            else:
                messagebox.showerror("Une erreur s'est produite lors de l'ajout de l'insulteur")
                return None
            add_menu.destroy()
            profile_buttons[ID] = tk.Button(scrollable_frame, text="@" + ID,pady=10,padx=80)
            profile_buttons[ID].configure(command=lambda user=ID: open_profile(user, profile_buttons[ID]))
            profile_buttons[ID].pack(fill=tk.X)


        elif search_type=='stream':
            messagebox.showinfo('Info LinkedInsult', "Oops ! Cette fonctionnalité n'est pas encore implémentée...")



    tk.Label(radio_frame, text=' ').pack()

    # Search button
    search_button = tk.Button(radio_frame, text='Chercher', command=lambda: gui_add(search_type.get(), analysis_type.get(), connexion, nb_max, profile_buttons, scrollable_frame), padx=5, pady=5)
    search_button.pack()

    tk.Label(radio_frame, text=' ').pack()

    # Help button

    def display_help():
        messagebox.showinfo('Aide LinkedInsult', "MODE DE RECHERCHE :\n\n- Chercher une insulte : recherche un tweet existant contenant l'insulte (en anglais) entrée\n\n- Streamer une insulte : attend la publication d'un tweet insultant correspondant à la requête (en anglais)\n\n\nMODE D'ANALYSE :\n\n- Mot à mot : compare chaque mot du tweet avec une liste d'insultes non exhaustive\n\n- IA : analyse le tweet en utilisant une IA (taux de réussite actuel : 70%)")
    
    help_button = tk.Button(radio_frame, text='?', command=lambda: display_help(), padx=9, pady=5)
    help_button.pack()


    radio_frame.pack(fill=tk.X)

    bottom_frame.pack()