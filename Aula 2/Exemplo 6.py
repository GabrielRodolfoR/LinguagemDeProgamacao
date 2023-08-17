a = ["Gabriel", "Rodolfo", "Marcos", "Nunes", "Joao"]

a.clear() #Limpa toda a lista
print(a)

a = ["Gabriel", "Rodolfo", "Marcos", "Nunes", "Joao"]

c = a.copy() #Copia a lista para outra variável
print(a)
print(c)

d = a + c #Juntar listas
print(d)

print(a.count("Gabriel")) #numeros de vezes que apareceu na lista
print(len(a))

print(a.index("Marcos"))