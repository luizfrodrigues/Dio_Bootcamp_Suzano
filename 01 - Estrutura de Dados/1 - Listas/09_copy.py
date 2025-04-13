lista = [1, "Python", [40, 30, 20]]

lista_2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]
print(id(lista), id(lista_2))

lista_2[0] = 2
print(lista_2)
