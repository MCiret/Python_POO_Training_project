""" https://www.tresfacile.net/tp-python-avec-solutions/
Exercice 60. Classe Compte bancaire

1) Créer une classe Python nommée CompteBancaire qui représente un compte bancaire, ayant pour attributs : numeroCompte (type numérique ) , nom (nom du propriétaire du compte du type chaine), solde.
2) Créer un constructeur ayant comme paramètres : numeroCompte, nom, solde.
3) Créer une méthode Versement() qui gère les versements.
4) Créer une méthode Retrait() qui gère les retraits.
5) Créer une méthode Agios() permettant d’appliquer les agios à un pourcentage de 5 % du solde
6) Créer une méthode afficher() permettant d’afficher les détails sur le compte
7) Donner le code complet de la classe CompteBancaire.
"""


class CompteBancaire:

    AGIOS_PERCENT = 5/100

    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def versement(self, versement):
        self.solde += versement

    def retrait(self, retrait):
        self.solde -= retrait

    def agios(self):
        self.solde -= self.solde * self.AGIOS_PERCENT

    def afficher(self):
        print(f"Le solde du compte n°{self.numeroCompte} appartenant à {self.nom} est de {self.solde}.")


def main():
    my_compte = CompteBancaire(321654123, "Ciret", 1000)
    my_compte.afficher()


main()

