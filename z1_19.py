# Korišdenjem programskog jezika Python, napisati funkciju stepenuj, koja listu tuple
# vrednosti transformiše u listu brojeva, koji se dobijaju primenom operacije stepenovanja,
# tako što se prvi element stepenuje drugim, zatim se rezultat stepenuje tredim sve dok se
# ne dođe do poslednjeg elementa u tuple-u.

def stepenovanje(lista):
    rezultat = lista[0]  # Počinjemo sa prvim elementom
    for i in range(1, len(lista)):
        rezultat = rezultat ** lista[i]  # Rezultat stepenujemo sledećim elementom
    return rezultat

def stepenuj(lista):
    novaLista=[]
    for podlista in lista:
        novaLista.append(stepenovanje(podlista))

    return novaLista

print(stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]))