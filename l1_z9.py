def prosek(lista):
    rezultat = [sum(torka)/len(torka) for torka in lista]  # Sabiramo elemente svake torke
    return rezultat

print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))