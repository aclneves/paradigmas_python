nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
sexo = input("Digite o seu sexo (M ou F): ")
telefone = input("Digite o seu telefone: ")

if sexo.lower() == "f":
    print('Nome:', nome, '\nTelefone:', telefone)
else:
    print("A pessoa é do sexo masculino")