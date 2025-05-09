import random
numero= random.randint(1,100)
print(numero)
quer_continuar = True
contador = 1
Não = quer_continuar == False
Sim = True
acertos = 1
erros = 0
while(quer_continuar):
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)
    print(f"Q(contador):{n1}+{n2}")
    resp= int(input('R: '))
    if(resp == n1+n2):
        acertos = +1
        print('Resposta Coreta!')
    else:
        erros = +1
        print('Resposta Incorreta!')
    contador = contador+1
    continuar = input(f'Quer continuar? 1{Sim} {2 Não}: ')
    if(continuar == 2):
        quer_continuar = False

print('Fim')
print(f'acertos: (acertos)')
print(f'acertos: (acertos)')