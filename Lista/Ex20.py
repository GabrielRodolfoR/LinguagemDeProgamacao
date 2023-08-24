idade = int(input("Digite a sua idade: "))
temp = int(input("Digite quanto tempo você trabalhou: "))

if idade>=60 and temp>=25:
    res = "Pode se aposentar"
elif idade>=65:
    res = "Pode se aposentar"
elif temp>=30:
    res = "Pode se aposentar"
else:
    res = "Não pode se aposentar"

print(f"Com base nas informação, você {res}")