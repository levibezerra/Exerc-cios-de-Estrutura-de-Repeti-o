r = 'S'
while r == 'S':
    idade = int(input('Informe sua idade: '))
    categoria = str(input('Informe a categoria do ingresso A = R$40,00, B = R$30,00 e C = R$25,00: ')).upper()
    if idade >= 60 and categoria == 'A':
        soma = 40 / 2
        print(f'O valor do ingresso é R${soma:.2f}')
    elif idade < 60 and categoria == 'A':
        print('O valor do ingresso é R$40,00')
    elif idade >= 60 and categoria == 'B':
        soma = 30 / 2
        print(f'O valor do ingresso é R${soma:.2f}')
    elif idade < 60 and categoria == 'B':
        print('O valor do ingresso é R$30,00')
    elif idade >= 60 and categoria == 'C':
        soma = 25 / 2
        print(f'O valor do ingresso é R${soma:.2f}')
    else:
        print('O valor do ingresso é R$25,00')
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')