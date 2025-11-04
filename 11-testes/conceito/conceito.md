Conceito: Testes Automatizados em Python (Python e Unittest)

1. O que são testes automatizados ?

    Os testes automatizados são scripts que verificam automaticamente se o código 
    funciona como esperado.
    Eles ajudam a detectar erros cedo, evitar regressões e garantir que novas alterações
    não quebrem o sistema.

    🔹 Raciocínio:

        "Em vez de testar o código manualmente, você ensina o computador a testar por você."
    
2. Por que testar ?

    ✅ Evita bugs em produção
    ✅ Facilita refatorações com segurança
    ✅ Aumenta a confiança no código
    ✅ Permite integração contínua (CI/CD)
    ✅ Serve como documentação viva do sistema

3. Tipos de testes

    | Tipo                | O que testa                                     | Exemplo                            |
    | ------------------- | ----------------------------------------------- | ---------------------------------- |
    | **Unitário**        | Uma função ou classe isolada                    | Testar uma função `soma()`         |
    | **De integração**   | Interação entre módulos                         | API + banco de dados               |
    | **Funcional / E2E** | O sistema completo em uso                       | Login, fluxo de compra             |
    | **De regressão**    | Verifica se algo “antigo” quebrou após mudanças | Testes repetidos após refatorações |

4. Estrutura básica de um teste unitário

    Um teste verficia se uma entrada produz a saída esperada.

    Ex:
        def somar(a, b):
            return a + b
        
        def test_soma():
            assert soma(2, 3) == 5
    
        # Saída (executando  com pyteste): pytest .
                                           ✓ test_soma PASSED

5. Testes com assert

    O comando assert verifica se uma condição é verdadeira.
    Se for falsa, o teste falha.

    Ex:
        def dobro(x):
            return x * 2

        def test_dobro():
            assert dobro(4) == 8
            assert dobro(0) == 0
            assert dobro(-2) == -4

6. Criando testes com o módulo unittest (nativo do Python)

    🔹 Estrutura básica:

        Ex:
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
            
            # Saída: ..
                     ----------------------------------------------------------------------
                     Ran 2 tests in 0.001s

                     OK

        🔹 1. Importação do módulo:

            import unittest

            -> Aqui está sendo importando o framework de testes do Python,
               chamado unittest.

               Ele serve para criar e executar testes automaticamente,
               verificando se as funções do código estão funcionando corretamente.

        🔹 2. Função a ser testada:

            def soma(a, b):
                return a + b
            
            -> Essa é uma função simples que retorna a soma de dois números.
               Será ela que o teste vai verificar.
        
        🔹 3. Criando a classe de teste:

            class TesteSoma(unittest.TestCase):

            -> Aqui é criado uma classe de teste, que:
            ° herda de unittest.TestCase (classe base do framework),
            ° e define métodos de test (funções que testam partes do código).
            ° Tudo o que estiver dentro dessa classe será avaliado automaticamente quando o teste rodar.
        
        🔹 4. Criando os métodos de teste:

            ✅ Teste 1 – soma positiva

                def test_soma_positiva(self):
                    self.assertEqual(soma(2, 3), 5)
            
            ° self.assertEqual(x, y) -> verifica se x é igual a y.
            ° Se for, o teste passa ✅
            ° Se não for, o teste falha ❌

            Aqui, ele verifica se:
                
                soma(2, 3) == 5 
            
            O resultado é verdadeiro -> teste aprovado.

            ✅ Teste 2 – soma negativa

                def test_soma_negativa(self):
                    self.assertEqual(soma(-1, -1), -2)
                
            Verifica se:

                soma(-1, -1) == -2

            Também é verdadeiro -> outro teste aprovado.

        🔹 5. Executando os testes:

            if __name__ == '__main__':
                unittest.main()

            -> Isso faz com que, ao rodar o arquivo (por exemplo, python teste.py),
            o Pytho procure automaticamente por classes de teste (que herdam de unittest.TestCase)
            e executa todos os métodos que começam com test_.

        🔹 6. Saída esperada:

            -> Quando é executado o script no terminal, verá algo assim:

            ..
            ----------------------------------------------------------------------
            Ran 2 tests in 0.000s

            OK

            ° Cada ponto (.) representa um teste que passou.
            ° "Ran 2 tests" -> foram executados dois testes.
            ° "OK" -> todos passaram com sucesso ✅
            Se algum teste falhar, o Python mostra o erro com detalhes.



            | Elemento                             | Função                                         |
            | ------------------------------------ | ---------------------------------------------- |
            | `unittest`                           | Módulo padrão para testes automáticos          |
            | `class TesteSoma(unittest.TestCase)` | Define uma classe de testes                    |
            | `test_...`                           | Métodos executados automaticamente como testes |
            | `assertEqual(a, b)`                  | Verifica se o resultado é o esperado           |
            | `unittest.main()`                    | Roda todos os testes do arquivo                |
            | `OK`                                 | Todos os testes passaram                       |

