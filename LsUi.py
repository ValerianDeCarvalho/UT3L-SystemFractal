from ast import Lambda
import imp
from math import ceil
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext 
import tkinter as tk
import csv
import utils
import LsConfig
import LsDef
import Ls
import LsTurtle

    

def create_scrollbar(root):

    screen_width = root.winfo_screenwidth()
    # Calculate the center coordinates
    center_x = int(screen_width / 2)

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    y_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    y_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

    # Configure the canvas
    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(tk.ALL)))

    # Create Another Frame INSIDE the Canvas
    window = tk.Frame(my_canvas)
    window.pack()    
    my_canvas.create_window((center_x,0), window=window, anchor="n")

    return my_canvas, window

# Creation de la fenetre principal d'interaction utilisateur
def create_ui_window(root,turtle):
    # Création de la fenêtre principale
    my_canvas, window = create_scrollbar(root)

    # séparateur ( on peut reutiliser la meme variable car elle n'est pas utilisée ultérieurement )
    separator = tk.Label(window, text="")
    separator.pack()

    # Affichage du gros titre
    label_title = tk.Label(window, text="L-System", font=("Arial", 24, "bold"), relief="raised", bd=5)
    label_title.pack()

    # séparateur ( on peut reutiliser la meme variable car elle n'est pas utilisée ultérieurement )
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'une frame pour regrouper les labels d'itération et de l'axiome
    frame_labelia = tk.Frame(window)
    frame_labelia.pack(side=tk.TOP)

    # Création d'une frame pour regrouper les entrées d'itération et de l'axiome
    frame_inputia = tk.Frame(window)
    frame_inputia.pack(side=tk.TOP)

    # Affichage du label pour l'itération et son entrée
    label_iteration = tk.Label(frame_labelia, padx=35, text="Itérations:")
    label_iteration.pack(side=tk.LEFT)
    iteration = tk.Entry(frame_inputia, width=20)
    iteration.pack(side=tk.LEFT)

    # Affichage du label pour l'axiome et son entrée
    label_axiom = tk.Label(frame_labelia, padx=30, text="Axiome:")
    label_axiom.pack(side=tk.LEFT)
    axiom = tk.Entry(frame_inputia, width=20)
    axiom.pack(side=tk.LEFT)


    # séparateur ( on peut reutiliser la meme variable car elle n'est pas utilisée ultérieurement )
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'une frame pour regrouper les labels de règles
    frame_labelir = tk.Frame(window)
    frame_labelir.pack(side=tk.TOP)
    # Création d'une frame pour regrouper les entrées de règles
    frame_inputir = tk.Frame(window)
    frame_inputir.pack(side=tk.TOP)


    # Affichage du label pour les règles
    label_rules = tk.Label(frame_labelir, text="Règles:")
    label_rules.pack(side=tk.LEFT)
    # Entrée pour les règles
    rules = scrolledtext.ScrolledText(frame_inputir, width=150, height=10)
    rules.pack(side=tk.LEFT)
    
    def updateItAxRule(it,ax,rul):
        iteration.delete(0,'end')
        iteration.insert(0,it)
        axiom.delete(0,'end')
        axiom.insert(0,ax)
        rules.delete('1.0','end')
        rules.insert('1.0',rul)

    # séparateur ( on peut reutiliser la meme variable car elle n'est pas utilisée ultérieurement )
    separator = tk.Label(window, text="")
    separator.pack()

    # La creation des graphiques liés au regles graphiques
    # Le format du parametre d'entree est un dictionnaire t un tableau de la commande { 'LettreCommand':[ 'NomDeLaCommande', ValeurRotationSiApplicable, LongueurDeDeplacementSiApplicable ], .... }
    def create_input_graphic_rule(ruleName,ruleDef):
        # Création d'un input avec un menu déroulant
        input_frame = tk.Frame(frame_graphrules)
        input_frame.pack(anchor=tk.W)

        input_entry = tk.Entry(input_frame, width=10,name="nomCommand")
        input_entry.pack(side=tk.LEFT)
        input_entry.insert(0,ruleName)

        selected_option = tk.StringVar(input_frame)
        selected_option.set(ruleDef[0])

        dropdown_menu = tk.OptionMenu(input_frame, selected_option, *LsConfig.predefined_options)
        dropdown_menu.var=selected_option
        dropdown_menu.config(width=20)
        dropdown_menu.pack(side=tk.LEFT)

        length_entry = tk.Entry(input_frame, width=10,name="length")
        length_entry.insert(0,ruleDef[1])
        length_entry.pack(side=tk.LEFT)
        selected_option.trace("w", lambda *args: update_input_entry(length_entry, selected_option))
        update_input_entry(length_entry, selected_option)

        rotate_entry = tk.Entry(input_frame, width=10, name = "rotate")
        rotate_entry.insert(0,ruleDef[2])
        rotate_entry.pack(side=tk.LEFT)
        selected_option.trace("w", lambda *args: update_input_entry(rotate_entry, selected_option))
        update_input_entry(rotate_entry, selected_option)

    # On a une liste de regles graphiques ( obtenues du fichier et on declenche une creation pour chaque de manière séquentielle )
    def create_tk_gr_rules(gr):
        for l in gr:
            create_input_graphic_rule(l,gr[l])

    # On recupere l'ensemble des regles graphiques en itérant sur les objets graphiques et en récuperant leur valeur
    # On obtient un dictionnaire qui fournit pour chaque lettre de command, une structure GraphRule associée qui contient la commande et ses parametres
    def get_graphic_rules():
        gr={}
        errs=[]
        input_frames = frame_graphrules.winfo_children()
        for i in range(len(input_frames)):
            fr=input_frames[i].winfo_children()
            if gr.get(fr[0].get())==None:
                if fr[1].var.get()==LsConfig.predefined_options[0]: # pour les autres cas que dessiner on ne teste pas les parametres
                    if not utils.testIfInt(fr[2].get()):
                        utils.appendIfNotPresent(errs,"Dessiner avec rotation "+fr[2].get()+" incorrecte")
                    else:
                        if not utils.testIfInt(fr[3].get()):
                            utils.appendIfNotPresent(errs,"Dessiner avec déplacement "+fr[3].get()+" incorrect")
                        else:
                            rule=LsDef.GraphRule(fr[1].var.get(),fr[2].get(),fr[3].get())
                            gr[fr[0].get()]=rule
                else:
                    rule=LsDef.GraphRule(fr[1].var.get(),'','')
                    gr[fr[0].get()]=rule
            else:
                utils.appendIfNotPresent(errs,"Graphic rule "+fr[0].get()+" duplicated")
        return gr,errs

    # On recupere l'ensemble des regles graphiques en itérant sur les objets graphiques et en récuperant leur valeur
    # Et on produit une string dont le format est le suivant
    # LettreCommandeGraphique=NomDeLaCommande:ValeurDeRotation:ValeurDeDeplacement;
    # LettreCommandeGraphique=NomDeLaCommande:ValeurDeRotation:ValeurDeDeplacement
    # Convertir une chaîne en tuple
    # une regle a le format 
    # LettreCommande=Dessiner:10:20;
    # LettreCommande=Charger::;
    # LettreCommande=Sauvergarder::

    def get_graphic_rules_string():
        ret=""
        gr,errs=get_graphic_rules()
        if not errs:
            for cmd in gr: # Pour l'ensemble des elements, on va recuperer les valeurs
                if ret != "": # si pas le dernier enregistrement, on rajout le separateur
                    ret=ret+";"
                # On recupere toutes les valeurs ( meme si elles sont non applicables ( elles ne sont pas affichées ))
                # Pour la gestion des erreurs , on verifie que certains characteres ne sont pas interdits ( il faudrait les empecher au niveau graphique ... )    
                ret=ret+cmd+"="+gr[cmd].command+":"+gr[cmd].rot+":"+gr[cmd].len
        return ret,errs
    
    
    def command_do():
        lsys=""
        r,errs,warns=LsDef.stringToRule(rules.get("1.0","end"))
        if not(errs) :
            if utils.testIfUInt(iteration.get()):
                it=int(iteration.get())
                ax=axiom.get()
                errs,warns=LsDef.test_axiom_in_rule(ax,r)
                if not(errs):
                    lsys=Ls.lSystemCreate(ax,r,it)
                    update_result(lsys)
            else:
                utils.appendIfNotPresent(errs,"Valeur d'itération "+iteration.get()+" incorrect")
        updateErrsWarns(errs,warns)
        return lsys,errs,warns

    # Création d'une frame pour le bouton DO et son bouton pour voir le resultat
    frame_button_do = tk.Frame(window)
    frame_button_do.pack(side=tk.TOP)
    button_do = tk.Button(frame_button_do, text="Afficher le résultat",font='Helvetica 10 bold', width=20, height=1,command=lambda: command_do())
    button_do.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Frame pour afficher le résultat et création d'un input non éditable
    frame_result = tk.Frame(window)
    frame_result.pack(side=tk.TOP)
    result = scrolledtext.ScrolledText(frame_result, width=150,height=3, state='disabled')
    result.pack(padx=10 )

    def update_result(r):
        result.config(state='normal') # on doit permettre la modification
        result.delete('1.0', 'end')
        result.insert('1.0', r)
        result.config(state='disabled') # on remet en mode lecture seule

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    frame_errors = tk.Frame(window)
    frame_errors.pack(side=tk.TOP)
    logErrors = scrolledtext.ScrolledText(frame_errors, width=150,height=3, state='disabled')
    logErrors.pack(padx=10 )

    
    def updateErrsWarns(errs,warns):
        txt=""
        bgCol='green'
        if warns:
            txt+="Warnings:\n"
            for w in warns:
                txt+=w+"\n"
            bgCol='orange'
        if errs:
            txt+="Errors:\n"
            for e in errs:
                txt+=e+"\n"
            bgCol='red'
            
        logErrors.config(state='normal',bg=bgCol) # on doit permettre la modification
        logErrors.delete('1.0', 'end')
        logErrors.insert('1.0',txt)
        logErrors.config(state='disabled') # on doit permettre la modification

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Frame pour afficher les trucs pour le graphique
    frame_graph = tk.Frame(window)
    frame_graph.pack(side=tk.TOP)

    # Frame pour les boutons create et delete
    frame_buttons = tk.Frame(frame_graph)
    frame_buttons.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    frame_graphrules = tk.Frame(window)
    frame_graphrules.pack(side=tk.TOP)


    def update_input_entry(entry, option):
        if option.get() == LsConfig.predefined_options[0]:
            entry.pack(side=tk.LEFT)
        else:
            entry.pack_forget()

        # Mettre à jour la scrollbar
        my_canvas.update_idletasks()
        my_canvas.config(scrollregion=my_canvas.bbox(tk.ALL))

    # Création d'un bouton pour créer un nouvel input avec menu déroulant
    button_create_input = tk.Button(frame_buttons,width=30, text="Ajouter +",font='Helvetica 10 bold', command=lambda:create_input_graphic_rule('',[LsConfig.predefined_options[0],0,10]))
    button_create_input.pack(padx=10,side=tk.LEFT)
        

    def delete_all_input():
        # Supprimer l'ensemble
        input_frames = frame_graphrules.winfo_children()
        for i in range(len(input_frames)) :
            input_frames[i].destroy()

    def delete_last_input():
        # Supprimer le dernier input
        input_frames = frame_graphrules.winfo_children()
        if len(input_frames) > 0:
            input_frames[len(input_frames)-1].destroy()

    # Création d'un bouton pour supprimer le dernier input
    button_delete_input = tk.Button(frame_buttons,width=30, text="Enlever -",font='Helvetica 10 bold', command=delete_last_input)
    button_delete_input.pack(padx=10,side=tk.LEFT)

    # La commande qui fait l'ensemble du cycle
    def command_draw():
        # recuperation du resultat de l'iteration
        ls,errs,warns = command_do()
        if not errs:
            gr,errs = get_graphic_rules()
            if not errs:
                LsTurtle.turtleRun(turtle,ls,gr,int(turtle_speed.get()))

    # Frame et bouton pour envoyer et dessiner le résultat
    frame_draw = tk.Frame(window)
    frame_draw.pack(side=tk.TOP)

    # Affichage du label pour la vitesse de la tortue
    label_turtle_speed = tk.Label(frame_draw, padx=5, text="Turtle speed:")
    label_turtle_speed.pack(side=tk.LEFT)
    turtle_speed = tk.Entry(frame_draw, width=20)
    turtle_speed.insert(0,"9")
    turtle_speed.pack(side=tk.LEFT)

    button_draw = tk.Button(frame_draw, text=LsConfig.predefined_options[0],command=lambda:command_draw())
    button_draw.pack(padx=10)

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # La gestion des fichiers ( lecture et ecriture )

    # Structure du csv
    # Ligne 1, nom des colonnes: iteration ; axiome ; regles ; regles graphiques
    # Ligne 2 valeur des cellules
    def loadCsv(filename):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            line_count = 0
            for row in csv_reader:
                if line_count==1:
                    gr,errs=LsDef.stringToGraphicRule(row[3])
                    updateItAxRule(row[0],row[1],row[2])
                    delete_all_input()
                    create_tk_gr_rules(gr)
                line_count += 1


    # On utilise une generation directe du fichier csv ( sans passer par le csv writer, car il ne gere pas correctement les terminaisons de ligne sur des machines windows )
    # Le format est simple:
    # Premiere ligne, liste des noms des parametres
    # Deuxieme ligne, valeur des parametres ( encadrés par ") car il peut y avoir des terminaisons de lignes, et le séparateur de champ est ;           
    def saveCsvFile(file):
        file.write("Iteration;Axiome;Regles;Regles graphiques\r")
        line,errs=get_graphic_rules_string()
        if not errs:
            file.write(iteration.get()+";\""+axiom.get()+"\";\""+rules.get("1.0","end")+"\";\""+line+"\"\r")

    def saveCsv(filename):
        with open(filename, "w+") as file:
            saveCsvFile(file)

    # Création d'une frame pour regrouper les labels d'itération et de l'axiome
    frame_saveload = tk.Frame(window)
    frame_saveload.pack(side=tk.TOP)
    
    # Création d'un bouton pour sauvegarder et d'un bouton pour charger
    button_save = tk.Button(frame_saveload,width=30, text="Sauvegarder",font='Helvetica 10 bold', command=lambda:saveCsvFile(filedialog.asksaveasfile(initialdir='./',mode="w+")))
    button_save.pack(side=tk.LEFT, padx=10)

    button_load = tk.Button(frame_saveload,width=30, text="Charger",font='Helvetica 10 bold',command=lambda:loadCsv(filedialog.askopenfilename(initialdir='./')))
    button_load.pack(side=tk.LEFT, padx=10)

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # Création d'un bouton pour fermer la fenêtre
    button_close = tk.Button(window, text="Fermer",font='Helvetica 12 bold', command=root.destroy)
    button_close.pack()

    # Séparateur
    separator = tk.Label(window, text="")
    separator.pack()

    # On charge un fichier par default
    loadCsv("flocon.csv")
    


