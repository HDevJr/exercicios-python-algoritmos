# 🧠 Conceito: Funções em Python

---

## 1. O que são funções

As **funções** são blocos de código reutilizáveis que executam uma tarefa específica.  
Elas ajudam a organizar o código, evitar repetição e tornar o programa mais legível e modular.

> 💡 “Em vez de repetir o mesmo código várias vezes, crie uma função que faz isso por você.”

Uma função pode **receber dados (parâmetros)**, executar ações e **retornar um resultado**.

---

## 2. Sintaxe básica

```python
def nome_da_funcao(parâmetro):
    # bloco de código
    return resultado
```

### Exemplo:

```python
def saudacao():
    print('Olá, mundo!')

saudacao()
# Saída: Olá, mundo!
```

---

## 3. Funções com parâmetros

As funções podem receber valores externos (argumentos).

```python
def cumprimentar(nome):
    print(f'Olá, {nome}!')

cumprimentar('Cesar')
# Saída: Olá, Cesar!
```

---

## 4. Funções com retorno (`return`)

O `return` envia o resultado de volta para quem chamou a função.

```python
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)

# Saída: 8
```

> Se você não usa `return`, a função retorna `None` por padrão.

---

## 5. Parâmetros padrão (default)

Pode-se definir valores padrão para parâmetros, que serão usados se nenhum argumento for passado.

```python
def mensagem(texto='Bem-vindo!'):
    print(texto)

mensagem()               # usa o padrão
mensagem('Olá, Python!') # substitui o padrão

# Saída:
# Bem-vindo!
# Olá, Python!
```

---

## 6. Retorno múltiplo

Uma função pode retornar vários valores, separados por vírgulas.

```python
def calcular(a, b):
    soma = a + b
    sub = a - b
    return soma, sub

resultado_soma, resultado_sub = calcular(10, 5)
print(resultado_soma, resultado_sub)

# Saída: 15 5
```

---

## 7. Escopo de variáveis

O escopo define **onde uma variável pode ser acessada**.

```python
x = 10  # variável global

def teste():
    y = 5  # variável local
    print(x + y)

teste()
print(x)  # funciona
# print(y)  # erro: variável local não existe fora da função
```

---

## 8. Documentando funções (docstring)

As **docstrings** são usadas para documentar o que a função faz.

```python
def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

help(soma)
```

**Saída no terminal:**

```
Help on function soma in module __main__:

soma(a, b)
    Retorna a soma de dois números.
```

---

## 9. Funções anônimas (`lambda`)

As funções `lambda` são funções pequenas, de uma linha só.

```python
dobro = lambda x: x * 2
print(dobro(5))
# Saída: 10
```

Usadas normalmente com `map()`, `filter()` e `sorted()`:

```python
numeros = [1, 2, 3, 4]
pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)

# Saída: [2, 4]
```

---

## 10. Argumentos especiais

### 🔹 Número variável de argumentos (`*args`)

```python
def somar(*numeros):
    return sum(numeros)

print(somar(2, 4, 6, 8))
# Saída: 20
```

### 🔹 Argumentos nomeados (`**kwargs`)

```python
def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

exibir_dados(nome='Cesar', idade=21)
# Saída:
# nome: Cesar
# idade: 21
```

---

## 11. Boas práticas

🔹 Usar nomes de função claros e descritivos (`calcular_media`, `enviar_email`).  
🔹 Manter as funções curtas e com uma única responsabilidade.  
🔹 Documentar funções complexas com docstrings.  
🔹 Preferir retornar valores em vez de imprimir dentro da função.  
🔹 Evitar variáveis globais (use parâmetros e retornos).  
🔹 Reaproveitar funções em outros arquivos (modularização).

---

## 12. Erros comuns

🔹 Esquecer os parênteses ao chamar a função:

```python
def ola():
    print('Oi!')

ola    # ❌ não executa
ola()  # ✅ executa
```

🔹 Usar `return` fora da função → erro de sintaxe.  
🔹 Alterar variáveis locais achando que são globais.  
🔹 Não retornar o valor esperado (falta de `return`).
