#Korišdenjem programskog jezika Python, napisati funkciju numlista, koja iz liste koja može da sadrži elemente različitog tipa izdvaja vrednosti po tipu i smešta ih u rečnik.
# Napomena: Naziv tipa može da se preuzme korišćenjem atributa __name__ nad samim tipom podataka.

import string


def numlista(elementi):
    rezultat={
        'str':[el for el in elementi
               if type(el).__name__== 'str'],
        'int':[el for el in elementi
               if type(el).__name__=='int'],
        'list':[el for el in elementi
                if type(el).__name__=='list']

    }
    return rezultat

print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]]))