sex = input("Digite seu sexo (F/M): ")
h = float(input("Digite sua altura: "))

if sex == "M":
    IMC = (72.7 * h) - 58

elif sex == "F":
    IMC = (62.1 * h) - 44, 7

print(f"Seu Peso Ideal é: {IMC}")