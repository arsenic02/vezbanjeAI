# Korišdenjem programskog jezika Python, napisati funkciju uredi, koja svaki od prvih N elemenata uvedava za definisanu vrednost a preostale umanjuje za definisanu vrednost. Funkciji se prosleđuje lista koja sadrži samo numeričke vrednosti i vrednost koja treba da se uvedava, odnosno umanjuje.
# Primer: uredi([1, 2, 3, 4, 5], 3, 1) = [2, 3, 4, 3, 4]

def uredi(elementi, N, vrednost):
    rezultat = []
    for i in range(len(elementi)):
        if i < N:
            rezultat.append(elementi[i] + vrednost)
        else:
            rezultat.append(elementi[i] - vrednost)
    return rezultat

print(uredi([1, 2, 3, 4, 5], 3, 1))  # Rezultat: [2, 3, 4, 3, 4]

# durgi nacin
# def uredi(elementi, N, vrednost):
#     rezultat = [
#         el + vrednost if i < N else el - vrednost
#         for i, el in enumerate(elementi)
#     ]
#     return rezultat
#
# # Primer korišćenja
# print(uredi([1, 2, 3, 4, 5], 3, 1))  # Rezultat: [2, 3, 4, 3, 4]

