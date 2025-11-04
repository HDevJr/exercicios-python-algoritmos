# 🧠 Conceito: Estruturas de Dados e Coleções em Python

---

## 1. O que são Estruturas de Dados?

As **estruturas de dados** são formas de **organizar, armazenar e manipular informações** de maneira eficiente dentro de um programa.

> 💡 “Como posso guardar e acessar meus dados da melhor forma possível?”

O Python oferece estruturas integradas muito poderosas, que são a base de praticamente todos os programas:

- `list` → listas  
- `tuple` → tuplas  
- `set` → conjuntos  
- `dict` → dicionários  

Cada uma tem suas vantagens e usos específicos.

---

## 2. Listas (`list`)

As **listas** são coleções **mutáveis** (podem ser alteradas) e **ordenadas**.  
Permitem armazenar diferentes tipos de dados.

```python
frutas = ['maçã', 'banana', 'uva']
numeros = [1, 2, 3, 4, 5]
mistura = ['texto', 10, True, 2.5]
```

### 🔹 Acessando elementos
```python
print(frutas[0])    # maçã
print(frutas[-1])   # uva
```

### 🔹 Modificando
```python
frutas.append('pera')           # adiciona no final
frutas.insert(1, 'laranja')     # insere em posição específica
frutas.remove('banana')         # remove por valor
del frutas[0]                   # remove por índice
```

### 🔹 Outras operações
```python
print(len(frutas))              # tamanho
print(sorted(frutas))           # ordena sem alterar
frutas.sort(reverse=True)       # ordena permanentemente (decrescente)
```

### 🔹 Percorrendo
```python
for fruta in frutas:
    print(fruta)
```

---

## 3. Tuplas (`tuple`)

As **tuplas** são **imutáveis** — depois de criadas, não podem ser alteradas.  
São úteis para representar **dados fixos**.

```python
cores = ('vermelho', 'verde', 'azul')
print(cores[1])  # verde
```

### 🔹 Desempacotando
```python
a, b, c = cores
print(a, c)  # vermelho azul
```

### 🔹 Convertendo
```python
lista = list(cores)
tupla = tuple(lista)
```
> Use tuplas quando os dados não devem ser modificados (ex: coordenadas, meses do ano).

---

## 4. Conjuntos (`set`)

Os **conjuntos** são coleções **não ordenadas**, **sem valores duplicados** e **mutáveis**.  
Ideais para eliminar duplicatas ou fazer operações matemáticas.

```python
numeros = {1, 2, 3, 4}
print(numeros)  # {1, 2, 3, 4}
```

### 🔹 Operações de conjunto
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # união → {1, 2, 3, 4, 5, 6}
print(a & b)  # interseção → {3, 4}
print(a - b)  # diferença → {1, 2}
print(a ^ b)  # diferença simétrica → {1, 2, 5, 6}
```

### 🔹 Métodos úteis
```python
a.add(7)
a.remove(2)
print(len(a))
```
> Use `set` quando a **ordem não importa** e é preciso **eliminar duplicatas rapidamente**.

---

## 5. Dicionários (`dict`)

Os **dicionários** armazenam **pares chave:valor**.  
Cada **chave** é única e mapeia para um valor.

```python
pessoa = {
    'nome': 'Paulo',
    'idade': 21,
    'cidade': 'Londrina'
}
```

### 🔹 Acessando
```python
print(pessoa['nome'])
print(pessoa.get('idade'))
```

### 🔹 Modificando
```python
pessoa['idade'] = 22
pessoa['profissao'] = 'Desenvolvedor'
del pessoa['cidade']
```

### 🔹 Iterando
```python
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
```

### 🔹 Métodos úteis
```python
print(pessoa.keys())    # chaves
print(pessoa.values())  # valores
print(pessoa.items())   # pares (tuplas)
```
> Use dicionários para representar **entidades com propriedades** (ex: pessoas, produtos, configurações).

---

## 6. Estruturas aninhadas

Podemos combinar estruturas, criando **listas de dicionários**, **dicionários de listas**, etc.

```python
alunos = [
    {'nome': 'Ana', 'nota': 9.0},
    {'nome': 'João', 'nota': 7.5}
]

for aluno in alunos:
    print(f"{aluno['nome']} tirou {aluno['nota']}")
# Saída: Ana tirou 9.0 / João tirou 7.5
```

---

## 7. Coleções úteis (`collections`)

O módulo `collections` traz **estruturas avançadas**.

### 🔹 Counter → conta ocorrências
```python
from collections import Counter

frutas = ['maçã', 'banana', 'maçã', 'uva']
contagem = Counter(frutas)
print(contagem)
# Saída: Counter({'maçã': 2, 'banana': 1, 'uva': 1})
```

### 🔹 Defaultdict → dicionário com valor padrão
```python
from collections import defaultdict

d = defaultdict(int)
d['chave'] += 1
print(d['chave'])  # 1
```

> Diferente de um `dict` comum, o `defaultdict` cria automaticamente valores padrão (ex: `int` → 0).

### 🔹 Namedtuple → tupla com nomes
```python
from collections import namedtuple

Pessoa = namedtuple('Pessoa', ['nome', 'idade'])
p = Pessoa('André', 21)
print(p.nome, p.idade)
```

| Conceito              | Explicação                               | Exemplo                                            |
| --------------------- | ---------------------------------------- | -------------------------------------------------- |
| **`namedtuple`**      | Cria tipo de dado com campos nomeados    | `Pessoa = namedtuple('Pessoa', ['nome', 'idade'])` |
| **Criação de objeto** | Passa valores na ordem dos campos        | `p = Pessoa('Junior', 21)`                         |
| **Acesso por nome**   | Usa ponto (.) como nas classes           | `p.nome`, `p.idade`                                |
| **Acesso por índice** | Funciona como tupla normal               | `p[0]`, `p[1]`                                     |
| **Saída**             | Exibe os dados                           | `Junior 21`                                        |

---

## 8. Boas práticas

🔹 Use **listas** para sequências mutáveis.  
🔹 Use **tuplas** para dados imutáveis.  
🔹 Use **sets** para eliminar duplicatas ou comparar grupos.  
🔹 Use **dicionários** para representar pares chave:valor.  
🔹 Prefira **compreensões** (`list`, `dict`, `set`) para criar coleções dinamicamente.  
🔹 Evite estruturas aninhadas muito profundas — prefira funções auxiliares.

---

## 9. Erros comuns

⚠️ **Atenção:**

| Erro | Descrição |
| ---- | ---------- |
| `IndexError` | Acessar índices inexistentes |
| `KeyError` | Acessar chaves que não existem |
| `TypeError` | Tentar alterar tuplas |
| ❗ | Supor que `set` mantém ordem — ele **não mantém** |

