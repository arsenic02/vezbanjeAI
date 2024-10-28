# Korišdenjem programskog jezika Python, napisati funkciju izmeni, koja elemente na parnim pozicijama uvedava za jedan i od njih kreira podlistu pp, dok elemente na neparnim pozicijama umanjuje za 1 i od njih kreira podlistu np. Funkcija vrada rečnik koji sadrži liste pp i np.
# Primer: izmeni([8, 6, 3, 1, 1]) = {'pp': [9, 4, 2], 'np': [5, 0]}

def izmeni(lista):
    pp=[]
    np=[]
    # recnik=[]
    for i in range(len(lista)):
        if i%2==0:
            lista[i]+=1
            pp.append(lista[i])
        else:
            lista[i]-=1
            np.append(lista[i])

    # recnik.append(pp)
    # recnik.append(np)

    recnik = {'pp': pp, 'np': np}
    return recnik

print(izmeni([8, 6, 3, 1, 1])) #[[9, 4, 2], [5, 0]]
#kako da mi ovo  bude izlaz {'pp': [9, 4, 2], 'np': [5, 0]}