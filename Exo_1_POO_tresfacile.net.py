""" https://www.tresfacile.net/tp-python-avec-solutions/

Exercice 59. Classe Rectangle :
1) Ecrire une classe Rectangle permettant de construire un rectangle doté d’attributs longueur et largeur.
2) Créer une méthode Perimetre() permettant de calculer le périmètre du rectangle
et une méthode Surface() permettant de calculer la surface du rectangle
3) Créer les getters et setters -> inutile ici et pas dans la correction...
4) Créer une classe fille Parallelepipede héritant de la classe Rectangle et dotée en plus d’un attribut hauteur
et d’une autre méthode Volume() permettant de calculer le volume du Parallélépipède.
"""


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width


class Parallelepipede(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


def main():
    rect = Rectangle(3, 2)
    parallep = Parallelepipede(4, 3, 2)

    print(rect.length)
    print(rect.width)
    print(rect.perimeter())
    print(rect.area())
    print("=============")
    print(parallep.width, parallep.length, parallep.height)
    print(parallep.perimeter(), parallep.area(), parallep.volume())


main()


