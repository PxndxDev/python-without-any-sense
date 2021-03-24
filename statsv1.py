# ce code a été réalisé par Elouann uniquement grâce à ses connaissances (eheh)

from math import *

# Entrez vos classes et vos effectifs juste en dessous. N'utilisez que des nombres réels,
# sans caractères spéciaux ni marque de string. Exemple :
# écrire : [10, 12, 20] et non : ['10', "12", a20]
classes = [1, 2, 3, 4, 5, 6, 7]
effectifs = [1, 5, 17, 8, 9, 0, 5]

# NE PAS REMPLIR CECI
ECC = []

indiceECC = 0
while indiceECC < len(effectifs):
    ECC.append(0)
    indiceECC += 1

x_Top = 0
N = 0
indice1 = 0
while indice1 < len(classes):
    x_Top += (classes[indice1] * effectifs[indice1])
    N += effectifs[indice1]
    indice1 += 1
x_ = x_Top/N

sTop = 0.0
indice2 = 0
while indice2 < len(classes):
    sTop += (float(effectifs[indice2]) * (float(classes[indice2]) - x_) * (float(classes[indice2]) - x_))
    indice2 += 1
sigma = sqrt(sTop / N)

indice3 = 0
ECCinCalc = 0
while indice3 < len(classes):
    ECC[indice3] = ECCinCalc + effectifs[indice3]
    ECCinCalc += effectifs[indice3]
    indice3 += 1

MeValeur = N/2

if MeValeur == int(MeValeur):
    indiceECC21 = 0
    foundClass1 = False
    while foundClass1 == False:
        if ECC[indiceECC21] < MeValeur:
            indiceECC21 += 1
        else:
            foundClass1 = True
    index1 = indiceECC21+1

    indiceECC22 = 0
    foundClass2 = False
    while foundClass2 == False:
        if ECC[indiceECC22] < MeValeur+1:
            indiceECC22 += 1
        else:
            foundClass2 = True
    index2 = indiceECC22+1

    Me = (classes[index1] + classes[index2]) / 2
else:
    MeValeur += 0.5

    indiceECC2 = 0
    foundClass = False
    while foundClass == False:
        if ECC[indiceECC2] < MeValeur:
            indiceECC2 += 1
        else:
            foundClass = True
    index = indiceECC2+1

    Me = classes[index]

print("Ecart-type : " + str(sigma))
print("Moyenne : " + str(x_))
print("Médiane : " + str(Me))
print("Effectif total : " + str(N))
print("Effectif cumulé croissant :")
print(ECC)
