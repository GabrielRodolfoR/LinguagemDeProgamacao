din = float(input("Digite o valor que tens na carteira: "))
dolar = float(input("Digite o valor do Dolar hoje: "))
euro = float(input("Digite o valor do euro hoje: "))

RD = din/dolar
RE = din/euro

print(f"Você tem R${din}, que podereiam ser convertidos em U${RD} ou em €{RE}")