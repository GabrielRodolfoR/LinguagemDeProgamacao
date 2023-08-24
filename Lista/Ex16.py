esc = int(input(f"1- Fahrenheit para Celsius\n2-Fahrenheit para Celsius\nSelecione a opção: "))

if esc == 1:
    far = float(input("Digite a temperatura em Fahrenheit: "))
    conv = (far-32)/1.8

if esc == 2:
    cel = float(input("Digite a temperatura em Celsius: "))
    conv = (cel*1.8)+32

print(f"Conversão: {conv}")