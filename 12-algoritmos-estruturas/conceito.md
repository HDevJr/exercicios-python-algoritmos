# 🧠 Conceito: Algoritmos e Estruturas Clássicas em Python

---

## 1. O que são algoritmos?

Um **algoritmo** é um conjunto de **passos lógicos e finitos** para resolver um problema.  
Na prática, é uma **receita de instruções** que transforma uma entrada em uma saída.

> 💡 “Um algoritmo é o cérebro de um programa — ele define como algo será feito.”

---

## 2. Estrutura básica de um algoritmo

Um algoritmo normalmente tem:

- **Entrada**: dados fornecidos ao programa  
- **Processamento**: regras, cálculos, decisões  
- **Saída**: resultado final

```python
# Cálculo do dobro de um número
numero = int(input('Digite um número: '))
resultado = numero * 2
print('O dobro é:', resultado)
```

---

## 3. Pilares da lógica de algoritmos

| Pilar             | Explicação                 | Exemplo                      |
| ----------------- | -------------------------- | ---------------------------- |
| **Sequência**     | Execução linha a linha     | `a = 5; b = 2; print(a + b)` |
| **Decisão**       | Estruturas condicionais    | `if`, `elif`, `else`         |
| **Repetição**     | Loops para repetir ações   | `for`, `while`               |
| **Modularização** | Dividir o código em partes | `def`, `class`               |

---

## 4. Estruturas clássicas de repetição e decisão

### 🔹 Estrutura condicional
```python
idade = 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### 🔹 Estrutura de repetição (`for`)
```python
for i in range(5):
    print(i)
```

### 🔹 Estrutura de repetição (`while`)
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

---

## 5. Estruturas clássicas de dados

Essas são as formas mais usadas para armazenar e manipular dados em algoritmos.

| Estrutura             | Características                             | Exemplo              |
| --------------------- | ------------------------------------------- | -------------------- |
| **Lista (list)**      | Dinâmica, ordenada e mutável                | `[1, 2, 3]`          |
| **Fila (queue)**      | FIFO (1º que entra, 1º que sai)             | `deque`              |
| **Pilha (stack)**     | LIFO (último que entra, 1º que sai)         | `append()` + `pop()` |
| **Dicionário (dict)** | Chave → valor                               | `{"nome": "Paulo"}`  |
| **Conjunto (set)**    | Sem ordem e sem repetição                   | `{1, 2, 3}`          |

---

## 6. Pilhas (Stack)

```python
pilha = []

pilha.append('A')
pilha.append('B')
pilha.append('C')

print(pilha)        # ['A', 'B', 'C']
print(pilha.pop())  # remove 'C'
```

> 📌 Uso comum: desfazer ações (Ctrl+Z), histórico de navegação.

---

## 7. Filas (Queue)

```python
from collections import deque

fila = deque()
fila.append('Cliente 1')
fila.append('Cliente 2')
fila.append('Cliente 3')

print(fila.popleft())  # remove o primeiro → Cliente 1
```

> 📌 Uso comum: processamento de tarefas, sistemas de atendimento.

---

## 8. Algoritmos de ordenação

Os algoritmos de ordenação organizam dados em uma sequência (ex: crescente ou decrescente).

### 🔹 Bubble Sort
```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print(bubble_sort([5, 2, 9, 1]))
# Saída: [1, 2, 5, 9]
```

### 🔹 Selection Sort
```python
def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista
```

---

## 9. Algoritmos de busca

### 🔹 Busca Linear
```python
def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1
```

### 🔹 Busca Binária (lista deve estar ordenada)
```python
def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1
```

---

## 10. Complexidade de algoritmos (Big-O)

A **complexidade** mede o desempenho de um algoritmo.  
O símbolo **O** indica o crescimento da execução conforme o tamanho da entrada.

| Complexidade | Nome        | Exemplo                 |
| ------------ | ----------- | ----------------------- |
| `O(1)`       | Constante   | Acesso direto a índice  |
| `O(log n)`   | Logarítmica | Busca binária           |
| `O(n)`       | Linear      | Percorrer lista         |
| `O(n²)`      | Quadrática  | Bubble Sort             |
| `O(2ⁿ)`      | Exponencial | Recursão sem otimização |

> 🎯 Busque sempre eficiência, mas mantenha clareza do código.

---

## 11. Algoritmos recursivos

Um algoritmo é **recursivo** quando chama a si mesmo até atingir uma **condição de parada**.

### 🔹 Fatorial (exemplo clássico)
```python
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))  # 120
```

---

## 12. Estruturas clássicas e aplicações

| Estrutura  | Aplicação comum                             |
| ---------- | ------------------------------------------- |
| Lista      | Armazenar coleções simples                  |
| Pilha      | Histórico, desfazer ações                   |
| Fila       | Processamento por ordem de chegada          |
| Árvore     | Organização hierárquica (menus, pastas)     |
| Grafo      | Rotas, redes sociais, mapas                 |
| Dicionário | Mapear relacionamentos (ex: nome → telefone) |

---

## 13. Boas práticas

✅ Entenda bem a **entrada e a saída** antes de escrever o algoritmo.  
✅ Escreva o passo a passo em português primeiro.  
✅ Prefira **clareza** à complexidade.  
✅ Avalie tempo e espaço (eficiência).  
✅ Teste **casos extremos** (vazio, negativo, muito grande).  
✅ Reescreva algoritmos clássicos — é um ótimo treino de lógica!

---

## 14. Erros comuns

❌ Loops infinitos (`while` sem condição de parada).  
❌ `IndexError` ao acessar posições inexistentes.  
❌ Não inicializar variáveis de contagem.  
❌ Não pensar em casos limites (ex: listas vazias).

---
