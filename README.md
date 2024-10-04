# Automação de Relatórios de Vendas

Este projeto consiste em uma automação de relatórios de vendas utilizando Python e um banco de dados SQLite.<br>
O objetivo é permitir a inserção de produtos e vendas, bem como a geração de relatórios de vendas de forma fácil e eficiente.

## Estrutura do Projeto

sales_report_automation/ │ ├── src/ │ ├── models/ │ │ ├── init.py │ │ ├── produto.py │ │ └── venda.py │ ├── services/ │ │ ├── init.py │ │ ├── carregar_vendas.py │ │ └── database.py │ ├── main.py │ ├── tests/ │ ├── test_carregar_vendas.py │ ├── test_produto.py │ ├── test_venda.py │ ├── Dockerfile ├── docker-compose.yml ├── vendas.xlsx ├── requirements.txt └── README.md


## Pré-requisitos

- Python 3.x
- SQLite3

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/automacao_relatorios_vendas.git

2. Navegue até o diretório do projeto:
```bash
    cd automacao_relatorios_vendas
