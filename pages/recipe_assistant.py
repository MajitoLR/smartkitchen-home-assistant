import streamlit as st

st.set_page_config(
    page_title="Asistente de Recetas",
    page_icon="🍳",
    layout="wide"
)

st.title("🍳 SmartKitchen AI")

st.markdown("""
## Generador Inteligente de Recetas

Escribe los ingredientes que tienes disponibles y SmartKitchen generará una receta automáticamente.
""")

# Entrada de ingredientes
ingredientes_usuario = st.text_area(
    "🧂 Escribe tus ingredientes separados por comas",
    placeholder="Ejemplo: pollo, arroz, tomate, queso"
)

# Base de recetas simuladas
recetas = [

    {
        "nombre": "Arroz con Pollo",
        "ingredientes": ["pollo", "arroz"],
        "pasos": [
            "Cocinar el arroz",
            "Cocinar el pollo",
            "Mezclar ambos ingredientes",
            "Servir caliente"
        ]
    },

    {
        "nombre": "Pasta con Queso",
        "ingredientes": ["pasta", "queso"],
        "pasos": [
            "Hervir la pasta",
            "Agregar queso",
            "Mezclar bien",
            "Servir"
        ]
    },

    {
        "nombre": "Ensalada Fresca",
        "ingredientes": ["lechuga", "tomate", "cebolla"],
        "pasos": [
            "Lavar los vegetales",
            "Cortar ingredientes",
            "Mezclar todo",
            "Agregar sal al gusto"
        ]
    },

    {
        "nombre": "Omelette de Queso",
        "ingredientes": ["huevo", "queso"],
        "pasos": [
            "Batir los huevos",
            "Agregar queso",
            "Cocinar en sartén",
            "Servir caliente"
        ]
    }

]

# Botón generar receta
if st.button("✨ Generar receta"):

    ingredientes = [
        ingrediente.strip().lower()
        for ingrediente in ingredientes_usuario.split(",")
    ]

    receta_encontrada = False

    for receta in recetas:

        coincidencias = 0

        for ingrediente in receta["ingredientes"]:

            if ingrediente in ingredientes:
                coincidencias += 1

        if coincidencias >= 2:

            receta_encontrada = True

            st.success(f"🍽️ Receta sugerida: {receta['nombre']}")

            st.subheader("🧂 Ingredientes")

            for ingrediente in receta["ingredientes"]:
                st.write(f"• {ingrediente}")

            st.subheader("👨‍🍳 Pasos")

            for i, paso in enumerate(receta["pasos"], start=1):
                st.write(f"{i}. {paso}")

            st.subheader("⏲️ Temporizador")

            tiempo = st.slider(
                "Selecciona los minutos",
                1,
                60,
                10
            )

            if st.button("▶️ Iniciar temporizador"):
                st.info(f"Temporizador iniciado por {tiempo} minutos")

            st.subheader("🎤 Asistente de voz")

            if st.button("Activar asistente"):
                st.success("Asistente de voz activado")

            break

    if not receta_encontrada:

        st.warning("No encontramos una receta exacta.")

        st.info("""
Puedes intentar agregando más ingredientes.
""")
