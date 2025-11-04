# 🧠 Conceito: Variáveis em Python

---

## 1. O que são variáveis?

Em programação, **variáveis** são como "caixas" que guardam valores temporariamente na memória do computador.  
Cada variável tem um **nome (identificador)** e um **valor associado**.

Como se fosse um "apelido" para um dado:

```python
idade = 19
```

Isso significa que o nome `idade` representa o número `19`.

> 💡 Python é uma linguagem de **tipagem dinâmica**, o que significa que não é preciso declarar o tipo da variável — ele é determinado automaticamente.

---

## 2. Sintaxe e exemplos

### 🔹 Atribuição básica

```python
nome = 'Pedro'
idade = 20
altura = 1.78
estudando = True
```

### 🔹 Múltiplas atribuições

```python
x, y, z = 10, 20, 30
```

### 🔹 Reatribuições

```python
x = 5
x = 'agora sou uma string'
```

> O Python permite trocar o tipo do valor — mas devemos usar com cuidado para não confundir o leitor do código.

---

## 3. Tipos primitivos em Python

| Tipo    | Exemplo           | Descrição           |
| ------- | ----------------- | ------------------- |
| `int`   | `idade = 25`      | números inteiros    |
| `float` | `altura = 1.75`   | números decimais    |
| `str`   | `nome = 'Junior'` | texto               |
| `bool`  | `ativo = True`    | verdadeiro ou falso |

---

## 4. Conversão de tipos (type casting)

```python
numero = '10'
numero = int(numero)  # converte a string para inteiro
print(numero + 5)     # saída: 15
```

### 🔹 Funções úteis:

```python
int(), float(), str(), bool()
```

---

## 5. Escopo de variáveis

### 🔹 Variáveis globais
Declaradas fora de funções, visíveis em todo o programa.

### 🔹 Variáveis locais
Criadas dentro de funções, só existem ali dentro.

Exemplo:

```python
x = 10  # global

def mostrar():
    y = 5  # local
    print(x + y)

mostrar()
```

---

## 6. Boas práticas

### 🔹 Usar nomes descritivos

```python
velocidade_media = 80
```

### 🔹 Evitar nomes genéricos

```python
v = 80
```

### 🔹 Outras recomendações
- Usar **snake_case** (minúsculas e separadas por `_`) para nomes de variáveis.  
- Preferir coerência de tipo (não trocar um número por texto na mesma variável).  
- Comentar variáveis complexas:

```python
taxa_juros = 0.035  # 3,5% ao ano
```

---

## 7. Erros comuns

### 🔹 Esquecer aspas em strings

```python
nome = Pedro  # ❌ Erro
nome = 'Pedro'  # ✅ Correto
```

### 🔹 Usar variáveis antes de definir

```python
print(x)
x = 10  # NameError
```

> Sempre defina a variável **antes de usá-la**.
