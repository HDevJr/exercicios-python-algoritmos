Conceito: Estruturas de Dados e Coleções em Python

1. O que são Estruturas de Dados ?

    As estruturas de dados são formas de organizar, armazenar e manipular informações
    de maneira eficiente dentro de um programa.

    🔹 Raciocínio:

        "Como posso guardar e acessar meus dados da melhor forma possível?".

        O Python oferece estruturas de dados integradas (built-in) muito poderosas, que são a base
        de praticamente todos os programas:

        ° list -> listas
        ° tuple -> tuplas
        ° set -> conjuntos
        ° dict -> dicionários

        Cada uma tem suas vantagens e usos específicos.

2. Listas (list)

    As listas são coleções mutáveis (podem ser alteradas) e ordenadas.
    Permitem armazenar diferentes tipos de dados.

    Ex:
        frutas = ['maçã', 'banana', 'uva']
        numeros = [1, 2, 3, 4, 5]
        mistura = ['texto', 10, True, 2.5]

        🔹 Acessando elementos:

            print(frutas[0])    # maçã
            print(frutas[-1])   # uva
        
        🔹 Modificando

            frutas.append('pera')           # adiciona no final
            frutas.insert(1, 'laranja')     # insere em posição específica
            frutas.remove('banana')         # remove por valor
            del frutas[0]                   # remove por índice

        🔹 Outras operações:

            print(len(frutas))              # tamanho
            print(sorted(frutas))           # ordena sem alterar
            frutas.sort(reverse=True)       # ordena permanentemente (decrescente)

        🔹 Percorrendo:

            for fruta in frutas:
                print(fruta)

3. Tuplas (tuple)

    As tuplas são imutáveis -- depois de criadas, não podem ser alteradas.
    São úteis para representar dados fixos.

    Ex:
        cores = ('vermelho', 'verde', 'azul')

        🔹 Acessando:

            print(cores[1])                 # verde
        
        🔹 Desempacotando:

            a, b, c = cores
            print(a, c)                     # vermelho azul
        
        🔹 Convertendo:

            lista = list(cores)
            tupla = tuple(lista)

            -> Quando usar: quando os dados não devem ser modificados (ex: coordenadas, meses do ano).

4. Conjuntos (set)

    Os conjuntos são coleções não ordenadas, sem valores duplicados e mutáveis.
    Ideais para filtrar duplicatas ou operações matemáticas.

    Ex:
        numeros = {1, 2, 3, 4}
        print(numeros)                      # {1, 2, 3, 4}

        🔹 Operações de conjunto:

            a = {1, 2, 3, 4}
            b = {3, 4, 5, 6}

            print(a | b)                    # união -> {1, 2, 3, 4, 5, 6}
            print(a & b)                    # interseção -> {3, 4}
            print(a - b)                    # diferença -> {1, 2}
            print(a ^ b)                    # diferença simétrica -> {1, 2, 5, 6}
        
        🔹 Métodos úteis

            a.add(7)
            a.remove(2)
            print(len(a))

            -> Usar quando a ordem não importa e é preciso eliminar duplicatas rapidamente.

