# Enunciado 43:
# Leia um texto digitado pelo usuário e conte quantas palavras ele contém, utilizando o método .split().

texto = input('Digite um texto: ')

palavras = texto.split()
quantidade = len(palavras)

print(f'O texto contém {quantidade} palavra(s).')