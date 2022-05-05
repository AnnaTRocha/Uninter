input('Seja bem vindo à loja Anna Letícia Teixeira da Rocha')
input('           O número do pedido é 3972384             ')
input('                                                    ')
preco = float(input('Qual o valor do produto? '))
quantidade = int(input('Qual a quantidade desejada? '))

if quantidade > 0 and preco > 0 :
    if 9 < quantidade < 99 :
        valorDesconto = '5%'
        desconto =  preco - (0.05 * preco) # 5%
    elif 100 <= quantidade <= 999:
        valorDesconto = '10%'
        desconto = preco - (0.1 * preco) # 10%
    elif quantidade >= 1000:
        valorDesconto = '15%'
        desconto = preco - (0.15 * preco) # 15%

    print('------------NOTA FISCAL------------')
    print('Loja Anna Letícia Teixeira da Rocha')
    print('                                   ')
    print('Quantidade:              {}'.format(quantidade))
    print('Valor(unidade):          {:.2f}'.format(preco))
    print('Desconto aplicado:       ' + valorDesconto)
    print('-----------------------------------')
    print('Valor sem desconto:      {:.2f}'.format(preco*quantidade))
    print('Valor com desconto:      {:.2f}'.format(desconto * quantidade))
    print('*Desconto aplicado somente na compra')
    print('de 10 unidades ou mais.')
    print('                                   ')
    print('            Volte sempre!          ')

else:
    if quantidade <= 0:
        print('A quantidade tem que ser maior que 0.')
    elif preco <= 0:
        print('O preço tem que ser maior que 0.')