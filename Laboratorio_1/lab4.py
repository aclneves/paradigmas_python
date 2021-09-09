nome = input("Digite o seu nome: ").capitalize()
estado_civil = input("Escolha o seu estado civil \nC - Casado \nS - Solteiro \nD - Divorciado \nV - Viúvo"
                     " \nO - Outros\n").capitalize()

if estado_civil == "C":
    print(f"{nome} é casado")
elif estado_civil == "S":
    print(f"{nome} é solteiro")
elif estado_civil == "D":
    print(f"{nome} é divorciado")
elif estado_civil == "V":
    print(f"{nome} é viúvo")
elif estado_civil == "O":
    print(f"{nome} é outros")
else:
    print("Você não digitou um estado civil correto")
