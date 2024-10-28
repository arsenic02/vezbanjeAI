def saberi(lista_torki):
    rezultat = [sum(torka) for torka in lista_torki]  # Sabiramo elemente svake torke
    return rezultat

# Primer korišćenja
print(saberi([(1, 4, 6), (2, 4), (4, 1)]))  # Očekivani rezultat: [11, 6, 5]
