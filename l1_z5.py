# Korišdenjem programskog jezika Python, napisati funkciju brojel, koja broji koliko elemenata ima svaka podlista liste koja joj je prosleđena. Ukoliko elemenat liste nije podlista funkcija vrada -1.
# Primer: brojel([1, 2], [3, 4, 5], 'el', ['1', 1]) = [2, 3, -1, 2]

#prvi nacin
def brojel(*elementi):
    rezultat = [len(el) if isinstance(el, list) else -1 for el in elementi]
    return rezultat

# Primer korišćenja
print(brojel([1, 2], [3, 4, 5], 'el', ['1', 1]))  # Rezultat: [2, 3, -1, 2]


# def brojel(elementi):
#     rezultat={
#         podlista for podlista in elementi
#             if podlista.len<2
#
#     }