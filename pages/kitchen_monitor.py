import streamlit as st
import random

st.title("🔥 Monitor Inteligente de Cocina")

st.markdown("""
Monitoreo en tiempo real de sensores y dispositivos de SmartKitchen.
""")

# Temperatura simulada
temperatura = random.randint(20, 100)

# Mostrar temperatura
st.metric(
    label="🌡️ Temperatura Actual",
    value=f"{temperatura} °C"
)

# Estado de la cocina
if temperatura < 50:

    st.success("✅ Temperatura estable")

    st.write("LED apagado")
    st.write("Buzzer apagado")

else:

    st.error("⚠️ ALERTA DE CALOR")

    st.write("🔴 LED encendido")
    st.write("🔊 Buzzer activado")

# Estado de dispositivos
st.subheader("📟 Estado de Dispositivos")

col1, col2 = st.columns(2)

with col1:
    st.info("ESP32 conectado")

with col2:
    st.info("Sensores activos")

# Botón de actualización
if st.button("🔄 Actualizar sensores"):
    st.rerun()

# Historial simulado
st.subheader("📈 Historial de Temperatura")

datos = [random.randint(20, 100) for _ in range(10)]

st.line_chart(datos)
