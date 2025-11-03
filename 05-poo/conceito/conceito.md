Conceito: Programação Orientada a Objetos (POO) em Python

1. O que é POO ?

    A Programação Orientada a Objetos (POO) é um paradigma que organiza o código em objetos, que representam
    coisas do mundo real com propriedades (atributos) e comportamento (métodos).

    🔹 Reciocínio:

        "Um carro tem características (cor, modelo) e comportamentos (acelerar, frear)."

        Em POO, é criado classes que servem como "molde" (modelo) e objetos que são instâncias dessas classes.

2. Classe e objeto

    🔹 Classe --> é o modelo:
    🔹 Objeto --> é a instância (exemplo real da classe):
    
    Ex:
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

        # Saída: Olá, meu nome é Ana e tenho 21 anos.
                 Olá, meu nome e Gabi e tenho 25 anos.

    🔹 Criação da classe:

        class Pessoa:
            def __init__(self, nome, idade):
                self.nome = nome
                self.idade = idade

        ° class Pessoa --> cria um molde (modelo) para gerar pessoas.
        ° __init__ --> é o método construtor, executando automaticamente quando você cria um novo objeto.
        ° self --> representa o próprio objeto (cada pessoa criada terá seus próprios dados).
        ° self.nome e self.idade = idade --> armazenam as informações passadas no momento da criação.

            Essa parte define como uma pessoa é construída (com nome e idade).
        
    🔹 Método da classe:

        def apresentar(self):
            print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

        ° Esse é um método (função dentro da classe).
        ° Ele usa os atributos do próprio objeto (self.nome e self.idade)
          para imprimir uma frase de apresentão.

    🔹 Criando objetos (instâncias da classe):

        p1 = Pessoa('Ana', 21)
        p2 = Pessoa('Gabi', 25)

        ° Nessa parte esta sendo criado duas pessoas a partir da classe:
        ° p1 --> tem nome = 'Ana' e idade = 21
        ° p2 --> tem nome = 'Gabi' e idade = 25

        ° Essas variáveis são chamadas de instâncias da classe Pessoa.
    
    🔹 Chamando o método:

        p1.apresentar()
        p2.apresentar()

        ° Cada objeto chama o seu próprio método apresentar(),
          e o self automaticamente representa o objeto que chamou.
    
    🔹 Saída:

        Olá, meu nome é Ana e tenho 21 anos.
        Olá, meu nome é Gabi e tenho 25 anos.

    🔹 Linguagem natural:

        A classe Pessoa é um molde para criar pessoas com nome e idade.
        Cada pessoa pode se apresentar dizendo seu nome e idade.
        Quando criamos p1 e p2, elas se comportam como duas pessoas diferentes,
        mas ambas seguem a mesma "forma" definida pela classe.

    🔹 Resumo:

        | Conceito               | O que é                       | Exemplo                   |
        | ---------------------- | ----------------------------- | ------------------------- |
        | **Classe**             | O molde                       | `class Pessoa:`           |
        | **Atributos**          | As informações de cada objeto | `self.nome`, `self.idade` |
        | **Método**             | Ações que o objeto executa    | `def apresentar(self):`   |
        | **Objeto (instância)** | Um exemplo real da classe     | `p1 = Pessoa('Ana', 21)`  |

3. O método __init (construtor)

    O método especial __init__ é excutado automaticamento quando criamos um objeto, e serve para
    inicializar os atributos.

    Ex:
        class Produto:
            def __init__(self, nome, preco):
                self.nome = nome
                self.preco = preco

    ° self representa o próprio objeto (é obrigatório em métados de instância).
    ° Cada atributo pertence a cada objeto criado.

4. Atributos

    🔹 Atributos de instância:

        Pertencem a um objeto específico.

        Ex:
            class Carro:
                def __init__(self, modelo, cor):
                    self.modelo = modelo
                    self.cor = cor

    🔹 Atributos de classe:

        Pertencem à classe e são compartilhados por todos os objetos.

        Ex:
            class Carro:
                rodas = 4       # atributo de classe
    
