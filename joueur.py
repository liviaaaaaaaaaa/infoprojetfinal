import random as rd
from control_rtta import *
import sys
nouveau 
#Par Livia Gattacceca

ListeJoueurs = []

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



        des = ['3 nourriture', '1 marchandise', '2 marchandises et un crane', '3 ouvriers',
               '2 nourriture ou 2 ouvriers',
               '7 pieces']
        destires = []
        nombredes = self.cites

        for i in range(nombredes):
            destires.append(des[rd.randrange(6)])

        print('Résultat des dés : ' + str(destires))

        relances = 0
        while relances < 2:

            choix = input('Voulez vous relancer des dés ? (Oui ou Non) :')

            try:
                if choix.upper().strip() == 'OUI':
                    choixdes = input(
                        'Entrez le(s) numero(s) des dés que vous souhaitez relancer (Si plusieurs, les séparer par une virgule).')
                    choixdes = [int(a) for a in choixdes.split(",")]
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
                        destires[choixdes[i] - 1] = des[rd.randrange(6)]
                    elif destires[choixdes[i] - 1] == '2 marchandises et un crane':
                        if int(nombrejoueurs) != 1:
                            print('Vous ne pouvez pas relancer le dé numéro ' + str(
                                int(choixdes[i])) + ' car il comporte un crane.')
                        else:
                            destires[choixdes[i] - 1] = des[rd.randrange(6)]

            except (ValueError, UnboundLocalError, SyntaxError, TypeError) as e:
                print('Erreur : ', e)
                relances -= 1

            relances += 1
            print('Résultat des dés : ' + str(destires))

        if 'Leadership' in self.developpements:
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
                if 'Agriculture' in self.developpements:
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
            self.nourriture = 15

        # maintenant on ajoute les marchandises
        ca, cb, cc, cd, ce = 0, 0, 0, 0, 0
        for a in range(march):
            if ce < cd:
                self.lance += 1
                ce += 1
            if cd < cc:
                self.tissu += 1
                cd += 1
            if cc < cb:
                self.poterie += 1
                cc += 1
            if cb < ca:
                self.pierre += 1
                cb += 1
            if ce == ca:
                self.bois += 1
                ca += 1
        if 'Carriere' in self.developpements:
            if cb>0:
                self.pierre += 1

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
        """defaussermarchandise permet au joueur de choisir quelle marhcandises il veut defausser s'il en a trop"""
        nbmarchandise = self.bois + self.pierre + self.poterie + self.tissu + self.lance
        c = 0

        if 'Caravanes' in self.developpements:
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
                self.defaussermarchandise()
                return
            if len(choix) == nbmarchandise - 6:
                for a in choix:
                    if a != 'bois' and a != 'pierre' and a != 'poterie' and a != 'tissu' and a != 'lance':
                        print('Le nom des marchandises est erroné.')
                        self.defaussermarchandise()
                        return
                for a in choix:
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

            if c != len(choix):
                print("Vous devez choisir des marchandises que vous possédez dans des quantités suffisantes "
                      "pour les défausser")
                self.defaussermarchandise()
        return


    def passerdes(self,mon):

        """passerdes permet, en fin de tour, de passer les dés au joueur suivant,
            ainsi que de verifier si les conditions de fin du jeu sont vérifiées."""

        self.pieces=0
        if self.conditionsfin(mon):
            if self == ListeJoueurs[-1]:
                findujeu(ListeJoueurs)
                sys.exit()
            else:
                print("\n" + 'Ceci est le dernier tour.')
        if self != ListeJoueurs[-1]:
            return ListeJoueurs[ListeJoueurs.index(self) + 1]
        else:
            return ListeJoueurs[0]

    """conditionsfin définit les conditions pour que le jeu s'arrete, 
    elle renvoie un bool. Elle est appelée dans passerdes"""
    def conditionsfin(self, mon):
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
        if Listem==[True, True, True, True, True, True, True]:
            monum=True

        unjoueur = False
        if len(ListeJoueurs) == 1:
            unjoueur = self.nbtours == 10
        bool = len(self.developpements) > 4 or unjoueur or monum
        return bool




def findujeu(ListeJoueurs):
    """Livia Gattacceca-
    findujeu est appelée si les condisitions de fin sont réunies,
    elle renvoie la liste des joueurs et leurs poinrs triés dans l'ordre."""

    ListeJoueurs = ListeJoueurs


    for i in ListeJoueurs:
        if 'Architecture' in i.developpements:
            i.points+=len(i.monuments)
        if 'Empire' in i.developpements:
            i.points+=i.cites
    points = []
    gagnants = []
    for i in ListeJoueurs:
        points.append(i.points)

    while len(points) > 0:
        maxi = max(points)
        nombre = points.count(maxi)
        for i in range(nombre):
            index = points.index(maxi)
            gagnants.append(["Joueur", ListeJoueurs[index].num, maxi])
            points.pop(index)
    print('Voici une liste des joueurs par odre de points, et de leurs points. Bien joué!')
    return gagnants

