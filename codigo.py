import streamlit as st
imagenes = [
    "Imagenestrabajo/produtos_500x500_bestburgers_big-tastysingle.png",
    "Imagenestrabajo/NR_202302_0005-999_BigMac_2000x2000.png",
    "Imagenestrabajo/987c799e3186217aa0a8e6f996a452a0.png",
    "Imagenestrabajo/DLV_1631_SEP_V2.png",
    "Imagenestrabajo/mc-nifica.png",
    "Imagenestrabajo/hamburguesa-doble-queso-bacon-1024x683.png"
]

descripciones = [
    "McPlant: Carne vegetal, lechuga, tomate, cebolla, pepinillos, ketchup, mayonesa y pan de hamburguesa.",
    "Big Mac: Dos hamburguesas de res, queso, lechuga, cebolla, pepinillos, salsa especial y pan con tres partes.",
    "Quarter Pounder: Carne de res (cuarto de libra), queso, cebolla, ketchup, mostaza y pan de hamburguesa.",
    "Quarter Pounder Western: Carne de res (cuarto de libra), queso, bacon, cebolla caramelizada, salsa barbacoa y pan de hamburguesa",
    "Macnífica: Carne de res, queso, bacon, cebolla caramelizada, lechuga, tomate, salsa especial y pan de hamburguesa.",
    "Mega Doble Queso Bacon: Dos carnes de res, dos rebanadas de queso, bacon crujiente, pan de hamburguesa y salsas."
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