5. Métodos

    Os métodos são funções dentro de classe que definem os comportamentos dos objetos.

    Ex:
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
                    print('Saldo insuficiente')
            
            def exibir_saldo(self):
                print(f'Saldo atual: R${self.saldo:.2f}')
            
    🔹 Definição de classe:

        class ContaBancaria:

        ° Criação da classe chamada ContaBancaria.
        ° Essa classe é como um molde que define como uma conta bancária
          funciona - o que ela tem (atributos) e o que ela pode fazer (métodos).

    🔹 O método construtor __init__:

        def __init__(self, titular, saldo=0):
            self.titular = titular
            self.saldo = saldo

        ° __init__ é o construtor, executando automaticamente quando criamos uma nova conta.
        ° self representa a própria conta.
        ° titular é o nome da pessoa dona da conta.
        ° saldo=0 significa que, por padrão, a conta começa zerada (mas pode começar com outro valor,
          se informado).

        Ex:
            conta1 = ContaBancaria('Junior')
            conta2 = ContaBancaria('Maria', 500)

            -> conta1 -> titular: Junior | saldo: 0
            -> conta2 -> titular: Maria | saldo: 500
    
    🔹 Método depositar():

        def depositar(self, valor):
            self.saldo += valor
            
        ° Esse método aumenta o saldo da conta.

        Ex:
            conta1.depositar(200)

        -> Soma 200 ao saldo atual.
    
    🔹 Método sacar():

        def sacar(self, valor):
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                print('Saldo insuficiente!')

        ° Esse método tenta sacar um da conta:
        ° Se o valor for menor ou igual ao saldo, saque é feito.
        ° Caso contrário, o programa mostra "Saldo insuficiente" e não altera o saldo.

        Ex:
            conta1.sacar(50)

            -> Diminiu 50 do saldo atual (se houver dinheiro suficiente).
    
    🔹 Método exibir_saldo():

        def exibir_saldo(self):
            print(f'Saldo atual: R${self.saldo:.2f}')

        -> Exibe o saldo da conta formatado com duas casas decimais (:.2f).

        Ex:
            conta1.exibir_saldo()       # Saída: Saldo atual: R$150.00

    🔹 Exemplo completo:

        conta = ContaBancaria("Junior")

        conta.exibir_saldo()  # Saldo atual: R$0.00
        conta.depositar(300)
        conta.exibir_saldo()  # Saldo atual: R$300.00
        conta.sacar(100)
        conta.exibir_saldo()  # Saldo atual: R$200.00
        conta.sacar(500)      # Saldo insuficiente!

6. Encapsulamento

    Encapsulamento é o conceito de proteger os dados internos de uma classe, permitindo que eles sejam acessados somente de maneira controlada (geralmente por métodos).

    Ex:
        class Conta:
            def __init__(self, saldo):
                self.__saldo = saldo        # atributo privado
            
            def ver_saldo(self):
                return self.__saldo
        
        conta = Contar(1000)
        print(conta.ver_saldo())    # acesso permitido
        # print(conta.__saldo)      # erro: atributo privado

    🔹 Classe Conta:

        class Conta:
            def __init__(self, saldo):
                self.__saldo = saldo    # atributo privado
        
        -> O saldo __saldo (com dois underlines) é um atributo privado.
        Isso significa que ele não pode ser acessado diretamente fora da classe.

        ° O Python não proíbe completamente, mas ele renomeia internamente o atributo para proteger.
        Então, por baixo dos pano, o nome vira _Conta_saldo.

    🔹 Método público para acessar o saldo:

        def ver_saldo(self):
            return self.__saldo

        -> Esse método é o "acesso controlado" ao saldo.
        Quem quiser ver o saldo precisa usar esse método, e não mexer direto no atributo.

    🔹 Criação do objeto:

        conta = Conta(1000)

        -> Aqui você cria uma conta com saldo incial de 1000,
           mas o saldo está protegido dentro da classe.

        print(conta.ver_saldo())    # acesso permitido

        Correto ->
        O método ver_saldo() tem acesso interno ao atributo privado,
        então ele pode retornar o valor com segurança.

        Acesso proibido
        print(conta.__saldo)

        Gera erro:
            AttributeError: 'Conta' object has no attribute '__saldo'

        
        | Termo                      | Significado                                         | Exemplo                |
        | -------------------------- | --------------------------------------------------- | ---------------------- |
        | **Atributo privado**       | Dado interno protegido da classe                    | `self.__saldo`         |
        | **Encapsulamento**         | Esconder dados e permitir acesso apenas por métodos | `ver_saldo()`          |
        | **Método público**         | Interface segura para acessar o dado                | `conta.ver_saldo()`    |
        | **Acesso direto proibido** | Evita alterar dados sem controle                    | `conta.__saldo → erro` |

