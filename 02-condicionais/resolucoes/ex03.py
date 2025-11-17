# Enunciado 03:
# Login simples: verificar usuário e senha cadastrado.

USUARIO_CADASTRADO = 'admin'
SENHA_CADASTRADA = '1234ABC'

usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
    print('Usuário autenticado')
else:
    print('Usuário ou senha incorretos')

