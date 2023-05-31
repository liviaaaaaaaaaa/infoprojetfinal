import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Tk, Canvas, PhotoImage, Entry, Button, Checkbutton, Label, IntVar
import pickle


# affichage de la petite case pour rentrer du texte
def on_entry_click(event):
    if text_entry.get() == 'Réponse':
        text_entry.delete(0, tk.END)
        text_entry.config(fg='black')

def on_entry_leave(event):
    if text_entry.get() == '':
        text_entry.insert(0, 'Réponse')
        text_entry.config(fg='gray')

#fonction de récupération de la réponse du joueur
def get_user_input():
    user_input = text_entry.get()
    print("Le joueur a saisi :", user_input)

#récupération de la case cochée par le joueur
def checkbox_changed():
    if var_pp.get() == 1:
        print("La case pp est cochée.")
        var_pp.set(0)
    if var_st.get() == 1:
        print("La case st est cochée.")
        var_st.set(0)
    if var_t.get() == 1:
        print("La case t est cochée.")
        var_t.set(0)
    if var_js.get() == 1:
        print("La case js est cochée.")
        var_js.set(0)
    if var_gp.get() == 1:
        print("La case gp est cochée.")
        var_gp.set(0)
    if var_ob.get() == 1:
        print("La case ob est cochée.")
        var_ob.set(0)
    if var_gm.get() == 1:
        print("La case gm est cochée.")
        var_gm.set(0)

#fonction pour placer les points selon le nombre de ressources
def placer_les_points(coords):
    for i in range(5):
        coord = coords[i]
        label[i].place(x=coord[cases_ressources[i]][0], y=coord[cases_ressources[i]][1])
        label[i].lift()

