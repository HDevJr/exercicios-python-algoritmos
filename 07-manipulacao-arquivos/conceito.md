# 🧠 Conceito: Manipulação de Arquivos em Python

---

## 1. O que é manipulação de arquivos?

A **manipulação de arquivos** permite que programas **leiam, gravem e gerenciem** dados armazenados no
disco (como `.txt`, `.csv`, `.json`, etc).  
É essencial para **persistência de dados** — ou seja, manter informações mesmo após o programa ser fechado.

> 💡 “Variáveis guardam dados temporariamente. Arquivos guardam dados permanentemente.”

---

## 2. Abertura de arquivos com `open()`

A função `open()` é usada para abrir arquivos.

```python
open(caminho, modo)
```

### 🔹 Modos de abertura

| Modo  | Descrição                                        |
| ----- | ------------------------------------------------ |
| `'r'` | leitura (padrão) — erro se o arquivo não existir |
| `'w'` | escrita — sobrescreve o conteúdo existente       |
| `'a'` | anexar — adiciona no final do arquivo            |
| `'x'` | cria novo arquivo — erro se já existir           |
| `'b'` | modo binário (imagens, PDFs, etc.)               |

---

## 3. Lendo arquivos (`read`, `readline`, `readlines`)

### 🔹 `read()` — lê todo o conteúdo

```python
arquivo = open('dados.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
```

### 🔹 `readline()` — lê linha por linha

```python
arquivo = open('dados.txt', 'r', encoding='utf-8')
linha = arquivo.readline()
print(linha)
arquivo.close()
```

### 🔹 `readlines()` — cria uma lista de linhas

```python
arquivo = open('dados.txt', 'r', encoding='utf-8')
linhas = arquivo.readlines()
for linha in linhas:
    print(linha.strip())
arquivo.close()
```

---

## 4. Escrevendo em arquivos (`write`, `writelines`)

### 🔹 Escrever texto novo

```python
arquivo = open('dados.txt', 'w', encoding='utf-8')
arquivo.write('Olá, mundo!\n')
arquivo.write('Aprendendo manipulação de arquivos.')
arquivo.close()
```

> ⚠️ Se o arquivo já existir, ele será **sobrescrito**.

### 🔹 Adicionar conteúdo sem apagar o existente

```python
arquivo = open('dados.txt', 'a', encoding='utf-8')
arquivo.write('\nNova linha adicionada!')
arquivo.close()
```

### 🔹 Escrever várias linhas de uma vez

```python
linhas = ['Python\n', 'JavaScript\n', 'Django\n']
arquivo = open('linguagens.txt', 'w', encoding='utf-8')
arquivo.writelines(linhas)
arquivo.close()
```

---

## 5. O gerenciador de contexto (`with`)

O comando `with` **fecha automaticamente** o arquivo, mesmo se ocorrer erro.  
É a forma mais **segura e recomendada**.

```python
with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

### 🔹 Resumo

| Comando                 | Função                                     |
| ----------------------- | ------------------------------------------ |
| `open('arquivo', 'r')`  | Abre o arquivo no modo leitura             |
| `encoding='utf-8'`      | Garante leitura correta de acentos         |
| `with ... as ...:`      | Fecha o arquivo automaticamente após o uso |
| `for linha in arquivo:` | Lê o arquivo linha por linha               |
| `linha.strip()`         | Remove quebras de linha e espaços extras   |

---

## 6. Verificando existência e excluindo arquivos

Usa-se o módulo `os` para manipular arquivos no sistema.

```python
import os

if os.path.exists('dados.txt'):
    os.remove('dados.txt')  # exclui o arquivo
else:
    print('Arquivo não encontrado.')
```

### 🔹 Manipulando diretórios

```python
os.mkdir('pasta_nova')    # cria pasta
os.listdir('.')           # lista arquivos do diretório atual
os.rmdir('pasta_nova')    # remove pasta vazia
```

---

## 7. Manipulando arquivos `.csv`

Os arquivos **CSV (Comma-Separated Values)** são comuns para guardar tabelas de dados.

### 🔹 Escrevendo CSV

```python
import csv

with open('alunos.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['Nome', 'Idade'])
    escritor.writerow(['Ana', 20])
    escritor.writerow(['João', 22])
```

### 🔹 Lendo CSV

```python
with open('alunos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
```

---

## 8. Manipulando arquivos `.json`

O **JSON (JavaScript Object Notation)** é um formato leve de troca de dados.  
O Python fornece o módulo `json` para lidar com ele facilmente.

### 🔹 Escrever JSON

```python
import json

dados = {'nome': 'Pedro', 'idade': 21, 'ativo': True}

with open('usuario.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
```

### 🔹 Ler JSON

```python
with open('usuario.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    print(dados['nome'])
# Saída: Pedro
```

---

## 9. Trabalhando com arquivos binários (ex: imagens)

```python
with open('foto.jpg', 'rb') as imagem:
    conteudo = imagem.read()

with open('copia.jpg', 'wb') as copia:
    copia.write(conteudo)
```

- `'rb'` → leitura binária  
- `'wb'` → escrita binária

---

## 10. Boas práticas

🔹 Sempre usar `with open()` para garantir fechamento automático.  
🔹 Usar `encoding='utf-8'` para evitar erros de acentuação.  
🔹 Evitar abrir o mesmo arquivo em modo escrita simultaneamente.  
🔹 Fazer **backups** antes de sobrescrever arquivos importantes.  
🔹 Preferir módulos (`csv`, `json`, `pathlib`) para formatos estruturados.  
🔹 Evitar ler arquivos gigantes inteiros — use leitura **linha a linha**.

---

## 11. Erros comuns

| Erro | Causa |
| ---- | ----- |
| `FileNotFoundError` | Arquivo não existe |
| `PermissionError` | Falta de permissão |
| `UnicodeDecodeError` | Problema de acentuação (use `encoding='utf-8'`) |
| `ValueError` | Arquivo aberto no modo errado (ex: `'r'` em vez de `'w'`) |

---
