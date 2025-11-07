# Enunciado 16:
# Leia um salário e calcule reajuste de 7,5% e 12% (dois novos valores).

salario = float(input('Digite o valor do salário: '))

reajuste1 = salario * 1.075
reajuste2 = salario * 1.12

print(f'Salário com reajuste de 7,5%: R$ {reajuste1:.2f}')
print(f'Salário com reajuste de 12%: R$ {reajuste2:.2f}')