7. Herança

    Permite reaproveitar código de uma classes.

    Ex:
        class Animal:
            def falar(self):
                print('Som genérico')

        class Cachorro(Animal):
            def falar(self):
                print('Au au!')
        
        class Gato(Animal)
            def falar(self):
                print('Miau!')
        
        c1 = Cachorro()
        c2 = Gato()
        c1.falar()
        c2.falar()

        # Saída: Au Au! e Miau!

    🔹 1. A classe base (ou classe pai):

        def Animal:
            def falar(self):
                print('Som genérico')
        
        -> A classe Animal é uma classe base, ou seja, serve como modelo genérico.
           Ela define um comportamento padrão -- no caso o método falar() que imprime "Som genérico".

           Em outras palavras:

            Todo animal pode “falar”, mas o tipo de som depende do animal específico.

    🔹 2. Classe filha Cachorro:

        class Cachorro(Animal):
            def falar(self):
                print('Au au!')

        -> A classe Cachorro herda tudo da classe Animal (isso está indicado por (Animal)),
           mas ela redefine o método falar().

           Isso se chama sobrescrita de método (method overrinding).
           Mesmo que Animal tenha um falar(), o Cachorro define sua própria versão.
    
    🔹 3. Classe filha Gato:

        class Gato(Animal):
            def falar(self):
                print('Miau!')
        
        -> A mesma ideia: Gato também herda de Animal,
           mas redefine o método falar() com o som típico do gato.

    🔹 4. Criando objetos (instâncias):

        c1 = Cachorro()
        c2 = Gato()

        Aqui criasse dois objetos:

        c1 → é um Cachorro
        c2 → é um Gato

        Ambos herdam da classe Animal,
        mas cada um tem seu próprio comportamento no método falar().

    🔹 5. Chamando os métodos:

        c1.falar()
        c2.falar()

        # Saída: Au au! e Miau!
    
    🔹 6. O que aconteceu internamente:

        O Python viu que c1 é um objeto da classe Cachorro.
        Então chamou a versão de falar() definida dentro de Cachorro.

        Depois viu que c2 é um Gato, e chamou a versão de falar() definida em Gato.

        Mesmo que ambas as classes herdem o mesmo método falar() de Animal,
        elas se comportam de maneira diferente.

        Esse é o conceito de polimorfismo:

        “métodos com o mesmo nome, mas comportamentos diferentes dependendo do objeto.”

        Resumo:

    | Conceito                    | Explicação                                      | Ex                                                       |
    | --------------------------- | ----------------------------------------------- | -------------------------------------------------------- |
    | **Herança**                 | Uma classe herda atributos e métodos de outra   | `class Cachorro(Animal)`                                 |
    | **Sobrescrita de método**   | A classe filha redefine um método da classe pai | `def falar(self): print("Au au!")`                       |
    | **Polimorfismo**            | Mesmo método, comportamentos diferentes         | `Cachorro.falar()` → “Au au!” / `Gato.falar()` → “Miau!” |
    | **Classe base (pai)**       | Modelo genérico                                 | `Animal`                                                 |
    | **Classe derivada (filha)** | Especialização                                  | `Cachorro`, `Gato`                                       |

8. Polimorfismo

    Permite usar o mesmo método com portamentos diferentes conforme o tipo do objeto.

    animais = [Cachorro(), Gato()]

    for animal in animais:
        animal.falar()      # cada um reage diferente

