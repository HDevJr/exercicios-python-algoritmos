# Enunciado 36:
# CPF string: exiba apenas dígitos (remova pontuações).

cpf = input('Digite o CPF (formato XXX.XXX.XXX-XX): ').strip()

cpf_limpo = cpf.replace('.', '').replace('-', '')

print(f'CPF sem pontuação: {cpf_limpo}')
