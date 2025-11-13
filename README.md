E-Commerce Analytics: Segmentación RFM + Predicción de Churn + Dashboard en Streamlit

Autor: insightiqx

Este proyecto es un pipeline completo de analítica avanzada aplicado a datos de e-commerce:
incluye ETL, EDA, Segmentación RFM, Machine Learning para churn, feature engineering, y un dashboard interactivo profesional en Streamlit.

Es ideal como proyecto de portfolio para roles de Data Analyst, Data Scientist, Machine Learning Engineer o Business Analytics.

Características principales
1. ETL + Limpieza de datos

Carga del dataset Superstore.

Manejo de nulos, tipos de datos, outliers.

Cálculo de precio total por pedido.

Conversión y normalización de fechas.

Exportación en formato Parquet.

2. Análisis Exploratorio (EDA)

Ventas por mes, región, categoría y segmento.

Ticket medio y KPIs comerciales.

Identificación de productos top por ventas y unidades.

3. Segmentación RFM

Se calcula para cada cliente:

Recency – días desde la última compra

Frequency – número de pedidos

Monetary – gasto total acumulado

Aplicación de K-Means para obtener segmentos de cliente:

🟢 High Value

🟠 Mid Value

🔵 Low Value

🔴 At Risk

4. Modelo de Predicción de Churn

Incluye:

✔ Feature engineering (ventas últimos 30/90/180 días, descuentos, AOV…)
✔ Variables de segmento, región y RFM
✔ Entrenamiento con Random Forest
✔ Optimización de threshold con curva ROC
✔ Exportación del modelo final

Métricas principales: ROC-AUC, accuracy, recall, matriz de confusión.

5. Dashboard Interactivo (Streamlit)

Incluye:

KPIs principales de negocio

Ventas temporales

Ventas por región y segmento

Ranking de churn

Tabla interactiva de clientes con mayor riesgo

Ejecutable localmente con:

streamlit run dashboard/app.py

Estructura del Proyecto
ecommerce-rfm-ml/
│
├── data/
│   ├── raw/               # dataset original
│   └── processed/         # datos limpios + resultados para dashboard
│
├── notebooks/
│   ├── 01_eda.ipynb       # ETL + Exploratory Data Analysis
│   ├── 02_rfm.ipynb       # Segmentación RFM + K-Means
│   ├── 03_churn.ipynb     # Entrenamiento del modelo
│   └── 04_dashboard_preparation.ipynb
│
├── dashboard/
│   └── app.py             # Streamlit dashboard
│
├── models/                # modelos exportados (.pkl)
│
├── src/                   # scripts auxiliares
│
├── .gitignore
├── requirements.txt
└── README.md

Cómo ejecutar el proyecto
1. Clonar el repositorio
git clone https://github.com/insightiqx/ecommerce-rfm-ml.git
cd ecommerce-rfm-ml

2. Crear entorno virtual
python -m venv .venv
.\.venv\Scripts\activate   # Windows

3. Instalar dependencias
pip install -r requirements.txt

4. Ejecutar el dashboard
streamlit run dashboard/app.py

Capturas del Dashboard (opcional)

Puedes añadir imágenes con:

![Dashboard](images/dashboard_main.png)


Si quieres, las generamos juntos.

Mejoras futuras

Filtros dinámicos por Segmento y Región

Exportación de clientes a Excel desde Streamlit

Explicabilidad del modelo con SHAP

Versión web desplegada en Streamlit Cloud

Contacto

GitHub: https://github.com/insightiqx
