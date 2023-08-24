M = J = R = P = N = B = T = 0

while True:
    voto = int(input("1-Manuel Gomes"
                    "\n2-James dasalada"
                    "\n3-Rodrigo Góes"
                    "\n4-Pope Francis"
                    "\n5-Voto Nulo"
                    "\n6-Voto Branco"
                    "\nDigite o seu voto: "))
    
    if voto == 1:
        M+=1
        T+=1
    elif voto == 2:
        J+=1
        T+=1
    elif voto == 3:
        R+=1
        T+=1
    elif voto == 4:
        P+=1
        T+=1
    elif voto == 5:
        N+=1
        T+=1
    elif voto == 6:
        B+=1
        T+=1
    elif voto == 0:
        break

print(F"Manuel: {M} Porcentagem: {(M/T)*100}%"
      F"\nJames: {J} Porcentagem: {(J/T)*100}%"
      F"\nRodrigo: {R} Porcentagem: {(R/T)*100}%"
      F"\nPope: {P} Porcentagem: {(P/T)*100}%"
      F"\nNulo: {N} Porcentagem: {(N/T)*100}%"
      F"\nBranco: {B} Porcentagem: {(B/T)*100}%"
      F"\nTotal: {T}")