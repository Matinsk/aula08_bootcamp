import pandas as pd
import os
import glob


# uma função de extract que le e consolida os json


def extrair_dados(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index= True)

    return df_total
# uma funcao que transforma

def calcular_kpi_total_vendas(df : pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# uma funcao que da load em csv ou parque

def carregar_dados(df : pd.DataFrame,formato_saida : list):

    for formato in formato_saida:

        if formato == "csv":
           df.to_csv("dados.csv")
        if formato  == "parquet":
            df.to_parquet("dados.parquet")


def pipeline_calcular_kpi_de_vendas_consolidado(pasta : str, formato_de_saida : list):
    
    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_kpi_total_vendas(data_frame)
    carregar_dados(data_frame_calculado,formato_saida= formato_de_saida)


if __name__ == "__main__":
    pasta_argumento = 'data'
    data_frame = extrair_dados(pasta_argumento)
    data_frame_calculado = calcular_kpi_total_vendas(data_frame)
    formato_de_saida = ["csv","parquet"]
    carregar_dados(data_frame_calculado,formato_saida= formato_de_saida)
    