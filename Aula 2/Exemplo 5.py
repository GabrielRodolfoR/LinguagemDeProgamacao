a = ["Gabriel", "Rodolfo", "Marcos", "Nunes"]
b = ["Matheus", "Manuel", "João"]

print(a)
del a[2]
print(a)
a.append("Marcos")
del a[1:3]
print(a)

a = ["Gabriel", "Rodolfo", "Marcos", "Nunes"]
a.append("Marcos")
print(a)

a.remove("Marcos")
print(a)


print(b)
b = a.pop(0)
print(a, "\n", b)