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

# class = juste un type


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
            self.image.append(liste_largeur)
            cpt_longueur+=1
        print(self.image)

    def get_width(self):
        return(len(self.image[0]))

    def get_length(self):
        return(len(self.image))

    def get_pixel(self, i, j):
        largeur = image.get_width()
        longueur = image.get_length()
        if i >= longueur:
            print("Les coordonnées sont incorrectes")
        elif j >= largeur:
            print("Les coordonnées sont incorrectes")
        else:
            print(self.image[i][j])

    def get_neighbours(self, i, j):
        largeur = image.get_width()
        longueur = image.get_length()
        # On vérifie que les coordonnées appartiennent bien à l'image
        if i >= longueur or j >= largeur:
            print("Les coordonnées sont incorrectes")
        else:
            if longueur <= 2:
               print("longueur <= 2")
            elif largeur <= 2:



image = Pictures()
image.init_white(3, 2)
image.get_pixel(2, 1)
image.get_neighbours(1, 1)


