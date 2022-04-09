import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

from src.getStats import get_name, insult_classification, insult_rate, profile_type
from src.dataBase import remove_insulter




def piechart(stats):
    """
    Trace le camember correspondant au données de dico

    Args:
        stats: dictionnaire python {'cat1':freq, 'cat2':..., ...}
    
    Returns:

    """
    labels = []
    sizes = []

    for x, y in stats.items():
        labels.append(x)
        sizes.append(y)

    fig = Figure((4,3))
    ax = fig.add_subplot(111)
    ax.pie(sizes)

    ax.axis('equal')
    ax.legend(labels, loc='center', bbox_to_anchor=(0.02,.5), prop={'size':6})

    return fig




## Fenêtre d'un profil

def open_profile(user, profile_button):
    """
    Ouvre le profile de l'utilisateur user.

    Args:
        user: ID de l'un des insulteurs de la db (str)
        profile_button: bouton tkinter lié au profil de l'insulteur

    Returns:
        None
    """
    # Fenêtre du profil
    profile_window = tk.Toplevel()
    profile_window.title("Profil de " + user)
    profile_window.minsize(700,500)


    # TOP PART: Profile picture and names
    title_frame = tk.Frame(profile_window, padx=10, pady=10, relief=tk.RAISED, borderwidth=1)

    # À remplacer par vrai photo de profile
    profile_pic = tk.Frame(title_frame, height=60, width=60, bg='blue')
    profile_pic.grid(row=0, column=0, rowspan=2, sticky='nsew')

    user_name = tk.Label(title_frame, text="  " + get_name(user))
    user_name.grid(row=0,column=1, sticky='w')

    user_id = tk.Label(title_frame, text="  @" + user)
    user_id.grid(row=1,column=1, sticky='w')

    profile_title = tk.Label(title_frame, text='Type de profil : ', padx=3)
    profile_title.grid(row=0, rowspan=2, column=2, sticky='e')

    user_type = tk.Label(title_frame, text=profile_type(user), relief='sunken', borderwidth=1, padx=5, pady=5)
    user_type.grid(row=0, column=3, rowspan=2, sticky='w')


    def delete_popup(user, profile_button):
        """
        Fait apparaître la fenêtre confirmant le choix de supprimer l'insulteur.
        Si 'yes' est sélectionné, supprime l'insulteur de la liste.

            Args:
                user: identifiant Twitter de l'utilisateur concerné (str)
                profile_button: bouton tkinter lié au profil de l'insulteur

            Return:
                None
        """
        del_popup = messagebox.askyesno('Info LinkedInsult', 'Supprimer cet insulteur ?')
        
        if del_popup == 1:
            remove_insulter(user)
            profile_window.destroy()
            profile_button.destroy()
            messagebox.showinfo('Info LinkedInsult', '@' + user + ' a été enlevé de la liste.')



    delete_button = tk.Button(title_frame, text='x', command=lambda user=user: delete_popup(user, profile_button), padx=8, pady=5)
    delete_button.grid(row=0, rowspan=2, column=4, sticky='e')

    # Mise en page :
    title_frame.columnconfigure(2,weight=1)
    title_frame.columnconfigure(3,weight=1)
    title_frame.columnconfigure(4,weight=1)

    title_frame.grid(row=0, sticky='new')


    # MIDDLE PART: Graphs

    main_frame = tk.Frame(profile_window, pady=20, relief=tk.RAISED, borderwidth=1)

    classification = insult_classification(user)

    canvas = FigureCanvasTkAgg(piechart(classification), master=main_frame)
    canvas.get_tk_widget().pack(side=tk.LEFT, expand=True)

    prop = insult_rate(user)
    load_bar = tk.Frame(main_frame, padx=20)
    
    # Titre de la barre

    bar_title = tk.Label(load_bar, text='Proportion de tweets insultants', pady=10)
    bar_title.grid(row=0)

    # Barre de chargement
    
    insult_bar = tk.Frame(load_bar, height=15, width=200, bg='light sky blue')
    insult_bar.grid(row=1, sticky='w')
    clean_bar = tk.Frame(load_bar, height=15, width=int(200*prop), bg='red')
    clean_bar.grid(row=1, stick='w')

    load_bar.pack(side=tk.RIGHT, expand=True)

    main_frame.grid(row=1, sticky='nsew')
    profile_window.rowconfigure(1, weight=1)
    profile_window.columnconfigure(0, weight=1)



    # BOTTOM PART: Close window
    lower_frame = tk.Frame(profile_window, pady=10)
    close_button = tk.Button(lower_frame, text="Fermer", command=profile_window.destroy, padx=10, pady=5)
    close_button.pack()
    lower_frame.grid(row=2, sticky='sew')