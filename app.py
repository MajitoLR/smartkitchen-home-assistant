import streamlit as st

st.set_page_config(
    page_title="SmartKitchen",
    page_icon="🍳",
    layout="wide"
)

st.title("🍳 SmartKitchen Home Assistant")

st.markdown("""
## Bienvenido a SmartKitchen

Una cocina inteligente multimodal que ayuda a cocinar de forma:

- segura
- organizada
- interactiva

---

### Funciones principales

✅ Asistente de recetas  
✅ Monitor inteligente de cocina  
✅ Alertas de temperatura  
✅ Sensores simulados  
✅ Automatización inteligente  

---

### Tecnologías utilizadas

- Streamlit
- ESP32
- Wokwi
- Python
- GitHub

---

### Proyecto académico de cocina inteligente
""")

st.sidebar.success("Selecciona una página")
