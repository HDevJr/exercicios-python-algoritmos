# ⚙️ Conceito: Tratamento de Exceções e Validações em Python

---

## 1. O que são exceções?

As **exceções** são erros que ocorrem durante a execução de um programa e **interrompem o fluxo normal** do código.  
Esses erros podem acontecer por entradas inválidas, divisão por zero, arquivos inexistentes, entre outros.

> 💡 “O tratamento de exceções serve para impedir que o programa quebre, mesmo quando algo está errado.”

---

## 2. Exemplo de erro sem tratamento

```python
numero = int(input('Digite um número: '))
print(10 / numero)
```

- Se o usuário digitar **0** → erro de divisão por zero  
- Se digitar uma **letra** → erro de conversão de tipo

**Resultado:**  
```
ZeroDivisionError: division by zero
ValueError: invalid literal for int()
```

---

## 3. Tratamento com `try` e `except`

A estrutura `try / except` permite **tentar** executar um bloco de código e **tratar o erro**, caso aconteça.

```python
try:
    numero = int(input('Digite um número: '))
    print(10 / numero)
except:
    print('Ocorreu um erro!')
```
> Agora o programa não quebra — apenas exibe uma mensagem personalizada.

---

## 4. Lidando com exceções específicas

Capturar **erros específicos** é uma prática mais segura e profissional.

```python
try:
    numero = int(input('Digite um número: '))
    print(10 / numero)
except ZeroDivisionError:
    print('Erro: não é possível dividir por zero!')
except ValueError:
    print('Erro: você precisa digitar um número!')
```

---

## 5. Usando `else` e `finally`

- `else` → executa apenas se **não ocorrer erro**
- `finally` → executa **sempre**, com ou sem erro

```python
try:
    numero = int(input('Digite um número: '))
    resultado = 10 / numero
except ZeroDivisionError:
    print('Divisão por zero não permitida.')
else:
    print(f'Resultado: {resultado}')
finally:
    print('Programa encerrado.')
```
**Saída:**  
```
Resultado: 5.0
Programa encerrado.
```

---

## 6. Capturando o erro em uma variável (`as e`)

```python
try:
    arquivo = open('inexistente.txt')
except FileNotFoundError as e:
    print(f'Erro: {e}')
```
**Saída:**  
```
Erro: [Errno 2] No such file or directory: 'inexistente.txt'
```

---

## 7. Criando exceções personalizadas (`raise`)

É possível **lançar seus próprios erros** quando detectar situações inválidas.

```python
def sacar(valor):
    if valor < 0:
        raise ValueError('O valor não pode ser negativo.')
    print(f'Saque de R$ {valor} realizado.')

try:
    sacar(-100)
except ValueError as erro:
    print(f'Erro: {erro}')
```
**Saída:**  
```
Erro: O valor não pode ser negativo.
```

---

## 8. Criando classes de exceção customizadas

```python
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError('Saldo insuficiente.')
    print('Saque realizado com sucesso!')

try:
    sacar(100, 250)
except SaldoInsuficienteError as e:
    print(e)
```
**Saída:**  
```
Saldo insuficiente.
```

---

## 9. Validações de entrada (Input Validation)

Validações verificam se os dados fornecidos estão **corretos** antes de processar.

```python
idade = input('Digite sua idade: ')

if not idade.isdigit():
    print('Erro: Digite apenas números.')
else:
    idade = int(idade)
    print(f'Idade registrada: {idade}')
```

### 🔹 Validação com `try` + `while`

```python
while True:
    try:
        idade = int(input('Digite sua idade: '))
        if idade < 0:
            print('Erro: a idade não pode ser negativa.')
            continue
        break
    except ValueError:
        print('Erro: digite um número válido.')
```
**Saída:**
```
Digite sua idade: abc
Erro: digite um número válido.
Digite sua idade: -2
Erro: a idade não pode ser negativa.
Digite sua idade: 25
```

---

## 10. Boas práticas

✅ Tratar exceções que podem acontecer (não capturar tudo com `except:` sem necessidade).  
✅ Usar tipos específicos (`ValueError`, `FileNotFoundError`, `ZeroDivisionError`).  
✅ Exibir mensagens de erro claras e amigáveis.  
✅ Validar entradas antes de processar.  
✅ Usar `finally` para liberar recursos (fechar arquivos, conexões, etc.).  
✅ Criar exceções personalizadas para regras de negócio.

---

## 11. Erros comuns

⚠️ **Atenção aos erros frequentes:**

- Esquecer de validar dados do usuário.  
- Usar `except:` sem tipo (dificulta depuração).  
- Não fechar arquivos em caso de erro (use `with open()`).  
- Ignorar exceções silenciosamente (sem `print` ou `log`).

---
