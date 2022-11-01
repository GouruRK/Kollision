#######################################################
#######################################################
### Nom du fichier: kollision.py                    ###
### Date début: Lundi 11 Octobre                    ###
### Date fin: Dimanche 24 Octobre                   ###
### Auteurs : Rémy Kies et Loric Blanchard.         ###
### Principe: S'amuser                              ###
### Utilisation: python3 kollision.py --mode --level###
#######################################################
#######################################################


from random import uniform, randint
from player import Joueur
from balls import Balle
import argparse
import fltk
import time


def gestionTemps(temps):
    """
    Permet de convertir le temps
    Arguments :
        <float> temps : temps en seconde a convertir
    Renvoie :
        <tuple> : Tuple de trois éléments
            [0] : <int> minutes
            [1] : <int> secondes
            [3] : <int> dixièmes de secondes
    """
    millisecondes = round(abs(int(temps) - temps), 2)
    millisecondes = str(millisecondes)[2:]
    seconde = int(temps) % 60
    minute = int(temps) // 60
    return minute, seconde, int(millisecondes)


def afficheTemps(t):
    """
    Permet d'afficher le temps
    Arguments :
        <list> t : Le temps
            [0] <int> : minutes
            [1] <int> : secondes
    Renvoie :
        None
    """
    fltk.texte(
        10,
        10,
        f"{t[0]}m {t[1]}s",
        police="Courier",
        taille=72,
        couleur="black",
        ancrage="nw",
    )
    return None


def checkpos(balle, joueur):
    """
    Permet de vérifier qu'une nouvelle balle n'est pas imbriquée
    dans la balle du joueur
    Arguments :
        <list> balle
            [0] <int> x
            [1] <int> y
        <class '__main__.Joueur'> : la balle du joueur
    Renvoie :
        <bool> True : si imbriquée
        <bool> False : sinon
    """
    x, y = balle
    x_joueur, y_joueur = joueur.getPosition()

    return (x_joueur - 30 < x < x_joueur + 30) and (y_joueur - 30 < y < y_joueur + 30)


def genBalle(joueur, tag, mini, maxi):
    """
    Permet de générer une balle qui n'est pas imbriquée dans
    la balle du joueur
    Arguments :
        <class '__main__.Joueur'> joueur : la balle du joueur
        <int> tag : le tag de la nouvelle balle
        <int> mini : valeur minimale de la vitesse aléatoire
        <int> maxi : valeur maximale de la vitesse aléatoire
    Renvoie :
        <class '__main__.Balle'> la nouvelle balle
    """
    pos = [randint(15, 585), randint(15, 585)]
    while checkpos(pos, joueur):
        pos = [randint(15, 585), randint(15, 585)]
    return Balle("red", pos, [uniform(mini, maxi), uniform(mini, maxi)], 15, tag)


def update_position(joueur, objets):
    """
    Permet de mettre a jour les dernières positions
    Arguments :
        <class '__main__.Joueur'> joueur : la balle du joueur
        <list> objets : liste contenant les balles
    Renvoie :
        None
    """
    joueur.update()
    for balle in objets:
        balle.update()
    return None


def scene(args):
    """
    Permet d'afficher la fenêtre et de gérer les imputs
    Arguments :
        <dic> args : les arguments transmis lors de l'appel du programme
            ["mode"] : <str> le mode de jeu
    Renvoie :
        <int> 0 si on ferme la fenêtre
        <int> 1 si on clique pour rejouer
    """
    level = {1: 30, 2: 15, 3: 5}
    joueur = Joueur("blue", [300, 300], 15)
    nb_balles = 4
    timeControl = 1
    mini = args["minimum"] * -1
    maxi = args["maximum"]
    
    objets = []
    for tag in range(nb_balles):
        objets.append(genBalle(joueur, tag, mini, maxi))

    fltk.cree_fenetre(600, 600)
    afficheTemps([0, 0])
    for balle in objets:
        balle.dessine()
    joueur.dessine()

    while True:
        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)
        
        if tev == "Quitte":
            fltk.ferme_fenetre()
            return 0
        if tev == "ClicGauche":
            break
        fltk.mise_a_jour()
    d = time.time()

    while True:
        f = gestionTemps(time.time() - d)
        afficheTemps(f)

        if time.time() - d > timeControl * level[args["level"]]:
            objets.append(genBalle(joueur, nb_balles, mini, maxi))
            nb_balles += 1
            timeControl += 1

        ev = fltk.donne_ev()
        tev = fltk.type_ev(ev)

        if tev == "Quitte":
            fltk.ferme_fenetre()
            return 0

        fltk.efface_tout()
        afficheTemps(f)
        joueur.update()
        for balle in objets:
            balle.update()
            if args["mode"] == "solide":
                balle.ifCollisionBalle(objets)
                
            if joueur.ifCollisionBalleJoueur(objets):
                afficheTemps(f)
                update_position(joueur, objets)
                while True:
                    ev = fltk.donne_ev()
                    tev = fltk.type_ev(ev)

                    if tev == "Quitte":
                        fltk.ferme_fenetre()
                        return 0

                    if tev == "ClicGauche":
                        fltk.ferme_fenetre()
                        return 1

                    fltk.mise_a_jour()
        fltk.mise_a_jour()
    fltk.ferme_fenetre()
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Jouer à Kollision")
    parser.add_argument(
        "--mode",
        "-m",
        type=str,
        action="store",
        required=False,
        choices=["gazeux", "solide"],
    )
    parser.add_argument(
        "--level", "-l", type=int, action="store", required=False, choices=[1, 2, 3]
    )
    parser.add_argument(
        "--minimum",
        "-min",
        type=int,
        action="store",
        required=False,
        choices=[3, 4, 5, 6, 7, 8, 9],
    )
    parser.add_argument(
        "--maximum",
        "-max",
        type=int,
        action="store",
        required=False,
        choices=[3, 4, 5, 6, 7, 8, 9],
    )
    args = vars(parser.parse_args())
    if args["level"] is None:
        args["level"] = 1
    if args["minimum"] is None:
        args["minimum"] = 3
    if args["maximum"] is None:
        args["maximum"] = 3
    while True:
        t = scene(args)
        if t == 0:
            break
