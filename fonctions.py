



from joueur import *
from catastrophes import *
from control_rtta import *







#afficher les points sur le bon nombre de ressources



#POUR JOUER EXECUTER CE FICHIER  /!\

#Par livia gattacceca


def tour(joueur, nbjoueurs, mon, dev):
    nbjoueurs=nbjoueurs

    """Livia Gattacceca_
la fonction tour permet de réaliser toutes les operations qui constituent le tour, dans l'ordre.
Elle passe les dés au joueur suivant en fin de tour, et elle est rappelée (fonction récursive)
 tant que les conditions de fin ne sont pas réunies."""

    print('Le joueur', joueur.num, 'doit jouer maintenant.')
    #ecrire('Le joueur'+ str(joueur.num) + 'doit jouer maintenant.')

    destires = joueur.lancerdes(nbjoueurs)

    joueur.recupdes(destires)
    resoudre(joueur, destires)
    nourrir_cites(joueur)
    achat(joueur, mon, dev)
    achat_dev(joueur, dev)
    joueur.defaussermarchandise()
    joueur.nbtours += 1
    joueur = joueur.passerdes(mon)

    tour(joueur,nbjoueurs, mon, dev)   # fonction récursive


def Partie():
    """
    Livia Gattacceca-
    a exécuter pour jouer.
    initialise le plateau, et lance le jeu en appelant la fonction tour."""

    mon = Monuments()
    dev = Type.developpement(Type())

    nombrejoueurs=0
    while nombrejoueurs not in ['1', '2', '3', '4']:
        nombrejoueurs = input('Entrez le nombre de joueurs, entre 1 et 4 : ')
        #ecrire('Entrez le nombre de joueurs dans la boite de dialogue, entre 1 et 4 : ')
        #nombrejoueurs = button_valider
        #fenetre.wait_variable(nombrejoueurs)

        if nombrejoueurs == '1':
            joueur1 = Joueur(1)

        elif nombrejoueurs == '2':
            joueur1 = Joueur(1)
            joueur2 = Joueur(2)

            mon[2] = ['Monument indisponible', [0, 0], 0]
            mon[4] = ['Monument indisponible', [0, 0], 0]

        elif nombrejoueurs == '3':

            joueur1 = Joueur(1)
            joueur2 = Joueur(2)
            joueur3 = Joueur(3)

            mon[3] = ['Monument indisponible', [0, 0], 0]

        elif nombrejoueurs == '4':
            joueur1 = Joueur(1)
            joueur2 = Joueur(2)
            joueur3 = Joueur(3)
            joueur4 = Joueur(4)


        else:
            print("Erreur, veuillez rentrer 1,2,3 ou 4.")
            #ecrire("Erreur, veuillez rentrer 1,2,3 ou 4.")


    tour(joueur1, nombrejoueurs, mon, dev)




Partie()



