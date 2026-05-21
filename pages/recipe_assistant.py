import streamlit as st

st.title("📖 Asistente de Recetas")

st.markdown("""
Bienvenido al asistente inteligente de recetas de SmartKitchen.
""")

# Buscador
busqueda = st.text_input("🔍 Buscar receta")

# Recetas simuladas
recetas = {
    "pasta": {
        "ingredientes": [
            "Pasta",
            "Salsa de tomate",
            "Queso",
            "Sal"
        ],
        "pasos": [
            "Hervir agua",
            "Agregar la pasta",
            "Cocinar durante 10 minutos",
            "Agregar salsa y queso"
        ]
    },

    "arroz": {
        "ingredientes": [
            "Arroz",
            "Agua",
            "Sal"
        ],
        "pasos": [
            "Agregar agua",
            "Añadir arroz",
            "Cocinar durante 20 minutos"
        ]
    }
}

# Mostrar receta
if busqueda.lower() in recetas:

    receta = recetas[busqueda.lower()]

    st.subheader("🧂 Ingredientes")

    for ingrediente in receta["ingredientes"]:
        st.write(f"• {ingrediente}")

    st.subheader("👨‍🍳 Pasos")

    for i, paso in enumerate(receta["pasos"], start=1):
        st.write(f"{i}. {paso}")

else:
    if busqueda != "":
        st.warning("Receta no encontrada")

# Temporizador
st.subheader("⏲️ Temporizador")

tiempo = st.slider(
    "Selecciona los minutos",
    1,
    60,
    10
)

if st.button("▶️ Iniciar temporizador"):
    st.success(f"Temporizador iniciado por {tiempo} minutos")

# Comando de voz simulado
st.subheader("🎤 Comandos de voz")

if st.button("Activar comando de voz"):
    st.info("Comando de voz activado")
