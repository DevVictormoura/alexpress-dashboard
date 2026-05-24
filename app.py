import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Dashboard ALEXPRESS/ROCKET", layout="wide", page_icon="🚀")

st.markdown("""
<style>
/* Fundo geral */
body, .stApp {
    background-color: #050A0F !important;
    color: #E6F1FF !important;
    font-family: 'Segoe UI', sans-serif;
}

/* Containers */
.block-container {
    padding: 2rem 2.5rem;
}

/* Divisores neon */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, #00E5FF, #007BFF, #00E5FF);
    margin: 25px 0;
}

/* Sidebar */
.css-1d391kg, .css-1lcbmhc {
    background: #07131B !important;
    border-right: 2px solid rgba(0,229,255,0.4);
}

/* Títulos */
h1, h2, h3 {
    color: #E6F1FF !important;
    text-shadow: 0px 0px 15px rgba(0,229,255,0.7);
}

/* Cards Premium */
.card {
    background: rgba(10, 20, 30, 0.7);
    border-radius: 14px;
    padding: 20px;
    margin: 12px 0;
    border: 1px solid rgba(0,229,255,0.5);
    box-shadow: 
        0 0 15px rgba(0,229,255,0.25),
        inset 0 0 10px rgba(0,229,255,0.2);
}

/* KPI Cards */
.kpi {
    background: rgba(15, 25, 35, 0.75);
    border-radius: 14px;
    padding: 15px;
    text-align: center;
    border: 1px solid rgba(0,229,255,0.7);
    box-shadow: 0 0 15px rgba(0,229,255,0.35);
}
.kpi h3 {
    color: #00E5FF;
    font-size: 14px;
    margin: 0;
}
.kpi .value {
    font-size: 30px;
    font-weight: bold;
    margin-top: 10px;
    color: #E6F1FF;
    text-shadow: 0px 0px 15px rgba(0,229,255,0.6);
}
.kpi .sub {
    font-size: 12px;
    color: #8FAFCF;
}

/* DataFrame dark premium */
.dataframe {
    color: #E6F1FF !important;
}

/* Inputs / Selects */
.stSelectbox, .stTextInput, .stNumberInput {
    background-color: rgba(10, 20, 30, 0.6) !important;
    color: #E6F1FF !important;
}

/* Plotly background fix */
.js-plotly-plot {
    background-color: transparent !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Dashboard Operacional ALEXPRESS / ROCKET")
st.markdown("<hr>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    np.random.seed(42)
    dates_april = pd.date_range(start="2025-04-01", end="2025-04-30", freq="D")
    dates_may = pd.date_range(start="2025-05-01", end="2025-05-31", freq="D")
    all_dates = list(dates_april) + list(dates_may)

    tipos = ["Cartão", "Imposto", "Serviços", "Folha", "Manutenção", "Alimentação", "Transporte", "IPVA"]
    data = []

    for date in all_dates:
        num_expenses = np.random.randint(1, 5)
        for _ in range(num_expenses):
            tipo = np.random.choice(tipos, p=[0.2, 0.15, 0.15, 0.2, 0.1, 0.1, 0.05, 0.05])
            if tipo == "IPVA":
                if np.random.rand() > 0.2:
                    continue
                valor = np.random.uniform(500, 2000)
                categoria = "IPVA"
            else:
                if tipo == "Cartão": valor = np.random.uniform(50, 500)
                elif tipo == "Imposto": valor = np.random.uniform(200, 3000)
                elif tipo == "Serviços": valor = np.random.uniform(100, 1500)
                elif tipo == "Folha": valor = np.random.uniform(1000, 5000)
                elif tipo == "Manutenção": valor = np.random.uniform(100, 2000)
                elif tipo == "Alimentação": valor = np.random.uniform(10, 200)
                elif tipo == "Transporte": valor = np.random.uniform(20, 300)
                else: valor = np.random.uniform(50, 1000)
                categoria = np.random.choice(["PF", "PJ"], p=[0.6, 0.4])

            rec = np.random.choice([True, False], p=[0.3, 0.7])
            data.append({
                "Data": date,
                "Tipo": tipo,
                "Valor": round(valor, 2),
                "Categoria": categoria,
                "Recorrente": "Sim" if rec else "Não",
                "Descrição": f"{tipo} - {np.random.choice(['Padrão', 'Extra', 'Urgente'])}"
            })

    df = pd.DataFrame(data)
    df["Mês"] = df["Data"].dt.month_name().str[:3]
    df["Dia"] = df["Data"].dt.day
    return df


df = load_data()

df_abril = df[df["Mês"] == "Apr"]
df_maio = df[df["Mês"] == "May"]

mes_atual = "Abril"
df_mes = df_abril.copy()

total_pf_abril = round(df_mes[df_mes["Categoria"] == "PF"]["Valor"].sum(), 2)
total_pj_abril = round(df_mes[df_mes["Categoria"] == "PJ"]["Valor"].sum(), 2)
media_dia = round(df_mes["Valor"].mean(), 2)
maior_despesa = round(df_mes["Valor"].max(), 2)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="kpi"><h3>Total PF</h3><div class="value">R$ {total_pf_abril:,.2f}</div><div class="sub">Abril</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="kpi"><h3>Total PJ</h3><div class="value">R$ {total_pj_abril:,.2f}</div><div class="sub">Abril</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="kpi"><h3>Média Diária</h3><div class="value">R$ {media_dia:,.2f}</div><div class="sub">Abril</div></div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    df_line = df_mes.groupby(["Dia", "Categoria"])["Valor"].sum().reset_index()
    fig_line = px.line(df_line, x="Dia", y="Valor", color="Categoria", template="plotly_dark")
    fig_line.update_layout(paper_bgcolor="#050A0F", plot_bgcolor="#07131B", font=dict(color="white"))
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    df_donut = df_mes.groupby("Tipo")["Valor"].sum().reset_index()
    fig_donut = px.pie(df_donut, values="Valor", names="Tipo", hole=0.5, template="plotly_dark")
    fig_donut.update_layout(paper_bgcolor="#050A0F", font=dict(color="white"))
    st.plotly_chart(fig_donut, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<h2>📊 Painel IPVA</h2>", unsafe_allow_html=True)
df_ipva = df_mes[df_mes["Tipo"] == "IPVA"]

if not df_ipva.empty:
    col1, col2 = st.columns(2)
    with col1:
        total_ipva = round(df_ipva["Valor"].sum(), 2)
        st.metric("Total IPVA Abril", f"R$ {total_ipva:,.2f}")
    with col2:
        fig_ipva = px.bar(df_ipva, x="Dia", y="Valor", template="plotly_dark")
        fig_ipva.update_layout(paper_bgcolor="#050A0F", plot_bgcolor="#07131B", font=dict(color="white"))
        st.plotly_chart(fig_ipva, use_container_width=True)
else:
    st.info("Nenhuma despesa IPVA em Abril.")
