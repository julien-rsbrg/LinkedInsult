import tkinter as tk
from tkinter import ttk

from src.gui_profile_window import open_profile
from src.gui_add_menu import open_add_menu


# Sera plus tard remplacé par la liste des insulteurs présents dans la db
# insulter_list = ['Jean-mi','kikoulol','Jay Padi D.','José','Capitaine Haddock','Kevin']

## Fenêtre principale

def start_gui(insulter_list, connexion, nb_max):
    """
    Lance l'interface graphique de LinkedInsult.

    Args:
        None
    
    Returns:
        None
    """
    main_window = tk.Tk()
    main_window.title("LinkedInsult")
    main_window.minsize(400,400)

    list_label = tk.Label(main_window, text="Insulteurs Répertoriés",pady=20)
    list_label.pack()




    # Liste des insulteurs connus
    main_list = ttk.Frame(main_window)

    # Canvas contenant les boutons et la scollbar
    list_canvas = tk.Canvas(main_list)

    # Scrollbar
    scrollbar = ttk.Scrollbar(main_list, orient='vertical', command=list_canvas.yview)

    scrollable_frame = ttk.Frame(list_canvas)
    scrollable_frame.bind('<Configure>', lambda e: list_canvas.configure(scrollregion=list_canvas.bbox("all")))

    list_canvas.create_window((0,0), window=scrollable_frame, anchor='nw')
    list_canvas.configure(yscrollcommand=scrollbar.set)

    # Boutons ouvrant les profils
    profile_buttons = {}
    for user in insulter_list:
        profile_buttons[user] = tk.Button(scrollable_frame, text="@" + user, pady=10,padx=80)
        profile_buttons[user].configure(command=lambda user=user, profile_button=profile_buttons[user]: open_profile(user, profile_button))
        profile_buttons[user].pack(fill=tk.X)

    main_list.pack(expand=True, fill=tk.Y)
    list_canvas.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)



    lower_frame = tk.Frame(main_window, pady=10)
    lower_frame.pack()

    # Ajouter un insulteur
    add_insulter = tk.Button(lower_frame, text='+', command=lambda: open_add_menu(connexion, nb_max, profile_buttons, scrollable_frame), padx=7, pady=5)
    add_insulter.grid(row=0, sticky='w')

    # Ligne d'information au bas de la fenêtre
    info_line = tk.Label(lower_frame,text="Cliquer sur un insulteur pour consulter son profil",pady=30)
    info_line.grid(row=1)

    # Bouton pour fermer l'application
    exit_button = tk.Button(lower_frame, text="Fermer", command=main_window.quit, padx=10, pady=5)
    exit_button.grid(row=2)

    main_window.mainloop()