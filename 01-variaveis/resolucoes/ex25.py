# Enunciado 25:
# Concatene três pequenas strings com separador '-'.

str1 = input('Digite a primeira palavra: ')
str2 = input('Digite a segunda palavra: ')
str3 = input('Digite a terceira palavra: ')

resultado = '-'.join([str1, str2, str3])

print(f'A junção das três palavras é: {resultado}')