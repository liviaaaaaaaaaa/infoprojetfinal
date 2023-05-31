import numpy
#import fonctions
'''Marie Lissillour 
Classe Type contenant les cites et les developpements pour faciliter le traitement des données 
relatives à chacun par la suite'''


class Type:
    # def __init__(self, ):
    # self.nom = nom

    """Marie Lissillour
    renvoie en fonction du nombre actuel de cités d'un joueur le nombre de constructeurs
    nécessaires pour construire la cité suivante"""

    def cites(self, joueur):
        if joueur.cites == 3:
            nb_const = 3
        if joueur.cites == 4:
            nb_const = 4
        if joueur.cites == 5:
            nb_const = 5
        if joueur.cites == 6:
            nb_const = 6
        return nb_const

    '''Marie Lissillour
    création d'une liste contenant les informations sur chaque développement'''

    def developpement(self):
        developpement = [[1, 'Leadership', 10, 2], [2, 'Irrigation', 10, 2], [3, 'Agriculture', 15, 3],
                         [4, 'Carriere', 15, 3], [5, 'Medecine', 15, 3], [6, 'Finance', 20, 4], [7, 'Caravanes', 20, 4],
                         [8, 'Religion', 20, 6], [9, 'Grenier', 30, 6], [10, 'Maconnerie', 30, 6],
                         [11, 'Ingenieurie', 40, 6], [12, 'Architecture', 50, 8], [13, 'Empire', 60, 8]]
        # [numéro du développement, nom du développement, coût, nb de points que ça rapporte]
        return developpement


'''Marie Lissillour
Class Monuments qui permet de référencer les différents monuments avec leurs propriétés propres'''

class Monuments(list):
    def __init__(self):
        super().__init__()
        self.ajouter_monuments()

    def ajouter_monument(self, nom, pts, nb_constructeurs):
        self.append([nom, pts, nb_constructeurs])

    '''Marie Lissillour
    création de la liste contenant les infos des monuments'''

    def ajouter_monuments(self):  # [nom du monument, nombre de points qu'il rapporte, nombre de constructeurs nécessaires]
        self.ajouter_monument('Petite pyramide', [1, 0], 3)
        self.ajouter_monument('Stonehenge', [2, 1], 5)
        self.ajouter_monument('Temple', [4, 2], 7)
        self.ajouter_monument('Jardins suspendus', [8, 4], 11)
        self.ajouter_monument('Grande pyramide', [12, 6], 15)
        self.ajouter_monument('Grande muraille', [10, 5], 13)
        self.ajouter_monument('Obélisque', [6, 3], 9)


'''Marie Lissillour
à chaque tour nourrissage des cités'''

def nourrir_cites(joueur):
    if joueur.nourriture > joueur.cites:
        joueur.nourriture -= joueur.cites
    else:
        joueur.nourriture = 0
        # lancer catastrophe



'''Marie Lissillour
placement des constructeurs afin de batir progressivement les cités et les monuments
Interraction'''

def achat(joueur, mon, dev):  # fonction construire progressivement les cités ou les monuments
    while joueur.constructeurs != 0:
        print("Vous avez " , joueur.constructeurs , "constructeurs")
        if joueur.cites != 7:
            print('0 : cités, nombre de cases à cocher pour construire la prochaine cité :' , (
                        Type.cites(Type(),joueur) - joueur.casecites) , '\n')
        if not (mon[0] in joueur.monuments):
            print('1 : Petite Pyramide, nombre de cases à cocher avant la construction :' , (
                        mon[0][2] - joueur.casemonuments[0][1]) , '\n')
        if not (mon[1] in joueur.monuments):
            print('2 : Stonehenge, nombre de cases à cocher avant la construction :' , (
                        mon[1][2] - joueur.casemonuments[1][1]) , '\n')
        if not (mon[2] in joueur.monuments):
            print('3 : Temple, nombre de cases à cocher avant la construction :' , (
                        mon[2][2] - joueur.casemonuments[2][1]) , '\n')
        if not (mon[3] in joueur.monuments):
            print('4 : Jardins suspendus, nombre de cases à cocher avant la construction :' , (
                        mon[3][2] - joueur.casemonuments[3][1]) , '\n')
        if not (mon[4] in joueur.monuments):
            print('5 : Grande Pyramide, nombre de cases à cocher avant la construction :' , (
                        mon[4][2] - joueur.casemonuments[4][1]) , '\n')
        if not (mon[5] in joueur.monuments):
            print('6 : Grande Muraille, nombre de cases à cocher avant la construction :' , (
                        mon[5][2] - joueur.casemonuments[5][1]) , '\n')
        if not (mon[6] in joueur.monuments):
            print('7 : Obélisque, nombre de cases à cocher avant la construction :' , (
                        mon[6][2] - joueur.casemonuments[6][1]) , '\n')
        construction = input('Que voulez-vous construire ? Rentrez seulement un numéro, cela cochera une case das la construction indiquée.')
        try:
            num = int(construction)

            if num == 0:  # construction de cité
                joueur.casecites += 1
                if joueur.casecites == Type.cites(Type(),joueur):
                    joueur.cites += 1
                    joueur.casecites = 0
                    print("Vous avez acheté une cité supplémentaire. Vous avez maintenant " , joueur.cites , " cités")
            else:  # construction de monument
                joueur.casemonuments[num - 1][1] += 1  # ajout d'une case constructeur à la construction
                if joueur.casemonuments[num - 1][1] == mon[num - 1][2]:  # si le batiment peut être construit
                    joueur.monuments.append(mon[num - 1][0])
                    joueur.points += mon[num - 1][1][0]
                    mon[num - 1][1].pop(0)
                    print("Vous avez acheté" , mon[num - 1][0])
            joueur.constructeurs -= 1

        except(ValueError, UnboundLocalError, SyntaxError, TypeError)as e:
            print('Erreur',e)
    if dev[11] in joueur.developpements and joueur.pierre != 0:
        reponse = input("Voulez-vous utiliser de la pierre pour continuer à batir ?")
        if reponse.upper == "OUI":
            reponse2 = input(
                "Combien de pierres voulez-vous vendre ? (Pour rappel, vous avez " + joueur.pierre + "pierres")
            while type(reponse2)!= int:
                print("Veuillez rentrer un chiffre.")
                reponse2 = input(
                    "Combien de pierres voulez-vous vendre ? (Pour rappel, vous avez " + joueur.pierre + "pierres")
            while int(reponse2) not in range(joueur.pierrereel + 1):
                print("Vous m'avez pas ce nombre de pierres")
                reponse2 = input(
                    "Combien de pierres voulez-vous vendre ? (Pour rappel, vous avez " + joueur.pierre + "pierres")
            joueur.constructeurs += 3 * int(reponse2)
            joueur.pierre-=reponse2
            achat(joueur)    #fonction récursive






