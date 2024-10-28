# Korišdenjem programskog jezika Python, napisati funkciju razlika, koja prihvata dve liste (bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svih elemenata iz prve liste, koji se ne nalaze u drugoj listi.
# Primer: razlika([1, 4, 6, "2", "6"], [4, 5, "2"]) = [1, 6, "6"]

def razlika(lista1, lista2):
    rezultat = [el for el in lista1 if el not in lista2]
    return rezultat

# Primer korišćenja
print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))  # Očekivani rezultat: [1, 6, "6"]


#ne radi to sto treba
# def razlika(lista1, lista2):
#     rezultat=[]
#     for el in lista1:
#         for elem in lista2:
#             if el!=elem:
#                 rezultat.append(el)
#
#     return rezultat
# print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))