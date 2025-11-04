# 🧠 Conceito: Estruturas Condicionais em Python

---

## 1. O que são estruturas condicionais?

As **estruturas condicionais** permitem que o programa tome decisões com base em determinadas condições.  
Em outras palavras, elas fazem o código “pensar” — executando blocos diferentes dependendo do resultado de uma verificação lógica (**verdadeiro ou falso**).

> 💡 “Se está chovendo, leve um guarda-chuva; senão, vá sem ele.”

Em Python, usamos as palavras-chave `if`, `elif` e `else`.

---

## 2. Sintaxe básica

```python
if condicao:
    # bloco executado se a condição for verdadeira
elif outra_condicao:
    # bloco executado se a primeira for falsa e esta for verdadeira
else:
    # bloco executado se todas as anteriores forem falsas
```

### Exemplo

```python
idade = 18

if idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
else:
    print('Adulto')

# Saída: Adulto
```

---

## 3. Operadores relacionais

| Operador | Significado      | Exemplo  | Resultado |
| -------- | ---------------- | -------- | ---------- |
| `==`     | Igual a          | `5 == 5` | `True`     |
| `!=`     | Diferente de     | `5 != 3` | `True`     |
| `>`      | Maior que        | `7 > 3`  | `True`     |
| `<`      | Menor que        | `2 < 8`  | `True`     |
| `>=`     | Maior ou igual a | `5 >= 5` | `True`     |
| `<=`     | Menor ou igual a | `4 <= 3` | `False`    |

---

## 4. Operadores lógicos

| Operador | Significado                        | Exemplo                  | Resultado |
| -------- | ---------------------------------- | ------------------------ | ---------- |
| `and`    | Todas as condições verdadeiras     | `(idade > 18 and ativo)` | `True`     |
| `or`     | Pelo menos uma condição verdadeira | `(idade < 18 or ativo)`  | `True`     |
| `not`    | Inverte o valor lógico             | `not True`               | `False`    |

### Exemplo

```python
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print('Pode dirigir!')
else:
    print('Não pode dirigir.')
```

---

## 5. Condicionais aninhadas

Podemos colocar um `if` dentro de outro para verificar múltiplos critérios.

```python
idade = 25
empregado = True

if idade >= 18:
    if empregado:
        print('Adulto empregado')
    else:
        print('Adulto desempregado')
else:
    print('Menor de idade')
```

---

## 6. Expressão condicional (if ternário)

Usada para escrever uma condição simples em uma linha.

```python
idade = 17
situacao = 'maior de idade' if idade >= 18 else 'menor de idade'
print(situacao)

# Saída: menor de idade
```

---

## 7. Boas práticas

🔹 Deixar o código mais legível (indentação correta e clara).  
🔹 Evitar condições muito longas — divida em variáveis intermediárias.  
🔹 Preferir `elif` a muitos `if` independentes.  
🔹 Usar o ternário apenas em casos simples.  
🔹 Nomear variáveis de forma clara para indicar o que está sendo testado.

---

## 8. Erros comuns

### 🔹 Usar `=` (atribuição) em vez de `==` (comparação)

```python
if x = 5:  # ❌ Errado
if x == 5:  # ✅ Correto
```

### 🔹 Esquecer indentação

```python
if idade >= 18:
print('Maior de idade')  # ❌ Errado

if idade >= 18:
    print('Maior de idade')  # ✅ Correto
```
