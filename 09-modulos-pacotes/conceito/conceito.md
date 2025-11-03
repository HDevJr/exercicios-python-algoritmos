Conceito: Módulos, Pacotes e Importações em Python

1.  O que são Módulos ?

    Um módulo é um arquivo Python (.py) que contém funções, classes ou variáveis que podem ser
    reutilizadas em outros programas.

    🔹 Raciocínio:

        "Um módulo é como uma caixa de ferramentas que você pode importar
         quando precisar."

         Isso ajudar a organizar o código, evitar repetição e facilitar manutenção.

2. Criando e usando um módulo

    🔹 Exemplo -> Criando um módulo:

        Arquivo matematica.py:

            def somar(a, b):
                return a + b

            def subtrair(a, b):
                return a - b

        Arquivo principal.py:

            import matematica

            print(matematica.somar(5, 3))
            print(matematica.subtrair(10, 4))
        
        # Saída: 8
                 6

3. Importações específicas

    É possível importar apenas o que precisa de um módulo.

    Ex:
        from matematica import somar

        print(somar(10, 5))

    Agora não é preciso usar matematica.somar, apenas somar().

4. Alias (apelidos)

    Usar as para criar um apelido para o módulo, útil quando o nome pe grande.

    Ex:
        import matematica as m

        print(m.somar(2, 3))

5. Módulos internos do Python (built-in)

    O Python já vem com uma biblioteca padrão com centenas de módulos prontos para uso.

    Ex:
        import math
        import random
        import datatime

        | Módulo     | Uso principal                                |
        | ---------- | -------------------------------------------- |
        | `math`     | Funções matemáticas (√, π, seno, log, etc.)  |
        | `random`   | Geração de números aleatórios                |
        | `datetime` | Manipulação de datas e horários              |
        | `os`       | Operações com arquivos e sistema operacional |
        | `sys`      | Interação com o interpretador Python         |
        | `json`     | Leitura e escrita de arquivos JSON           |
        | `csv`      | Manipulação de arquivos CSV                  |

    Exemplos práticos:

        import math

        print(math.sqrt(16))            # raiz quadrada
        print(math.pi)                  # contante π


        import datatime import datatime

        agora = datatime.now()
        print(agora.strftime('%d/%m/%Y %H:%M'))

6. Instalando módulos externos

    Além dos módulos internos, existem módulos externos criado pela comunidade,
    instaláveis via pip (gerenciador de pacotes Python).

    🔹 Instalar:

        pip install requests

    🔹 Usar:

        import requests

        resposta = requeste.get('https://api.github.com')
        print(resposta.status_code)

7. O que são pacotes ?

    Um pacote é uma pasta que contém vários módulos organizados logicamente, junto com um arquivo
    especial chamado __init__.py.

    🔹 Estrutura:

        meu_pacote/
        │
        ├── __init__.py
        ├── calculos.py
        └── conversoes.py

    Exemplos de uso:

        from meu_pacote.calculos import somar

        O arquivo __init__.py indica ao Python que a pasta é um pacote importável.
        (Desde o Python 3.3 ele pode estar vazio, mas é boa prática incluí-lo.)

8. Estrutura de um projeto modular

    projeto/
    │
    ├── main.py
    ├── util/
    │   ├── __init__.py
    │   ├── arquivos.py
    │   ├── calculos.py
    │   └── strings.py

    🔹 Dentro de main.py:

        from util.calculos import soma
        from util.strings import capitalizar

        print(soma(3, 5))
        print(capitalizar("André Augusto"))

9. Importações relativas (em pacotes)

    Dentro de pacotes, é possível importar de forma relativa.

    Ex:
        # dentro de util/calculos.py
        from .strings import capitalizar

    ° O ponto (.) indica o mesmo pacote.
    ° Dois pontos (..) indicam o pacote pai.

10. O módulo __name__ e a execução direta

    Cada arquivo Python tem um atributo interno __name__.
    Se o arquivo for executado diretamente __name__== "__main__"

    Ex:
        # arquivo matematica.py
        def soma(a, b):
            return a + b

        if __name__ == "__main__":
            print("Executando diretamente")

11. Boas práticas

    🔹 Manter módulos pequenos e coesos (um tema por arquivo).
    🔹 Usar nomes descritivos (arquivo.py, usaurio.py, api.py).
    🔹 Evitar importações circulares (um módulo importando o outro).
    🔹 Agrupar funções comuns em pacotes.
    🔹 Usar requirements.txt para listar depedências externas.
    🔹 Testar cada módulo isoladamente com __name__ == "__main__".

12. Erros comuns

    🔹 ModuleNotFoundError -> módulo não existe ou não está no mesmo diretório.
    🔹 ImportError -> função/classe não encontrada dentro do módulo.
    🔹 Caminhos incorretos de importação dentro de pacotes.
    🔹 Esquecer o __init__.py em pastas de pacotes.
    