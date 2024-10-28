# Korišdenjem programskog jezika Python, napisati funkciju kreiraj, koja kreira listu N tuple obekata. Prvi element u svakom tuple objektu je redni broj tog tuple objekta a drugi kvadrat zbira svih indeksa od 0 do trenutnog indeksa.
# Primer: kreiraj(4) = [(0, 0), (1, 1), (2, 9), (3, 36), (4, 100)]

def zbirKvadrata(N): #ovde N zapravo predstavlja i koji je prosledjen
    suma=0
    for i in range(N+1):
        suma+=i
    suma=suma**2
    return suma

def kreiraj(N):
    lista=[]

    for i in range(N+1):
        tuple=(i,zbirKvadrata(i))
        lista.append(tuple)

    return lista

print(kreiraj(4)) 
