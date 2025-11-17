# Enunciado 09:
# Leia o valor total das despesas mensais do usuário.
# Considere um limite de R$ 3000,00.
# Exiba se o usuário ultrapassou o limite ou se ainda está dentro dele e se tem algum valor disponível.

despesas = float(input('Digite o valor total das despesas: '))

limite = 3000

disponivel = limite - despesas

if despesas < limite:
    print(f'Você está dentro do orçamento: Disponível {disponivel:.2f}')
else:
    print('Limite atingido')