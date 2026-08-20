import streamlit as st
from PIL import Image

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
  moddo = st.radio("que modalidad jdsjlksajk",("visual", "auditiva", "tactil")
