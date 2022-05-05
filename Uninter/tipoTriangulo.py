l1 = int(input('Digite o valor do lado 1: '))
l2 = int(input('Digite o valor do lado 2: '))
l3 = int(input('Digite o valor do lado 3: '))

if (l1 > 0 and l2 > 0 and l3 > 0) and ( l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2):
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('Seu triângulo é EQUILÁTERO')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Seu triângulo é ESCALENO')
    else:
        print('Seu triângulo é isósceles')
else:
    print('Não é possível formar um triângulo.')