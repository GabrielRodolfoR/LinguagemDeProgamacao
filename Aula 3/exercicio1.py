def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    result = a / b
    return result

while True:
    a = 0
    code = int(input("1-Add"
                     "\n2-Subtract"
                     "\n3-Multiply"
                     "\n4-Divide"
                     "\n5-Exit"
                     "\nEnter the code: "))
    if code == 5:
        break

    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))

    if code == 1:
        a = add(a, b)
    elif code == 2:
        a = subtract(a, b)
    elif code == 3:
        a = multiply(a, b)
    elif code == 4:
        a = divide(a, b)

    print(f"The result is {a}")