import pandas as pd

class DatabaseManager:
    def __init__(self, db_path: str):
        """
        Inicializa o gerenciador de banco de dados.

        :param db_path: Caminho para o arquivo do banco de dados (CSV).
        """
        self.db_path = db_path

    def read_data(self) -> pd.DataFrame:
        """
        Lê os dados do banco de dados.

        :return: DataFrame contendo os dados do banco.
        """
        return pd.read_csv(self.db_path)

    def write_data(self, df: pd.DataFrame) -> None:
        """
        Escreve os dados no banco de dados.

        :param df: DataFrame a ser escrito no banco de dados.
        """
        df.to_csv(self.db_path, index=False)

    def update_data(self, df: pd.DataFrame) -> None:
        """
        Atualiza os dados no banco de dados.

        :param df: DataFrame com os dados atualizados.
        """
        self.write_data(df)

    def filter_data(self, condition: dict) -> pd.DataFrame:
        """
        Filtra os dados com base em condições.

        :param condition: Dicionário com as condições de filtro.
        :return: DataFrame filtrado.
        """
        df = self.read_data()
        for column, value in condition.items():
            df = df[df[column] == value]
        return df
