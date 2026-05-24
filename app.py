
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(page_title='Dashboard ALEXPRESS/ROCKET', layout='wide', page_icon='🚀')

# Tema dark premium com CSS customizado
st.markdown("""
<style>
body, .stApp {
    background-color: #0D0D0D !important;
    color: #FFFFFF !important;
}
.css-1offfwp {
    background-color: #1A1A1A !important;
}
.css-1q8dd3e {
    color: #FFFFFF !important;
}
.card {
    background-color: #1A1A1A;
    border-radius: 10px;
    padding: 20px;
    margin: 10px 0;
    border-left: 5px solid #00E5FF;
    box-shadow: 0 0 15px rgba(0,229,255,0.3);
}
.kpi {
    background-color: #1A1A1A;
    border: 1px solid #00E5FF;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    color: #FFFFFF;
    box-shadow: 0 0 10px rgba(0,229,255,0.2);
}
.kpi h3 {
    margin: 0;
    font-size: 14px;
    color: #00E5FF;
}
.kpi .value {
    font-size: 28px;
    font-weight: bold;
    margin: 5px 0;
}
.kpi .sub {
    font-size: 12px;
    color: #AAAAAA;
}
.block-container {
    padding: 1rem;
}
h1, h2, h3 {
    color: #FFFFFF !important;
}
.st-cc {
    background-color: #1A1A1A !important;
}
.metric-card {
    background: #1A1A1A;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    border: 1px solid #FF6F61;
    box-shadow: 0 0 10px rgba(255,111,97,0.3);
}
</style>
""", unsafe_allow_html=True)

# Título premium
st.title('🚀 Dashboard Operacional ALEXPRESS / ROCKET')
st.markdown('<hr style="border: 1px solid #00E5FF;">', unsafe_allow_html=True)

# Simulação de dados via CSV mockado
@st.cache_data
def load_data():
    np.random.seed(42)
    dates_april = pd.date_range(start='2025-04-01', end='2025-04-30', freq='D')
    dates_may = pd.date_range(start='2025-05-01', end='2025-05-31', freq='D')
    all_dates = list(dates_april) + list(dates_may)
    
    # Tipos de despesa
    tipos = ['Cartão', 'Imposto', 'Serviços', 'Folha', 'Manutenção', 'Alimentação', 'Transporte', 'IPVA']
    
    data = []
    for date in all_dates:
        num_expenses = np.random.randint(1, 5)
        for _ in range(num_expenses):
            tipo = np.random.choice(tipos, p=[0.2, 0.15, 0.15, 0.2, 0.1, 0.1, 0.05, 0.05])
            if tipo == 'IPVA':
                if np.random.rand() > 0.2:  # só aparece em alguns dias
                    continue
                valor = np.random.uniform(500, 2000)
                categoria = 'IPVA'
            else:
                if tipo == 'Cartão':
                    valor = np.random.uniform(50, 500)
                elif tipo == 'Imposto':
                    valor = np.random.uniform(200, 3000)
                elif tipo == 'Serviços':
                    valor = np.random.uniform(100, 1500)
                elif tipo == 'Folha':
                    valor = np.random.uniform(1000, 5000)
                elif tipo == 'Manutenção':
                    valor = np.random.uniform(100, 2000)
                elif tipo == 'Alimentação':
                    valor = np.random.uniform(10, 200)
                elif tipo == 'Transporte':
                    valor = np.random.uniform(20, 300)
                else:
                    valor = np.random.uniform(50, 1000)
                categoria = np.random.choice(['PF', 'PJ'], p=[0.6, 0.4])
            rec = np.random.choice([True, False], p=[0.3, 0.7])
            data.append({
                'Data': date,
                'Tipo': tipo,
                'Valor': round(valor, 2),
                'Categoria': categoria if tipo != 'IPVA' else 'IPVA',
                'Recorrente': 'Sim' if rec else 'Não',
                'Descrição': f'{tipo} - {np.random.choice(["Padrão", "Extra", "Urgente"])}'
            })
    
    df = pd.DataFrame(data)
    df['Mês'] = df['Data'].dt.month_name().str[:3]
    df['Dia'] = df['Data'].dt.day
    return df

