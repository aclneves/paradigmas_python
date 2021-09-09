num_1 = int(input("Digite o primeiro numero: "))
num_2 = int(input("Digite o segundo numero: "))
num_3 = int(input("Digite o terceiro numero: "))

if num_1 > num_2 and num_1 > num_3:
    maior = num_1
    if num_2 > num_3:
        mediano = num_2
        menor = num_3
    else:
        mediano = num_3
        menor = num_2
    print(f"Maior: {maior} \nMediano: {mediano} \nMenor: {menor}")

elif num_2 > num_1 and num_2 > num_3:
    maior = num_2
    if num_1 > num_3:
        mediano = num_1
        menor = num_3
    else:
        mediano = num_3
        menor = num_1
    print(f"Maior: {maior} \nMediano: {mediano} \nMenor: {menor}")

elif num_3 > num_1 and num_3 > num_1:
    maior = num_3
    if num_1 > num_2:
        mediano = num_1
        menor = num_2
    else:
        mediano = num_2
        menor = num_1
    print(f"Maior: {maior} \nMediano: {mediano} \nMenor: {menor}")

