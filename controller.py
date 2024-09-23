from reader import lerArquivoTXT
from collections import Counter

DATA_SET = lerArquivoTXT()

def colunas_disponiveis():
    """
    Retorna as colunas disponíveis no dataset.
    """
    if DATA_SET:
        return list(DATA_SET[0].keys())
    else:
        return []

def obter_dados_coluna(nome_coluna):
    """
    Retorna os dados de uma coluna específica, se ela existir no dataset.
    """
    if DATA_SET and nome_coluna in DATA_SET[0]:
        return [linha[nome_coluna] for linha in DATA_SET]
    else:
        return f"Coluna '{nome_coluna}' não encontrada."

import csv

def gerarCSVPessoasPorMunicipio():
    """
    Gera um arquivo CSV com a quantidade de pessoas por município.
    """
    
    dados_municipio = obter_dados_coluna('MUNICÍPIO')
    
    contagem_municipios = Counter(dados_municipio)

    with open('pessoas_por_municipio.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Município', 'Quantidade de Pessoas'])
        
        for municipio, quantidade in contagem_municipios.items():
            writer.writerow([municipio, quantidade])

    print("Arquivo CSV 'pessoas_por_municipio.csv' gerado com sucesso!")





