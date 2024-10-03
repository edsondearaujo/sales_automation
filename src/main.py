from services.relatorio import Relatorio
from database.db_manager import DatabaseManager
from utils.excel_helper import read_excel, write_excel

def main():
    # Caminho para o arquivo de vendas
    vendas_file_path = 'data/vendas.xlsx'
    # Caminho para o arquivo de banco de dados (CSV)
    db_file_path = 'data/outros_dados.csv'

    # Leitura dos dados de vendas
    vendas_df = read_excel(vendas_file_path)

    # Instanciação do gerenciador de banco de dados
    db_manager = DatabaseManager(db_file_path)

    # Supondo que você tenha uma lógica para processar as vendas
    relatorio = Relatorio(vendas_df)
    relatorio.gerar_relatorio()

    # Aqui você pode adicionar qualquer outra lógica necessária, como salvar os dados no banco
    db_manager.write_data(vendas_df)

if __name__ == "__main__":
    main()
