base = int(input('Informe um numero natural: '))
expoente = int(input('Informe outro numero natural: '))
num1 = 1
num2 = 0
while base < 0 or expoente < 0:
    print('Valor Invalido!')
    base = int(input('Informe um numero natural: '))
    expoente = int(input('Informe outro numero: '))
while num2 < expoente:
    num1 = num1 * base
    num2 += 1
print(num1)