df = load_data()

# Filtro de mês (Abril e Maio)
df_abril = df[df['Mês'] == 'Apr']
df_maio = df[df['Mês'] == 'May']

# KPIs Avançados (mês atual = Abril como padrão)
mes_atual = 'Abril'
df_mes = df_abril.copy()

total_pf_abril = round(df_mes[df_mes['Categoria'] == 'PF']['Valor'].sum(), 2)
total_pj_abril = round(df_mes[df_mes['Categoria'] == 'PJ']['Valor'].sum(), 2)
media_dia = round(df_mes['Valor'].mean(), 2)
maior_despesa = round(df_mes['Valor'].max(), 2)
top3_categorias = df_mes.groupby('Tipo')['Valor'].sum().nlargest(3).reset_index()
top3_str = ', '.join([f'{row.Tipo} (R${row.Valor:.0f})' for _, row in top3_categorias.iterrows()])
previsao_gastos = round(total_pf_abril + total_pj_abril + np.random.uniform(1000, 3000), 2)

# Layout de KPIs
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.markdown(f'<div class="kpi"><h3>Total PF (Abril)</h3><div class="value" style="color:#007BFF;">R$ {total_pf_abril:,.2f}</div><div class="sub">+12% vs Mar</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="kpi"><h3>Total PJ (Abril)</h3><div class="value" style="color:#FF3B30;">R$ {total_pj_abril:,.2f}</div><div class="sub">+8% vs Mar</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="kpi"><h3>Média por Dia</h3><div class="value" style="color:#00E5FF;">R$ {media_dia:,.2f}</div><div class="sub">Abril</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="kpi"><h3>Maior Despesa</h3><div class="value" style="color:#FF6F61;">R$ {maior_despesa:,.2f}</div><div class="sub">Individual</div></div>', unsafe_allow_html=True)
with col5:
    st.markdown(f'<div class="kpi"><h3>Top 3 Categorias</h3><div class="value" style="font-size:12px; color:#FFFFFF;">{top3_str}</div><div class="sub">Por valor total</div></div>', unsafe_allow_html=True)
