Conceito: Estruturas de Repetição (Loops) em Python

1. O que são estruturas de repetição ?

    As estruturas de repetição, ou loops, permitem que o programa execute um mesmo bloco de código várias
    vezes, até que uma condição seja satisfeita ou um conjunto de elementos seja percorrido.

    🔹 Raciocínio:

        "Repita até que o trabalho seja concluído."

        Elas são usadas para automatizar tarefas repetitivas, percorrer listas, gerar seqências ou fazer cálculos
        progressivos.

    🔹 Python possui dois tipos principais de laços:
        
        for --> usado para percorrer elementos.
        while --> usado para repetir enquanto uma condição for verdadeira.

2. Loop for

    O for é ideal para percorrer coleções (listas, strings, tuplas, ranges, etc..).

    🔹 Sintaxe:
        
        for item in sequência:
            # código a ser executado
        
        Ex:
            frutas = ['maçã', 'banana', 'uva']

            for fruta in frutas:
                print(fruta)
            
            # Saída: maçã
                     banana
                     uva

    🔹 Usando o range():

        A função range() gera uma sequência de números

        for i in range(5):
            print(i)

        # Saída: 0
                 1
                 2
                 3
                 4

        É possível também controlar o início, fim e passo:

        for i in range(2, 11, 2):

        # Saída: 2
                 4
                 6
                 8
                 10

    🔹 Loop while:

        while condição:
            # código executado enquanto condição for verdadeira

        Ex:
            contador = 1
            while contador <= 5:
                print(contador)
                contador += 1

        Se a condição nunca se tornar falsa, o loop se tornará infinito.

4. Comandos de controle

    🔹 Break:

        O break interrompe o loop imediatamente.

        Ex:
            for i in range(10):
                if i == 5:
                    break
                print(i)

            # Saída 0 1 2 3 4

    🔹 Continue:

        pula para a próxima iteração

        Ex:
            for i in range(5):
                if i ==  2:
                    continue
                print(i)
            
            # Saída 0 1 3 4

    🔹 Else com loops:

        O bloco else é executado quando o loop termina naturalmente, sem o break.

        Ex:
            for i in range(3):
                print(i)
            else:
                print('loop concluído!')
            
            # Saída 0
                    1
                    2
                    Loop concluído

5. Laços aninhados (loops dentro de loops)

    Ex:
        for i in range(1, 3):
            for j in range(1, 3):
                print(i, j)
        
        # Saída: 1 1
                 1 2
                 2 1
                 2 2
                 3 1
                 3 2

    🔹 O que significa range(1, 3):
        range(1, 3) gera os números de 1 a 3
        (o 3 é exclusívo, ou seja, o laço para antes de chegar nele).
    Então:
        ° O i vai assumir os valores --> 1 e 2
        ° o j também vai assumir os valores --> 1 e 2

    🔹 Entendendo o loop externo e interno:
        ° O loop externo (for i in range(1, 3)) controla o número das "linhas".
        ° O loop interno (for j in range(1, 3)) roda completo para cada valor de i.

    🔹 Raciocínio:

        Para cada valor de i, o programa repete todos os valores de j.
    
    🔹 Passo a passo da execução

        | Passo | Valor de `i` | Valor de `j` | O que imprime |
        | ----- | ------------ | ------------ | ------------- |
        | 1     | 1            | 1            | `1 1`         |
        | 2     | 1            | 2            | `1 2`         |
        | 3     | 2            | 1            | `2 1`         |
        | 4     | 2            | 2            | `2 2`         |

        O i só muda depois que o j termina seu ciclo completo.

6. Funções úteis com loops

    🔹 Enumerate():

        Retorna o índice e o valor ao percorrer uma sequência.

        Ex:
            frutas = ['maçã', 'banana', 'uva']

            for indice, fruta in enumarate(frutas):
                print(indice, fruta)

            # Saída: 0 maçã
                     1 banana
                     2 uva

    🔹 Zip():

        Percorre duas listas ao mesmo tempo:

        Ex:
            nomes = ['Ana', 'João', 'Pedro']
            idades = [20, 25, 30]

            for nome, idade in zip(nomes, idades):
                print(nome, idade)

            # Saída: Ana 20
                     João 25
                     Pedro 30

7. Boas práticas

    🔹 Usar for para listas e sequências conhecidas.
    🔹 Usar while quando a repetição depende de uma condição.
    🔹 Evitar loops infinitos sem necessidade.
    🔹 Prefirir enumarate() a contar índices manualmente.
    🔹 Deixe nomes de variáveis representativos (for aluno in alunos: )
    🔹 Quebrar loops longos em funções menores para facilitar a leitura.

8. Erros comuns

    🔹 Esquecer de atualizar a variável dentro do while (loop infinito).
    🔹 Alterar a lista que está sendo percorrida (pode causar bugs).
    🔹 Falta de indentação após o for ou while.
    🔹 Usar range(len(lista)) sem precisar -- prefira for item in lista: .