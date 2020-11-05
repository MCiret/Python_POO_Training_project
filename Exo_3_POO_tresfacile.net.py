""" https://www.tresfacile.net/tp-python-avec-solutions/
Exercice 63

Coder une classe myString permettant de doter les chaines de caractères des méthodes append() et pop() faisant les
mêmes opérations que celles des listes. Exemple si on crée  des chaines via l’instanciation s1 = myString(“Hello”) et
s2 = “bonjour”, et on lui applique les méthodes :

print(s1.append(" world !")) # affiche  'Hello world !'
print(s2.pop(2))  # affiche 'bojour'
"""


class MyString:

    def __init__(self, string):
        self.string = string

    def append(self, string_added):
        res_string = self.string + string_added
        return res_string

    def pop(self, int_pop):
        res_string = self.string[:int_pop] + self.string[int_pop+1:]
        return res_string


def main():
    s1 = MyString("Hello")
    s2 = MyString("bonjour")

    print(s1.append(" world !"))
    print(s2.pop(2))


main()
