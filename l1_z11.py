def razlika(lista):
    rezultat=[lista[i]-lista[i+1] for i in range(len(lista)-1)]
    return rezultat

print(razlika([8, 5, 3, 1, 1]))