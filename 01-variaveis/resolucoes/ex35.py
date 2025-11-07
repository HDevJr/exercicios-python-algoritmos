# Enunciado 35:
# Crie variáveis para armazenar o nome de um funcionário, cargo e salário.
# Em seguida, exiba uma mensagem formatada mostrando todas essas informações.

nome_funcionario = input('Digite o nome do funcionário: ')
cargo_funcionario = input('Digite o cargo do funcionário: ')
salario_funcionario = float(input('Digite o salário do funcionário (R$): '))

print(f'''
Funcionário: {nome_funcionario}
Cargo:       {cargo_funcionario}
Salário:     R$ {salario_funcionario:.2f}
''')
