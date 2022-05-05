n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
input('[1] multiplicação    [2] divisão    [3] subtração   [4] adição')
operacao = int(input('Qual operacção você deseja fazer? '))

if operacao == 1:
    print('O resultado de {} x {} é {}'.format(n1, n2, n1*n2))
elif operacao == 2:
    print('O resultado de {} / {} é {}'.format(n1, n2, n1/n2))
elif operacao == 3:
    print('O resultado de {} - {} é {}'.format(n1, n2, n1-n2))
elif operacao == 4:
    print('O resultado de {} + {} é {}'.format(n1, n2, n1+n2))
else:
    print('Digite uma operação válida.')

