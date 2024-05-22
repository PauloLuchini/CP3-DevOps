# CP3-DevOps
## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Docker: [Instruções de instalação](https://docs.docker.com/get-docker/)
- Docker Compose: [Instruções de instalação](https://docs.docker.com/compose/install/)

## Executando o Projeto

1. Clone este repositório para sua máquina local:

    ```bash
    git clone https://github.com/seu_usuario/seu_projeto.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd seu_projeto
    ```

3. Execute o comando abaixo para construir e iniciar os serviços com Docker Compose:

    ```bash
    docker-compose up --build
    ```

4. Após a inicialização bem-sucedida, abra o navegador e acesse o aplicativo em:

    ```
    http://localhost:5000
    ```

5. Para parar os serviços, pressione `Ctrl + C` no terminal e execute o seguinte comando:

    ```bash
    docker-compose down
    ```

## Endpoints da API

- `GET /empregados`: Retorna uma lista de todos os empregados.
- `POST /empregados`: Adiciona um novo empregado ao banco de dados.
- `PUT /empregados/<id>`: Atualiza os detalhes de um empregado existente.
- `DELETE /empregados/<id>`: Deleta um empregado do banco de dados.


!Arquitetura da solução:
![Captura de tela 2024-05-22 114122](https://github.com/PauloLuchini/CP3-DevOps/assets/126570230/8297c793-ccdf-4438-947d-ad9c0432a479)
