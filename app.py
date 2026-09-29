```python
import streamlit as st
from PIL import Image

# =========================
# DISEÑO
# =========================
st.markdown("""
<style>

    /* Fondo general */
    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #eef1ff 100%);
        color: #20243a;
    }

    /* Contenedor principal */
    .block-container {
        max-width: 950px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Título */
    h1 {
        color: #5b4bdb;
        font-size: 3rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 1rem;
    }

    /* Headers */
    h2 {
        color: #302b63;
        font-weight: 700 !important;
        margin-top: 2rem;
    }

    h3 {
        color: #5b4bdb;
        font-weight: 700 !important;
    }

    /* Texto */
    p {
        color: #45495e;
        font-size: 1.05rem;
    }

    /* Imagen */
    img {
        border-radius: 18px;
        box-shadow: 0 8px 25px rgba(50, 45, 100, 0.15);
    }

    /* Input */
    div[data-baseweb="input"] {
        border-radius: 12px;
        border: 2px solid #dcd9ff;
        background-color: white;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #6c5ce7;
        box-shadow: 0 0 0 2px rgba(108, 92, 231, 0.15);
    }

    /* Checkbox y radio */
    div[data-testid="stCheckbox"],
    div[data-testid="stRadio"] {
        background: white;
        padding: 15px;
        border-radius: 14px;
        box-shadow: 0 5px 18px rgba(50, 45, 100, 0.08);
    }

    /* Columnas */
    div[data-testid="column"] {
        background: rgba(255,255,255,0.75);
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #e4e2f7;
    }

    /* Caption de imagen */
    .stImage figcaption {
        color: #68647c;
        font-style: italic;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# CONTENIDO ORIGINAL
# =========================

st.title("y un sabio dijo")


st.header("en este jdklajkl")
st.write("slkjflksjlk entonces dijeron")
image = Image.open("tin.jpg")
st.image(image, caption="interfaces multimodales")


texto = st.text_input("escribe","this is my")
st.write("el texto escrito es", texto)


col1,col2 = st.columns(2)

with col1:
  st.subheader("aaaaaaaaaaaaaa")
  st.write("eeeeeeeeeeeee")
  resp = st.checkbox("estoy")
  if resp:
    st.write("oooooo")


with col2:
  image= Image.open("tin.jpg")
  modo = st.radio("que modalidad jdsjlksajk",("visual", "auditiva", "tactil"))
  if modo == "visual":
    st.write("la vista es fundamental")
  if modo == "auditiva":
    st.write("la audicion es fundamental para")
  if modo == "tactil":
    st.write("el tactil es fundamental para todo")
```

El **contenido y funcionamiento original quedan iguales**; lo único añadido es el bloque CSS del principio para darle apariencia de interfaz más limpia y moderna.
