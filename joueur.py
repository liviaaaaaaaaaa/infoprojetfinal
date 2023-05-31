import random as rd
from control_rtta import *
import sys

#Par Livia Gattacceca

#Création d'une liste qui va contenir les objets joueurs
ListeJoueurs = []

#ces listes correspondent aux valeurs que prennent les marchandises 
lbois = [0, 1, 3, 6, 10, 15, 21, 28, 36]
lpierre = [0, 2, 6, 12, 20, 30, 42, 56]
lpoterie = [0, 3, 9, 18, 30, 45, 63]
ltissu = [0, 4, 12, 24, 40, 60]
llance = [0, 5, 15, 30, 50]


class Joueur():
    """Livia Gattacceca-
    permet de créer un joueur et de definir les methodes qui le concernent, soit :
    afficher sa fiche joueur, ainsi que
     lancer les dés, récuperer les ouvriers, nourriture, marchandises et les defausser"""


    def __init__(self, numerojoueur: int):

        self.num = numerojoueur
        self.points = 0
        self.bois = 0
        self.pierre = 0
        self.poterie = 0
        self.tissu = 0
        self.lance = 0
        self.nourriture = 3
        self.cites = 3
        self.casecites=0
        self.constructeurs = 0
        self.developpements = []
        self.monuments = []
        self.casemonuments=[[1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0]]
        self.pieces = 0
        self.nbtours = 0
        ListeJoueurs.append(self)

    """les property ici permettent d'avoir la valeur réelle des marchandises"""
    @property
    def boisreel(self):
        return lbois[self.bois]

    @property
    def pierrereel(self):
        return lpierre[self.pierre]

    @property
    def poteriereel(self):
        return lpoterie[self.poterie]

    @property
    def tissureel(self):
        return ltissu[self.tissu]

    @property
    def lancereel(self):
        return llance[self.lance]


    def __str__(self):

        "Affiche l'etat courant du joueur"

        return "\n" + 'Joueur ' + str(self.num) + "\n" + "\n" + \
            'cités : ' + str(self.cites) + "\n" + \
            'points : ' + str(self.points) + "\n" + \
            'constructeurs : ' + str(self.constructeurs) + "\n" + \
            'développements :' + str(self.developpements) + "\n" + \
            'monuments :' + str(self.monuments) + "\n" + \
            'nourriture : ' + str(self.nourriture) + "\n" + "\n" + \
            'MARCHANDISES :' + "\n" + \
            'bois : ' + str(self.bois) + " <-> " + str(self.boisreel) + "\n" + \
            'pierre : ' + str(self.pierre) + " <-> " + str(self.pierrereel) + "\n" + \
            'poterie : ' + str(self.poterie) + " <-> " + str(self.poteriereel) + "\n" + \
            'tissu : ' + str(self.tissu) + " <-> " + str(self.tissureel) + "\n" + \
            'lance : ' + str(self.lance) + " <-> " + str(self.lancereel) + "\n"