9. Métodos especiais (dunder methods)

    São métodos "mágicos" que começam e terminam com dois sublinhados (__).

    | Método     | Descrição              | Exemplo          |
    | ---------- | ---------------------- | ---------------- |
    | `__init__` | Construtor             | `obj = Classe()` |
    | `__str__`  | Representação em texto | `print(obj)`     |
    | `__len__`  | Retorna tamanho        | `len(obj)`       |
    | `__add__`  | Soma personalizada     | `obj1 + obj2`    |

    Ex:
        class Produto:
            def __init__(self, nome, preco):
                self.nome = nome
                self.preco = preco

            def __str__(self):
                return f'{self.nome} - R${self.preco:.2f}'

        p = produto('Teclado', 250)
        print(p)

        # Saída: Teclado - R$250.00

    🔹 1. Definição da classe:

        class Produto:

        -> Aqui você está criando uma classe chamada Produto,
           que servirá como modelo para representar produtos de uma loja.

    🔹 2. O método construtor (__init__):

        def __init__(self, nome, preco):
            self.nome = nome
            self.preco

        ° __init__ é o construtor, executando automaticamente sempre que um novo Produto é criado.
        ° self representa o próprio objeto(cada produto tem seu próprio nome e preço).
        ° nome e preco são parâmetros recebidos ao criar o produto.

        Ex:
            p = Produto('Teclado', 250)

            -> Cria um produto com:
                ° self.nome = 'Teclado'
                ° self.preco = 250
            
    🔹 3. O método especial __str__:

        def __str__(self):
            return f'{self.nome} - R${self.preco:.2f}'

        ° Define como o objeto será mostrado quando for convertido em texto --
          por exemplo, quando usamos print(p) ou str(p).
        ° Retorna uma string formatada com o nome e o preço do produto.
        ° :.2f -> formata o preço com duas casas decimais.

    🔹 4. Criando o objeto:

        p = Produto('Teclado', 250)

        -> Aqui o Python executa automaticamente o __init__,
           guardando os valores:
            
            ° self.nome = 'Teclado'
            ° self.preco = 250
        
    🔹 5. Exibindo o objeto:

        print(p)

        -> Quando se faz print(p), o Python chama automaticamente o metodo __str__.

        É executado:
            return f'{self.nome} - R${self.preco:.2f}'

            # Saída: Teclado - R$250.00

10. Métodos estáticos e de classe

    🔹 Estático (@staticmethod):

        Não depende de atributos da instância.

        Ex:
            class Matematica:
                @staticmethod
                def dobro(x):
                    return X * 2
            print(Matematica.dobro(4))

            🔹 1. A classe:

                class Matematica:

                -> Aqui está sendo criado uma classe chamada Matematica,
                   que serve como agrupador de funções matemáticas.
                   Ela não representa um objeto com atributos(como nome, saldo etc.),
                   mas sim um conjunto de operações.

            🔹 2. O método estático:

                @staticmethod
                def dobro(x):
                    return x * 2

                ° @staticmethod é um decorador,
                  que transforma o método abaixo dele (dobro) em estático.
                ° Um método estático:
                    ° Pertence à classe, não a um objeto específico.
                    ° Não usa self, porque não depende de atributos da instância.
                    ° Pode ser chamado sem precisar criar um objeto da classe.

                -> Ou seja, o método dobro() é uma função comum,
                   mas está organizada dentro da classe apenas para manter o código agrupado.

            🔹 3. O que o método faz:

                def dobro(x):
                    return x * 2
                
                -> Recebe um número (x) e retorna p dobro dele.

                Ex:
                    ° Entrada: 4
                    ° Saída: 8
                
            🔹 Chamando o método

                print(Matematica.dobro(4))

                -> Não é criado nenhum objeto da classe.
                   É chamado o método diretamente pela classe -- isso é possível porque ele é estático.

                   # Saída: 8

    🔹 De classe (classmethod)

        Acessa a própria classe, não o objeto.

        Ex:
            class Pessoa:
                contador = 0

                def __init__(self, nome):
                    self.nome = nome
                    Pessoa.contador += 1
                
                @classmethod
                def total_pessoas(cls):
                    return cls.contador

        🔹 1. Definição da classe:

            class Pessoa:
                contador: 0

            -> Aqui é criado uma classe chamada Pessoa,
               e dentro dela define um atributo de classe chamado contador.

        🔹 2 . O que é um atributo de classe:

            Um atributo de classe:
                
                ° É compartilhado por todas as instâncias (objetos) dessa classe.
                ° Pertence à classe em si, e não a cada objeto individual.

                No caso:

                contador = 0

                Significa que todas as pessoas criadas compartilham o mesmo contador.

        🔹 3. O método construtor (__init__):

            def __init__(self, nome):
                self.nome = nome
                Pessoa.contador += 1

            ° self.nome = nome -> cria um atributo de instância, ou seja, específico de cada pessoa.
            ° Pessoa.contador += 1 -> acessa o atributo da classe e soma 1 toda vez que uma nova pessoa é criada.
            ° Cada vez que se cria um novo objeto Pessoa,
              o contado aumenta em +1 automaticamente.
        
        🔹 4. O método de classe (@classmethod):

            @classmethod
            def total_pessoas(cls):
                return cls.contador

            ° O decorador @classmethod transforma o método em um método da classe.
            ° Ele recebe cls como parâmetros (em vez de self):
                ° cls -> representa a classe.
                ° self -> representa a instÂncia (objeto).
            ° O método pode acessar atributos da classe, como cls.contador.

        🔹 5. Exemplo de uso:

            p1 = Pessoa("Ana")
            p2 = Pessoa("Bruno")
            p3 = Pessoa("Gabi")

            print(Pessoa.total_pessoas())

            # Saída: 3

            ° Cada vez que se cria uma pessoa (p1, p2, p3), o construtor soma 1 no contador.
            ° Quando se chama Pessoa.total_pessoas(), ele retorna o valor acumulado (3)

