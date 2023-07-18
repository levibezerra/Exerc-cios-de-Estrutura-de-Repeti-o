nota = 0
while nota == 0:
    nota = float(input('Informe uma nota entre zero e dez: '))
    if nota < 0 or nota > 10:
        print('Valor Invalido')
        nota = 0
if nota >= 7 or nota == 10:
     print(f'Aprovado sua nota foi {nota:.1f}')
else:
    print(f'Reprovado sua nota foi {nota:.1f}')