with col6:
    st.markdown(f'<div class="kpi"><h3>Previsão Gastos Mês</h3><div class="value" style="color:#00E5FF;">R$ {previsao_gastos:,.2f}</div><div class="sub">Estimado</div></div>', unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #FF3B30;'>", unsafe_allow_html=True)

# Gráficos
col1, col2 = st.columns(2)

with col1:
    # Linha PF/PJ por dia (Abril)
    df_line = df_mes.groupby(['Dia', 'Categoria'])['Valor'].sum().reset_index()
    fig_line = px.line(df_line, x='Dia', y='Valor', color='Categoria',
                       title='Despesas PF e PJ por Dia - Abril',
                       color_discrete_map={'PF':'#007BFF','PJ':'#FF3B30'},
                       template='plotly_dark')
    fig_line.update_layout(paper_bgcolor='#0D0D0D', plot_bgcolor='#1A1A1A', font=dict(color='white'))
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    # Donut categorias (Abril)
    df_donut = df_mes.groupby('Tipo')['Valor'].sum().reset_index()
    fig_donut = px.pie(df_donut, values='Valor', names='Tipo', title='Distribuição por Tipo de Despesa',
                       hole=0.4, template='plotly_dark',
                       color_discrete_sequence=px.colors.sequential.Plasma)
    fig_donut.update_layout(paper_bgcolor='#0D0D0D', font=dict(color='white'))
    st.plotly_chart(fig_donut, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    # Barras top categorias
    top_cat = df_mes.groupby('Tipo')['Valor'].sum().nlargest(5).reset_index()
    fig_bar = px.bar(top_cat, x='Tipo', y='Valor', title='Top 5 Categorias - Abril',
                     template='plotly_dark', color='Valor', color_continuous_scale='Viridis')
    fig_bar.update_layout(paper_bgcolor='#0D0D0D', plot_bgcolor='#1A1A1A', font=dict(color='white'))
    st.plotly_chart(fig_bar, use_container_width=True)

with col4:
    # Gauge de previsão (gasto atual vs previsão)
    gasto_atual = total_pf_abril + total_pj_abril
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = gasto_atual,
        number = {'suffix': "", 'font': {'color': 'white'}},
        title = {'text': "Gasto Atual vs Previsão", 'font': {'color': 'white'}},
        delta = {'reference': previsao_gastos, 'increasing': {'color': "#FF3B30"}},
        gauge = {
            'axis': {'range': [None, previsao_gastos*1.2], 'tickcolor': "white"},
            'bar': {'color': "#00E5FF"},
            'bgcolor': "#1A1A1A",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, previsao_gastos*0.5], 'color': '#007BFF'},
                {'range': [previsao_gastos*0.5, previsao_gastos*1.0], 'color': '#FF6F61'},
                {'range': [previsao_gastos*1.0, previsao_gastos*1.2], 'color': '#FF3B30'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': previsao_gastos}}))
    fig_gauge.update_layout(paper_bgcolor='#0D0D0D', font=dict(color='white'))
    st.plotly_chart(fig_gauge, use_container_width=True)

# Painel IPVA separado
st.markdown('<h2 style="color:#FF6F61;">📊 Painel IPVA</h2>', unsafe_allow_html=True)

df_ipva = df_mes[df_mes['Tipo'] == 'IPVA']
if not df_ipva.empty:
    col1, col2 = st.columns(2)
    with col1:
        total_ipva = round(df_ipva['Valor'].sum(), 2)
        st.metric('Total IPVA Abril', f'R$ {total_ipva:,.2f}')
    with col2:
        # Distribuição IPVA por dia
        fig_ipva = px.bar(df_ipva, x='Dia', y='Valor', title='Distribuição IPVA por Dia',
                          template='plotly_dark', color='Valor', color_continuous_scale='Reds')
        fig_ipva.update_layout(paper_bgcolor='#0D0D0D', plot_bgcolor='#1A1A1A', font=dict(color='white'))
        st.plotly_chart(fig_ipva, use_container_width=True)
else:
    st.info('Nenhuma despesa IPVA em Abril.')

# Segmentação visual por tipo de despesa
st.markdown('<h2 style="color:#00E5FF;">📁 Segmentação por Tipo</h2>', unsafe_allow_html=True)
tipos_unicos = df_mes['Tipo'].unique()
for tipo in tipos_unicos:
    df_tipo = df_mes[df_mes['Tipo'] == tipo]
    total_tipo = round(df_tipo['Valor'].sum(), 2)
    rec_count = df_tipo[df_tipo['Recorrente'] == 'Sim'].shape[0]
    st.markdown(f'<div class="card"><h3>{tipo}</h3><p style="color:#FFFFFF;">Total: R$ {total_tipo:,.2f} | Recorrentes: {rec_count}</p></div>', unsafe_allow_html=True)

# Destaque de despesas recorrentes
st.markdown('<h2 style="color:#FF6F61;">🔁 Despesas Recorrentes</h2>', unsafe_allow_html=True)
df_rec = df_mes[df_mes['Recorrente'] == 'Sim']
if not df_rec.empty:
    st.dataframe(df_rec[['Data', 'Descrição', 'Tipo', 'Valor', 'Categoria']].style.set_properties(**{'background-color': '#1A1A1A', 'color': 'white'}))
else:
    st.info('Nenhuma despesa recorrente cadastrada.')

# Nota
st.markdown('<hr style="border: 1px solid #00E5FF;">', unsafe_allow_html=True)
st.caption('Dashboard premium ALEXPRESS/ROCKET - Dados mockados para demonstração')
