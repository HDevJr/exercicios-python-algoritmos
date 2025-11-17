# Enunciado 13:
# Leia a renda mensal do usuário e o valor da parcela desejada para o empréstimo.
# O empréstimo só pode ser aprovado se:
# - A renda for maior que R$ 2.000,00
# - O valor da parcela for menor ou igual a 30% da renda
# Informe se o empréstimo foi aprovado ou negado.

renda_mes = float(input('Informe o valor da renda mensal: R$ '))
valor_parcela = float(input('Informe o valor da parcela desejada: R$ '))

limite_parcela = renda_mes * 0.3

if renda_mes <= 2000:
    print('Empréstimo negado: renda insuficiente.')
elif valor_parcela > limite_parcela:
    print(f'Empréstimo negado: a parcela excede 30% da renda (máximo permitido: R$ {limite_parcela:.2f}).')
else:
    print('Empréstimo aprovado.')