#ecrire('Le joueur' + str(self.num) + 'doit jouer maintenant.')

    def lancerdes(self, nombrejoueurs):
        """Livia Gattacceca- Lancerdes renvoie la liste desdes tirés par le joueur."""


        #la liste des contient les différentes "valeurs" que peuvent prendre les dés
        des = ['3 nourriture', '1 marchandise', '2 marchandises et un crane', '3 ouvriers',
               '2 nourriture ou 2 ouvriers',
               '7 pieces']
       
        destires = []  #cette liste contiendra les dés qui ont été tirés par le joueur
        nombredes = self.cites

        for i in range(nombredes):
            destires.append(des[rd.randrange(6)])   #on tire les dés de maniere aléatoire dans la liste des valeurs

        print('Résultat des dés : ' + str(destires))

        relances = 0
        while relances < 2:   #pour s'assurer qu'il n'y ait que deux relances

            choix = input('Voulez vous relancer des dés ? (Oui ou Non) :')

            try:     #pour éviter que le programme s'arrete a cause d'une erreur de frappe
                if choix.upper().strip() == 'OUI':
                    choixdes = input(
                        'Entrez le(s) numero(s) des dés que vous souhaitez relancer (Si plusieurs, les séparer par une virgule).')
                    choixdes = [int(a) for a in choixdes.split(",")]     #on crée une liste avec les numeros des dés a relancer
                    # Vérifier si le numéro de dé est valide
                    for elt in choixdes:
                        if elt < 1 or elt > len(destires):
                            raise ValueError("Numéro de dé invalide.")

                elif choix.upper().strip() == 'NON':
                    return destires

                else:
                    raise ValueError("Veuillez entrer 'Oui' ou 'Non'.")

                for i in range(len(choixdes)):

                    if destires[choixdes[i] - 1] != '2 marchandises et un crane':   
                        destires[choixdes[i] - 1] = des[rd.randrange(6)]           #on retire un dé
                    elif destires[choixdes[i] - 1] == '2 marchandises et un crane':
                        if int(nombrejoueurs) != 1:
                            print('Vous ne pouvez pas relancer le dé numéro ' + str(
                                int(choixdes[i])) + ' car il comporte un crane.')
                        else:
                            destires[choixdes[i] - 1] = des[rd.randrange(6)]

            except (ValueError, UnboundLocalError, SyntaxError, TypeError) as e: #cela permet de revenir dans la boucle while relances<2 en cas d'erreur de frappe, car on n'ajoute pas 1 au compteur de relances
                print('Erreur : ', e)
                relances -= 1

            relances += 1
            print('Résultat des dés : ' + str(destires))

        if 'Leadership' in self.developpements:     # les joueur ayant le leadership peuvent relancer une dernièere fois
            t = 0
            while t == 0:
                choix = input('Voulez vous relancer un dé ? (Oui ou Non) :')
                try:
                    if choix.upper() == 'OUI':
                        choixdes = int(input('Entrez le numéro du dé que vous souhaitez relancer.'))
                        # Vérifier si le numéro de dé est valide
                        if choixdes < 1 or choixdes > len(destires):
                            raise ValueError("Numéro de dé invalide.")

                    elif choix.upper() == 'NON':
                        return destires

                    else:
                        raise ValueError("Veuillez entrer 'Oui' ou 'Non'.")

                    destires[choixdes - 1] = des[rd.randrange(6)]
                    print('Résultat des dés : ' + str(destires))


                except (ValueError, UnboundLocalError, SyntaxError, TypeError) as e:
                    print('Erreur : ', e)
                    t -= 1

                t += 1

        print('Vos Lancers sont finis.')

        return destires


    def recupdes(self, destires):

        """recupdes permet au joueur de récuperer les marchandises/pieces/ouvriers/nourriture
        qu'il a tire aux des"""

        march = 0
        for i in destires:
            if i == '3 nourriture':
                self.nourriture += 3
                if 'Agriculture' in self.developpements:   #on applique aussi les effets de certains développements
                    self.nourriture+=1
            if i == '1 marchandise':
                march += 1
            if i == '2 marchandises et un crane':
                march += 2
            if i == '3 ouvriers':
                self.constructeurs += 3
                if 'Maconnerie' in self.developpements:
                    self.constructeurs+=1
            if i == '2 nourriture ou 2 ouvriers':
                choix = ''
                while choix != '1' and choix != '2':
                    choix = input('Voulez vous recuperer 2 nourriture (entrez 1) ou 2 ouvriers (entrez 2) ?')
                if choix == '1':
                    self.nourriture += 2
                    if 'Agriculture' in self.developpements:
                        self.nourriture += 1
                if choix == '2':
                    self.constructeurs += 2
                    if 'Maconnerie' in self.developpements:
                        self.constructeurs += 1
            if i == '7 pieces':
                if 'Finance' in self.developpements:
                    self.pieces+= 5
                self.pieces += 7
        if self.nourriture > 15:
            self.nourriture = 15   #le compteur de nourriture de va pas au dela de 15

        # maintenant on ajoute les marchandises, selon les règles
        #ce systeme permet qu'on les ajoute dans l'ordre et que si on arrive au bout on recommence jusqu'a l'epuisement des marhcandises gagnées.
        ca, cb, cc, cd, ce = 0, 0, 0, 0, 0   #compteurs de marchandises ajoutées : ca pour le bois, cb pour la pierre, etc
        for a in range(march): 
            #l'ordre des if est important ici, pour etre sur de n'ajouter qu'une marchandise pour chaque passage dans la bouvcle for
            
            if ce < cd:       #si le compteur ce < cd, cela veut dire que l'on a ajouté un tissu de plus que de lances, il faut donc ajouter une lance
                self.lance += 1
                ce += 1      #on ajoute 1 au compteur de lances ajoutées
            if cd < cc:      #si le compteur cd < cc, cela veut dire que l'on a ajouté une poterie de plus que de tissus, il faut donc ajouter un tissu
                self.tissu += 1
                cd += 1
            if cc < cb:
                self.poterie += 1
                cc += 1
            if cb < ca:       #si le compteur cb<ca, alors cela veut dire que l'on a ajouté un bois de plus que de pierre, et qu'il faut ajouter une pierre.
                self.pierre += 1
                cb += 1
            if ce == ca:       #si le compteur e est égal au compteur a, alors soit on a pas commencé a ajouter les marchandises, soit on en a ajouté une de chaque
                self.bois += 1     #on ajoute 1 au compteur de bois ajouté
                ca += 1
        if 'Carriere' in self.developpements:   #effet d'un développement
            if cb>0:
                self.pierre += 1

        #on s'assure que les quantités de marchandises ne dépassent pas le maximum        
        if self.bois > 8:
            self.bois = 8
        if self.pierre > 7:
            self.pierre = 7
        if self.poterie > 6:
            self.poterie = 6
        if self.tissu > 5:
            self.tissu = 5
        if self.lance > 4:
            self.lance = 4


    def defaussermarchandise(self):
        """defaussermarchandise permet au joueur de choisir quelle marhcandises il veut defausser s'il en a trop, car il a droit à un max de 6 marchandises"""
        nbmarchandise = self.bois + self.pierre + self.poterie + self.tissu + self.lance
        c = 0

        if 'Caravanes' in self.developpements: #les joueurs ayant la caravane peuvent tout garder
            pass
        elif nbmarchandise > 6:
            print(self)
            print('Vous devez défausser ', nbmarchandise - 6, ' marchandises.')
            print('Quelle(s) marchandise(s) voulez vous défausser?')
            print('Si plusieurs, les séparer par une virgule. ')
            choix = input('(Et si on souhaite défausser deux bois par exemple, on écrira bois, bois). ')
            choix = [a.strip() for a in choix.split(",")]

            if len(choix) != nbmarchandise - 6:
                print('Vous avez indiqué un mauvais nombre de marchandises.')
                self.defaussermarchandise()   #on rappelle la fonction pour permettre de rentrer une autre valeur
                return
            if len(choix) == nbmarchandise - 6:
                for a in choix:       #pour éviter que le programme s'arrete en cas d'erreur de frappe, et pour permettre de rentrer autre chose
                    if a != 'bois' and a != 'pierre' and a != 'poterie' and a != 'tissu' and a != 'lance':
                        print('Le nom des marchandises est erroné.')
                        self.defaussermarchandise()
                        return
                for a in choix:   #on retire les marchandises choisies
                    if a == 'bois' and self.bois > 0:
                        self.bois -= 1
                        c += 1
                    if a == 'pierre' and self.pierre > 0:
                        self.pierre -= 1
                        c += 1
                    if a == 'poterie' and self.poterie > 0:
                        self.poterie -= 1
                        c += 1
                    if a == 'tissu' and self.tissu > 0:
                        self.tissu -= 1
                        c += 1
                    if a == 'lance' and self.lance > 0:
                        self.lance -= 1
                        c += 1

            if c != len(choix):  #cela veut dire qu'on a pas pu defausser certaines marchandises, car le joueur n'en possedait pas dans des quantités suffisantes
                print("Vous devez choisir des marchandises que vous possédez dans des quantités suffisantes "
                      "pour les défausser")
                self.defaussermarchandise() #on rappelle la fonction (récursivité) pour que le joueur finisse de defausser ses marchandises
        return


    def passerdes(self,mon):

        """passerdes permet, en fin de tour, de passer les dés au joueur suivant,
            ainsi que de verifier si les conditions de fin du jeu sont vérifiées."""

        self.pieces=0      #les pieces reviennent a zero en fin de tour
        if self.conditionsfin(mon):              #si les conditions de fin sont atteintes pour ce joueur
            if self == ListeJoueurs[-1]:
                findujeu(ListeJoueurs)          #on arrete le jeu seulement si c'est le dernier joueur
                sys.exit()
            else:
                print("\n" + 'Ceci est le dernier tour.')
        if self != ListeJoueurs[-1]:           #si les conditions de fin ne sont pas atteintes, on renvoie le joueur suivant car c'est à son tour
            return ListeJoueurs[ListeJoueurs.index(self) + 1]
        else:
            return ListeJoueurs[0]          #dans le cas ou le joueur actuel est le dernier, on renvoie le premier joueur car c'est a son tour

   
    def conditionsfin(self, mon):
        """conditionsfin définit les conditions pour que le jeu s'arrete, 
    elle renvoie un bool. Elle est appelée dans passerdes"""
        monum=False
        monu=mon
        Listem=[]
        for i in monu:
            booli=False
            for j in ListeJoueurs:
                if i[0] in j.monuments:
                    booli=True
            if i[-1]!=0:
                booli=True
            Listem.append(booli)
        if Listem==[True, True, True, True, True, True, True]:   #si tous les monuments ont étés construits
            monum=True       #alors une condition est remplie

        unjoueur = False
        if len(ListeJoueurs) == 1:
            unjoueur = self.nbtours == 10     #si un joueur solitaire a fait 10 tours, le jeu s'arrete
        bool = len(self.developpements) > 4 or unjoueur or monum     #si une des conditions est remplie, on renvoie True
        return bool




def findujeu(ListeJoueurs):
    """Livia Gattacceca-
    findujeu est appelée si les condisitions de fin sont réunies,
    elle renvoie la liste des joueurs et leurs points triés dans l'ordre."""

    ListeJoueurs = ListeJoueurs


    for i in ListeJoueurs:
 #effet de certains développements
        if 'Architecture' in i.developpements:
            i.points+=len(i.monuments)
        if 'Empire' in i.developpements:
            i.points+=i.cites
    points = []      #on crée une liste des points des joueurs, pour pouvoir trouver le max et les mettre dans l'ordre dans la liste gagnants
    gagnants = []
    for i in ListeJoueurs:
        points.append(i.points)

    while len(points) > 0:
        maxi = max(points)
        nombre = points.count(maxi)     #si jamais deux joueurs ont le meme score
        for i in range(nombre):
            index = points.index(maxi)
            gagnants.append(["Joueur", ListeJoueurs[index].num, maxi])  #on ajoute les joueurs par ordre de points, avec leur rang et leur score
            points.pop(index)
    print('Voici une liste des joueurs par odre de points, et de leurs points. Bien joué!')
    return gagnants

