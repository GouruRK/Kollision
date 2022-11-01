from vector import Vecteurs
import fltk


class Joueur:

    # Constructeurs

    def __init__(self, couleur, position, taille):
        """
        Initialisation de l'objet
        Arguments :
            <str> couleur
            <list> position
                [0] <int> x
                [1] <int> y
            <list> direction
                [0] <int> x
                [1] <int> y
            <int> taille
        Renvoie :
            None
        """
        self.couleur = couleur
        self.position = position
        self.taille = taille

        return None

    # Acesseurs

    def getPosition(self):
        """
        Permet d'accéder a la position de la balle
        Arguments :
            None
        Renvoie :
            <list> position : la position
                [0] <int> x
                [1] <int> y
        """
        return self.position

    def getTaille(self):
        """
        Permet d'accéder a la taille de la balle
        Arguments :
            None
        Renvoie :
            <int> taille : la taille
        """
        return self.taille

    def setPositionX(self, x):
        """
        Permet de modifier la position en x de la balle
        Arguments :
            <int> x : la nouvelle position
        Renvoie :
            None
        """
        self.position[0] = x
        return None

    def setPositionY(self, y):
        """
        Permet de modifier la position en x de la balle
        Arguments :
            <int> x : la nouvelle position
        Renvoie :
            None
        """
        self.position[1] = y
        return None

    def updatePosition(self, x, y):
        """
        Permet de modifier la position de la balle
        Arguments :
            <int> x
            <int> y
        Renvoie :
            None
        """
        self.position[0] = x
        self.position[1] = y
        return None

    # Autre

    def dessine(self):
        """
        Permet d'afficher la balle
        Arguments :
            None
        Renvoie :
            None
        """
        x = self.position[0]
        y = self.position[1]
        fltk.cercle(x, y, self.taille, couleur=self.couleur, remplissage=self.couleur)
        return None

    def coordsCursor(self):
        """
        Permet d'accéder aux coordonnées du curseur
        Arguments :
            None
        Renvoie :
            <tuple> (x,y)
                [0] <int> x
                [1] <int> y
        """
        x = fltk.abscisse_souris()
        y = fltk.ordonnee_souris()
        return x, y

    def update(self):
        """
        Permet de gérer l'affichage et la position de la balle
        Arguments :
            None
        Renvoie :
            None
        """
        x, y = self.coordsCursor()
        self.updatePosition(x, y)
        self.ifCollisionMur()
        self.dessine()
        return None

    def ifCollisionBalleJoueur(self, balles):
        """
        Permet de savoir si collision entre joueur et balle
        Arguments:
            <class '__main__.Balle'> balle : la balle a vérifier
        Revoie :
            <bool> True : si collision
            <bool> False : sinon
        """
        x, y = self.getPosition()
        taille = self.getTaille()

        for balle in balles:
            x_balle, y_balle = balle.getPosition()
            taille_balle = balle.getTaille()
            distance = Vecteurs.distancePoints(x_balle, y_balle, x, y)

            if distance < taille + taille_balle:
                return True
        return False

    def ifCollisionMur(self):
        """
        Permet de savoir si collision avec un mur
        Arguments:
            None
        Renvoie :
            None
        """
        taille = self.getTaille()
        x, y = self.getPosition()

        if x > 600 - taille:
            self.setPositionX(600 - taille)
        elif x < 0 + taille:
            self.setPositionX(0 + taille)
        if y > 600 - taille:
            self.setPositionY(600 - taille)
        elif y < 0 + taille:
            self.setPositionY(0 + taille)
        return None
