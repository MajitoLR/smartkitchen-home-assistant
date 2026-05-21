import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="SmartKitchen",
    page_icon="🍳",
    layout="wide"
)

# ===== ESTILOS PERSONALIZADOS =====
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom right, #dbeafe, #bfdbfe, #93c5fd);
}

/* TITULOS */
h1, h2, h3 {
    color: #1e3a8a !important;
    font-family: 'Trebuchet MS', sans-serif;
}

/* TEXTO */
p, li {
    color: #1e293b;
    font-size: 18px;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #dbeafe;
}

/* TARJETAS */
.card {
    background-color: rgba(255,255,255,0.70);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
    backdrop-filter: blur(10px);
    margin-bottom: 25px;
}

/* HERO */
.hero {
    background: linear-gradient(to right, #60a5fa, #3b82f6);
    padding: 60px;
    border-radius: 30px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.2);
}

.hero-title {
    color: white;
    font-size: 60px;
    font-weight: bold;
    margin-bottom: 15px;
}

.hero-text {
    color: white;
    font-size: 24px;
    line-height: 1.6;
    font-weight: 500;
}

/* INFO BOX */
.stAlert {
    border-radius: 20px;
}

/* BOTONES */
.stButton > button {
    background-color: #3b82f6;
    color: white;
    border-radius: 15px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
}

.stButton > button:hover {
    background-color: #2563eb;
    color: white;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #1e3a8a;
    margin-top: 40px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ===== HERO =====
st.markdown("""
<div class="hero">

    <div class="hero-title">
        🍳 SmartKitchen
    </div>

    <div class="hero-text">
        Disfruta de tu cocina inteligente a través de una gran experiencia interactiva y moderna 💙
    </div>

</div>
""", unsafe_allow_html=True)

# ===== CONTENIDO =====
st.markdown("""
<div class="card">

<h2>👩‍🍳 Bienvenido a SmartKitchen</h2>

<p>
Una cocina inteligente multimodal que permite:
</p>

<ul>
<li>🍳 Asistente de Cocina Inteligente</li>
<li>🌡️💧 Monitoreo de Sensores</li>
<li>🌀💨 Control Extractor de Humo</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ===== IMAGEN =====
try:

    img = Image.open("cocina.jpg")

    st.image(
        img,
        caption="💙 Centro de Control SmartKitchen",
        use_container_width=True
    )

except FileNotFoundError:

    st.image(
        "https://images.unsplash.com/photo-1556911220-e15b29be8c8f",
        caption="💙 Ecosistema SmartKitchen conectado",
        use_container_width=True
    )

# ===== TARJETAS =====
col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">

    <h3>🤖 IA de Cocina</h3>

    <p>
        Genera recetas inteligentes utilizando ingredientes disponibles.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">

    <h3>🌡️ Sensores Inteligentes</h3>

    <p>
        Monitorea temperatura y alertas desde Wokwi.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="card">

    <h3>🎀 Experiencia Multimodal</h3>

    <p>
        Interacción visual, sensores y automatización inteligente.
    </p>

    </div>
    """, unsafe_allow_html=True)

# ===== INFO =====
st.info("💙 Usa el menú lateral para navegar entre páginas.")

# ===== SIDEBAR =====
st.sidebar.title("🍳 SmartKitchen")

st.sidebar.markdown("---")

st.sidebar.success("✨ Navegación")

st.sidebar.markdown("""
### 📌 Páginas

- Inicio
- Asistente de Recetas
- Monitor Inteligente
""")

st.sidebar.markdown("---")

st.sidebar.info("💙 Cocina inteligente multimodal")

# ===== FOOTER =====
st.markdown("""
<div class="footer">
    SmartKitchen © 2026 💙
</div>
""", unsafe_allow_html=True)
