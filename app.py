import streamlit as st

st.set_page_config(
    page_title="SmartKitchen AI",
    page_icon="🍳",
    layout="wide"
)

# Título principal
st.title("🍳 SmartKitchen AI")

st.markdown("""
# Cocina Inteligente Multimodal

Bienvenido a SmartKitchen AI, un asistente inteligente de cocina que utiliza automatización, sensores y generación inteligente de recetas para mejorar la experiencia del usuario.
""")

# Separador
st.divider()

# Tarjetas informativas
col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("🤖 IA de Recetas")

    st.write("""
Genera recetas automáticamente usando los ingredientes disponibles.
""")

with col2:

    st.subheader("🔥 Monitoreo Inteligente")

    st.write("""
Visualiza sensores, temperatura y alertas de cocina en tiempo real.
""")

with col3:

    st.subheader("🎤 Interacción Multimodal")

    st.write("""
Utiliza comandos simulados, alertas y automatización inteligente.
""")

# Separador
st.divider()

# Información del proyecto
st.header("📌 Objetivo del Proyecto")

st.write("""
SmartKitchen AI busca crear una experiencia de cocina más segura, organizada e interactiva mediante tecnologías inteligentes y dispositivos IoT.
""")

# Tecnologías
st.header("🛠️ Tecnologías Utilizadas")

st.markdown("""
- Streamlit
- Python
- ESP32
- Wokwi
- GitHub
- Flask
""")

# Sidebar
st.sidebar.title("🍳 SmartKitchen")

st.sidebar.success("Selecciona una página")

st.sidebar.markdown("""
### Navegación

- Inicio
- Asistente de Recetas
- Monitor Inteligente
""")

# Pie de página
st.divider()

st.caption("SmartKitchen AI © 2026")
