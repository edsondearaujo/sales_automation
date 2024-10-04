FROM python:3.9-slim

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de dependências para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código para o contêiner
COPY . .

# Comando para rodar a aplicação
CMD ["python3", "-m", "src.main"]
