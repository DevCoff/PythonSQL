# CRUD com Python e MySQL

Este projeto demonstra um simples CRUD (Create, Read, Update, Delete) utilizando Python e MySQL. A integração é feita utilizando o MySQL Workbench para gerenciar o banco de dados e o `mysql.connector` para a conexão com Python.

## Pré-requisitos

- **Python 3.x**: Certifique-se de ter o Python instalado. [Baixe Python](https://www.python.org/downloads/)
- **MySQL Workbench**: Ferramenta para gerenciamento de bancos de dados MySQL. [Baixe MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
- **MySQL Server**: Para hospedar seu banco de dados. Ele geralmente é instalado junto com o MySQL Workbench.
- **mysql-connector-python**: Biblioteca Python para conectar ao MySQL.

## Instalação do MySQL Workbench

1. Baixe o MySQL Workbench do site oficial: [MySQL Workbench Download](https://dev.mysql.com/downloads/workbench/)
2. Siga o assistente de instalação para completar a instalação do MySQL Workbench e do MySQL Server.
3. Após a instalação, abra o MySQL Workbench e conecte-se ao seu servidor MySQL local.

## Configuração do Banco de Dados

1. **Crie um novo banco de dados no MySQL Workbench**:
   - Abra o MySQL Workbench.
   - Conecte-se ao seu servidor MySQL.
   - Na aba de navegação, clique com o botão direito em "Schemas" e selecione "Create Schema".
   - Dê um nome ao seu banco de dados (por exemplo, `seu_database`) e clique em "Apply".

2. **Crie uma tabela chamada `Vendas` para armazenar os dados**:

    ```sql
    CREATE TABLE Vendas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome_produto VARCHAR(50),
        valor DECIMAL(10, 2)
    );
    ```

## Integração com Python

### Instalação do `mysql-connector`

Antes de executar o código Python, você precisa instalar o conector MySQL. Execute o seguinte comando no terminal:

```bash
pip install mysql-connector-python
