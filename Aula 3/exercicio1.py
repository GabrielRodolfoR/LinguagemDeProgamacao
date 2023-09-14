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
    if(cod == 5):
            break

    a = int(input("Digite o 1º numero: "))
    b = int(input("Digite o 2º numero: "))
        
    if(cod == 1):
            a = soma(a,b)
    elif(cod == 2):
            a = sub(a,b)
    elif(cod == 3):
            a= mult(a,b)
    elif(cod == 4):
            a = div(a,b)
    
    print(f"O resultado é {a}")

    