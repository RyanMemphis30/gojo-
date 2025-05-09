palavras = {
'anya','ban','cain','diane','escanor','fushiguro','gaara','hinata','ichigo','jack','kabuto','lawliet','madara','nagato','obito','pain',"quanxi",'rin','satoru','tomori','ugo','vegeta','wakuraba','xarvier','yuta','zabuza'}

letra_digitada = input('Digite uma letra: ').lower()

print(f'\nPalavras que começam com "{letra_digitada.upper()}":')
for palavra in palavras:
    if palavra.startswith(letra_digitada):
        print(palavra.capitalize())