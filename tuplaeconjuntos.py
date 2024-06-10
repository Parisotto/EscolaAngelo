lista = ["Escola", 9, True, 0.5]
dicionario = {"texto":"Angelo", "numero":7, "situação":False, "decimal":1.4}

tupla1 = ("Mendes", 1, True, 5.4)
tupla2 = "rua", 4, False, 0.7

print(tupla1[0])

lista2 = list(tupla2)
print(lista2)
lista2[0] = "Avenida"
tupla3 = tuple(lista2)
print(tupla3)
