
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

novoPedido = 'S'

def pedido(comida,preco):
    global comidaNota += comida + ' \n'
    global precoNota += preco

while novoPedido == 'S':
    atendente = int(input('Qual o código do seu pedido? \n'))
    if atendente == 100:
        pedido('Cachorro-quente', 9)
    elif atendente == 101:
        pedido('Cachorro-quente duplo', 11)
    elif atendente == 102:
        pedido('X-egg', 12)
    elif atendente == 103:
        pedido('X-salada', 13)
    elif atendente == 104:
        pedido('X-bacon', 14)
    elif atendente == 105:
        pedido('X-tudo', 17)
    elif atendente == 200:
        pedido('Refrigerante lata', 5)
    elif atendente == 201:
        pedido('Chá-gelado', 4)
    else:
        print('Digite um pedido válido!')
        continue
    novoPedido = input('Deseja pedir algo mais? [S]sim [N]não \n')

    if novoPedido == 'N':
        break
    else:
        continue

print('Seu pedido final foi: \n ' \
             '{}, ficando um valor total de {}'.format(comidaNota, precoNota))

