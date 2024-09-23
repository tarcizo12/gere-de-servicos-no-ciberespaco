from controller import *


def verColunasDisponives():
    """
     Exibe as colunas disponíveis
    """
 
    print("Colunas disponíveis no dataset:", colunas_disponiveis())


def verDadosDaColuna():
    """
     Obtem dados de uma coluna específica
    """
    coluna_escolhida = "MUNICÍPIO"  
    
    dados_coluna = obter_dados_coluna(coluna_escolhida)
    print(f"Dados da coluna '{coluna_escolhida}':", dados_coluna)



if __name__ == "__main__":    
    #verColunasDisponives()
    #verDadosDaColuna()
    gerarCSVPessoasPorMunicipio()