usuario = str(input('Digite seu nome de usuario: '))
senha = (input('Digite sua senha: '))
while usuario == senha:
   print('O nome de usuario nao pode ser igual a sua senha!')
   usuario = str(input('Digite seu nome de usuario: '))
   senha = input('Informe sua senha: ')
if usuario != senha:
    print(f'O seu nome de usuario é: {usuario}.')
    print(f'Sua senha é: {senha}.')