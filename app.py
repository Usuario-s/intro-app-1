
import streamlit as st
from PIL import Image

st.title("Primera app")


st.header("Multimodales")
st.write("Texto")
image = Image.open("tin.jpg")
st.image(image, caption="interfaces multimodales")


texto = st.text_input("escribe","escribe aqui")
st.write("el texto escrito es", texto)


col1,col2 = st.columns(2)

with col1:
  st.subheader("a")
  st.write("r")
  resp = st.checkbox("estoy")
  if resp:
    st.write("epa")


with col2:
  image= Image.open("tin.jpg")
  modo = st.radio("que modalidad jdsjlksajk",("visual", "auditiva", "tactil"))
  if modo == "visual":
    st.write("la vista es fundamental")
  if modo == "auditiva":
    st.write("la audicion es fundamental para escuchar")
  if modo == "tactil":
    st.write("el tactil es fundamental para todo")
