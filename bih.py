meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

try:
    numero_mes = int(input("Escolha um número de 1 a 12: "))
    if 1 <= numero_mes <= 12:
        mes_escolhido = meses[numero_mes - 1]
        print(f"  {numero_mes} é o mês de {mes_escolhido}.")
    else:
        print("Por favor, digite um número entre 1 e 12.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")