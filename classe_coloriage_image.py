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
        print(self.entier_rouge, self.entier_vert, self.entier_bleu)

pixel = Pixel(255, 255, 255)
pixel.get_pixel_color()