# Enunciado 20:
# Leia uma frase e verifique se ela é um palíndromo,
# desconsiderando espaços em branco e diferenças entre maiúsculas e minúsculas.

frase = input('Digite uma frase: ')

frase_limpa = frase.replace(" ", "").lower()

palindromo = frase_limpa[::-1]

if frase_limpa == palindromo:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')

