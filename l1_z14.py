# Korišdenjem programskog jezika Python, napisati funkciju unija, koja prihvata dve liste (bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svih elemenata obe liste bez ponavljanja.
# Primer: unija([5, 4, "1", "8", 7], [1, 9, "1"]) = [5, 4, "1", "8", 7, 9, 1]

#moje resenje, ne valja
# def unija(lista1, lista2):
#     for el1 in lista1:
#         for el2 in lista2:
#             if el1!=el2:
#                 lista1.append(el2)
#
#     return lista1
#
# print(unija([5, 4, "1", "8", 7], [1, 9, "1"]))

def unija(lista1, lista2):
    # Kreiramo set od dve liste i spajamo ih, što automatski uklanja duplikate
    rezultat = list(set(lista1) | set(lista2))
    return rezultat

print(unija([5, 4, "1", "8", 7], [1, 9, "1"]))  # izlaz: [1, '1', 4, 5, '8', 7, 9], samo je promenjen redosled elemenata
