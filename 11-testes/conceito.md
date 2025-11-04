# Conceito: Testes Automatizados em Python (Python e Unittest)

---

## 1. O que são testes automatizados?

Os testes automatizados são scripts que verificam automaticamente se o código funciona como esperado.  
Eles ajudam a detectar erros cedo, evitar regressões e garantir que novas alterações não quebrem o sistema.

>  “Em vez de testar o código manualmente, você ensina o computador a testar por você.”

---

## 2. Por que testar?

✅ Evita bugs em produção  
✅ Facilita refatorações com segurança  
✅ Aumenta a confiança no código  
✅ Permite integração contínua (CI/CD)  
✅ Serve como documentação viva do sistema

---

## 3. Tipos de testes

| Tipo                | O que testa                                     | Exemplo                            |
| ------------------- | ----------------------------------------------- | ---------------------------------- |
| **Unitário**        | Uma função ou classe isolada                    | Testar uma função `soma()`         |
| **De integração**   | Interação entre módulos                         | API + banco de dados               |
| **Funcional / E2E** | O sistema completo em uso                       | Login, fluxo de compra             |
| **De regressão**    | Verifica se algo “antigo” quebrou após mudanças | Testes repetidos após refatorações |

---

## 4. Estrutura básica de um teste unitário

Um teste verifica se uma entrada produz a saída esperada.

```python
def somar(a, b):
    return a + b

def test_soma():
    assert somar(2, 3) == 5

# Saída (executando com pytest): pytest .
# ✓ test_soma PASSED
```

---

## 5. Testes com `assert`

O comando `assert` verifica se uma condição é verdadeira.  
Se for falsa, o teste falha.

```python
def dobro(x):
    return x * 2

def test_dobro():
    assert dobro(4) == 8
    assert dobro(0) == 0
    assert dobro(-2) == -4
```

---

## 6. Criando testes com o módulo `unittest` (nativo do Python)

### 🔹 Estrutura básica

```python
import unittest

def soma(a, b):
    return a + b

class TesteSoma(unittest.TestCase):
    def test_soma_positiva(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativa(self):
        self.assertEqual(soma(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

**Saída esperada:**
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

---

### 🔹 Explicação

#### 1. Importação do módulo
```python
import unittest
```
Importa o framework de testes nativo do Python.

#### 2. Função a ser testada
```python
def soma(a, b):
    return a + b
```
Função simples para somar dois números.

#### 3. Classe de teste
```python
class TesteSoma(unittest.TestCase):
```
Define uma classe de testes que herda de `unittest.TestCase`.

#### 4. Métodos de teste
```python
def test_soma_positiva(self):
    self.assertEqual(soma(2, 3), 5)
```

- `self.assertEqual(x, y)` → verifica se `x` é igual a `y`.  
- Se for, o teste passa ✅  
- Caso contrário, falha ❌  

#### 5. Executando os testes
```python
if __name__ == '__main__':
    unittest.main()
```

O Python procura automaticamente classes herdando de `unittest.TestCase` e executa métodos que começam com `test_`.

---

### 🔹 Saída esperada

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Cada ponto (.) representa um teste que passou ✅  
“Ran 2 tests” → dois testes executados.  
“OK” → todos passaram.

---

### 🔹 Resumo

| Elemento                             | Função                                         |
| ------------------------------------ | ---------------------------------------------- |
| `unittest`                           | Módulo padrão para testes automáticos          |
| `class TesteSoma(unittest.TestCase)` | Define uma classe de testes                    |
| `test_...`                           | Métodos executados automaticamente como testes |
| `assertEqual(a, b)`                  | Verifica se o resultado é o esperado           |
| `unittest.main()`                    | Roda todos os testes do arquivo                |
| `OK`                                 | Todos os testes passaram                       |

---

## 7. Testando exceções com `unittest`

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida.")
    return a / b

class TesteDivisao(unittest.TestCase):
    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)
```

Essa função lança um erro (`ValueError`) se `b == 0`.  
O teste usa `self.assertRaises` para garantir que esse erro realmente aconteça.

---

## 8. Testes com **Pytest** (biblioteca moderna e popular)

### 🔹 Instalação
```
pip install pytest
```

### 🔹 Exemplo
```python
def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
```

### 🔹 Estrutura recomendada
```
meu_projeto/
│
├── app/
│   └── funcoes.py
└── tests/
    └── test_funcoes.py
```

### 🔹 Executar
```
pytest
```

---

## 9. Testando exceções com Pytest

```python
import pytest

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero.")
    return a / b

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)
```

---

## 10. Usando **setup** e **teardown**

Às vezes, é necessário preparar ou limpar algo antes/depois dos testes.

### 🔹 Com unittest

```python
class TesteConta(unittest.TestCase):
    def setUp(self):
        self.saldo = 100  # executa antes de cada teste
    
    def tearDown(self):
        self.saldo = 0  # executa depois de cada teste
    
    def test_saque(self):
        self.saldo -= 50
        self.assertEqual(self.saldo, 50)
```

### 🔹 Com pytest (fixture)
```python
import pytest

@pytest.fixture
def saldo_inicial():
    return 100

def test_saque(saldo_inicial):
    novo_saldo = saldo_inicial - 50
    assert novo_saldo == 50
```

---

## 11. Cobertura de testes (coverage)

Para medir quanto do código foi testado:

```bash
pip install pytest-cov
pytest --cov=app/
```

**Saída:**
```
----------- coverage: platform win, python 3.12 -----------
Name                 Stmts   Miss  Cover
----------------------------------------
app/funcoes.py          10      0   100%
```

---

## 12. Integração com CI/CD (GitHub Actions)

Exemplo de arquivo `.github/workflows/test.yml`:

```yaml
name: Python Tests

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install pytest pytest-cov
      - name: Run tests
        run: pytest --cov=app/
```

Assim, os testes rodam automaticamente a cada atualização do repositório.

---

## 13. Boas práticas

✅ Nomeie arquivos de teste com o prefixo `test_`.  
✅ Cada função deve testar apenas uma coisa.  
✅ Escreva testes antes ou junto com o código (TDD).  
✅ Use mensagens de erro claras nos asserts.  
✅ Mantenha os testes rápidos e independentes.  
✅ Garanta cobertura acima de 80%.

---

## 14. Erros comuns

❌ Testes dependentes da ordem de execução.  
❌ Não isolar dados entre testes (usar variáveis globais).  
❌ Testes lentos e pouco específicos.  
❌ Esquecer de configurar o ambiente de teste.
