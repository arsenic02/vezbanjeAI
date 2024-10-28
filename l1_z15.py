# Korišdenjem programskog jezika Python, napisati funkciju izdvoji, koja iz zadate liste čiji su elementi liste, izdvaja n-ti element i formira rezultujudu listu, pri čemu je n=0 za prvu podlistu i uvedava se sukcesivno za 1. Ukoliko ne postoji n-ti element u listi vrada se 0.
# Primer: izdvoji([5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]) = [5, 9, 0, 12]

# kada u funkciji izdvoji koristimo *lista, to nam omogućava da prosledimo bilo koji broj listi kao argumente funkcije.
def izdvoji(*lista):  #*lista ovde omogućava da funkcija izdvoji primi promenljiv broj argumenata i da ih sve spakuje u jedan tuple pod nazivom lista
    n = 0  # Početni indeks
    nova_lista = []

    for podlista in lista:
        # Provera da li postoji n-ti element u podlisti
        if len(podlista) > n:
            nova_lista.append(podlista[n])
        else:
            nova_lista.append(0)  # Dodaj 0 ako n-ti element ne postoji
        n += 1  # Povećavamo n za sledeću podlistu

    return nova_lista

# Primer poziva funkcije
print(izdvoji([5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]))  # Očekivani izlaz: [5, 9, 0, 12]


