from dossier_code.classe_coloriage_image import Pictures
from unittest import TestCase

picture = Pictures()


class TestPictures(TestCase):

    def test_get_pixel(self):
        self.assertEqual((50, 50, 50), picture.get_pixel(2, 1))  # On vérifie qu'on récupère bien un pixel coloré et non un pixel blanc
        self.assertEqual((50, 50, 50), picture.get_pixel(1, 1))  # On vérifie que si l'on récupère un pixel blanc, le test échoue

    def test_get_neighbours(self):
        self.assertEqual([(0, 1), (2, 1), (1, 0)], picture.get_neighbours(1, 1))  # On vérifie que les voisins attendus sont les bons
        self.assertEqual([(1, 0), (0, 1)], picture.get_neighbours(0, 0))  # On vérifie qu'il n'y a que deux voisins pour un pixel dans un coin
        self.assertNotEqual([(-1, 0), (1, 0), (0, -1), (0, 1)], picture.get_neighbours(0, 0))  # On vérifie qu'on ne prend pas de coordonnées négatives si un pixel est dans le coin en haut à gauche


picture.init_white(4, 2)  # Besoin de créer une image pour tester la class get_neighbours
picture.color_pixel(2, 1, 50, 50, 50)  # On colorie le pixel aux coordonnées (2, 1) pour vérifier qu'on récupère bien ce dernier et non un pixel blanc avec get_pixel()