7. Testando exceções com unittest

    Ex:
        def dividir(a, b):
            if b == 0:
                raise ValueError("Divisão por zero não permitida.")
            return a / b
        
        class TesteDivisão(unittest.TestCase):
            def test_divisao_por_zero(self):
                with self.assertRaises(ValueError):
                    dividir(10, 0)

    🔹 1. Função dividir()

        def dividir(a, b):
            if b == 0:
                raise ValueError("Divisão por zero não permitida.")
            return a / b
        
        ° Essa função tenta dividir a por b .
        ° Tratamento de erro
        ° Antes de fazer a divisão, ela verifica se o divisor b é zero.
        ° Se for, ela lança um erro (exceção) com o comando raise.

        raise ValueError("Divisão por zero não permitida.")

        🔹 Isso significa:
            "Pare a execução e informe que houve um erro de tipo ValueError com essa mensagem".

        🔹 Caso contrário:
            Se b for diferente de zero, a função executa normalmente:

            return a / b

    🔹 2. A classe de teste:

        class TesteDivisão(unittest.TestCase):

        -> Essa classe herda de unittest.TestCase,
        o que significa que ela é um conjunto de testes automatizados.

    🔹 3. O método de teste:

        def test_divisao_por_zero(self):
            with self.assertRaises(ValueError):
                dividir(10, 0)
        
        -> Aqui está a parte mais importante:

        🔸 with self.assertRaises(ValueError):

        Esse comando verifica se uma exceção específica e lançada dentro do bloco with.

        Em outras palavras:
            "Espere que a função dentro deste bloco gere um erro do tipo ValueError."
        
        🔸 Dentro do bloco:

            dividir(10, 0)

        -> Essa chamada deveria causar um erro,
        porque b = 0 e a função usa:

            raise ValueError("Divisão por zero não permitida.")

        Então o teste só passa se o erro realmente for lançado.
        Se a função não lançar o erro, o teste falha.
    
    🔹 4. O que acontece quando você executa:

        Quando o unittest roda esse teste, ele:
        ° Chama dividir(10, 0);
        ° Vê que a função lançou um ValueError;
        ° Confirma que era exatamente o tipo de erro esperado;
        ° E marca o teste como aprovado.

8. Testes com Pytest (biblioteca mais moderna e popular)

    O pytest torna testes mais simples e legíveis.

    🔹 Instalação:

        pip install pytest
    
    🔹 Exemplo:

        def soma(a, b):
            return a + b
        
        def test_soma():
            assert soma(2, 3) == 5

    🔹 Estrutura recomendada:

        meu_projeto/
        │
        ├── app/
        │   └── funcoes.py
        └── tests/
            └── test_funcoes.py
    
    🔹 Executar:

        pytest
    
9. Testando exceções com pytest

    import pytest

    def dividir(a, b):
        if b ==0:
            raise ValueError("Divisão por zero.")
        return a / b
    
    def test_dividir_por_zero():
        with pytest.raises(ValueError):
            dividir(10, 0)

10. Usando setup e teardown

    Às vezes, precisamos preparar ou limpar algo antes/despois dos testes.
    Podemos usar fixtures ou métodos especiais.

    🔹 Com unittest:

        class TesteConta(unittest.TestCase):
            def setup(self):
                self.saldo = 100                    # executa antes de cada teste
            
            def tearDown(self):
                self.saldo = 0                      # executa depois de cada teste
            
            def test_saque(self):
                self.saldo -= 50
                self.assertEqual(self.saldo, 50)
            
    🔹 Com pytest (fixture):

        import pytest

        @pytest.fixture
        def saldo_inicial():
            return 100

        def test_saque(saldo_inicial):
            novo_saldo = saldo_inicial - 50
            assert nova_saldo == 50

11. Cobertura de testes (coverage)

    Para medir quanto do código foi testado, instale o pytest-cov:

    Ex:
        pip install pytest-cov
        pytest --cov=app/

        # Saída:    ----------- coverage: platform win, python 3.12 -----------
                    Name                 Stmts   Miss  Cover
                    ----------------------------------------
                    app/funcoes.py          10      0   100%

12. Integração com CI/CD (GitHub Actions)

    É possível automatizar a exceção de teste em cada commit no GitHub.

    Exemplo de arquivo .github/workflows/test.yml :

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
    
    Assim, os teste rodam automaticamente em cada atualização do repositório.

13. Boas práticas

    ✅ Nomeie arquivos de teste com o prefixo test_.
    ✅ Cada função deve testar apenas uma coisa.
    ✅ Escreva testes antes ou junto com o código (TDD).
    ✅ Use mensagens de erro claras nos asserts.
    ✅ Mantenha os testes rápidos e independentes entre si.
    ✅ Garanta cobertura acima de 80%.

14. Erros comuns

    ❌ Testes dependentes da ordem de execução.
    ❌ Não isolar dados entre testes (usar variáveis globais).
    ❌ Testes lentos e pouco específicos.
    ❌ Esquecer de configurar o ambiente de teste.
