import streamlit as st
import pandas as pd
import json
import plotly.express as px

# ===========================================
# Cargar datos procesados
# ===========================================

@st.cache_data
def load_data():
    df_sales_month = pd.read_parquet("../data/processed/dashboard_sales_by_month.parquet")
    df_sales_region = pd.read_parquet("../data/processed/dashboard_sales_by_region.parquet")
    df_sales_segment = pd.read_parquet("../data/processed/dashboard_sales_by_segment.parquet")
    df_churn_region = pd.read_parquet("../data/processed/dashboard_churn_by_region.parquet")
    df_customers = pd.read_parquet("../data/processed/model_df_fe.parquet")

    with open("../data/processed/dashboard_kpis_numeric.json", encoding="utf-8") as f:
        kpis_num = json.load(f)

    with open("../data/processed/dashboard_kpis_formatted.json", encoding="utf-8") as f:
        kpis_fmt = json.load(f)

    return df_sales_month, df_sales_region, df_sales_segment, df_churn_region, df_customers, kpis_num, kpis_fmt


(
    df_sales_month,
    df_sales_region,
    df_sales_segment,
    df_churn_region,
    df_customers,
    kpis_num,
    kpis_fmt,
) = load_data()


# ===========================================
# CONFIGURACIÓN GENERAL
# ===========================================

st.set_page_config(
    page_title="E-Commerce Customer Analytics",
    layout="wide"
)

st.title("E-Commerce Analytics Dashboard")
st.markdown("### Ventas · Segmentos RFM · Predicción de Churn")


# ===========================================
# SECCIÓN 1 – KPI CARDS
# ===========================================

st.write("## KPIs Principales")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Clientes Totales", kpis_fmt["total_customers"])
col2.metric("Ventas Totales", kpis_fmt["total_sales"])
col3.metric("Ticket Medio", kpis_fmt["avg_ticket"])
col4.metric("Churn Rate", kpis_fmt["churn_rate"])
col5.metric("Prob. Churn Promedio", kpis_fmt["avg_proba_churn"])


# ===========================================
# SECCIÓN 2 – Ventas Mensuales
# ===========================================

st.write("## Ventas por Mes")

fig_month = px.line(
    df_sales_month,
    x="Order Date",
    y="sales",
    markers=True,
    title="Evolución Mensual de Ventas"
)

st.plotly_chart(fig_month, use_container_width=True)


# ===========================================
# SECCIÓN 3 – Ventas por Región y Segmento
# ===========================================

colA, colB = st.columns(2)

with colA:
    st.write("### Ventas por Región")
    fig_region = px.bar(
        df_sales_region,
        x="Region",
        y="sales",
        text="sales_fmt",
        title="Ventas por Región",
    )
    fig_region.update_traces(textposition="outside")
    st.plotly_chart(fig_region, use_container_width=True)

with colB:
    st.write("### Ventas por Segmento")
    fig_segment = px.bar(
        df_sales_segment,
        x="Segment",
        y="sales",
        text="sales_fmt",
        title="Ventas por Segmento",
    )
    fig_segment.update_traces(textposition="outside")
    st.plotly_chart(fig_segment, use_container_width=True)


# ===========================================
# SECCIÓN 4 – Churn por Región
# ===========================================

st.write("## Churn por Región")

fig_churn_region = px.bar(
    df_churn_region,
    x="Region",
    y="churn_rate",
    title="Tasa de Churn por Región",
    text=df_churn_region["churn_rate"].apply(lambda x: f"{round(x*100,1)}%"),
)

fig_churn_region.update_traces(textposition="outside")
st.plotly_chart(fig_churn_region, use_container_width=True)


# ===========================================
# SECCIÓN 5 – Clientes con Mayor Probabilidad de Churn
# ===========================================

st.write("## Top Clientes con Mayor Riesgo de Churn")

top_n = st.slider("Selecciona cuántos clientes mostrar:", 5, 50, 10)

# Reconstruir columna Segment_main si solo tenemos dummies
if "Segment_main" not in df_customers.columns:
    segment_dummy_cols = [c for c in df_customers.columns if c.startswith("Segment_main_")]
    if segment_dummy_cols:
        df_customers["Segment_main"] = (
            df_customers[segment_dummy_cols]
            .idxmax(axis=1)
            .str.replace("Segment_main_", "", regex=False)
        )
    else:
        df_customers["Segment_main"] = "Desconocido"

# Seleccionar columnas necesarias
df_top_churn = df_customers[["Customer ID", "proba_churn", "Segment_main"]].copy()

# ORDENAR ANTES de recortar
df_top_churn = df_top_churn.sort_values(by="proba_churn", ascending=False)

# Recortar según el slider
df_top_churn = df_top_churn.head(top_n)

# Convertir probabilidad a %
df_top_churn["Prob. Churn (%)"] = (df_top_churn["proba_churn"] * 100).round(1).astype(str) + " %"

# Mostrar tabla
st.dataframe(
    df_top_churn[["Customer ID", "Segment_main", "Prob. Churn (%)"]],
    hide_index=True
)

# ===========================================
# FOOTER
# ===========================================

st.markdown("---")
st.markdown("Dashboard generado automáticamente para análisis E-Commerce + Churn Prediction.")