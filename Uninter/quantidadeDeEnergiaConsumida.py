input('[R] Residência   [I] Indústrial  [C] Comércio')
tipoInstalacao = input('A letra referênte ao tipo de instalação: ')
faixa = float(input('Qual a quantidade de kWh consumida? '))

if tipoInstalacao == 'R':
    if  faixa <= 500:
        preco = 0.40
    else:
        preco = 0.65

elif tipoInstalacao == 'I':
    if faixa <= 5000:
        preco = 0.55
    else:
        preco = 0.60

elif tipoInstalacao == 'C':
    if faixa <= 100:
        preco = 0.55
    else:
        preco = 0.60
else:
    print('Instalação desconhecida.')

print('Total a pagar; {}'.format(preco*faixa))