import streamlit as st
import paho.mqtt.client as mqtt
import json
import time

# ── CONFIGURACIÓN INICIAL ────────────────────────────────
st.set_page_config(
    page_title="Monitoreo Wokwi",
    page_icon="🌡️",
    layout="wide"
)

# ── ESTÉTICA VISUAL ──────────────────────────────────────
st.markdown("""
<style>

/* FONDO GENERAL */
.stApp {
    background: linear-gradient(to bottom right, #dbeafe, #93c5fd);
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #dbeafe;
}

/* TITULOS */
h1, h2, h3 {
    color: #1E3A8A !important;
    font-family: 'Trebuchet MS', sans-serif;
}

/* TEXTOS */
p, span, label {
    color: #1E3A8A !important;
}

/* HERO */
.hero {
    background: linear-gradient(to right, #60A5FA, #3B82F6);
    padding: 40px;
    border-radius: 30px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.2);
}

.hero-title {
    color: white;
    font-size: 50px;
    font-weight: bold;
    margin-bottom: 10px;
}

.hero-text {
    color: white;
    font-size: 20px;
}

/* TARJETAS */
.card {
    background-color: rgba(255,255,255,0.80);
    padding: 25px;
    border-radius: 25px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
}

/* MÉTRICAS */
[data-testid="stMetric"] {
    background-color: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 25px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
}

/* BOTONES */
div.stButton > button {
    background-color: #3B82F6 !important;
    color: white !important;
    border-radius: 20px !important;
    border: none !important;
    width: 100%;
    font-weight: bold;
    transition: 0.3s;
    height: 55px;
}

div.stButton > button:hover {
    background-color: #1D4ED8 !important;
    transform: scale(1.02);
}

/* ALERTAS */
.stAlert {
    border-radius: 20px;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #1E3A8A;
    margin-top: 40px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ── HERO ────────────────────────────────────────────────
st.markdown("""
<div class="hero">

    <div class="hero-title">
        🌡️💧 Monitor Inteligente
    </div>

    <div class="hero-text">
        Visualiza los sensores de SmartKitchen en tiempo real desde Wokwi 💙
    </div>

</div>
""", unsafe_allow_html=True)

# ── DESCRIPCIÓN ──────────────────────────────────────────
st.markdown("""
<div class="card">

<h3>👩‍🍳 Panel de Monitoreo Inteligente</h3>

<p>
Esta sección permite visualizar la temperatura y humedad de la cocina inteligente
simulada en Wokwi en tiempo real ✨
</p>

</div>
""", unsafe_allow_html=True)

# 📡 Datos MQTT
BROKER = "broker.mqttdashboard.com"
PORT = 1883
TOPIC = "manuela_vallejo/smartkitchen"

# Estados iniciales
if "temperatura" not in st.session_state:
    st.session_state["temperatura"] = "Esperando..."

if "humedad" not in st.session_state:
    st.session_state["humedad"] = "Esperando..."

# Callback MQTT
def mensaje_recibido(client, userdata, msg):

    try:

        payload = msg.payload.decode("utf-8")

        datos = json.loads(payload)

        if "Temp" in datos and "Hum" in datos:

            st.session_state["temperatura"] = f"{datos['Temp']} °C"
            st.session_state["humedad"] = f"{datos['Hum']} %"

    except Exception:
        pass

# ── MÉTRICAS ────────────────────────────────────────────
c1, c2 = st.columns(2)

with c1:

    st.metric(
        label="🌡️ Temperatura Horno",
        value=st.session_state["temperatura"]
    )

with c2:

    st.metric(
        label="💧 Humedad Ambiente",
        value=st.session_state["humedad"]
    )

st.write("")

# ── BOTÓN ACTUALIZAR ────────────────────────────────────
if st.button(
    "🔄 Actualizar Lecturas de Wokwi",
    type="primary",
    use_container_width=True
):

    with st.spinner("📡 Conectando con Wokwi..."):

        st.session_state["temperatura"] = "Esperando..."
        st.session_state["humedad"] = "Esperando..."

        try:

            api_version = mqtt.CallbackAPIVersion.VERSION1

            cliente = mqtt.Client(
                callback_api_version=api_version
            )

        except AttributeError:

            cliente = mqtt.Client()

        cliente.on_message = mensaje_recibido

        try:

            cliente.connect(BROKER, PORT, 60)

            cliente.subscribe(TOPIC)

            intentos = 0

            while intentos < 30:

                cliente.loop(timeout=0.2)

                if st.session_state["temperatura"] != "Esperando...":
                    break

                time.sleep(0.2)

                intentos += 1

            cliente.disconnect()

            if st.session_state["temperatura"] != "Esperando...":

                st.toast(
                    "¡Datos sincronizados desde Wokwi!",
                    icon="📡"
                )

            else:

                st.warning(
                    "No se recibió información nueva desde Wokwi."
                )

            st.rerun()

        except Exception as e:

            st.error(f"Error de conexión: {e}")

# ── FOOTER ──────────────────────────────────────────────
st.markdown("""
<div class="footer">
    SmartKitchen © 2026 💙
</div>
""", unsafe_allow_html=True)
