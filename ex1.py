pessoas = int(input('Informe a quantidade de pessoas: '))
menor_altura = 1000
soma_altura = 0
maior_185 = 0
for var in range(1, pessoas + 1):
    print(f'_{var}ªPESSOA_')
    nome = str(input('Digite seu nome: '))
    altura = float(input('Informe sua altura: '))
    soma_altura += altura
    if altura < menor_altura:
        menor_altura = altura
        menor = nome
    if altura > 1.85:
        maior_185 = maior_185 + 1
media_altura = soma_altura / pessoas
print(f'O nome da pessoa com menor altura é {menor} e sua altura é de {menor_altura:.2f}')
print(f'A media de altura do grupo é {media_altura:.2f}')
print(f'O numero de pessoas com a altura maior que 1.85 é {maior_185} pessoa(s).')