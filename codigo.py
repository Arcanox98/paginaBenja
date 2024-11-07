import streamlit as st
st.title("Ingreso de Productos")
st.subheader("Sube una imagen y escribe una breve descripción para cada producto")

# Crear un contenedor para alinear los productos en una cuadrícula de 3 columnas por fila
for row in range(2):  # Dos filas
    cols = st.columns(3)  # Tres columnas por fila
    for i, col in enumerate(cols):
        with col:
            product_num = row * 3 + i + 1
            st.markdown(f"### Producto {product_num}")
            image = st.imagen(f"Sube la imagen del producto {product_num}", type=["jpg", "jpeg", "png"], key=f"image_{product_num}")
            description = st.text_input(f"Descripción para el producto {product_num}", key=f"description_{product_num}")
            st.markdown("---")  # Separador entre productos (opcional)

st.write("Gracias por ingresar los productos!")
