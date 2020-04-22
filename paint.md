# Le pot de peinture (difficile)

Critères de notation:

* Difficulté du sujet choisi 
* Lisibilité du code
* Effort de groupe, au moins 1 commit par membre du groupe (pas de commit = pas de note!)

## Enoncé du problème

L'objectif est d'implémenter la fonctionnalité "pot de peinture" disponible dans Paint qui permet de remplir
uniformément une forme d’une couleur:

* On chosit une couleur `A`
* On clique sur un pixel de l'image d'une couleur `B`
* Tous les pixels voisins de couleur `B` sont coloriés en `A`

Exemple:

<img height="350" src="https://www.astucesinternet.com/data/paint.net/paint-net-outils-009.jpg">


## Modélisation

On souhaite modéliser l'image comme suit:

- une classe `Picture` qui modélise l'image
- une classe `Pixel` qui modélise un pixel de l'image

## Classe Pixel

Chaque pixel a une couleur RGB. Cette couleur est définie par 3 entiers compris entre 0 et 255. 
Chaque valeur indique la teneur en couleur primaire (R=red, G=green, B=blue).

La classe `Pixel` dispose donc de trois attributs qui correspondent à chacun de ces entiers.

## Classe Picture

Une image est composée d'un tableau à 2 dimensions de pixels. La classe `Picture` dispose donc d'un unique attribut:

* un tableau à 2 dimensions de pixels (on utilisera une liste de listes)

La classe dispose des méthodes suivantes:

* `init_white`: qui crée une image blanche de taille longueur x largeur 
* `get_witdh`: qui retourne la largeur de l'image (nombre de pixels)
* `get_height`: qui retourne la hauteur de l'image (nombre de pixels)
* `get_pixel`: qui prend en paramètre des coordonnées (i, j) et renvoie le pixel correspondant
* `get_neighbours`: qui prend en paramètre les coordonnées d'un pixel et retourne la liste des coordonnées (i, j) de ses proches voisins.

Un pixel a au maximum quatre proches voisins (un au-dessus, un au-dessous, un à gauche et un à droite).

## Implémentation

Soient `p` le pixel selectionné et `pixel_color` sa couleur. On notera `target_color` la couleur selectionnée.

L'algorithme de coloriage se déroule de la manière suivante :

* on crée une liste des pixels à traiter

* on ajoute le premier pixel `p` à cette liste

* tant que la liste n'est pas vide:

    * on récupère un pixel dans la liste
    
    * si ce pixel est de couleur `pixel_color` alors:
    
         * on le colorie en `target_color`
         
         * on ajoute tous ces proches voisins à la liste des pixels à traiter
         
    * on retire ce pixel de la liste

__Note:__

Bien penser à tester tous les cas (le pixel est au bord de l'image, la couleur choisie est la même que la couleur originale du pixel, etc.)

## Tests unitaires

Ecrire des tests unitaires vérifiant le bon fonctionnement des méthodes et fonctions implémentées.
