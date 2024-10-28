# Korišdenjem programskog jezika Python, napisati funkciju zbir, koja kreira novu listu čiji su elementi zbirovi susednih elementa liste.
# Primer: zbir([1, 2, 3, 4, 5]) = [3, 5, 7, 9]


def zbir(lista):
    rezultat = [lista[i] + lista[i + 1] for i in range(len(lista) - 1)]
    return rezultat

print(zbir([1, 2, 3, 4, 5]))  # Rezultat: [3, 5, 7, 9]



