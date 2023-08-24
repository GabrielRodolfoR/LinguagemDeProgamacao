import random
while True:
    player = int(input("Digite 1 para impar ou 2 para par: "))
    num = random.randint(1, 2)

    if (player == 1 and num == 1) or (player == 2 and num == 2):
        print("Parabéns, você acertou!!")
    else:
        print("Mais sorte da proxima vez!!")

    print(player, num)