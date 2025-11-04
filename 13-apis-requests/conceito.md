# 🌐 Conceito: APIs e Consumo de Dados em Python (com `requests`)

---

## 1. O que é uma API?

Uma **API (Application Programming Interface)** é uma interface que permite a comunicação entre sistemas.  
Ela define **como um programa pode pedir dados** ou **enviar informações** para outro.

> 💡 “Uma API é como um garçom — você faz o pedido (requisição), ele leva até a cozinha (servidor) e traz o prato pronto (resposta).”

---

## 2. Tipos de APIs mais comuns

| Tipo        | Descrição                       | Exemplo                        |
| ------------ | ------------------------------- | ------------------------------ |
| **REST**     | Baseada em URLs e métodos HTTP  | `https://api.github.com/users` |
| **SOAP**     | Baseada em XML (mais antiga)    | Web Services corporativos      |
| **GraphQL**  | Consulta personalizada via JSON | APIs modernas do GitHub        |

Neste módulo, o foco será **REST APIs** com **requisições HTTP**.

---

## 3. O que é o módulo `requests`?

O módulo `requests` é a biblioteca mais popular para fazer **requisições HTTP** em Python.  
Com ela, é possível **consumir APIs**, **enviar dados**, **autenticar** e **trabalhar com JSON** facilmente.

🔹 **Instalação:**  
```
pip install requests
```

---

## 4. Fazendo uma requisição GET

```python
import requests

url = "https://api.github.com/users/HDevJr"
resposta = requests.get(url)

print(resposta.status_code)
print(resposta.json())
```

**Saída (resumida):**
```json
{
  "login": "HDevJr",
  "id": 12345,
  "public_repos": 10
}
```

---

## 5. Entendendo os códigos de status HTTP

| Código | Significado                           |
| ------ | ------------------------------------- |
| `200`  | OK – requisição bem-sucedida          |
| `201`  | Criado – novo recurso salvo           |
| `400`  | Erro do cliente (requisição inválida) |
| `401`  | Não autorizado                        |
| `403`  | Acesso proibido                       |
| `404`  | Não encontrado                        |
| `500`  | Erro interno do servidor              |

```python
if resposta.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print("Erro:", resposta.status_code)
```

---

## 6. Trabalhando com JSON

A maioria das APIs modernas retorna dados em formato **JSON**.

```python
dados = resposta.json()
print(dados["login"])
print(dados["public_repos"])
```

---

## 7. Enviando dados (POST)

```python
import requests

url = "https://httpbin.org/post"
payload = {"nome": "Junior", "idade": 21}

resposta = requests.post(url, json=payload)
print(resposta.status_code)
print(resposta.json())
```

**Saída:**
```json
{
  "json": {"nome": "Junior", "idade": 21}
}
```

---

## 8. Enviando dados com `form-data` (como formulários)

```python
dados = {"usuario": "admin", "senha": "123"}
resposta = requests.post("https://httpbin.org/post", data=dados)
print(resposta.json())
```

💡 `data=` envia como formulário (`x-www-form-urlencoded`)  
💡 `json=` envia como JSON puro

---

## 9. Enviando headers (autenticação e configuração)

Algumas APIs exigem **headers personalizados** (como tokens de acesso).

```python
headers = {
    "Authorization": "Bearer MEU_TOKEN_AQUI",
    "Content-Type": "application/json"
}

resposta = requests.get("https://api.exemplo.com/dados", headers=headers)
print(resposta.status_code)
```

---

## 10. Enviando parâmetros (query params)

```python
params = {"page": 1, "limit": 5}
resposta = requests.get("https://api.exemplo.com/usuarios", params=params)
print(resposta.url)
```

**Saída:**
```
https://api.exemplo.com/usuarios?page=1&limit=5
```

---

## 11. Manipulando respostas

```python
r = requests.get("https://api.github.com/users/HDevJr")

print(r.headers)    # Cabeçalhos da resposta
print(r.encoding)   # Codificação
print(r.text[:100]) # Texto bruto da resposta
print(r.elapsed)    # Tempo de resposta
```

---

## 12. Tratamento de erros em requisições

```python
try:
    r = requests.get("https://api.github.com/users/HDevJr", timeout=5)
    r.raise_for_status()  # levanta erro se não for 200
    print(r.json())
except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
```

> Isso captura erros de rede, timeout e status HTTP automaticamente.

---

## 13. Salvando resposta em arquivo

```python
r = requests.get("https://api.github.com/users/HDevJr")
with open("usuario.json", "w", encoding="utf-8") as f:
    f.write(r.text)
```

---

## 14. APIs públicas populares para praticar

| API                 | Descrição              | URL                                              |
| ------------------- | ---------------------- | ------------------------------------------------ |
| **JSONPlaceholder** | API fake para testes   | `https://jsonplaceholder.typicode.com`           |
| **ViaCEP**          | Busca CEPs brasileiros | `https://viacep.com.br/ws/01001000/json/`        |
| **PokeAPI**         | Dados de Pokémon       | `https://pokeapi.co/api/v2/pokemon/1`            |
| **CoinGecko**       | Dados de criptomoedas  | `https://api.coingecko.com/api/v3/coins/bitcoin` |
| **The Cat API**     | Imagens de gatos       | `https://api.thecatapi.com/v1/images/search`     |

---

## 15. Exemplo completo — consumindo uma API pública

```python
import requests

cep = "01001000"
url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    print(f"Endereço: {dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}")
else:
    print("Erro ao buscar o CEP.")
```

**Saída:**
```
Endereço: Praça da Sé, Sé - São Paulo/SP
```

---

## 16. Boas práticas

✅ Sempre trate erros de rede e status HTTP.  
✅ Use `timeout=` para evitar travamentos.  
✅ Armazene tokens e chaves de API em variáveis de ambiente (`.env`).  
✅ Evite loops infinitos de requisições.  
✅ Registre (log) erros e respostas inesperadas.  
✅ Documente as APIs usadas no projeto.

---

## 17. Erros comuns

❌ `requests.exceptions.ConnectionError` → problema de conexão.  
❌ `requests.exceptions.Timeout` → tempo limite excedido.  
❌ `JSONDecodeError` → resposta não é JSON válido.  
❌ `401 Unauthorized` → falta de autenticação.  
❌ `404 Not Found` → endpoint incorreto.

---
