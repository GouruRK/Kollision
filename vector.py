from math import sqrt


class Vecteurs:

    def produitVectoriel(v1, v2):
        """
        Calcule le produit de deux vecteurs
        Arguments:
            <tuple> v1
                [0] <int> x
                [1] <int> y
            <tuple> v2
                [0] <int> x
                [1] <int> y
        Renvoie:
            <int>
        """
        return v1[0] * v2[1] - v2[0] * v1[1]

    def produitScalaire(v1, v2):
        """
        Calcule le produit scalaire de deux vecteurs
        Arguments:
            <tuple> v1
                [0] <int> x
                [1] <int> y
            <tuple> v2
                [0] <int> x
                [1] <int> y
        Renvoie:
            <int>
        """
        return v1[0] * v2[0] + v1[1] * v2[1]

    def distancePoints(xa, ya, xb, yb):
        """
        Calcule la distance entre deux points
        Arguments:
            <int> xa : abscisse point A
            <int> ya : ordonnée point A
            <int> xb : abscisse point B
            <int> yb : ordonnée point B
        Renvoie:
            <float>
        """
        return sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

    def sommeVecteurs(v1, v2):
        """
        Calcule la somme de deux vecteurs
        Arguments:
            <tuple> v1
                [0] <int> x
                [1] <int> y
            <tuple> v2
                [0] <int> x
                [1] <int> y
        Renvoie:
            <list>
                [0] <int> : somme des x
                [1] <int> : somme des y
        """
        return [v1[0] + v2[0], v1[1] + v2[1]]

    def milieuVecteurs(v1, v2):
        """
        Calcule le milieu de deux vecteurs
        Arguments:
            <tuple> v1
                [0] <int> x
                [1] <int> y
            <tuple> v2
                [0] <int> x
                [1] <int> y
        Renvoie:
            <list>
                [0] <int> x
                [1] <int> y
        """
        cx = (v1[0] + v2[0]) // 2
        cy = (v1[1] + v2[1]) // 2
        return [cx, cy]
