
# Sales Report Automation

Uma aplicação simples para gerenciar produtos, registrar vendas e gerar relatórios utilizando SQLite.

## Como rodar o projeto

### Usando Python localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sales_report_automation.git
   cd sales_report_automation
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Rode a aplicação:
   ```bash
   python3 -m src.main
   ```

### Usando Docker

1. Construa a imagem Docker:
   ```bash
   docker build -t sales-report-automation .
   ```

2. Rode o contêiner:
   ```bash
   docker run -it sales-report-automation
   ```

## Funcionalidades

- Inserção de Produtos
- Registro de Vendas
- Geração de Relatórios
