
input('Seja bem vindo à lanchonete Anna Letícia Teixeira da Rocha\n'
      '             O número do pedido é 3972384                 \n'
      '                                                          \n'
      '-------------------------Cardápio-------------------------\n'
      '|  Código  |              Comida             | Preço(R$) |\n'
      '|   100    |          Cachorro-Quente        |    9,00   |\n'
      '|   101    |       Cachorro-Quente Duplo     |   11,00   |\n'
      '|   102    |              X-Egg              |   12,00   |\n'
      '|   103    |             X-Salada            |   13,00   |\n'
      '|   104    |             X-Bacon             |   14,00   |\n'
      '|   105    |              X-Tudo             |   17,00   |\n'
      '|   200    |        Refrigerante Lata        |    5,00   |\n'
      '|   201    |            Chá Gelado           |    4,00   |\n'
      '                                                          \n')


preco = 0
comida = ""

while True:
    codigo = int(input('Qual o código do seu pedido? \n'))
    if codigo == 100:
        comida += 'Cachorro-quente'
        preco += 9
    elif codigo == 101:
        comida += 'Cachorro-quente Duplo'
        preco += 11
    elif codigo == 102:
        comida += 'X-Egg'
        preco += 12
    elif codigo == 103:
        comida += 'X-Salada'
        preco += 13
    elif codigo == 104:
        comida += 'X-Bacon'
        preco += 14
    elif codigo == 105:
        comida += 'X-Tudo'
        preco += 17
    elif codigo == 200:
        comida += 'Refrigerante Lata'
        preco += 5
    elif codigo == 201:
        comida += 'Chá Gelado'
        preco += 4
    else:
        print('Código inválido!')
        continue
    continuar = input('Deseja fazer um novo pedido? [S] Sim  [N] Não \n')
    if(continuar == 'N'):
        break
    elif(continuar == 'S'):
        comida += "\n"
        continue
    else:
        while continuar != 'S' and continuar != 'N':
            continuar = input('Digite [S] para SIM e [N] para NÃO! \n')
        continue

print('Seu pedido foi: \n{} \nFicando um valor de R$:{} '.format(comida, preco))