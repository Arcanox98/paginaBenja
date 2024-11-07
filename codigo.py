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
    "Mcnífica: Carne de res, queso, bacon, cebolla caramelizada, lechuga, tomate, salsa especial y pan de hamburguesa.",
    "Mega Doble Queso Bacon: Dos carnes de res, dos rebanadas de queso, bacon crujiente, pan de hamburguesa y salsas."
]

urls = [
    "https://www.mcdonalds.com/us/es-us/product/mcplant.html",
    "https://www.mcdonalds.cl/menu/hamburguesas/big-mac",
    "https://www.mcdonalds.com/us/es-us/product/quarter-pounder-with-cheese.html",
    "https://www.mcdonalds.com.pr/productos/hamburgers/quarter-pounder-western-bbq",
    "https://www.mcdonalds.cl/menu/hamburguesas/mcnifica",
    "https://www.mcdonalds.cl/menu/hamburguesas-linea-signature/smoke-house-2-carnes"
]

# Colocar una imagen en la parte superior izquierda
st.markdown(
    """
    <style>
    .top-left {
        position: absolute;
        top: 10px;
        left: 10px;
    }
    </style>
    <div class="top-left">
        <img src="Imagenestrabajo/732217.png" width="150">
    </div>
    """, unsafe_allow_html=True
)

st.title("Macdonaldo")
st.subheader("Visualización de Hamburguesas")

# Crear un contenedor para mostrar los productos en una cuadrícula de 3 columnas por fila
for row in range(2):  # Dos filas
    cols = st.columns(3)  # Tres columnas por fila
    for i, col in enumerate(cols):
        product_index = row * 3 + i  # Índice para cada producto
        
        # Asegúrate de que no se exceda el índice de la lista
        if product_index < len(imagenes):
            with col:
                st.image(imagenes[product_index], caption=f"Producto {product_index + 1}", use_column_width=True)
                st.write(descripciones[product_index])
                
                # Botón para ordenar
                if st.button(f"Ordenar", key=f"btn_{product_index}"):
                    # Redirigir a la URL del producto correspondiente
                    st.markdown(f"[Ordenar aquí]({urls[product_index]})", unsafe_allow_html=True)
