import streamlit as st

st.set_page_config(
    page_title="Monitor Inteligente",
    page_icon="🔥",
    layout="wide"
)

# ===== ESTILOS =====
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #0f172a, #1e293b);
    color: white;
}

.card {
    background-color: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

h1, h2, h3 {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ===== TITULO =====
st.title("🔥 SmartKitchen Monitor")

st.markdown("""
Sistema inteligente de monitoreo de cocina.
""")

# ===== ENTRADA MANUAL =====
st.subheader("🌡️ Temperatura de Wokwi")

temperatura = st.slider(
    "Selecciona la temperatura actual",
    0,
    100,
    25
)

# ===== TARJETAS =====
col1, col2 = st.columns(2)

with col1:

    st.metric(
        label="🌡️ Temperatura Actual",
        value=f"{temperatura} °C"
    )

with col2:

    st.metric(
        label="📊 Nivel de Calor",
        value=f"{temperatura}%"
    )

# ===== BARRA =====
st.progress(temperatura)

# ===== ALERTAS =====
st.subheader("🚨 Estado de la Cocina")

if temperatura < 50:

    st.success("✅ Cocina estable")

    st.write("🟢 LED apagado")
    st.write("🔇 Buzzer desactivado")

elif temperatura < 80:

    st.warning("⚠️ Temperatura elevada")

    st.write("🟠 LED activo")
    st.write("🔊 Buzzer en espera")

else:

    st.error("🔥 PELIGRO DE SOBRECALENTAMIENTO")

    st.write("🔴 LED encendido")
    st.write("🚨 Buzzer activado")

# ===== SENSORES =====
st.subheader("📡 Sensores Inteligentes")

col3, col4, col5 = st.columns(3)

with col3:
    st.info("ESP32 conectado")

with col4:
    st.info("Sensor de temperatura activo")

with col5:
    st.info("Sistema SmartKitchen operativo")

# ===== HISTORIAL =====
st.subheader("📈 Historial de Temperatura")

datos = [
    temperatura - 10,
    temperatura - 5,
    temperatura,
    temperatura + 3
]

st.line_chart(datos)
