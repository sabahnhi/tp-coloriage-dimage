import pylint, coverage, pytest

class Pixel:

    """
    une classe qui modélise un pixel de l'image

    Attributs
    __________
    entier_rouge : int
        Valeur du rouge compris entre 0 et 255
    entier_vert : int
        Valeur du vert compris entre 0 et 255
    entier_bleu : int
        Valeur du bleu compris entre 0 et 255

    Methodes
    ________
    get_pixel_color()
        Renvoie la couleur du pixel
    """

    def __init__(self, entier_rouge, entier_vert, entier_bleu):
        self.entier_rouge = entier_rouge
        self.entier_vert = entier_vert
        self.entier_bleu = entier_bleu

    def get_pixel_color(self):
        return(self.entier_rouge, self.entier_vert, self.entier_bleu)


class Pictures:

    def __init__(self):
        self.image = []

    def init_white(self, longueur, largeur):
        cpt_longueur = 0
        cpt_largeur = 0
        liste_largeur = []
        pixel_blanc = Pixel(255, 255, 255)
        p = pixel_blanc.get_pixel_color()
        while cpt_largeur < largeur:
            liste_largeur.append(p)
            cpt_largeur+=1
        while cpt_longueur < longueur:
            self.append(liste_largeur)
            cpt_longueur+=1
        print(self)


Pictures.init_white([],3,2)