from vector import Vecteurs
import fltk


class Balle:

    # Constructeurs

    def __init__(self, couleur, position, direction, taille, tag):
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
            <int> tag
        Renvoie:
            None
        """
        self.couleur = couleur
        self.position = position
        self.direction = direction
        self.taille = taille
        self.tag = tag
        return None

    def __eq__(self, balle):
        """
        Permet de vérifier si deux objects sont égaux
        Arguments :
            <class '__main__.Balle'> balle : la balle a vérifier
        Renvoie:
            <bool> True : si égal
            <bool> False : si différent
        """
        return self.tag == balle.getTag()

    # Acesseurs

    def getTag(self):
        """
        Permet d'accéder au tag de la balle
        Arguments :
            None
        Renvoie :
            <int> tag : le tag
        """
        return self.tag

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

    def getDirection(self):
        """
        Permet d'accéder a la direction de la balle
        Arguments :
            None
        Renvoie :
            <list> direction : la direction
                [0] <int> x
                [1] <int> y
        """
        return self.direction

    def getTaille(self):
        """
        Permet d'accéder a la taille de la balle
        Arguments :
            None
        Renvoie :
            <int> taille : la taille
        """
        return self.taille

    # Mutateurs

    def setDirection(self, vec):
        """
        Permet de modifier la direction
        Arguments :
            <list> vec : le vecteur direction
                [0] <int> x
                [1] <in> y
        Renvoie:
            None
        """
        self.direction = vec
        return None

    def setDirectionX(self, x):
        """
        Permet de modifier la direction en x de la balle
        Arguments :
            <int> x : la nouvelle direction
        Renvoie : None
        """
        self.direction[0] = x
        return None

    def setDirectionY(self, y):
        """
        Permet de modifier la direction en y de la balle
        Arguments :
            <int> y : la nouvelle direction
        Renvoie : None
        """
        self.direction[1] = y
        return None

    def updatePosition(self, direc):
        """
        Permet de modifier la position en fonction de la direction
        Arguments :
            <list> direc : vecteur direction
        Renvoie : None
        """
        self.position[0] += direc[0]
        self.position[1] += direc[1]
        return None

    # Autres

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

    def update(self):
        """
        Permet de gérer l'affichage et la position de la balle
        Arguments :
            None
        Renvoie :
            None
        """
        self.updatePosition(self.direction)
        self.ifCollisionMur()
        self.dessine()
        return None

    def ifCollisionBalle(self, balles):
        """
        Permet de vérifier si collision avec une balle
        Arguments :
            <class '__main__.Balle'> balle : la balle a vérifier
        Renvoie:
            None
        """
        x, y = self.getPosition()
        taille = self.getTaille()
        for balle in balles:
            if self == balle:
                break

            x_balle, y_balle = balle.getPosition()
            taille_balle = balle.getTaille()
            distance = Vecteurs.distancePoints(x_balle, y_balle, x, y)

            if distance < taille + taille_balle:
                return self.collision(balle)
        return None

    def ifCollisionMur(self):
        """
        Permet de modifier la direction si collision avec un mur
        Arguments :
            <class '__main__.Balle'> balle : la balle a vérifier
        Renvoie:
            None
        """
        taille = self.getTaille()
        x, y = self.getPosition()
        vx, vy = self.getDirection()

        if x > 600 - self.taille or x < 0 + taille:
            self.setDirectionX(vx * -1)
        if y > 600 - self.taille or y < 0 + taille:
            self.setDirectionY(vy * -1)
        return None

    def collision(self, balle):
        """
        Permet de modifier la direction si collision avec une balle
        Arguments :
            <class '__main__.Balle'> balle : la balle a vérifier
        Renvoie:
            None
        """
        x, y = self.getPosition()
        x_balle, y_balle = balle.getPosition()
        taille = self.getTaille()
        taille_balle = balle.getTaille()

        cx, cy = Vecteurs.milieuVecteurs((x, y), (x_balle, y_balle))

        newVecteur = ((cx - x) / taille_balle, (cy - y) / taille_balle)
        newVecteurBall = ((cx - x_balle) / taille, (cy - y_balle) / taille)

        self.setDirection(Vecteurs.sommeVecteurs(self.direction, newVecteurBall))
        balle.setDirection(Vecteurs.sommeVecteurs(balle.direction, newVecteur))
        return None