def achat_dev(joueur, dev):  # achat de développement
    '''Marie Lissillour et Livia Gattacceca
    achat des développements'''

    monnaie = joueur.pieces + joueur.boisreel + joueur.pierrereel + joueur.poteriereel + joueur.tissureel + joueur.lancereel
    if 'Grenier' in joueur.developpements:
        monnaie+=joueur.nourriture
    dev_dispo = []
    achetes = []
    for i in range(len(dev)):
        if dev[i][1] not in joueur.developpements:  # création d'une liste avec les développements non achetés
            dev_dispo.append(dev[i])
        else:
            achetes.append(i+1)  # liste des developpements deja achetés par le joueur
    c=0
    for i in dev_dispo:
        if i[2]<= monnaie:
            c+=1


    if c==0:
        return

    print(dev_dispo)
    for l in range(len(dev_dispo)):
        print(str(dev_dispo[l][0]) , " : " + dev_dispo[l][1] , ", à " , dev_dispo[l][2] , "pièces" , "\n")

    print('développement maximal autorisé: ', c)
    reponse = input("Voulez-vous acheter un développement ?")
    reponse=reponse.upper()
    while reponse.upper().strip()!='OUI' and reponse.upper().strip!='NON':
        print(reponse.upper().strip())
        reponse=input('Rentrez Oui ou Non.')
    if reponse.upper().strip() == "OUI":
        reponse = input("Que voulez-vous acheter ?")
        while reponse.strip()!= '0' and reponse.strip()!='1' and reponse.strip() != '2' and reponse.strip()!= '3' and reponse.strip()!='4' and reponse.strip() != '5' and reponse.strip()!= '6' and reponse.strip()!='7' and reponse.strip() != '8' and reponse.strip()!= '9' and reponse.strip()!='10' and reponse.strip() != '11' and reponse.strip()!= '12' and reponse.strip()!='13' :
            reponse = input("Que voulez-vous acheter ? Entrez un chiffre.")
        achat = int(reponse.strip())
        while achat in achetes or achat>c: #dev[int(achat)-1][2] >= monnaie:
            print("Vous avez déjà acheté ce développement, ou il est trop cher, veuillez en choisir un autre")
            reponse = input("Que voulez-vous acheter ?")
            while reponse.strip() not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"] or dev[achat - 1][2] >= monnaie:
                reponse = input("Que voulez-vous acheter ? Entrez un autre chiffre, ce développement est trop cher ou n'existe pas.")
            achat = int(reponse)
        if dev[achat-1][2] <= monnaie:
            print("Vous avez acheté" , dev[achat - 1][1])
            joueur.developpements.append(dev[achat - 1][1])
            joueur.points += dev[achat - 1][3]
            paye = 0
            payement = [joueur.pieces, joueur.boisreel, joueur.pierrereel, joueur.poteriereel, joueur.tissureel,
                        joueur.lancereel, joueur.nourriture]
            while paye < dev[achat - 1][2]:
                print(
                    "0 : pièces" + "\n" + "1 : bois" + "\n" + "2 : pierre" + "\n" + "3 : poterie" + "\n" + "4 : tissu" + "\n" + "5 : lance" + "\n" + "6 : nourriture, seulement si vous avez le grenier.")
                espece = input("Que voulez vous utiliser ? ")
                while espece.strip()not in ['0', '1', '2', '3', '4', '5', '6']:
                    espece=input('Que voulez-vous utiliser? Entrez un chiffre entre 0 et 6.')
                while int(espece) not in range(7):
                    print("Ce moyen de paiement n'existe pas. Veuillez-choisir une des propositions ci-dessus ")
                    espece = input("Que voulez vous utiliser ? ")
                paye += payement[int(espece)]
                print('payé : ', paye)
                if Type.developpement(Type())[9][1] not in joueur.developpements and int(espece)==6:
                    print('Vous ne pouvez pas utiliser la nourriture pour payer.')
                    espece=input("Que voulez vous utiliser ? Hors nourriture.")
                    while espece.strip() not in ['0', '1', '2', '3', '4', '5', '6']:
                        espece = input('Que voulez-vous utiliser? Entrez un chiffre entre 0 et 5.')
                if Type.developpement(Type())[9][1] in joueur.developpements:  # si le joueur a le grenier
                    if int(espece) == 6:
                        joueur.piece += 4 * joueur.nourriture
                payement[int(espece)] = 0

    joueur.pieces = 0


