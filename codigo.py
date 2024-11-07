import streamlit as st
st.title("")
st.subheader("Sube una imagen y escribe una breve descripción para cada producto")

# Configuración del layout centrado
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    for i in range(1, 7):
        st.markdown(f"### Producto {i}")
        image = st.file_uploader(f"Sube la imagen del producto {i}", type=["jpg", "jpeg", "png"], key=f"image_{i}")
        description = st.text_input(f"Escribe una descripción para el producto {i}", key=f"description_{i}")
        st.markdown("---")  # Separador entre productos

st.write("Gracias por ingresar los productos!")
