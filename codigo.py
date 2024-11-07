import streamlit as st
imagenes = [
    "ruta_imagen_1.jpg",
    "ruta_imagen_2.jpg",
    "ruta_imagen_3.jpg",
    "ruta_imagen_4.jpg",
    "ruta_imagen_5.jpg",
    "ruta_imagen_6.jpg"
]

descripciones = [
    "Descripción del producto 1",
    "Descripción del producto 2",
    "Descripción del producto 3",
    "Descripción del producto 4",
    "Descripción del producto 5",
    "Descripción del producto 6"
]

st.title("Productos")
st.subheader("Visualización de imágenes y descripciones de productos")

# Crear un contenedor para mostrar los productos en una cuadrícula de 3 columnas por fila
for row in range(2):  # Dos filas
    cols = st.columns(3)  # Tres columnas por fila
    for i, col in enumerate(cols):
        product_index = row * 3 + i  # Índice para cada producto
        with col:
            st.image(imagenes[product_index], caption=f"Producto {product_index + 1}", use_column_width=True)
            st.write(descripciones[product_index])

st.write("Estos son todos los productos.")
