
## 📋 Pré-requisitos

Para rodar este projeto, você precisa ter **uma** das seguintes opções configuradas em sua máquina:


### Opção 1: Executar com Python 3

- [Python 3.8+](https://www.python.org/downloads/) instalado

### Opção 2: Executar com Docker

- [Docker Engine](https://docs.docker.com/get-docker/) instalado (versão 20+ recomendada)

---

## 🚀 Como rodar o projeto

Você pode executar este projeto de duas formas: diretamente com Python ou utilizando Docker.

### ✅ Rodando com Python 3

1. Clone este repositório:
    ```bash
    git clone https://github.com/devisonsantana/7-days-of-code-py.git
    ```
2. Crie e ative um ambiente virtual (Opcional):
    ```bash
    # Cria um ambiente virtual para instalar os módulos necessarios
    python3 -m venv .venv
    
    # Ativa o ambiente virtual
    source ./.venv/bin/activate
    ```
3. Instale as dependências:
    ```bash
    # Com base no arquivo de texto em `util/requirements.txt` 
    # instala todos os modulos necessarios para o funcionamento do programa
    pip install -r util/requirements.txt
    ```
4. Execute o projeto:
   ```bash
   python3 main.py
   ```
#### Desativando ambiente virtual
   
Caso não deseje usar mais o ambiente virtual você pode desativa-lo passando esse commando:
```bash
deactivate
```

### 🐳 Rodando com Docker

1. Clone este repositório:
    ```bash
    git clone https://github.com/devisonsantana/7-days-of-code-py.git && cd 7-days-of-code-py/
    ```
2. Construa a imagem Docker:
    ```bash
    docker build -t app
    ```
3. Execute o container:
    ```bash
    docker run --rm app
    ```
