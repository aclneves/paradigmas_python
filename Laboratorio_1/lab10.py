posicao_inicial = int(input("Digite a distância atual (metros): "))
velocidade = float(input("Digite a velocidade (km/h): "))

print("\nLetra (a) - Função horária da posição do veículo\n")

velocidade = velocidade / 3.6
print(f"{velocidade} m/s")

print(f"S = So + vt\n"
      f"S = {posicao_inicial} + {velocidade}t\n")

# S = S0 + vt -> S - S0 / v

print("Letra (b) - Em qual instante de tempo esse veiculo estará na posição final\n")
posicao_final = int(input("Digite a posição desejada: \n"))

instante = (posicao_final - posicao_inicial) / velocidade

print(f"O veiculo estará na posição no instante {instante}s")


