# def izmeni(lista,n):
#     suma = 0
#     # for el in lista:
#     for i in range(len(lista)) and el in lista:
#       if i<n:
#           suma+=el
#     elif i==n
#         el=suma #zamenjuje se n-ti element sumom
#     else
#         break

#nesto ne radi kako treba
# def izmeni(lista, n):
#     suma = 0
#     for i in range(len(lista)):
#         # Ako je trenutni indeks manji od n, dodajemo element u sumu
#         if i < n:
#             suma += lista[i]
#         # Kada dostignemo n-ti element, zamenjujemo ga sumom
#         elif i == n:
#             lista[i] = suma
#             break  # Završavamo petlju nakon zamene n-tog elementa
#     return lista
#
# # Primer korišćenja
# print(izmeni([1, 2, 4, 7, 9], 3))  # Očekivani rezultat: [1, 2, 4, 7]


def izmeni(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]  # Dodajemo vrednost trenutnog elementa na sumu
        lista[i] = suma   # Zamenjujemo trenutni element sa novom sumom
    return lista

# Primer korišćenja
print(izmeni([1, 2, 4, 7, 9]))  # Očekivani rezultat: [1, 3, 7, 14, 23]
