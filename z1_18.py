def kreiraj(lista):
    rezultat = []
    for i in range(len(lista) - 1):
        razlika = list(set(lista[i]) - set(lista[i + 1]))  # Razlika između susednih podlisti
        rezultat.append(razlika)
    return rezultat

# Test primer
print(kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]))
