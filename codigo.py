import streamlit as st
st.title("")
st.markdown("<h1 style='text-align: center;'>Lista de Productos</h1>", unsafe_allow_html=True)

# Contenedor para los productos con checkboxes grandes
st.markdown("<h3 style='text-align: center;'>Selecciona los productos deseados:</h3>", unsafe_allow_html=True)

# Lista de productos
productos = [
    "Producto 1 - Camisa",
    "Producto 2 - Pantalón",
    "Producto 3 - Zapatos",
    "Producto 4 - Sombrero",
    "Producto 5 - Bufanda",
    "Producto 6 - Abrigo"
]
