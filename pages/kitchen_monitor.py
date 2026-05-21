import streamlit as st
from openai import OpenAI

# ── CONFIGURACIÓN ───────────────────────────────────────
st.set_page_config(
    page_title="Asistente de Cocina Virtual",
    page_icon="🍳",
    layout="wide"
)

# ── ESTILOS VISUALES ────────────────────────────────────
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

/* TEXTO */
p, label, span {
    color: #1E3A8A !important;
}

/* HERO */
.hero {
    background: linear-gradient(to right, #60A5FA, #3B82F6);
    padding: 50px;
    border-radius: 30px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.2);
}

.hero-title {
    color: white;
    font-size: 55px;
    font-weight: bold;
    margin-bottom: 15px;
}

.hero-text {
    color: white;
    font-size: 22px;
    line-height: 1.6;
}

/* TARJETAS */
.card {
    background-color: rgba(255,255,255,0.75);
    padding: 25px;
    border-radius: 25px;
    margin-bottom: 25px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
}

/* CHAT */
.stChatMessage {
    background-color: rgba(255,255,255,0.85);
    border-radius: 20px;
    padding: 10px;
    border: 1px solid #bfdbfe;
    margin-bottom: 10px;
}

/* INPUT CHAT */
[data-testid="stChatInput"] {
    background-color: white;
    border-radius: 20px;
}

/* BOTONES */
.stButton > button {
    background-color: #3B82F6 !important;
    color: white !important;
    border-radius: 18px !important;
    border: none !important;
    padding: 12px 18px !important;
    font-weight: bold !important;
    width: 100%;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #2563EB !important;
    transform: scale(1.02);
}

/* SELECTBOX */
div[data-baseweb="select"] {
    background-color: white;
    border-radius: 15px;
}

/* INPUT PASSWORD */
input {
    border-radius: 15px !important;
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
        🍳🧑‍🍳 Asistente de Cocina Virtual
    </div>

    <div class="hero-text">
        Descubre recetas deliciosas utilizando los ingredientes que tienes en casa 💙
    </div>

</div>
""", unsafe_allow_html=True)

# ── SIDEBAR ─────────────────────────────────────────────
with st.sidebar:

    st.title("⚙️ Configuración")

    st.markdown("---")

    api_key = st.text_input(
        "🔑 OpenAI API Key",
        type="password",
        placeholder="sk-..."
    )

    model = st.selectbox(
        "🤖 Modelo IA",
        [
            "gpt-4o-mini",
            "gpt-4o",
            "gpt-3.5-turbo"
        ]
    )

    st.markdown("---")

    st.info("💙 SmartKitchen AI")

    # PROMPT OCULTO
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = (
            "Eres un chef profesional alegre, creativo y experto en optimizar "
            "ingredientes. Tu objetivo es ayudar a los usuarios a crear recetas deliciosas "
            "con lo que tengan en su nevera. Habla con entusiasmo, da tips de cocina "
            "y usa emojis relacionados con alimentos."
        )

# ── BIENVENIDA ──────────────────────────────────────────
st.markdown("""
<div class="card">

<h2>👩‍🍳 Bienvenido a SmartKitchen AI</h2>

<p>
Escribe los ingredientes que tienes disponibles y nuestra IA creará recetas increíbles para ti ✨
</p>

<ul>
<li>🥗 Ideas de recetas inteligentes</li>
<li>🍝 Recomendaciones personalizadas</li>
<li>🧁 Tips de cocina creativos</li>
<li>🤖 Asistencia culinaria con IA</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ── HISTORIAL ───────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ── INPUT USUARIO ───────────────────────────────────────
if prompt := st.chat_input("🍳 Escribe tus ingredientes o dudas culinarias..."):

    if not api_key:

        st.warning("⚠️ Por favor ingresa tu API Key en el panel lateral.")
        st.stop()

    # Mensaje usuario
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Construcción mensajes
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

        with st.spinner("👩‍🍳 Cocinando una receta increíble..."):

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

                st.error(f"❌ Error: {e}")

# ── BOTÓN LIMPIAR ───────────────────────────────────────
if st.session_state.messages:

    st.write("")

    if st.button("🗑️ Limpiar conversación"):

        st.session_state.messages = []

        st.rerun()

# ── FOOTER ──────────────────────────────────────────────
st.markdown("""
<div class="footer">
    SmartKitchen AI © 2026 💙
</div>
""", unsafe_allow_html=True)
