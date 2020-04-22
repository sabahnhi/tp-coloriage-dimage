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
        # il y avait quelques soucis dans les déclarations de variable
        # (subtilité du langage Python ==> c'est corrigé)
        cpt_longueur = 0
        while cpt_longueur < longueur:
            liste_largeur = []
            cpt_largeur = 0
            while cpt_largeur < largeur:
                liste_largeur.append(Pixel(255, 255, 255).get_pixel_color())
                cpt_largeur+=1
            self.image.append(liste_largeur)
            cpt_longueur+=1
        self.display()

    def get_width(self):
        return(len(self.image[0]))

    def get_length(self):
        return(len(self.image))

    def get_pixel(self, i, j):
        largeur = self.get_width()    #  attention à utiliser le self: on modifiait la variable "image" déclarée en bas
        longueur = self.get_length()  #  attention à utiliser le self: on modifiait la variable "image" déclarée en bas
        if i >= longueur:
            print("Les coordonnées sont incorrectes")
        elif j >= largeur:
            print("Les coordonnées sont incorrectes")
        else:
            print(self.image[i][j])
            return self.image[i][j]  # penser à faire un return pour pouvoir récupérer la valeur

    def display(self):
        """
        La méthode display affiche l'image
        """
        for i in range(self.get_length()):
            ligne = self.image[i]
            print(ligne)

    def color_pixel(self, i, j, entier_rouge, entier_vert, entier_bleu):
        """
        La méthode prend en paramètre les cordonnées du pixel (i, j) et une couleur RVB
        Elle modifie la couleur du pixel passé en paramètre dans l'image
        """
        self.image[i][j] = (entier_rouge, entier_vert, entier_bleu)

    def get_neighbours(self, i, j):
        largeur = image.get_width()
        longueur = image.get_length()
        # On vérifie que les coordonnées appartiennent bien à l'picture
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


