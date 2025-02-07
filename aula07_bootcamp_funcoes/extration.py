import pandas as pd
import os
import glob

# Função de extract, ler  e consolida o json
pasta = 'data'

def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

# Função que transforma

def calcular_total(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# Função que dar load em csv ou parquet

def carregar_dados(df: pd.DataFrame, formato_saida: list):
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_csv("dados.parquet", index=False)


def pipeline_calcular_kpi_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_total(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)