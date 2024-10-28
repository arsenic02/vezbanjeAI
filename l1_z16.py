# Korišdenjem programskog jezika Python, napisati funkciju brojanje, koja na osnovu datog rečnika koji sadrži elemente različitog tipa kreira listu tuple objekata. Svaki tuple objekat na prvoj poziciji sadrži tip elementa a na drugoj koliko je takvih elemenata bilo u rečniku.
# Primer: brojanje({1 : 4, 2 : [2, 3], 3 : [5, 6], 4 : 'test', 5 : 9, 6 : 8}) =
# [('int', 3), ('list', 2), ('str',1)]

def brojanje(recnik):
    tipovi = {}

    # prolazak kroz vrednosti rečnika i brojanje tipova
    for vrednost in recnik.values():
        tip_vrednosti = type(vrednost).__name__  # uzimanje imena tipa
        if tip_vrednosti in tipovi:
            tipovi[tip_vrednosti] += 1
        else:
            tipovi[tip_vrednosti] = 1

    # pretvaranje rezultata u listu tuple objekata
    rezultat = [(tip, broj) for tip, broj in tipovi.items()]
    return rezultat

# Test primera
print(brojanje({1: 4, 2: [2, 3], 3: [5, 6], 4: 'test', 5: 9, 6: 8}))
# Izlaz bi trebalo da bude: [('int', 3), ('list', 2), ('str', 1)]
#4,9,8 su int, [2,3] i [5,6] su list, 'test' je str

