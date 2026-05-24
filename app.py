import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide', page_title='Neon Cyberpunk Dashboard', page_icon='\U0001f52e')

st.markdown('''
<style>
    .stApp { background: #0a0a2e; }
    .css-18e3th9 { padding: 0 !important; }
    .css-1d391kg { padding: 0 !important; }
    .main .block-container { padding: 0.5rem !important; }
    .kpi-card {
        background: linear-gradient(135deg, #0d0d4a, #1a1a6e);
        border: 1px solid #00ffff;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        box-shadow: 0 0 15px #00ffff33;
    }
    .kpi-value { font-size: 1.8em; font-weight: bold; color: #00ffff; }
    .kpi-label { font-size: 0.8em; color: #88ffff; }
    .chart-container {
        background: #0d0d4a;
        border: 1px solid #00ffff;
        border-radius: 8px;
        padding: 5px;
        box-shadow: 0 0 10px #00ffff33;
    }
    .table-container {
        background: #0d0d4a;
        border: 1px solid #00ffff;
        border-radius: 8px;
        padding: 5px;
        max-height: 300px;
        overflow-y: auto;
        box-shadow: 0 0 10px #00ffff33;
    }
    .stDataFrame { width: 100%; }
    .stDataFrame thead tr th { background: #1a1a6e !important; color: #00ffff !important; }
    .stDataFrame tbody tr:nth-child(even) { background: #0d0d4a; }
    .stDataFrame tbody tr:nth-child(odd) { background: #0a0a3e; }
    .stDataFrame tbody td { color: #ccffff; font-size: 0.9em; }
    h1, h2, h3, h4, h5, h6 { color: #00ffff !important; }
    .st-bb { color: #00ffff; }
    .st-at { color: #00ffff; }
</style>
''', unsafe_allow_html=True)

np.random.seed(42)
n = 100
dates = pd.date_range(start='2024-01-01', periods=n, freq='D')
fleet = np.random.randint(50, 200, size=n)
maintenance_cost = np.random.uniform(1000, 5000, size=n)
fuel_cost = np.random.uniform(500, 3000, size=n)
billing = np.random.uniform(5000, 20000, size=n)
efficiency = np.random.uniform(70, 100, size=n)
utilization = np.random.uniform(60, 95, size=n)

df = pd.DataFrame({
    'Date': dates,
    'Fleet Size': fleet,
    'Maintenance Cost': maintenance_cost,
    'Fuel Cost': fuel_cost,
    'Billing': billing,
    'Efficiency (%)': efficiency,
    'Utilization (%)': utilization
})

kpi1 = f'${df["Billing"].sum():,.0f}'
kpi2 = f'{df["Fleet Size"].mean():.0f}'
kpi3 = f'${df["Maintenance Cost"].mean():,.0f}'
kpi4 = f'${df["Fuel Cost"].mean():,.0f}'
kpi5 = f'{df["Efficiency (%)"].mean():.1f}%'
kpi6 = f'{df["Utilization (%)"].mean():.1f}%'

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.markdown(f'<div class="kpi-card"><div class="kpi-value">{kpi1}</div><div class="kpi-label">Total Billing</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="kpi-card"><div class="kpi-value">{kpi2}</div><div class="kpi-label">Avg Fleet Size</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="kpi-card"><div class="kpi-value">{kpi3}</div><div class="kpi-label">Avg Maintenance</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="kpi-card"><div class="kpi-value">{kpi4}</div><div class="kpi-label">Avg Fuel Cost</div></div>', unsafe_allow_html=True)
with col5:
    st.markdown(f'<div class="kpi-card"><div class="kpi-value">{kpi5}</div><div class="kpi-label">Efficiency</div></div>', unsafe_allow_html=True)
with col6:
    st.markdown(f'<div class="kpi-card"><div class="kpi-value">{kpi6}</div><div class="kpi-label">Utilization</div></div>', unsafe_allow_html=True)

st.markdown('## \U0001f4ca Operational Overview')
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    fig1 = px.line(df, x='Date', y='Fleet Size', title='Fleet Size Over Time', template='plotly_dark')
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#00ffff', title_font_color='#00ffff', height=250, margin=dict(l=20, r=20, t=30, b=20))
    fig1.update_traces(line_color='#00ffff')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.area(df, x='Date', y='Billing', title='Billing Revenue', template='plotly_dark')
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#00ffff', title_font_color='#00ffff', height=250, margin=dict(l=20, r=20, t=30, b=20))
    fig2.update_traces(fillcolor='rgba(0,255,255,0.2)', line_color='#00ffff')
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    fig3 = px.bar(df, x='Date', y='Maintenance Cost', title='Maintenance Cost', template='plotly_dark')
    fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#00ffff', title_font_color='#00ffff', height=250, margin=dict(l=20, r=20, t=30, b=20))
    fig3.update_traces(marker_color='#00ffff')
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.scatter(df, x='Fuel Cost', y='Efficiency (%)', size='Utilization (%)', title='Fuel vs Efficiency', template='plotly_dark')
    fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#00ffff', title_font_color='#00ffff', height=250, margin=dict(l=20, r=20, t=30, b=20))
    fig4.update_traces(marker=dict(color='#00ffff', line=dict(color='#00ffff', width=1)))
    st.plotly_chart(fig4, use_container_width=True)

st.markdown('## \U0001f4cb Detailed Data')
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.dataframe(df[['Date', 'Fleet Size', 'Maintenance Cost', 'Fuel Cost']].head(10))
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.dataframe(df[['Date', 'Billing', 'Efficiency (%)', 'Utilization (%)']].head(10))
    st.markdown('</div>', unsafe_allow_html=True)
