dias_semana_pt = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
dias_semana_en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

try:
    dia_semana = int(input("Escolha um dia da semana (1-7): "))
    if 1 <= dia_semana <= 7:
        print(f" {dias_semana_pt[dia_semana - 1]},em inglês é {dias_semana_en[dia_semana - 1]}.")
    else:
        print("Dia inválido. Por favor, escolha um número de 1 a 7.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")