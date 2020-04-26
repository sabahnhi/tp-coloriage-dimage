from dossier_code.classe_coloriage_image import Pictures

picture = Pictures()

"""
Nous avions commencé à rendre le programme interactif

On a besoin de récupérer la largeur (entier) et la hauteur (entier) de l'utilisateur :

print("Saisissez la largeur de l'image (entier) : ")
largeur_saisie = int(input())
print("Saisir la hauteur de l'image (entier) : ")
hauteur_saisie = int(input())

picture.init_white(largeur_saisie, hauteur_saisie)
"""

# On crée une image blanche de 3 pixels par 3 pixels de large
print("Voici l'image blanche créée :")
picture.init_white(3, 3)

# On colorie les 3 pixels en diagonale
picture.color_pixel(0, 0, 0, 0, 0)  # On colorie le pixel (0, 0) en noir
picture.color_pixel(1, 1, 20, 20, 20)  # On colorie le pixel (1, 1) en une couleur quelconque
picture.color_pixel(2, 2, 0, 0, 0)  # On colorie le pixel (2, 2) en noir

# On affiche l'image modifiée
print("Voici l'image avec les 3 pixels en diagonale coloriés :")
picture.display()

# On récupère le pixel en position (1, 1)
print("Le pixel en position (1, 1) est :", picture.get_pixel(1, 1))
picture.get_pixel(1, 1)  # on s'attend à avoir le pixel de couleur (20, 20, 20) ==> OK

print("Les voisins du pixel en position (1, 1) ont pour coordonnées : ", picture.get_neighbours(1, 1))

"""
Je dois avouer que nous n'avons pas compris votre commentaire ci-dessous. 

De notre point de vue, les voisins du pixel (1, 1) sont les pixels au-dessus et en-dessous de lui, ainsi que ceux à sa gauche et à sa droite.

Les voisins du pixel en position (1, 1) sont donc les pixels (0, 1), (2, 1), (1, 0) et (1, 2).

Il est écrit dans l'énoncé : 'Un pixel a au maximum quatre proches voisins (un au-dessus, un au-dessous, un à gauche et un à droite)'
"""
# On s'attend à avoir le pixel en haut (0, 0, 0), en bas (255, 255, 255) et à droite (0, 0, 0)
