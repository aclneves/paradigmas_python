print("### Cálculo de juros ###")

capital = float(input("Digite o capital desejado: "))
taxa = float(input("Digite a taxa de juros: "))
tempo = int(input("Digite o tempo do empréstimo em meses: "))

juros = capital * taxa/100 * tempo

print(f"Os juros desse empréstimo são de R$ {juros:.2f}")
