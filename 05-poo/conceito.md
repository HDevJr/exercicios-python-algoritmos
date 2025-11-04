# 🧠 Conceito: Programação Orientada a Objetos (POO) em Python

---

## 1. O que é POO?

A **Programação Orientada a Objetos (POO)** é um paradigma que organiza o código em **objetos**, que representam coisas do mundo real com **propriedades (atributos)** e **comportamentos (métodos)**.

> 💡 “Um carro tem características (cor, modelo) e comportamentos (acelerar, frear).”

Em POO, criamos **classes** que servem como “molde” e **objetos** que são instâncias dessas classes.

---

## 2. Classe e objeto

🔹 **Classe** → é o modelo.  
🔹 **Objeto** → é a instância (um exemplo real da classe).

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

p1 = Pessoa('Ana', 21)
p2 = Pessoa('Gabi', 25)

p1.apresentar()
p2.apresentar()

# Saída:
# Olá, meu nome é Ana e tenho 21 anos.
# Olá, meu nome é Gabi e tenho 25 anos.
```

| Conceito               | O que é                       | Exemplo                   |
| ---------------------- | ----------------------------- | ------------------------- |
| **Classe**             | O molde                       | `class Pessoa:`           |
| **Atributos**          | As informações de cada objeto | `self.nome`, `self.idade` |
| **Método**             | Ações que o objeto executa    | `def apresentar(self):`   |
| **Objeto (instância)** | Um exemplo real da classe     | `p1 = Pessoa('Ana', 21)`  |

---

## 3. O método `__init__` (construtor)

O método especial `__init__` é executado automaticamente quando criamos um objeto, e serve para inicializar os atributos.

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
```

> `self` representa o próprio objeto.  
> Cada atributo pertence a cada instância criada.

---

## 4. Atributos

### 🔹 Atributos de instância
Pertencem a um objeto específico.

```python
class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
```

### 🔹 Atributos de classe
Pertencem à classe e são compartilhados por todos os objetos.

```python
class Carro:
    rodas = 4  # atributo de classe
```

---

## 5. Métodos

Os métodos são **funções dentro da classe** que definem os comportamentos dos objetos.

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')

    def exibir_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')
```

### Exemplo de uso:

```python
conta = ContaBancaria("Junior")

conta.exibir_saldo()  # Saldo atual: R$0.00
conta.depositar(300)
conta.exibir_saldo()  # Saldo atual: R$300.00
conta.sacar(100)
conta.exibir_saldo()  # Saldo atual: R$200.00
conta.sacar(500)      # Saldo insuficiente!
```

---

## 6. Encapsulamento

Encapsulamento é o conceito de **proteger os dados internos de uma classe**, permitindo acesso controlado por métodos.

```python
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def ver_saldo(self):
        return self.__saldo

conta = Conta(1000)
print(conta.ver_saldo())  # acesso permitido
# print(conta.__saldo)    # erro: atributo privado
```

| Termo                | Significado                                         | Exemplo             |
| -------------------- | --------------------------------------------------- | ------------------- |
| **Atributo privado** | Dado interno protegido da classe                    | `self.__saldo`      |
| **Encapsulamento**   | Esconder dados e permitir acesso controlado         | `ver_saldo()`       |
| **Método público**   | Interface segura para acessar o dado                | `conta.ver_saldo()` |
| **Acesso direto**    | Evita alterar dados sem controle                    | `conta.__saldo` → erro |

---

## 7. Herança

Permite **reaproveitar código** de uma classe base.

```python
class Animal:
    def falar(self):
        print("Som genérico")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

c1 = Cachorro()
c2 = Gato()

c1.falar()  # Au au!
c2.falar()  # Miau!
```

| Conceito                  | Explicação                                    | Exemplo                                                |
| -------------------------- | --------------------------------------------- | ------------------------------------------------------ |
| **Herança**                | Classe herda atributos e métodos de outra     | `class Cachorro(Animal)`                              |
| **Sobrescrita de método**  | Classe filha redefine método da classe pai    | `def falar(self): print("Au au!")`                    |
| **Polimorfismo**           | Mesmo método, comportamentos diferentes       | `Cachorro.falar()` → “Au au!” / `Gato.falar()` → “Miau!” |
| **Classe base (pai)**      | Modelo genérico                               | `Animal`                                               |
| **Classe derivada (filha)**| Especialização                                | `Cachorro`, `Gato`                                     |

---

## 8. Polimorfismo

Permite usar o mesmo método com comportamentos diferentes conforme o tipo do objeto.

```python
animais = [Cachorro(), Gato()]

for animal in animais:
    animal.falar()  # cada um reage diferente
```

---

## 9. Métodos especiais (Dunder Methods)

São métodos “mágicos” que começam e terminam com `__`.

| Método     | Descrição              | Exemplo          |
| ----------- | ---------------------- | ---------------- |
| `__init__`  | Construtor             | `obj = Classe()` |
| `__str__`   | Representação em texto | `print(obj)`     |
| `__len__`   | Retorna tamanho        | `len(obj)`       |
| `__add__`   | Soma personalizada     | `obj1 + obj2`    |

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

p = Produto("Teclado", 250)
print(p)
# Saída: Teclado - R$250.00
```

---

## 10. Métodos estáticos e de classe

### 🔹 Estático (`@staticmethod`)

```python
class Matematica:
    @staticmethod
    def dobro(x):
        return x * 2

print(Matematica.dobro(4))  # Saída: 8
```

> Métodos estáticos não dependem de instâncias, apenas da classe.

---

### 🔹 De classe (`@classmethod`)

```python
class Pessoa:
    contador = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.contador += 1

    @classmethod
    def total_pessoas(cls):
        return cls.contador

p1 = Pessoa("Ana")
p2 = Pessoa("Bruno")
p3 = Pessoa("Gabi")

print(Pessoa.total_pessoas())  # Saída: 3
```

> Métodos de classe acessam atributos da classe (`cls`), e não do objeto (`self`).

---

## 11. Composição (objetos dentro de objetos)

Composição é quando **uma classe contém objetos de outras classes** como parte de sua estrutura.

```python
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor

motor1 = Motor(120)
carro = Carro("Gol", motor1)

print(carro.motor.potencia)  # Saída: 120
```

---

## 12. Boas práticas

🔹 Usar nomes descritivos para classes (`Aluno`, `Conta`, `Produto`).  
🔹 Primeira letra maiúscula no nome da classe (**PascalCase**).  
🔹 Manter as classes coesas (uma responsabilidade principal).  
🔹 Usar encapsulamento para proteger dados sensíveis.  
🔹 Reaproveitar código com herança, mas sem exagerar.  
🔹 Preferir **composição** quando um objeto contém outro (`Carro` tem `Motor`).