5. Dicionários (dict)

    Os Dicionários armazenam para chaves:valor
    Cada chave é única e mapeia para um valor.

    Ex:
        pessoa = {
            'nome': 'Paulo',
            'idade': '21',
            'cidade': 'Londrina'
        }

        🔹 Acessando:

            print(pessoa['nome'])
            print(pessoa.get('idade'))
        
        🔹 Modificando:

            pessoa['idade'] = 22
            pessoa['profissao'] = 'Desenvolvedor'
            del pessoa['cidade]

        🔹 Iterando:

            for chave, valor in pessoa.items():
                print(f'{chave}: {valor}')

        🔹 Métodos úteis:

            print(pessoa.keys())            # chaves
            print(pessoa.values())          # valores
            print(pessoa.items())           # pares (tuplas)

            -> Usar para representar entidades com prioridades (ex: pessoas, produtos, configurações).

6. Estruturas aninhadas

    Podesse combinar estruturas, criando listas de dicionários, dicionário de listas, etc.

    Ex:
        alunos = [
            {'nome': 'Ana', 'nota': 9.0},
            {'nome': 'João', 'nota': 7.5}
        ]

        for aluno in alunos:
            print((f'{aluno['nome']} tirou {aluno['nota']}'))

        # Saída: Ana tirou 9.0 e João tirou 7.5

7. Coleções úteis (módulo collections)

    O Python possui uma biblioteca especial chamada collections, com estruturas avançadas.

    🔹 Counter -> conta ocorrências:

        Ex:
            from collections import Counter

            frutas = ['maçã', 'banana', 'maçã', 'uva']
            contagem = Counter(frutas)
            print(contagem)

            # Saída: Counter({'maçã': 2, 'banana': 1, 'uva': 1})

    🔹 Defaultdict -> dicionário com valor padrão:

        Ex:
            from collections import defaultdict

            d = defaultdict(int)
            d['chave'] += 1
            print(d['chave'])               # 1

        🔹 Importação:  

            from collections import defaultdict

            -> Aqui está sendo importado defaultdict,
               uma classe especial da biblioteca collections, que vem junto com o Python.

               Ela funciona como um dicionário comum (dict),
               mas com um diferencial importante:
               -> Quando se tenta acessar uma chave que ainda não existe,
                  ele cria automaticamente um valor padrão para ela.
        
        🔹 Criando o defaultdict:

            d = defaultdict(int)

            -> Aqui está o segredo:
                ° O int dentro de defaultdict(int) é uma função que define o valor padrão.
                ° No caso de intm ele retorna 0 por padrão.
                ° Se acessar uma chave inexistente, o dicionário automaticamente cria essa chave com valor 0.

        🔹 3. A linha:

            d['chave'] += 1

            Em um dicionário normal, isso daria erro:

            d = {}
            d['chave'] += 1             # KeyError — a chave não existe ainda

            Mas com o defaultdict(int), o comportamento muda:
            ° d['chave'] não existe -> o defaultdict cria automaticamente d['chave'] = 0
            ° depois faz o cálculo: d['chave'] = 0 + 1

            -> Agora d['chave'] passa a valer 1.

        🔹 4. Exibindo o valor:

            print(d['chave'])               # 1
    
    🔹 Namedtuple -> tupla com nomes:

        Ex:
            from collections import namedtuple

            Pessoa = namedtuple('Pessoa', ['nome', 'idade'])
            p = Pessoa('André', 21)
            print(p.nome, p.idade)

        🔹 Importação:

            Aqui está sendo importado a função namedtuple da biblioteca padrão collections,
            que serve para criar tipo de dados personalizados, pareceidos com classes,
            mas muito mais simples e leves.
        
        🔹 Criando o tipo Pessoa:

            Pessoa = namedtuple('Pessoa', ['nome', 'idade'])

            ° 'Pessoa' -> é o nome do novo tipo que está sendo criado.
            ° ['nome', 'idade'] -> são os campos (atributos) que cada Pessoa vai ter.

            ° É criado um novo tipo de dado, chamado Pessoa,
            com dois campos: nome e idade.

            É como se você tivesse criado uma mini classe:
            
            Ex:
                class Pessoa:
                    def __init__(self, nome, idade):
                        self.nome = nome
                        self.idade = idade

            Mas sem precisar escrever tudo isso!

        🔹 Criando um objeto Pessoa

            p = Pessoa('André', 21)

            -> Aqui está sendo criado uma instância de Pessoa,
            passando os valores para os campos definidos anteriormente:

            ° nome='André'
            ° idade = 21

            Agora p é uma tupla nomeada, ou seja,
            um objeto que:

                ° se comporta como uma tupla comum.
                ° Mas permite acesso por nome de campo e por índice.
        
        🔹 Acessando os valores:

            print(p.nome, p.idade)

            Podesse ser acessada:

                ° Por nome -> p.nome ou p.idade
                ° Ou por índice -> p[0] e p[1]

                # Saída: André 21

        | Conceito              | Explicação                               | Exemplo                                            |
        | --------------------- | ---------------------------------------- | -------------------------------------------------- |
        | **`namedtuple`**      | Cria um tipo de dado com campos nomeados | `Pessoa = namedtuple('Pessoa', ['nome', 'idade'])` |
        | **Criação de objeto** | Passa os valores na ordem dos campos     | `p = Pessoa('Junior', 21)`                         |
        | **Acesso por nome**   | Usa ponto (.) como nas classes           | `p.nome`, `p.idade`                                |
        | **Acesso por índice** | Funciona como tupla normal               | `p[0]`, `p[1]`                                     |
        | **Saída**             | Exibe os dados                           | `Junior 21`                                        |

8. Boas práticas

    🔹 Usar listas quando precisar de sequência mutável.
    🔹 Usar tuplas quando os dados forem imutáveis.
    🔹 Usar sets para eliminar duplicatas ou comparar grupos.
    🔹 Usar dicionários para representar objetos com pares chave:valor.
    🔹 Preferir compreensões (list, dict, set) para criar coleções dinamicamente.
    🔹 Evitar estruturas aninhadas muito profundas -- separar em funções.

9. Erros comuns

    🔹 Tentar acessar índices inexistentes -> IndexError.
    🔹 Acessar chaves que não existem no dicionário -> KeyError.
    🔹 Alterar tuplas -> TypeError.
    🔹 Supor que set mantém ordem -> ele não mantém.
