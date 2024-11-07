import streamlit as st
imagenes = [
    "Imagenestrabajo/produtos_500x500_bestburgers_big-tastysingle.png",
    "Imagenestrabajo/NR_202302_0005-999_BigMac_2000x2000.png",
    "Imagenestrabajo/png-transparent-cheeseburger-mcdonald-s-big-mac-hamburger-whopper-patty-bacon-smokehouse-mcdonalds.png",
    "Imagenestrabajo/png-clipart-mcdonald-s-quarter-pounder-hamburger-fast-food-kfc-junk-food-burger-and-sandwich-food-cheese-thumbnail.png",
    "Imagenestrabajo/mc-nifica.png",
    "Imagenestrabajo/DC_202302_0005-999_BigMac_1564x1564-1_product-header-mobile.jpg"
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
