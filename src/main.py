from services.relatorio import Relatorio
from services.carregar_vendas import carregar_vendas

def main():
    vendas_file_path = 'data/vendas.xlsx'
    vendas = carregar_vendas(vendas_file_path)

    relatorio = Relatorio(vendas)

    print(relatorio)

if __name__ == "__main__":
    main()
