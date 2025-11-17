# Enunciado 10:
# Leia a hora atual (formato 0 a 23).
# O acesso ao escritório é permitido apenas entre 8h e 18h (inclusive 8h, exclusivo 18h).
# Informe ao usuário se o acesso é permitido ou negado.

hora_atual = int(input('Informe o horário atual no formato 24hrs: '))

if 8 <= hora_atual < 18:
    print('Acesso permitido')
else:
    print('Escritório fechado')