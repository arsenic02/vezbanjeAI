# Korišdenjem programskog jezika Python, napisati funkciju izbroj, koja određuje broj elemenata liste, gde svaki element može da bude podlista ili broj.
# Primer: izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]) = 13

def izbroj(lista):
    broj_elemenata = 0
    for element in lista:
        if isinstance(element, list):
            broj_elemenata += izbroj(element)  # Rekurzivno prebrojavamo elemente u podlisti
        else:
            broj_elemenata += 1  # Dodajemo 1 ako je element broj
    return broj_elemenata

# Primer korišćenja
print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))  # Očekivani rezultat: 13