11. Composição (objetos dentro de objetos)

    Composição significa que um objeto é formado (composto) por outros objetos.
    Ou seja, uma classe usa outra classe como parte da sua estrutura.

        Ex:
            class Motor:
                def __init_(self, potencial):
                    self.potencia = potencia

            class Carro:
                def __init__(self, modelo, motor):
                    self.modelo = modelo
                    self.motor = motor

            motor1 = Motor(120)
            carro = Carro('Gol', motor1)

            print(carro.motor.potencia)   

            # Saída: 120
        
    🔹 Classe Motor:

        class Motor:
            def__init__(self, potencia):
                self.potencia = potencia
            
            -> Essa classe representa um motor, com apenas um atributo:
               ° potencia: indica quando cavalos (ou watts) o motor tem.

            Ex:
                motor1 = Motor(120)

            Cria um motor com potência de 120.

    🔹 Classe Carro:

        class Carro:
            def__init__(self, modelo, motor):
                self.modelo = modelo
                self.motor = motor
        
        -> A classe Carro recebe dois parâmetros:
           ° modelo -> nome do carro (ex: 'Gol')
           ° motor -> um objeto da classe Motor
        ° O carro contém um motor dentro dele.
        Isso é composição: um objeto sendo parte de outro.

    🔹 Criado os objetos:

        motor1 = Motor(120)
        carro = Carro('Gol', motor1)

        1. motor1 -> cria o motor com potência 120.
        2. carro cria o carro 'Gol' e coloca o motor1 dentro dele.

    🔹 Acessando os dados:

        print(carro.moto.potencia)

        -> aqui acessa o motoro dentro do carro e depois o atributo potência do motor.

        1. carro.motor -> acessa o objeto motor dentro do carro.
        2. .potencia -> acessa o valor da potência dentro do motor.
        
        # Saída: 120

12. Boas práticas

    🔹 Usar nomes descritivos para classes (ex: Aluno, Conta, Produto).
    🔹 Colocar a primeira letra maiúscula no nome da classe (convenção:PascalCase).
    🔹 Mater as classes enxutas e coesas (uma responsabilidaed principal).
    🔹 Usar encapsulamento para proteger dados sensíveis.
    🔹 Reaproveitar código com herança, mas sem exagerar.
    🔹 Prefir composição quando um objeto possui outro (ex: Carro te Motor).
            



