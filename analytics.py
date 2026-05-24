
# FILE: analytics.py
import pandas as pd
import numpy as np

def load_data():
    df = pd.read_csv('despesas.csv')
    df['data'] = pd.to_datetime(df['data'])
    return df

def total_por_mes_tipo(df, tipo):
    # Total PF ou PJ por mês
    df_tipo = df[df['tipo'] == tipo]
    return df_tipo.groupby(df_tipo['data'].dt.month)['valor'].sum()

def media_por_dia(df):
    # Média de gasto por dia (total)
    return df.groupby('data')['valor'].sum().mean()

def maior_despesa_individual(df):
    return df.loc[df['valor'].idxmax()]

def top_3_categorias(df):
    return df.groupby('categoria')['valor'].sum().nlargest(3)

def previsao_gastos_mes(df, mes):
    # Previsão simples: média diária * dias restantes
    df_mes = df[df['data'].dt.month == mes]
    dias = df_mes['data'].dt.day.nunique()
    media_diaria = df_mes.groupby('data')['valor'].sum().mean()
    dias_restantes = 30 - dias if mes == 4 else 31 - dias
    return media_diaria * dias_restantes

def despesas_recorrentes(df):
    # Simples: categorias que aparecem em todos os meses
    meses = df['data'].dt.month.unique()
    rec = []
    for cat in df['categoria'].unique():
        if df[df['categoria'] == cat]['data'].dt.month.nunique() == len(meses):
            rec.append(cat)
    return rec
