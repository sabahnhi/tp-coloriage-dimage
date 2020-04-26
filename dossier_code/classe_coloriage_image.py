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

    def init_white(self, largeur, hauteur):  # La largeur correspond au nombre de colonnes de pixels de l'image et la hauteur au nombre de lignes de pixels
        cpt_hauteur = 0
        while cpt_hauteur < hauteur:  # Pour chaque ligne (hauteur)
            liste_largeur = []
            cpt_largeur = 0
            while cpt_largeur < largeur:
                liste_largeur.append(Pixel(255, 255, 255).get_pixel_color())
                cpt_largeur += 1
            self.image.append(liste_largeur) # On ajoute le bon nombre de colonnes de pixels (largeur)
            cpt_hauteur += 1
        self.display()

    def get_width(self):  # Renvoie la largeur de l'image
        return len(self.image[0])  #self.image[0] correspond à la première ligne de pixels de notre image.
        # En récupérant, le nombre de pixels qui composent cette ligne, on récupère la largeur de l'image.

    def get_height(self):  # Renvoie la hauteur de l'image
        return len(self.image) # En récupérant, le nombre de lignes de pixels qui composent cette image, on récupère la hauteur de l'image.

    def get_pixel(self, i, j):  # Soit i la coordonnée en abscisse de notre image et j la coordonnée en ordonnée.
        largeur = self.get_width()
        hauteur = self.get_height()
        # On vérifie que les coordonnées sont valides.
        if i >= largeur:
            print("Les coordonnées sont incorrectes")
        elif j >= hauteur:
            print("Les coordonnées sont incorrectes")
        else:
            return self.image[j][i]  # Il faut bien penser à passer la coordonnée en ordonnée en premier.
            # En-effet, on accède d'abord à la ligne de pixels de notre image (ligne = hauteur = ordonnée), puis au pixel de cette ligne (colonne = abscisse)

    def display(self):
        """
        La méthode display affiche l'image
        """
        for i in range(self.get_height()):
            ligne = self.image[i]
            print(ligne)

    def color_pixel(self, i, j, entier_rouge, entier_vert, entier_bleu):
        """
        La méthode prend en paramètres les cordonnées du pixel (i, j) et une couleur RVB
        Elle modifie la couleur du pixel passé en paramètre dans l'image
        """
        largeur = self.get_width()
        hauteur = self.get_height()
        # On vérifie que les coordonnées appartiennent bien à l'image
        if i >= largeur or j >= hauteur:
            print("Les coordonnées sont incorrectes")
        else:
            self.image[j][i] = (entier_rouge, entier_vert, entier_bleu)  # Comme pour get_pixel, il faut bien penser à passer la coordonnée en ordonnée en premier.

    def get_neighbours(self, i, j):
        largeur = self.get_width()
        hauteur = self.get_height()
        voisins = []
        # On vérifie que les coordonnées appartiennent bien à l'image
        if i >= largeur or j >= hauteur:
            print("Les coordonnées sont incorrectes")
        else:
            if i - 1 >= 0:  # On vérifie si le pixel est dans la première colonne de pixels de l'image
                voisins.append((i - 1, j))  # Si ce n'est pas le cas, on peut ajouter le pixel à sa gauche comme son voisin
            if i + 1 < largeur:  # On vérifie si le pixel est dans la dernière colonne de pixels de l'image
                voisins.append((i + 1, j))  # Si ce n'est pas le cas, on peut ajouter le pixel à sa droite comme son voisin
            if j - 1 >= 0:  # On vérifie si le pixel est dans la première ligne de pixels de l'image
                voisins.append((i, j - 1))  # Si ce n'est pas le cas, on peut ajouter le pixel au-dessus comme son voisin
            if j + 1 < hauteur:  # On vérifie si le pixel est dans la dernière ligne de pixels de l'image
                voisins.append((i, j + 1))  # Si ce n'est pas le cas, on peut ajouter le pixel en-dessous comme son voisin
            return voisins
