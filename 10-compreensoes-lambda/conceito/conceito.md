Conceito: Compreensões e Expressões Lambda em Python

1. O que são compreensões ?

    As Compreensões são uma forma concisa e elegante de criar novas coleções
    (listasm dicionários, conjuntos) a partir de iteráveis existentes (listas, ranges, strings, etc).

    🔹 Raciocínio:

        "É uma maneira de transformar ou filtrar dados em uma única linha,
        sem precisar de loops explícitos."

2. List Comprehension (compreensão de listas)

    É a forma mais usada.
    Permite criar listas em uma linha usando a sintaxe?

    Ex:
        [expressão for item in iterável if condição]

    🔹 Ex 1 -- Quadrados de 1 a 5:

        quadrados = [x**2 for x in range(1, 6)]
        print(quadrados)

        # Saída: [1, 4, 9, 16, 25]

    🔹 Ex 2 -- Filtrar números pares:

        pares = [x for in range(10) if x % 2 == 0]
        print(pares)

        # Saída: [0, 2, 4, 6, 8]

    🔹 Ex 3 -- Manipular strings:

        nomes = ['ana', 'pedro', 'maria']
        nomes_maiusculos = [nome.upper() for nome in nomes]

        print(nomes_maiusculos)

        # Saída: ['ANA', 'PEDRO', MARIA']

    🔹 Ex 4 -- Condicional inline:

        numeros = [1, 2, 3, 4, 5]
        resultado = ['par' if x % 2 == 0 else 'ímpar' for x in numeros]
        print(resultado)

        # Saída: ['ímpar', 'par', 'ímpar', 'par', 'ímpar']

3. Dict Comprehension (compreensão de dicionários)

    Permite criar dicionários a partir de iteráveis.

    Ex:
        quadrados = {x: x**2 for x in range(5)}
        print(quadrados)

        # Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    
4. Set Comprehesion (compreensão de conjuntos)

    Permite criar conjuntos sem duplicatas.

    Ex:
        numeros = [1, 2, 2, 3, 4, 4]
        sem_duplicatas = {x for x in numeros}
        print(sem_duplicatas)

        # Saída: {1, 2, 3, 4}
    
5. Generator Expression (geradores)

    Os geradores são semelhantes às list comprehensions, mas não armazenam todos os elementos
    na memória -- geram um item por vez, sob demanda.

    Ex:
        quadrados = (x**2 for x in range(5))
        for q in quadrados:
            print(q)

        # Saída: 0
                 1
                 4
                 9
                 16
        
        -> Ideal para grandes volumes de dados, pois economiza memória.
    
6. O que são Expressões Lambda ?

    As funções lambda (também chamadas de funções anônimas) são pequenas funções sem nome,
    geralmente usadas em operações simples e temporárias.

    🔹 Raciocínio:

        "É uma função rápida,de um linha só, usada no lugar onde uma função comum seria loga demais."
    
    🔹 Sintaxe:

        lambda argumentos: expressão

    🔹 Ex 1 -- Função lambda simples:

        dobro = lambda x: x * 2
        print(dobro(5))

        # Saída: 10

    🔹 Ex 2 -- Com dois argumentos:

        soma = lambda a, b: a + b
        print(soma(3, 7))

        # Saída: 10


    🔹 Ex 3 -- Com condição:

        par_ou_impar = lambda x: 'par' if x % 2 == 0 else 'ímpar'
        print(par_ou_impar(7))

        # Saída: ímpar

7. Lambda com funções embutidas (map, filterm sorted)

    🔹 Map() -- aplica uma função a todos os elementos:

        numeros = [1, 2, 3, 4]
        dobrados = list(map(lambda x: x * 2, numeros))
        print(dobrados)

        # Saída: [2, 4, 6, 8]
    
    🔹 Filter() -- filtrar elementos com base em uma condição:

        Ex:
            numeros = [1, 2, 3, 4, 5, 6]
            pares = list(filter(lambda x: x % 2 == 0, numeros))
            print(pares)

            # Saída: [2, 4, 6]

    🔹 Sorted() -- ordenar com critério personalizado:

        Ex:
            nomes = ['Ana', 'Pedro', 'João', 'Maria']
            ordenados = sorted(nomes, key=lambda nome: nome.lower())
            print(ordenados)

            # Saída: ['Ana', 'João', 'Maria', Pedro']

8. Lambda dentro de dicionários e listas

    Ex:
        operacoes = {
            'soma': lambda a, b,: a + b,
            'multiplica': lambda a, b: a * b
        }

        print(operacoes['soma'](3, 4))
        print(operacoes['multiplica'](3, 4))

        # Saída: 7
                 12

9. Boas práticas

    🔹 Usar compreensões quando elas realmente melhoram a legibildiade.
    🔹 Usar lambda apenas para funções simples (1 linha).
    🔹 Prefira funções nomeadas para lógicas complexas.
    🔹 Combine lambda com map/filter/sorted para operações funcionais rápidas.
    🔹 Para expressões longas, divida em funções normais com def.

10. Erros comuns

    🔹 Funções lambda com mais de uma linha -> não é permitido.
    🔹 Usar excessivamente de compreensões complexas (difíceis de ler).
    🔹 Esquecer de converter map e filter em lista (list()).
    🔹 Usar lambda onde seria melhor usar uma função nomeada.

    
