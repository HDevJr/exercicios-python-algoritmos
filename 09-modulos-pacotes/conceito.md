# 📦 Conceito: Módulos, Pacotes e Importações em Python

---

## 1. O que são módulos?

Um **módulo** é um arquivo Python (`.py`) que contém **funções**, **classes** ou **variáveis** que podem ser reutilizadas em outros programas.

> 💡 “Um módulo é como uma caixa de ferramentas que você pode importar quando precisar.”

Isso ajuda a **organizar o código**, **evitar repetição** e **facilitar a manutenção**.

---

## 2. Criando e usando um módulo

### 🔹 Exemplo — criando um módulo:

**Arquivo `matematica.py`:**
```python
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b
```

**Arquivo `principal.py`:**
```python
import matematica

print(matematica.somar(5, 3))
print(matematica.subtrair(10, 4))
```
**Saída:**
```
8
6
```

---

## 3. Importações específicas

É possível importar **apenas o que precisa** de um módulo:

```python
from matematica import somar

print(somar(10, 5))
```
Agora não é preciso usar `matematica.somar`, apenas `somar()`.

---

## 4. Alias (apelidos)

Use `as` para criar um **apelido** para o módulo — útil quando o nome é longo:

```python
import matematica as m

print(m.somar(2, 3))
```

---

## 5. Módulos internos do Python (built-in)

O Python já vem com uma **biblioteca padrão** com centenas de módulos prontos para uso.

| Módulo     | Uso principal                                |
| ----------- | -------------------------------------------- |
| `math`      | Funções matemáticas (√, π, seno, log, etc.)  |
| `random`    | Geração de números aleatórios                |
| `datetime`  | Manipulação de datas e horários              |
| `os`        | Operações com arquivos e sistema operacional |
| `sys`       | Interação com o interpretador Python         |
| `json`      | Leitura e escrita de arquivos JSON           |
| `csv`       | Manipulação de arquivos CSV                  |

### 🔹 Exemplos práticos

```python
import math
print(math.sqrt(16))  # raiz quadrada
print(math.pi)        # constante π

from datetime import datetime
agora = datetime.now()
print(agora.strftime('%d/%m/%Y %H:%M'))
```

---

## 6. Instalando módulos externos

Além dos internos, existem módulos **externos** criados pela comunidade, instaláveis via **pip** (gerenciador de pacotes Python).

### 🔹 Instalar:
```
pip install requests
```

### 🔹 Usar:
```python
import requests

resposta = requests.get('https://api.github.com')
print(resposta.status_code)
```

---

## 7. O que são pacotes?

Um **pacote** é uma **pasta** que contém vários módulos organizados logicamente, junto com um arquivo especial chamado `__init__.py`.

### 🔹 Estrutura:
```
meu_pacote/
│
├── __init__.py
├── calculos.py
└── conversoes.py
```

### 🔹 Uso:
```python
from meu_pacote.calculos import somar
```

> O arquivo `__init__.py` indica ao Python que a pasta é um **pacote importável**.  
> Desde o Python 3.3 ele pode estar vazio, mas é boa prática incluí-lo.

---

## 8. Estrutura de um projeto modular

```
projeto/
│
├── main.py
├── util/
│   ├── __init__.py
│   ├── arquivos.py
│   ├── calculos.py
│   └── strings.py
```

**Dentro de `main.py`:**
```python
from util.calculos import soma
from util.strings import capitalizar

print(soma(3, 5))
print(capitalizar("André Augusto"))
```

---

## 9. Importações relativas (em pacotes)

Dentro de pacotes, é possível importar de forma **relativa**:

```python
# dentro de util/calculos.py
from .strings import capitalizar
```

- `.` → indica o mesmo pacote.  
- `..` → indica o pacote pai.

---

## 10. O módulo `__name__` e a execução direta

Cada arquivo Python tem um atributo interno `__name__`.  
Quando o arquivo é executado diretamente, `__name__ == "__main__"`.

```python
# arquivo matematica.py
def soma(a, b):
    return a + b

if __name__ == "__main__":
    print("Executando diretamente")
```

---

## 11. Boas práticas

✅ Mantenha módulos pequenos e coesos (um tema por arquivo).  
✅ Use nomes descritivos (`arquivo.py`, `usuario.py`, `api.py`).  
✅ Evite importações circulares (um módulo importando o outro).  
✅ Agrupe funções comuns em pacotes.  
✅ Use `requirements.txt` para listar dependências externas.  
✅ Teste cada módulo isoladamente com `__name__ == "__main__"`.

---

## 12. Erros comuns

⚠️ **Atenção a erros frequentes:**

- `ModuleNotFoundError` → módulo não existe ou não está no mesmo diretório.  
- `ImportError` → função ou classe não encontrada dentro do módulo.  
- Caminhos incorretos de importação dentro de pacotes.  
- Esquecer o arquivo `__init__.py` em pastas de pacotes.

---
