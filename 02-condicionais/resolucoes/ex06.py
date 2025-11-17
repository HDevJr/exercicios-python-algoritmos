# Enunciado 06:
# Leia o número de dias de três atividades. 
# Se algum valor for negativo, exiba erro. 
# Caso todos sejam válidos, some os dias e apresente o total.

atv1 = int(input('Digite o número de dias da Atividade 1: '))
atv2 = int(input('Digite o número de dias da Atividade 2: '))
atv3 = int(input('Digite o número de dias da Atividade 3: '))

if atv1 < 0 or atv2 < 0 or atv3 < 0:
    print('Erro: dias não podem ser negativos.')
else:
    resultado = atv1 + atv2 + atv3
    print(f'O total de dias é: {resultado}')
