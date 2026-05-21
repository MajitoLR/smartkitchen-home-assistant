# Reemplaza TODO el contenido de `app.py` por este código

```python
import streamlit as st

st.set_page_config(
    page_title="SmartKitchen AI",
    page_icon="🍳",
    layout="wide"
)

# ===== ESTILOS PERSONALIZADOS =====
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #0f172a, #1e293b, #334155);
    color: white;
}

h1, h2, h3, h4 {
    color: white !important;
}

p {
    color: #e2e8f0;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

.card {
    background-color: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    backdrop-filter: blur(10px);
    transition: 0.3s;
    margin-bottom: 20px;
}

.card:hover {
    transform: scale(1.02);
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 10px;
}

.hero {
    background: linear-gradient(to right, #f97316, #ea580c);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0px 6px 25px rgba(0,0,0,0.35);
}

.hero h1 {
    font-size: 50px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 20px;
    color: white;
}

.footer {
    text-align: center;
    color: #cbd5e1;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# ===== HERO PRINCIPAL =====
st.markdown("""
<div class="hero">
    <h1>🍳 SmartKitchen AI</h1>
    <p>
        Cocina inteligente multimodal con generación de recetas,
        sensores inteligentes y automatización IoT.
    </p>
</div>
""", unsafe_allow_html=True)

# ===== DESCRIPCIÓN =====
st.markdown("""
<div class="card">
    <div class="section-title">🤖 ¿Qué es SmartKitchen AI?</div>
    <p>
        SmartKitchen AI es un asistente inteligente de cocina que ayuda a los usuarios
        a cocinar de manera más segura, organizada e interactiva utilizando tecnologías
        inteligentes y sensores conectados.
    </p>
</div>
""", unsafe_allow_html=True)

# ===== TARJETAS =====
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>✨ IA de Recetas</h3>
        <p>
            Genera recetas automáticamente utilizando los ingredientes
            que tengas disponibles en casa.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🔥 Monitor Inteligente</h3>
        <p>
            Visualiza temperatura, sensores y alertas inteligentes
            en tiempo real.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🎤 Multimodalidad</h3>
        <p>
            Interactúa mediante botones, alertas visuales,
            automatización y comandos simulados.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ===== OBJETIVO =====
st.markdown("""
<div class="card">
    <div class="section-title">🎯 Objetivo del Proyecto</div>
    <p>
        Crear una experiencia de cocina moderna e inteligente combinando:
    </p>

    <ul>
        <li>Automatización inteligente</li>
        <li>Interacción multimodal</li>
        <li>Sensores IoT</li>
        <li>Generación inteligente de recetas</li>
        <li>Monitoreo en tiempo real</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ===== TECNOLOGÍAS =====
st.markdown("""
<div class="card">
    <div class="section-title">🛠️ Tecnologías Utilizadas</div>

- Streamlit  
- Python  
- ESP32  
- Wokwi  
- Flask  
- GitHub  
- IoT  

</div>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
st.sidebar.title("🍳 SmartKitchen AI")

st.sidebar.markdown("---")

st.sidebar.success("Navegación")

st.sidebar.markdown("""
### 📌 Páginas

- Inicio
- Asistente de Recetas
- Monitor Inteligente
""")

st.sidebar.markdown("---")

st.sidebar.info("Proyecto de cocina inteligente multimodal")

# ===== FOOTER =====
st.markdown("""
<div class="footer">
    <p>SmartKitchen AI © 2026</p>
</div>
""", unsafe_allow_html=True)
```

# Después de pegar el código:

1. Baja hasta el final
2. Presiona `Commit changes`
3. Guarda los cambios

Con esto la aplicación tendrá:

* fondo moderno degradado
* tarjetas elegantes
* estilo futurista
* diseño tipo IA
* sombras y efectos visuales
* interfaz mucho más profesional
* sidebar personalizada
* apariencia moderna tipo dashboard
