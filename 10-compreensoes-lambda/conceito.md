# 🧩 Conceito: Compreensões e Expressões Lambda em Python

---

## 1. O que são Compreensões?

As **Compreensões** são uma forma concisa e elegante de criar novas coleções  
(**listas**, **dicionários**, **conjuntos**) a partir de **iteráveis existentes** (listas, ranges, strings, etc).

> 💡 “É uma maneira de transformar ou filtrar dados em uma única linha, sem precisar de loops explícitos.”

---

## 2. List Comprehension (Compreensão de Listas)

A forma mais usada — permite criar listas em **uma única linha**.

**Sintaxe:**  
```python
[expressão for item in iterável if condição]
```

### 🔹 Exemplo 1 — Quadrados de 1 a 5
```python
quadrados = [x**2 for x in range(1, 6)]
print(quadrados)
# Saída: [1, 4, 9, 16, 25]
```

### 🔹 Exemplo 2 — Filtrar números pares
```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)
# Saída: [0, 2, 4, 6, 8]
```

### 🔹 Exemplo 3 — Manipular strings
```python
nomes = ['ana', 'pedro', 'maria']
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)
# Saída: ['ANA', 'PEDRO', 'MARIA']
```

### 🔹 Exemplo 4 — Condicional inline
```python
numeros = [1, 2, 3, 4, 5]
resultado = ['par' if x % 2 == 0 else 'ímpar' for x in numeros]
print(resultado)
# Saída: ['ímpar', 'par', 'ímpar', 'par', 'ímpar']
```

---

## 3. Dict Comprehension (Compreensão de Dicionários)

Permite criar **dicionários** a partir de iteráveis.

```python
quadrados = {x: x**2 for x in range(5)}
print(quadrados)
# Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 4. Set Comprehension (Compreensão de Conjuntos)

Permite criar **conjuntos** sem duplicatas.

```python
numeros = [1, 2, 2, 3, 4, 4]
sem_duplicatas = {x for x in numeros}
print(sem_duplicatas)
# Saída: {1, 2, 3, 4}
```

---

## 5. Generator Expression (Geradores)

Geradores são semelhantes às list comprehensions,  
mas **não armazenam todos os elementos na memória** — geram um item por vez, sob demanda.

```python
quadrados = (x**2 for x in range(5))
for q in quadrados:
    print(q)
# Saída:
# 0
# 1
# 4
# 9
# 16
```
> 💡 Ideal para grandes volumes de dados — economiza memória.

---

## 6. O que são Expressões Lambda?

As **funções lambda** (também chamadas de **funções anônimas**) são pequenas funções sem nome,  
geralmente usadas em operações simples e temporárias.

> 💡 “É uma função rápida, de uma linha só, usada quando uma função comum seria longa demais.”

**Sintaxe:**  
```python
lambda argumentos: expressão
```

### 🔹 Exemplo 1 — Função lambda simples
```python
dobro = lambda x: x * 2
print(dobro(5))
# Saída: 10
```

### 🔹 Exemplo 2 — Com dois argumentos
```python
soma = lambda a, b: a + b
print(soma(3, 7))
# Saída: 10
```

### 🔹 Exemplo 3 — Com condição
```python
par_ou_impar = lambda x: 'par' if x % 2 == 0 else 'ímpar'
print(par_ou_impar(7))
# Saída: ímpar
```

---

## 7. Lambda com Funções Embutidas (`map`, `filter`, `sorted`)

### 🔹 `map()` — aplica uma função a todos os elementos
```python
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)
# Saída: [2, 4, 6, 8]
```

### 🔹 `filter()` — filtra elementos com base em uma condição
```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
# Saída: [2, 4, 6]
```

### 🔹 `sorted()` — ordena com critério personalizado
```python
nomes = ['Ana', 'Pedro', 'João', 'Maria']
ordenados = sorted(nomes, key=lambda nome: nome.lower())
print(ordenados)
# Saída: ['Ana', 'João', 'Maria', 'Pedro']
```

---

## 8. Lambda dentro de Dicionários e Listas

```python
operacoes = {
    'soma': lambda a, b: a + b,
    'multiplica': lambda a, b: a * b
}

print(operacoes['soma'](3, 4))
print(operacoes['multiplica'](3, 4))
# Saída:
# 7
# 12
```

---

## 9. Boas Práticas

✅ Use compreensões quando **melhorarem a legibilidade**.  
✅ Use `lambda` apenas para **funções simples** (uma linha).  
✅ Prefira **funções nomeadas** para lógicas complexas.  
✅ Combine `lambda` com `map`, `filter` e `sorted` para operações funcionais rápidas.  
✅ Para expressões longas, **divida em funções normais** com `def`.

---

## 10. Erros Comuns

⚠️ Funções `lambda` com mais de uma linha → não é permitido.  
⚠️ Compreensões muito complexas → perdem legibilidade.  
⚠️ Esquecer de converter `map()` e `filter()` em lista → `list()`.  
⚠️ Usar `lambda` onde uma função nomeada seria mais clara.

---
