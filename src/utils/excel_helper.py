import pandas as pd

def read_excel(file_path: str, sheet_name: str = None) -> pd.DataFrame:
    """
    Lê um arquivo Excel e retorna um DataFrame.

    :param file_path: Caminho para o arquivo Excel.
    :param sheet_name: Nome da planilha a ser lida (opcional).
    :return: DataFrame contendo os dados da planilha.
    """
    return pd.read_excel(file_path, sheet_name=sheet_name)

def write_excel(file_path: str, df: pd.DataFrame, sheet_name: str = 'Sheet1') -> None:
    """
    Escreve um DataFrame em um arquivo Excel.

    :param file_path: Caminho para o arquivo Excel onde os dados serão escritos.
    :param df: DataFrame a ser escrito.
    :param sheet_name: Nome da planilha onde os dados serão escritos (padrão: 'Sheet1').
    """
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
