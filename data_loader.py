
# FILE: data_loader.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_data():
    # Gera dados mockados de despesas para Abril e Maio
    np.random.seed(42)
    categories = {
        'Alimentação': ['restaurante', 'supermercado', 'padaria', 'açai', 'lanche'],
        'Transporte': ['uber', 'gasolina', 'estacionamento', 'pedagio', 'onibus'],
        'Moradia': ['aluguel', 'condominio', 'agua', 'luz', 'internet'],
        'Lazer': ['cinema', 'show', 'viagem', 'jogo', 'streaming'],
        'Saúde': ['farmacia', 'medico', 'plano de saude', 'exercicio'],
        'Educação': ['curso', 'livro', 'faculdade', 'material'],
        'IPVA': ['ipva'],
        'Outros': ['presente', 'roupa', 'assinatura', 'seguro']
    }
    
    # Mapeamento de palavras-chave para tipo PF/PJ
    keyword_to_type = {
        'pf': ['salario', 'freela', 'beneficio', 'restituição'],
        'pj': ['faturamento', 'nota fiscal', 'aluguel comercial', 'imposto']
    }
    
    # Gerar despesas recorrentes
    dates = []
    for month in [4, 5]:
        for day in range(1, 29):
            dates.append(datetime(2025, month, day))
    dates = sorted(dates * 3)  # multiplas despesas por dia
    
    data = []
    for date in dates[:200]:
        cat = np.random.choice(list(categories.keys()))
        desc_base = np.random.choice(categories[cat])
        valor = np.random.uniform(20, 500)
        if cat == 'IPVA':
            valor = np.random.uniform(300, 1000)
        # classificar tipo (PF/PJ) por palavra-chave
        type_ = 'pf'
        for kw in keyword_to_type['pj']:
            if kw in desc_base:
                type_ = 'pj'
                break
        data.append({
            'data': date.strftime('%Y-%m-%d'),
            'descricao': desc_base.capitalize(),
            'categoria': cat,
            'valor': round(valor, 2),
            'tipo': type_
        })
    df = pd.DataFrame(data)
    # Adicionar despesa de destaque IPVA
    df.loc[df['categoria'] == 'IPVA', 'destaque'] = True
    else:
        df['destaque'] = False
    return df

if __name__ == '__main__':
    df = generate_mock_data()
    df.to_csv('despesas.csv', index=False)
    print('Dados gerados com sucesso.')
