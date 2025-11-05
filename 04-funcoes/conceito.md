# 🧠 Funções e Métodos em Python

---

## 🧩 Parte 1: Conceito de Funções

### 1. O que são funções

As **funções** são blocos de código reutilizáveis que executam uma tarefa específica.
Elas ajudam a organizar o código, evitar repetição e tornar o programa mais legível e modular.

> 💡 “Em vez de repetir o mesmo código várias vezes, crie uma função que faz isso por você.”

Uma função pode **receber dados (parâmetros)**, executar ações e **retornar um resultado**.

---

### 2. Sintaxe básica

```python
def nome_da_funcao(parâmetro):
    # bloco de código
    return resultado
```

**Exemplo:**

```python
def saudacao():
    print('Olá, mundo!')

saudacao()
# Saída: Olá, mundo!
```

---

### 3. Funções com parâmetros

As funções podem receber valores externos (argumentos).

```python
def cumprimentar(nome):
    print(f'Olá, {nome}!')

cumprimentar('Cesar')
# Saída: Olá, Cesar!
```

---

### 4. Funções com retorno (`return`)

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

### 5. Parâmetros padrão (default)

Pode-se definir valores padrão para parâmetros, que serão usados se nenhum argumento for passado.

```python
def mensagem(texto='Bem-vindo!'):
    print(texto)

mensagem()               # usa o padrão
mensagem('Olá, Python!') # substitui o padrão
```

---

### 6. Retorno múltiplo

Uma função pode retornar vários valores, separados por vírgulas.

```python
def calcular(a, b):
    soma = a + b
    sub = a - b
    return soma, sub

resultado_soma, resultado_sub = calcular(10, 5)
print(resultado_soma, resultado_sub)
```

---

### 7. Escopo de variáveis

Define **onde uma variável pode ser acessada**.

```python
x = 10  # global

def teste():
    y = 5  # local
    print(x + y)

teste()
```

---

### 8. Documentando funções (docstring)

```python
def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

help(soma)
```

---

### 9. Funções anônimas (`lambda`)

Usadas em operações simples e rápidas.

```python
dobro = lambda x: x * 2
print(dobro(5))
```

---

### 10. Argumentos especiais

#### 🔹 Número variável de argumentos (`*args`)

```python
def somar(*numeros):
    return sum(numeros)
```

#### 🔹 Argumentos nomeados (`**kwargs`)

```python
def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')
```

---

### 11. Métodos úteis relacionados a funções

| Função / Método              | Descrição                                                              |
| ---------------------------- | ---------------------------------------------------------------------- |
| `map(func, iterável)`        | Aplica uma função a cada item do iterável                              |
| `filter(func, iterável)`     | Filtra os itens que retornam `True`                                    |
| `reduce(func, seq)`          | Acumula valores aplicando uma função (precisa importar de `functools`) |
| `lambda`                     | Cria funções anônimas inline                                           |
| `zip(*iteráveis)`            | Une elementos de iteráveis em pares                                    |
| `enumerate(iterável)`        | Itera com índice e valor                                               |
| `any(iterável)`              | `True` se algum elemento for verdadeiro                                |
| `all(iterável)`              | `True` se todos forem verdadeiros                                      |
| `sorted(iterável, key=func)` | Ordena aplicando função personalizada                                  |

---

### 12. Boas práticas

* Use nomes claros (`calcular_media`, `gerar_relatorio`).
* Funções curtas e com uma única responsabilidade.
* Documente com **docstrings**.
* Prefira retornar valores a imprimir.
* Evite variáveis globais.
* Reutilize funções em módulos.

---

### 13. Erros comuns

* Esquecer `()` ao chamar uma função.
* Usar `return` fora da função.
* Confundir variáveis locais e globais.
* Não retornar o valor esperado.

---

## 🧩 Parte 2: Funções e Métodos Fundamentais do Python

### 🟩 Funções Built-in

| Função                | Descrição                                 |
| --------------------- | ----------------------------------------- |
| `abs()`               | Valor absoluto                            |
| `all()` / `any()`     | Verifica se todos / algum são verdadeiros |
| `enumerate()`         | Itera com índice                          |
| `zip()`               | Junta listas                              |
| `map()`               | Aplica função                             |
| `filter()`            | Filtra valores                            |
| `sum()`               | Soma elementos                            |
| `max()` / `min()`     | Maior / menor                             |
| `sorted()`            | Ordena lista                              |
| `len()`               | Comprimento                               |
| `type()`              | Tipo                                      |
| `isinstance()`        | Verifica tipo                             |
| `input()` / `print()` | Entrada / saída                           |
| `range()`             | Sequência numérica                        |

---

### 🟨 Métodos de String (`str`)

| Método                        | Descrição                 |
| ----------------------------- | ------------------------- |
| `upper()` / `lower()`         | Maiúsculas / minúsculas   |
| `strip()`                     | Remove espaços            |
| `split()`                     | Divide em lista           |
| `join()`                      | Junta strings             |
| `replace()`                   | Substitui texto           |
| `count()`                     | Conta ocorrências         |
| `find()`                      | Encontra posição          |
| `startswith()` / `endswith()` | Verifica início/fim       |
| `isalpha()` / `isdigit()`     | Verifica letras / números |

---

### 🟦 Métodos de Lista (`list`)

| Método                 | Descrição               |
| ---------------------- | ----------------------- |
| `append()`             | Adiciona elemento       |
| `insert()`             | Insere na posição       |
| `extend()`             | Junta listas            |
| `remove()` / `pop()`   | Remove elemento         |
| `sort()` / `reverse()` | Ordena / inverte        |
| `count()` / `index()`  | Conta / encontra índice |

---

### 🟥 Métodos de Dicionário (`dict`)

| Método                | Descrição                |
| --------------------- | ------------------------ |
| `keys()` / `values()` | Retorna chaves / valores |
| `items()`             | Retorna pares            |
| `get()`               | Retorna valor seguro     |
| `update()`            | Atualiza valores         |
| `pop()` / `clear()`   | Remove / limpa           |

---

### 🟧 Métodos de Conjunto (`set`)

| Método                       | Descrição          |
| ---------------------------- | ------------------ |
| `add()` / `update()`         | Adiciona itens     |
| `remove()` / `discard()`     | Remove itens       |
| `union()` / `intersection()` | União / interseção |
| `difference()`               | Diferença          |

---

### 🟪 Métodos de Tupla (`tuple`)

| Método    | Descrição         |
| --------- | ----------------- |
| `count()` | Conta ocorrências |
| `index()` | Índice do valor   |

---

### ⚫ Métodos de Arquivo (`file`)

| Método               | Descrição             |
| -------------------- | --------------------- |
| `open()`             | Abre arquivo          |
| `read()` / `write()` | Lê / escreve          |
| `readlines()`        | Lê todas as linhas    |
| `writelines()`       | Escreve várias linhas |
| `close()`            | Fecha arquivo         |

---

### 🧩 Dicas e boas práticas

✅ Use `dir(obj)` para ver todos os métodos disponíveis.
✅ Use `help(func)` para entender uma função.
✅ Use `type(obj)` para descobrir o tipo.
✅ Teste os métodos manualmente no terminal para fixar o aprendizado.
