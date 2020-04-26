from dossier_code.classe_coloriage_image import Pictures


picture = Pictures()
picture.init_white(3, 3)

picture.color_pixel(0, 0, 0, 0, 0)  # je colorie le pixel (0, 0) en noir
picture.color_pixel(1, 1, 20, 20, 20)  # je colorie le pixel (1, 1) en une couleur quelconque
picture.color_pixel(2, 2, 0, 0, 0)  # je colorie le pixel (2, 2) en noir

print("apres")
picture.display()

print("pixel en position (1, 1)")
picture.get_pixel(1, 1)  # on s'attend à avoir le pixel de couleur (20, 20, 20) ==> OK

print("voisins du pixel en position (1, 1)")
print(picture.get_neighbours(1, 1))
# On s'attend à avoir le pixel en haut (0, 0, 0), en bas (255, 255, 255) et à droite (0, 0, 0)
