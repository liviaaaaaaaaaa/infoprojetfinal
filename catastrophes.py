from joueur import *

#Par Livia Gattacceca

def resoudre(joueur, destires):
    """Livia Gattacceca-
    permet d'appliquer les effets des desastres"""

    if joueur.nourriture < joueur.cites:
        Famine.declencher(Famine(), joueur)
    if destires.count('2 marchandises et un crane') == 2 and Secheresse.dev not in joueur.developpements:
        Secheresse.declencher(Secheresse(), joueur)
    if destires.count('2 marchandises et un crane') == 3:
        if len(ListeJoueurs) == 1 and Peste.dev not in joueur.developpements:
            Peste.declencher(Peste(), joueur)
        if len(ListeJoueurs) > 1:
            print("La peste touche vos ennemis.")
            for i in ListeJoueurs:
                if Peste.dev not in i.developpements and i != joueur:
                    Peste.declencher(Peste(), i)
    if destires.count('2 marchandises et un crane') == 4 and Invasion.dev not in joueur.developpements:
        Invasion.declencher(Invasion(), joueur)
    if destires.count('2 marchandises et un crane') == 5 or destires.count(
            '2 marchandises et un crane') == 6 or destires.count('2 marchandises et un crane') == 7:
        if Revolte.dev not in joueur.developpements:
            Revolte.declencher(Revolte(), joueur)
        elif Revolte.dev in joueur.developpements:
            for i in ListeJoueurs:
                if Revolte.dev not in i.developpements and i != joueur:
                    Revolte.declencher(Revolte(), i)


class Desastre():
    """Livia Gattacceca- classe mère, permet de prevenir le joueur lorsqu'un desastre s'applique.
     Chaque classe fille correspond a un désastre et permet de definir ses effets."""

    def declencher(self, joueur):
        print(self.nom, "a été déclenchée:", self.effet)





class Famine(Desastre):
    nom = "Famine"
    effet = "Vous perdez 1 point pour chaque ville que vous ne pouvez pas alimenter."
    dev = ''

    def declencher(self, joueur):
        super().declencher(joueur)
        joueur.points -= joueur.cites - joueur.nourriture


class Secheresse(Desastre):
    nom = "Secheresse"
    dev = 'Irrigation'
    effet = "Vous perdez 2 points."

    def declencher(self, joueur):
        super().declencher(joueur)
        # if self.dev not in joueur.developpements:
        joueur.points -= 2


class Invasion(Desastre):
    nom = "Invasion"
    effet = "Vous perdez 4 points."
    dev = 'Grande Muraille'

    def declencher(self, joueur):
        super().declencher(joueur)
        joueur.points -= 4


class Peste(Desastre):
    nom = "Peste"
    effet = "Perdez 3 points."
    dev = 'Medecine'

    def declencher(self, joueur):
        super().declencher(joueur)
        joueur.points -= 3


class Revolte(Desastre):
    nom = "Révolte"
    effet = "Vous perdez toutes vos marchandises (y compris celles que vous venez de collecter)."
    dev = 'Religion'

    def declencher(self, joueur):
        super().declencher(joueur)
        joueur.bois = 0
        joueur.pierre = 0
        joueur.poterie = 0
        joueur.tissu = 0
        joueur.lance = 0

