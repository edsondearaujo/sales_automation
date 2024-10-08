import logging
from src.utils import carregar_dados_aba
from src.database import create_connection, insert_produto, insert_vendedor, insert_venda
from config.variaveis_de_ambiente import *

logging.basicConfig(filename='logs/execution.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Iniciando o processo de carregamento e processamento de dados.")
    
    try:
        dados_produtos = carregar_dados_aba(SPREADSHEET_ID, "produtos!A2:D6")
        dados_vendedores = carregar_dados_aba(SPREADSHEET_ID, "vendedores!A2:C6")
        dados_vendas = carregar_dados_aba(SPREADSHEET_ID, "vendas!A2:E6")

        if not dados_produtos or not dados_vendedores or not dados_vendas:
            logging.error("Erro ao carregar os dados.")
            return
        
        conn = create_connection(DATABASE_PATH)
        processar_dados_e_inserir(conn, dados_produtos, dados_vendedores, dados_vendas)
        
    except Exception as e:
        logging.error(f"Erro na execução: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
