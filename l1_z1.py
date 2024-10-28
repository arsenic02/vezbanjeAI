def parni(brojevi):
    rezultat = {
        'Parni': [broj for broj in brojevi #ovo broj ispred for petlje je povratna vrednost ako je uslov zadovoljen
                  if broj % 2 == 0],
        'Neparni': [broj for broj in brojevi
                    if broj % 2 != 0]
    }
    return rezultat

# Primer korišćenja
print(parni([1, 7, 2, 4, 5]))  # {'Parni': [2, 4], 'Neparni': [1, 7, 5]}
