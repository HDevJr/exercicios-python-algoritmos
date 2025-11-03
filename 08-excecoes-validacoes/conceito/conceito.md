Conceito: Tratamento de Exceções e Validações em Python

1. O que são exceções?

    As exceções são erros que ocorrem durante a execução de um programa e interrompem o fluxo normal do código.
    Esses erros podem acontecer por entradas inválidas, divisão por zero, arquivos inexistentes, entre outros.

    🔹 Raciocínio:

        "O tratamento de exceções serve para impedir que o programa quebre,
         mesmo quando algo está errado."

2. Exemplo de erro sem tratamento

    numero = int(input('Digite um número: '))
    print(10 / numero)

    ° Se o usuário digitar 0 -> erro de divisão por zero.
    ° Se digitar uma letra -> erro de conversão de tipo.

    ° Resultado:
        ZeroDivisionError: division by zero
        ValueError: invalid literal for int()

3. Tratamento com try e except

    A estrutura try / except permite tentar executar um bloco de código
    e lidar com o erro, caso aconteça.

    Ex:
        try:
            numero = int(input('Digite um número: '))
            print(10 / numero)
        except:
            print('Ocorreu um erro!')
    
    -> Agora o programa não quebra -- apenas exibe a mensagem personalizada.

4. Lidando com exceções específicas

    Podesse capturar tipos específicos de erro, o que é mais profissional e seguro.

    Ex:
        try:
            numero = int(input('Digite um número: '))
            print(10 / numero)
        except ZeroDivisionError:
            print('Erro: não é possível dividir por zero!')
        except ValueError:
            print('Erro: você precisa digitar um número!')

5. Usando else e finally

    🔹 else -> executa apenas se não ocorrer erro.
    🔹 finally -> executa sempre, com ou sem erro.

    Ex:
        try:
            numero = int(input('Digite um número: '))
            resultado = 10 / numero
        except ZeroDivisionError:
            print('Divisão por zero não permitida.')
        else:
            print(f'Resultado: {resultado'})
        finally:
            print('Programa encerrado).
        
        # Saída: Resultado: 5.0
                 Programa encerrado.

6. Capturando o erro em uma variável (as e)

    try:
        arquivo = open('inexistente.txt')
    except FileNotFoundError as e:
        print(f'Erro: {e}')
        
        # Saída: Erro: [Errno 2] No such file or directory: 'inexistente.txt'

7. Criando exceções personalizadas (raise)

    É possível lançar os próprios erros quando detectar situações inválidas.

    Ex:
        def sacar(valor):
            if valor < 0:
                raise ValueError('O valor não pode ser negativo.')
            print(f'Saque de R$ {valor} realizado.')
        
        try:
            sacar(-100)
        except ValueError as erro:
            print(f'Erro: {erro}')
        
        # Saída: Erro> O valor não pode ser negativo.

8. Criando classes de exceção customizadas

    Ex:
        class SaldoInsuficienteErro(Exception):
            pass
        
        def sacar(saldo, valor):
            if valor > saldo:
                raise SaldoInsuficienteError('Saldo insuficiente.')
            print('Saque realizado com sucesso!)
        try:
            sacar(100, 250)
        except SaldoInsuficienteErroe as e:
            print(e)
        
        # Saída: Saldo insuficiente.

9. Validações de entrada (input validation)

    Validações servem para verificar se os dados fornecidos estão corretos antes de processar.

    Ex:
        idade = input('Digite sua idade: ')

        if not idade.isdigit():
            print('Erro: Digite apenas números.')
        else:
            idade = int(idade)
            print(f'Idade registrada: {idade}')

    🔹 Validação com try + while

        Ex:
            while True:
                try:
                    idade = int(input('Digite sua idade: '))
                    if idade < 0:
                        print('Erro: a idade não pode ser negativa.')
                        continue
                    break
                except ValueError:
                    print('Erro: digite um número válido.')
            
            # Saída: Digite sua idade: abc
                     Erro: digite um número válido.
                     Digite sua idade: -2
                     Erro: a idade não pode ser negativa.
                     Digite sua idade: 25

10. Boas práticas

    🔹 Sempre tratar exceções que podem acontecer (não "capture tudo" com except: sem necessidade).
    🔹 Usar sempre tipos específicos de erro (ex: ValueError, FileFoundError, ZeroDivisionError).
    🔹 Fornecer mensagens de erro claras e amigáveis.
    🔹 Validar entradas antes de processar.
    🔹 Usar finally para liberar recursos (fechar arquivos, conexões etc.).
    🔹 Criar exceções personalizadas para regras de negócio específicas.

11. Erros comuns

    🔹 Esquecer de validar dados do usuário.
    🔹 Usar except: sem tipo (dificuldade depuração).
    🔹 Não fechar arquivos em caso de erro (use with open()).
    🔹 Ignorar exceções silenciosas (sem print ou log).