#fonction d'affichage des dés
def afficher_dés(destires):
    # Chemin des dés
    chemin_dé1 = "Images/dé1.jpg"
    chemin_dé2 = "Images/dé2.jpg"
    chemin_dé3 = "Images/dé3.jpg"
    chemin_dé4 = "Images/dé4.jpg"
    chemin_dé5 = "Images/dé5.jpg"
    chemin_dé6 = "Images/dé6.jpg"

    # Réduire la taille des images
    taille_dés = (50, 50)

    dé1_image = Image.open(chemin_dé1).resize(taille_dés)
    dé2_image = Image.open(chemin_dé2).resize(taille_dés)
    dé3_image = Image.open(chemin_dé3).resize(taille_dés)
    dé4_image = Image.open(chemin_dé4).resize(taille_dés)
    dé5_image = Image.open(chemin_dé5).resize(taille_dés)
    dé6_image = Image.open(chemin_dé6).resize(taille_dés)

    global dé1, dé2, dé3, dé4, dé5, dé6
    dé1 = ImageTk.PhotoImage(dé1_image)
    dé2 = ImageTk.PhotoImage(dé2_image)
    dé3 = ImageTk.PhotoImage(dé3_image)
    dé4 = ImageTk.PhotoImage(dé4_image)
    dé5 = ImageTk.PhotoImage(dé5_image)
    dé6 = ImageTk.PhotoImage(dé6_image)

    tableau_dés = []
    for destire in destires:
        if destire == '3 nourriture':
            image = dé1
        elif destire == '1 marchandise':
            image = dé2
        elif destire == '2 marchandises et un cran':
            image = dé3
        elif destire == '3 ouvriers':
            image = dé4
        elif destire == '2 nourriture ou 2 ouvriers':
            image = dé5
        elif destire == '7 pieces':
            image = dé6
        else:
            continue
        tableau_dés.append(image)

    for i, image in enumerate(tableau_dés):
        label = tk.Label(fenetre, image=image)
        label.place(x=530 + (i % 4) * 50, y=400 + (i // 4) * 50)
        label.lift()




def jeu():
    #création de la fenêtre
    fenetre = tk.Tk()
    fenetre.title("Jeu")

    #création du plateau pour l'affichage des images
    plateau = tk.Canvas(fenetre, width = 100, height = 0)

    #création d'un label pour l'affichage de texte
    label_text = tk.Label(fenetre, text=" Bonjour ")

    #importation des images
    image1 = Image.open("Images/fiche_joueur.jpg")
    image2 = Image.open("Images/Ressources.jpg")
    #mise en forme des images
    image1 = image1.rotate(-90)
    image1 = image1.resize((500, 400))
    image2 = image2.resize((400, 200))
    image1 = ImageTk.PhotoImage(image1)
    image2 = ImageTk.PhotoImage(image2)

    #importation et mise en forme des points pour l'affichage des ressources
    bois_image = Image.open("Images/rond_noir.jpg")
    bois_image = bois_image.resize((10, 10))
    global bois
    bois = ImageTk.PhotoImage(bois_image)
    pierre_image = Image.open("Images/rond_noir.jpg")
    pierre_image = pierre_image.resize((10, 10))
    global pierre
    pierre = ImageTk.PhotoImage(pierre_image)
    poterie_image = Image.open("Images/rond_noir.jpg")
    poterie_image = poterie_image.resize((10, 10))
    global poterie
    poterie = ImageTk.PhotoImage(poterie_image)
    tissue_image = Image.open("Images/rond_noir.jpg")
    tissue_image = tissue_image.resize((10, 10))
    global tissue
    tissue = ImageTk.PhotoImage(tissue_image)
    lance_image = Image.open("Images/rond_noir.jpg")
    lance_image = lance_image.resize((10, 10))
    global lance
    lance = ImageTk.PhotoImage(lance_image)

    label_bois = tk.Label(fenetre, image = bois)
    label_pierre = tk.Label(fenetre, image = pierre)
    label_poterie = tk.Label(fenetre, image = poterie)
    label_tissue = tk.Label(fenetre, image = tissue)
    label_lance = tk.Label(fenetre, image = lance)

    label1 = tk.Label(fenetre, image = image1)
    label2 = tk.Label(fenetre, image = image2)


    text_entry = tk.Entry(fenetre)
    text_entry.insert(0, 'Réponse')
    text_entry.config(fg='gray')
    text_entry.bind('<FocusIn>', on_entry_click)
    text_entry.bind('<FocusOut>', on_entry_leave)

    #création du bouton pour valider le texte
    button_valider = Button(fenetre, text="Valider", command=get_user_input)

    #création du bouton "Sauvegarde"
    button_sauvegarde = Button(fenetre, text = "Sauvegarde")

    #création des checkbox pour les monuments
    var_pp = tk.IntVar()
    checkbox_pp = tk.Checkbutton(fenetre, variable=var_pp, command=checkbox_changed)
    var_st = tk.IntVar()
    checkbox_st = tk.Checkbutton(fenetre, variable=var_st, command=checkbox_changed)
    var_t = tk.IntVar()
    checkbox_t = tk.Checkbutton(fenetre, variable=var_t, command=checkbox_changed)
    var_js = tk.IntVar()
    checkbox_js = tk.Checkbutton(fenetre, variable=var_js, command=checkbox_changed)
    var_gp = tk.IntVar()
    checkbox_gp = tk.Checkbutton(fenetre, variable=var_gp, command=checkbox_changed)
    var_ob = tk.IntVar()
    checkbox_ob = tk.Checkbutton(fenetre, variable=var_ob, command=checkbox_changed)
    var_gm = tk.IntVar()
    checkbox_gm = tk.Checkbutton(fenetre, variable=var_gm, command=checkbox_changed)

    #affichage en grille et positionnement des items sur la fenetre
    label1.grid(row=0, column=0, rowspan = 2)
    label2.grid(row=2, column=0, rowspan = 2)
    label_text.place(x = 530, y = 100)
    label_text.lift()
    text_entry.place(x = 530, y = 200)
    text_entry.lift()
    button_valider.place(x = 530, y = 250)
    button_valider.lift()
    button_sauvegarde.place(x = 530, y = 550)
    button_sauvegarde.lift()


    #placement des checkbox des monuments
    checkbox_pp.place(x = 100, y = 275)
    checkbox_pp.lift()
    checkbox_st.place(x = 150, y = 275)
    checkbox_st.lift()
    checkbox_t.place(x = 205, y = 275)
    checkbox_t.lift()
    checkbox_js.place(x = 110, y = 330)
    checkbox_js.lift()
    checkbox_gp.place(x = 173, y = 330)
    checkbox_gp.lift()
    checkbox_ob.place(x = 230, y = 335)
    checkbox_ob.lift()
    checkbox_gm.place(x = 150, y = 367)
    checkbox_gm.lift()


    #afficher les points sur le bon nombre de ressources
    coordbois = 0
    coordpierre = 0
    coordpoterie = 0
    coordtissue = 0
    coordlance = 0

    # il aurait fallu que le nombre de ressource corresponde au nombre de ressource du joueur mais on aurait du pour cela mettre joueur en argument de jeu
        # et donc relancer une partie pour chaque joueur
    # coordbois = joueur.bois
    # coordpierre = joueur.pierre
    # coordpoterie = joueur.poterie
    # coordtissue = joueur.tissu
    # coordlance = joueur.lance

    #définition des positions des points d'affichage des ressources
    label = [label_bois, label_pierre, label_poterie, label_tissue, label_lance]
    coord_bois = [(122, 573), (160, 573), (198, 573), (235, 573), (272, 573), (310, 573), (346, 573), (384, 573)]
    coord_pierre = [(123, 532), (160, 532), (198, 532), (234, 532), (271, 532), (310, 532), (346, 532)]
    coord_poterie = [(122, 495), (160, 495), (197, 495), (234, 495), (271, 495), (309, 495)]
    coord_tissue = [(120, 457), (159, 457), (197, 457), (234, 457), (272, 457)]
    coord_lance = [(120, 423), (159, 423), (197, 423), (235, 423)]
    coords = [coord_bois, coord_pierre, coord_poterie, coord_tissue, coord_lance]
    cases_ressources = (coordbois, coordpierre, coordpoterie, coordtissue, coordlance) #entiers qui indiquent la case (par défaut 0)


    placer_les_points(coords)

    #affichage du texte "Résultat des dés"
    label_des = tk.Label(fenetre, text=" Résultat des dés : ")
    label_des.place(x = 530, y = 350)
    label_des.lift()

    dés = ['3 nourriture', '1 marchandise', '2 marchandises et un cran', '3 ouvriers',
           '2 nourriture ou 2 ouvriers', '7 pieces']
    afficher_dés(dés)

    fenetre.mainloop()



#Fonction de démarrage du jeu
def demarrer_jeu():
    #Fonction pour démarrer le jeu
    jeu()

def afficher_accueil():
    fenetre = tk.Tk()
    fenetre.geometry("800x600")
    global image_fond
    image_fond = Image.open("Images/accueil.jpg")
    image_fond = ImageTk.PhotoImage(image_fond)
    label_fond = tk.Label(fenetre, image=image_fond)
    label_fond.place(x=0, y=0, relwidth=1, relheight=1)
    label_titre = tk.Label(fenetre, text="Bienvenue sur la page d'accueil !", font=("Arial", 24))
    label_titre.pack(pady=50)

    bouton_demarrer = tk.Button(fenetre, text="Démarrer le jeu", font=("Arial", 18), command=demarrer_jeu)
    bouton_demarrer.pack()

    fenetre.mainloop()

afficher_accueil()