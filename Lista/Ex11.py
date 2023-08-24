nome = input("Digite o nome do funcionário: ")
hrs = int(input("Numero de horas trabalhadas em 1 dia: "))
vhrs = float(input("Valor da hora: "))

bruto = hrs*vhrs*21

INSS = bruto*0.98

print(f"Funcionário: {nome}, Salário: {INSS}")