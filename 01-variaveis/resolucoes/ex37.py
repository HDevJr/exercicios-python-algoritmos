# Enunciado 37:
# Leia um texto e substitua todas as vogais (maiúsculas e minúsculas) por *.

texto = input('Digite um texto: ')

vogais = 'aeiouAEIOU'

for v in vogais:
    texto = texto.replace(v, '*')

print(f'Texto modificado: {texto}')