# Sales Automation
***Autor:*** [Edson Soares](https://github.com/edsondearaujo)
## Descrição do Projeto
O projeto Sales Automation é uma solução para **automatizar relatórios** de vendas utilizando **integração** com **Google Sheets** e **AWS SageMaker** para realizar **previsões** e **análises de dados**. A aplicação foi desenvolvida com foco em **automação de processos de negócios**, extraindo dados de planilhas do Google Drive e realizando análises preditivas com AWS SageMaker.

Este projeto pode ser utilizado para gerar relatórios, consolidar dados de vendas, **prever comportamentos** e **gerar insights** que agregam valor às operações comerciais.

## Funcionalidades Principais
- **Integração com Google Sheets**: Carrega dados de vendas, produtos e vendedores diretamente de planilhas armazenadas no Google Drive.
- **Automação de Relatórios**: Gera relatórios automáticos de vendas consolidadas, analisando métricas de desempenho.
- **Análise Preditiva com AWS SageMaker**: Utiliza AWS SageMaker para análise de dados e geração de previsões baseadas em algoritmos de machine learning.
- **Banco de Dados Local**: Armazena os dados em um banco de dados SQLite para consulta e análise futura.

## Tecnologias Envolvidas
- **Python**: Linguagem de programação principal utilizada no projeto.
- **Google Sheets API**: Para integração e extração de dados diretamente das planilhas.
- **Google Drive API**: Para acesso e gerenciamento de arquivos no Google Drive.
- **AWS SageMaker**: Para realizar análises preditivas de vendas e machine learning.
- **SQLite**: Banco de dados local para armazenar as informações de vendas, produtos e vendedores.
- **Jupyter Notebook**: Para desenvolvimento e teste de código diretamente no AWS SageMaker.
- **Git**: Controle de versão e gerenciamento do projeto no GitHub.
- **Bibliotecas Python**: Pandas, Matplotlib, Gspread, Oauth2client, Boto3.

## Estrutura do Projeto
```bash
sales_automation/
│
├── config/
│   └── credentials_google_api.json  # Credenciais de serviços para autenticação com Google API
│
├── data/
│   └── (Aqui estarão os arquivos de dados de entrada, se necessário)
│
├── logs/
│   └── execution.log  # Log da execução do projeto
│
├── src/
│   ├── auth_google.py  # Autenticação com Google API
│   ├── google_sheets_interaction.py  # Integração com Google Sheets
│   ├── sagemaker_integration.py  # Integração com AWS SageMaker
│   ├── database.py  # Conexão com banco de dados SQLite
│   ├── setup.py  # Criação das tabelas no banco de dados
│   ├── utils.py  # Funções auxiliares (carregar planilhas, processar dados, etc.)
│   └── main.py  # Execução principal do projeto
│
└── README.md
```

## Como Executar o Projeto Localmente
### Pré-requisitos
Antes de executar o projeto, certifique-se de que você tem os seguintes itens instalados:

- Python 3.x
- Pip (gerenciador de pacotes Python)
- Conta no Google Cloud para acessar as APIs do Google (Google Sheets e Drive)
- AWS CLI configurada para acesso ao AWS SageMaker

## Passo a Passo para Executar o Projeto
### Clone o Repositório:
### _No terminal, execute_:

```bash
git clone https://github.com/edsondearaujo/sales_automation.git
```

```bash
  cd sales_automation
```
## Instale as Dependências:

Execute o comando para instalar todas as bibliotecas Python necessárias:

```bash
pip install -r requirements.txt
```
### Configuração das Credenciais do Google API:

Obtenha as credenciais do Google API seguindo este guia.
- Salve o arquivo credentials_google_api.json no diretório config/.
Configuração do AWS SageMaker:

- Certifique-se de que sua AWS CLI está configurada corretamente com suas credenciais.
- Configure um endpoint no SageMaker que o código possa usar para inferências.
- Inicialize o Banco de Dados:
- Execute o script de configuração do banco de dados para criar as tabelas:

```bash
python3 src/setup.py
```

### Executar a Aplicação:

Depois que o banco de dados estiver configurado e as credenciais estiverem corretas, execute o arquivo principal para iniciar o processamento:

```bash
python3 src/main.py
```
ou
```bash
python3 -m src.main #executar como módulo
```
Isso irá:

- Autenticar-se nas APIs do Google para acessar os dados do Google Sheets.
- Carregar os dados de produtos, vendas e vendedores.
- Inserir os dados no banco de dados SQLite.
- Gerar relatórios e interagir com o AWS SageMaker para previsões.
- Testar o Projeto com Dados Locais.

Se preferir testar o projeto com dados locais, você pode colocar um arquivo Excel na pasta _**data/**_ e modificar o código para carregar os dados a partir desse arquivo.

### Logs
Os logs da execução são gravados no arquivo _**logs/execution.log**_, onde você pode verificar eventuais erros ou sucessos na execução das tarefas.

### Como Contribuir
Sinta-se à vontade para enviar pull requests ou abrir issues no GitHub para contribuir com melhorias no projeto.

Se você tiver qualquer dúvida ou encontrar problemas, por favor, entre em contato!