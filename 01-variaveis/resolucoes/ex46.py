# Enunciado 46:
# Leia uma cor em formato hexadecimal (#rrggbb)
# e converta-a para seus componentes R, G e B (inteiros de 0 a 255).

cor_hex = input("Digite a cor em formato hexadecimal (ex: #1E90FF): ").strip().lstrip('#')

r = int(cor_hex[0:2], 16)
g = int(cor_hex[2:4], 16)
b = int(cor_hex[4:6], 16)

print(f'''
Cor hexadecimal: #{cor_hex.upper()}
R: {r}
G: {g}
B: {b}
''')
