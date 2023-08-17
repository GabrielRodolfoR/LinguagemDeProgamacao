a = ["Gabriel", "Rodolfo", "Marcos", "Nunes", "Joao", "Gabriel", "Rodolfo", "Rodolfo"]

print(a)
for i in a:
    if "Rodolfo" in a:
        a.remove("Rodolfo")
print(a)