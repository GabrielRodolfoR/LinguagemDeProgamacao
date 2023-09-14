def soma(a,b):
    s = a+b
    return s

def sub(a,b):
    s = a-b
    return s

def mult(a,b):
    s = a*b
    return s

def div(a,b):
    s = a/b
    return s

while True:
    a=0
    cod = int(input("1-Soma"
                "\n2-Subtração"
                "\n3-Multiplicação"
                "\n4-Divisão"
                "\n5-Sair"
                "\nDigite o código: "))
        
    if(cod == 1):
            a = soma(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))
    elif(cod == 2):
            a = sub(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))
    elif(cod == 3):
            a= mult(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))
    elif(cod == 4):
            a = div(int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: ")))
    
    print(f"O resultado é {a}")

    if(cod == 5):
            break