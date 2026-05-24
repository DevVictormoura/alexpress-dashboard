import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="ALEXPRESS / ROCKET", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for neon dark blue theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Exo+2:wght@300;500&display=swap');
    
    body, .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #141b3a 50%, #1a243f 100%);
        color: #e0e0ff;
        font-family: 'Exo 2', sans-serif;
    }
    .main-header {
        text-align: center;
        padding: 0.2rem 0;
        border-bottom: 1px solid #00e5ff;
        box-shadow: 0 0 20px rgba(0,229,255,0.3);
        margin-bottom: 0.5rem;
    }
    .main-header h1 {
        color: #00e5ff;
        font-family: 'Orbitron', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        text-shadow: 0 0 15px #00e5ff;
        letter-spacing: 3px;
        margin: 0;
    }
    .main-header p {
        color: #7a8ba8;
        font-size: 0.9rem;
        margin: 0;
        letter-spacing: 5px;
    }
    .kpi-card {
        background: rgba(10, 14, 39, 0.8);
        border: 1px solid #00e5ff;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 0 20px rgba(0,229,255,0.2), inset 0 0 20px rgba(0,229,255,0.05);
        backdrop-filter: blur(5px);
        margin: 5px;
    }
    .kpi-card h2 {
        color: #00e5ff;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        margin: 0;
        text-shadow: 0 0 10px #00e5ff;
    }
    .kpi-card p {
        color: #8899bb;
        font-size: 0.8rem;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .section-card {
        background: rgba(10, 14, 39, 0.7);
        border: 1px solid #00e5ff;
        border-radius: 12px;
        padding: 15px;
        margin: 5px 0;
        box-shadow: 0 0 15px rgba(0,229,255,0.15);
    }
    .section-card h3 {
        color: #00e5ff;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2rem;
        margin: 0 0 8px 0;
        border-bottom: 1px solid rgba(0,229,255,0.3);
        padding-bottom: 5px;
    }
    .stTable {
        background: transparent !important;
    }
    .stTable table {
        background: rgba(10, 14, 39, 0.6) !important;
        border-collapse: collapse;
        width: 100%;
        color: #c8d4e6 !important;
        font-size: 0.8rem;
    }
    .stTable th {
        background: #0a0e27 !important;
        color: #00e5ff !important;
        font-family: 'Exo 2', sans-serif;
        font-weight: 500;
        border-bottom: 2px solid #00e5ff;
        text-align: center;
    }
    .stTable td {
        background: rgba(20, 27, 58, 0.5) !important;
        border: 1px solid rgba(0,229,255,0.1);
        text-align: center;
        padding: 4px 8px;
    }
    .stPlotlyChart {
        background: transparent !important;
    }
    .main > div:first-child {
        padding-top: 0;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>ALEXPRESS / ROCKET</h1>
    <p>• DASHBOARD DE MONITORAMENTO •</p>
</div>
""", unsafe_allow_html=True)

# KPI Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="kpi-card">
        <h2>R$ 1.2M</h2>
        <p>Faturamento</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="kpi-card">
        <h2>8.5K</h2>
        <p>Pedidos</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="kpi-card">
        <h2>94.2%</h2>
        <p>Entregas no Prazo</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="kpi-card">
        <h2>R$ 142</h2>
        <p>Ticket Médio</p>
    </div>
    """, unsafe_allow_html=True)

# Charts and Data Section
row2_cols = st.columns([2, 1])
with row2_cols[0]:
    st.markdown("""<div class="section-card"><h3>📊 Vendas ao Longo do Tempo</h3>""", unsafe_allow_html=True)
    # Sample data
    df_time = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=12, freq='M'),
        'Sales': [120, 135, 150, 170, 160, 190, 210, 195, 220, 240, 230, 260]
    })
    fig1 = px.line(df_time, x='Date', y='Sales', title=None)
    fig1.update_traces(line_color='#00e5ff', line_width=2)
    fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                       font_color='#8899bb', margin=dict(l=10,r=10,t=10,b=10))
    fig1.update_xaxes(gridcolor='rgba(0,229,255,0.1)', tickformat='%b', showgrid=False)
    fig1.update_yaxes(gridcolor='rgba(0,229,255,0.1)', showgrid=True)
    st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})
    st.markdown("</div>", unsafe_allow_html=True)

with row2_cols[1]:
    st.markdown("""<div class="section-card"><h3>📦 Top Produtos</h3>""", unsafe_allow_html=True)
    df_prod = pd.DataFrame({
        'Produto': ['Eletrônicos', 'Roupas', 'Livros', 'Casa', 'Esporte'],
        'Quantidade': [320, 280, 210, 170, 130]
    })
    fig2 = px.bar(df_prod, x='Quantidade', y='Produto', orientation='h', title=None)
    fig2.update_traces(marker_color='#00e5ff', opacity=0.7)
    fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                       font_color='#8899bb', margin=dict(l=10,r=10,t=10,b=10), height=200)
    fig2.update_xaxes(gridcolor='rgba(0,229,255,0.1)', showgrid=False)
    fig2.update_yaxes(gridcolor='rgba(0,229,255,0.1)', showgrid=False)
    st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})
    st.markdown("</div>", unsafe_allow_html=True)

# Bottom row: Table and another chart
row3_cols = st.columns([1, 1])
with row3_cols[0]:
    st.markdown("""<div class="section-card"><h3>📋 Últimos Pedidos</h3>""", unsafe_allow_html=True)
    df_orders = pd.DataFrame({
        'Pedido': ['#001', '#002', '#003', '#004', '#005'],
        'Cliente': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas'],
        'Valor': [250.00, 320.50, 189.90, 450.00, 275.80],
        'Status': ['Entregue', 'Em trânsito', 'Preparando', 'Entregue', 'Cancelado']
    })
    # Custom styling for table
    styled_df = df_orders.style.set_table_styles(
        [{'selector': 'th', 'props': [('color', '#00e5ff'), ('background', '#0a0e27'), ('border-bottom', '2px solid #00e5ff')]},
         {'selector': 'td', 'props': [('color', '#c8d4e6'), ('background', 'rgba(20,27,58,0.5)'), ('border', '1px solid rgba(0,229,255,0.1)')]},
         {'selector': 'tr:hover td', 'props': [('background', 'rgba(0,229,255,0.1)')]}]
    )
    st.dataframe(styled_df, use_container_width=True, height=200)
    st.markdown("</div>", unsafe_allow_html=True)

with row3_cols[1]:
    st.markdown("""<div class="section-card"><h3>📍 Entregas por Região</h3>""", unsafe_allow_html=True)
    df_reg = pd.DataFrame({
        'Região': ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste', 'Norte'],
        'Entregas': [450, 320, 280, 190, 110]
    })
    fig3 = px.pie(df_reg, values='Entregas', names='Região', title=None)
    fig3.update_traces(marker=dict(colors=['#00e5ff', '#2a6f97', '#3a7ca5', '#4a8bb5', '#5a9ac5']),
                       textfont_color='#c8d4e6', textinfo='label+percent')
    fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                       font_color='#8899bb', margin=dict(l=10,r=10,t=10,b=10), height=220)
    st.plotly_chart(fig3, use_container_width=True, config={'displayModeBar': False})
    st.markdown("</div>", unsafe_allow_html=True)

# Footer note
st.markdown("""
<div style="text-align:center; font-size:0.7rem; color:#4a5a7a; padding:10px 0; border-top:1px solid rgba(0,229,255,0.2); margin-top:10px;">
    ALEXPRESS / ROCKET • Dashboard v1.0 • Todos os direitos reservados
</div>
""", unsafe_allow_html=True)

