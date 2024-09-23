import csv

PATH = "DADOS.txt"

def lerArquivoTXT():
    """
    Lê um arquivo .txt separado por vírgulas e retorna os dados como uma lista de dicionários.
    Cada dicionário representa uma linha com chave como o nome da coluna.
    """
    with open(PATH, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        dados = [linha for linha in leitor_csv]

    return dados