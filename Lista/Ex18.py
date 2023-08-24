n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceir nota: "))

media = (n1+n2+n3)/2
if media >=6:
    est = "passou"
else:
    est = "reprovou"

print(f"media: {media}, logo, {est}")