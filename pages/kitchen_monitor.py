import streamlit as st
import random
import time

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
Sistema inteligente de monitoreo de cocina en tiempo real.
""")

# ===== TEMPERATURA SIMULADA =====
temperatura = random.randint(20, 100)

# ===== TARJETAS =====
col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">
    <h3>🌡️ Temperatura Actual</h3>
    </div>
    """, unsafe_allow_html=True)

    st.metric(
        label="Temperatura",
        value=f"{temperatura} °C"
    )

with col2:

    st.markdown("""
    <div class="card">
    <h3>📊 Nivel de Calor</h3>
    </div>
    """, unsafe_allow_html=True)

    st.progress(temperatura)

# ===== ALERTAS =====
st.markdown("""
<div class="card">
<h3>🚨 Estado de la Cocina</h3>
</div>
""", unsafe_allow_html=True)

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
st.markdown("""
<div class="card">
<h3>📡 Sensores Inteligentes</h3>
</div>
""", unsafe_allow_html=True)

sensor1, sensor2, sensor3 = st.columns(3)

with sensor1:
    st.info("ESP32 conectado")

with sensor2:
    st.info("Sensor de temperatura activo")

with sensor3:
    st.info("Sistema SmartKitchen operativo")

# ===== HISTORIAL =====
st.markdown("""
<div class="card">
<h3>📈 Historial de Temperatura</h3>
</div>
""", unsafe_allow_html=True)

datos = [random.randint(20, 100) for _ in range(15)]

st.line_chart(datos)

# ===== AUTO REFRESH =====
time.sleep(2)
st.rerun()
