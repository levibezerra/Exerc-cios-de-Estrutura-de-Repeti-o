par = impar = 0
for i in range(1, 11):
        numero = int(input('Digite um numero inteiro: '))
        while numero <= 0:
            print('Valor Invalido')
            numero = int(input('Digite um numero inteiro: '))
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} pares e {impar} impares.')