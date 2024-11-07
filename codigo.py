import streamlit as st
st.title("GitHub Loggin")


# Diccionario de usuarios y contraseñas
USUARIOS = {
    "usuario1": "password1",
    "usuario2": "password2"
}

# Estado de sesión
if 'login' not in st.session_state:
    st.session_state['login'] = False

# Si el usuario no está logueado, mostrar el formulario de login
if not st.session_state['login']:
    # Contenedor para centrar el formulario
    espacio = st.empty()
    with espacio.container():
        st.markdown("<h2 style='text-align: center;'>Iniciar Sesión</h2>", unsafe_allow_html=True)
        usuario = st.text_input("Usuario", key="usuario", label_visibility="collapsed")
        contraseña = st.text_input("Contraseña", type="password", key="contraseña", label_visibility="collapsed")
        login_boton = st.button("Login")

        # Verificar las credenciales
        if login_boton:
            if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
                st.session_state['login'] = True
                st.success("Inicio de sesión exitoso")
                espacio.empty()  # Limpiar el espacio del formulario
            else:
                st.error("Usuario o contraseña incorrectos")

# Si el usuario está logueado, mostrar el contenido principal
if st.session_state['login']:
    st.write("¡Bienvenido! Has iniciado sesión correctamente.")
    if st.sidebar.button("Cerrar sesión"):
        st.session_state['login'] = False
