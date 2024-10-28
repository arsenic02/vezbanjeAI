# Korišdenjem programskog jezika Python, napisati funkciju presek, koja prihvata dve liste (bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svih elemenata koji se nalaze u obe liste.
# Primer: presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]) = [1, "1"]

#moj nacin, rezultat je ['1']
def presek(lista1, lista2):
    listaPresek=[]
    for el in lista1:
        for elem in lista2:
            if el==elem:
                listaPresek.append(el)
    return listaPresek

print(presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]))

#rezultat je [1]
def presek(lista1, lista2):
    # Konvertujemo sve elemente obe liste u setove koristeći njihove vrednosti kao stringove
    set1 = {str(el) for el in lista1}
    set2 = {str(el) for el in lista2}

    # Pronalazimo presek setova i konvertujemo nazad u odgovarajuće tipove
    zajednicki = [int(el) if el.isdigit() else el for el in set1 & set2]

    return zajednicki


# Primer korišćenja
print(presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]))  # Očekivani rezultat: [1, "1"]

