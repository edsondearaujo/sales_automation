#src/main.py
from src.utils import carregar_dados_aba
from src.database import create_connection, insert_produto, insert_vendedor, insert_venda
import logging
from config.variaveis_de_ambiente import *

logging.basicConfig(filename='logs/execution.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def processar_dados_e_inserir(conn, dados_produtos, dados_vendedores, dados_vendas):
    """Processa os dados das planilhas e insere no banco de dados."""
    try:
        # Processa e insere produtos
        for item in dados_produtos[1:]:  # Ignora o cabeçalho
            nome, preco, categoria = item[1], float(item[2]), item[3]
            logging.info(f"Processando produto: {nome}, Categoria: {categoria}, Preço: R$ {preco:.2f}")
            insert_produto(conn, nome, categoria, preco)

        # Processa e insere vendedores
        for item in dados_vendedores[1:]:
            nome_vendedor, email_vendedor = item[1], item[2]
            logging.info(f"Processando vendedor: {nome_vendedor}, Email: {email_vendedor}")
            insert_vendedor(conn, nome_vendedor)

        # Processa e insere vendas
        for item in dados_vendas[1:]:
            produto_id, vendedor_id, quantidade = int(item[1]), int(item[2]), int(item[3])
            logging.info(
                f"Processando venda: Produto ID {produto_id}, Vendedor ID {vendedor_id}, Quantidade: {quantidade}")
            insert_venda(conn, produto_id, vendedor_id, quantidade)

        logging.info("Dados inseridos com sucesso no banco de dados.")
    except Exception as e:
        logging.error(f"Erro ao processar e inserir dados: {e}")


def main():
    logging.info("Iniciando o processo de autenticação e carregamento de dados.")

    try:
        # Carrega os dados de cada aba
        dados_produtos = carregar_dados_aba(SPREADSHEET_ID, "produtos!A2:D6")
        dados_vendedores = carregar_dados_aba(SPREADSHEET_ID, "vendedores!A2:C6")
        dados_vendas = carregar_dados_aba(SPREADSHEET_ID, "vendas!A2:E6")

        if not dados_produtos or not dados_vendedores or not dados_vendas:
            logging.error("Erro: Não foi possível carregar os dados da planilha.")
            return

        # Conecta ao banco de dados
        conn = create_connection(DATABASE_PATH)
        if not conn:
            logging.error("Erro ao conectar ao banco de dados.")
            return

        # Processa e insere os dados no banco
        processar_dados_e_inserir(conn, dados_produtos, dados_vendedores, dados_vendas)

    except Exception as e:
        logging.error(f"Erro na execução da função principal: {e}")

    finally:
        # Fechar a conexão com o banco de dados
        if conn:
            conn.close()
            logging.info("Conexão com o banco de dados fechada.")
        logging.info("Processo concluído com sucesso.")


if __name__ == "__main__":
    main()
