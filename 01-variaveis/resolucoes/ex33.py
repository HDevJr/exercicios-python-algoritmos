# Enunciado 33:
# Intercale caracteres de duas strings até o fim da menor.

str1 = input('Digite a primeira string: ')
str2 = input('Digite a segunda string: ')

resultado = ''

for c1, c2 in zip(str1, str2):
    resultado += c1 + c2

print(f'String intercalada: {resultado}')