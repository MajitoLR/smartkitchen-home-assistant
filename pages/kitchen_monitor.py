import streamlit as st
from openai import OpenAI

# ── CONFIGURACIÓN INICIAL ────────────────────────────────
st.set_page_config(
    page_title="Asistente de Cocina Virtual",
    page_icon="💬",
    layout="centered"
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
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 10px;
}

.hero-text {
    color: white;
    font-size: 20px;
}

/* TARJETAS */
.card {
    background-color: rgba(255,255,255,0.75);
    padding: 25px;
    border-radius: 25px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
}

/* BOTONES */
div.stButton > button {
    background-color: #3B82F6 !important;
    color: white !important;
    border-radius: 20px !important;
    border: 2px solid #60A5FA !important;
    width: 100%;
    font-weight: bold;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #1D4ED8 !important;
    border: 2px solid #2563EB !important;
    transform: scale(1.02);
}

/* CHAT */
.stChatMessage {
    background-color: rgba(255,255,255,0.85);
    border-radius: 20px;
    border: 1px solid #E2E8F0;
    margin-bottom: 10px;
    padding: 10px;
}

/* INPUT CHAT */
[data-testid="stChatInput"] {
    background-color: white;
    border-radius: 20px;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #1E3A8A;
    margin-top: 30px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ── HERO ────────────────────────────────────────────────
st.markdown("""
<div class="hero">

    <div class="hero-title">
        🍳🧑‍🍳 Asistente de Cocina Virtual
    </div>

    <div class="hero-text">
        Descubre recetas deliciosas utilizando los ingredientes que tienes disponibles 💙
    </div>

</div>
""", unsafe_allow_html=True)

# ── SIDEBAR (CONFIGURACIÓN) ──────────────────────────────
with st.sidebar:

    st.header("⚙️ Configuración")

    api_key = st.text_input(
        "🔑 OpenAI API Key",
        type="password",
        placeholder="sk-..."
    )

    model = st.selectbox(
        "Modelo",
        ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"]
    )

    # PROMPT OCULTO
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = (
            "Eres un chef profesional alegre, creativo y experto en optimizar "
            "ingredientes. Tu objetivo es ayudar a los usuarios a crear recetas deliciosas "
            "con lo que tengan en su nevera. Habla con entusiasmo, da tips de cocina "
            "y usa emojis relacionados con alimentos."
        )

# ── MAIN ────────────────────────────────────────────────
st.markdown("""
<div class="card">

<h2>👩‍🍳 Bienvenido a SmartKitchen AI</h2>

<p>
¡Hola! Soy tu chef personal. Dime qué ingredientes tienes y crearemos algo increíble juntos ✨
</p>

</div>
""", unsafe_allow_html=True)

# Inicializar historial
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input usuario
if prompt := st.chat_input("🍳 Escribe tus ingredientes o dudas culinarias..."):

    if not api_key:

        st.warning("Por favor ingresa tu API Key en el panel lateral.")
        st.stop()

    # Mensaje usuario
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Construir mensajes
    messages_to_send = []

    if st.session_state.system_prompt:
        messages_to_send.append({
            "role": "system",
            "content": st.session_state.system_prompt
        })

    messages_to_send += st.session_state.messages

    # OpenAI
    client = OpenAI(api_key=api_key)

    with st.chat_message("assistant"):

        with st.spinner("🍳 Cocinando una respuesta..."):

            try:

                response = client.chat.completions.create(
                    model=model,
                    messages=messages_to_send,
                )

                reply = response.choices[0].message.content

                st.write(reply)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": reply
                })

            except Exception as e:

                st.error(f"Error: {e}")

# Botón limpiar
if st.session_state.messages:

    st.write("---")

    if st.button("🗑️ Limpiar conversación"):

        st.session_state.messages = []

        st.rerun()

# FOOTER
st.markdown("""
<div class="footer">
    SmartKitchen © 2026 💙
</div>
""", unsafe_allow_html=True)
