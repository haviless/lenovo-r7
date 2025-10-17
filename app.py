import streamlit as st
import streamlit.components.v1 as components

# Configurar la página para usar todo el ancho
st.set_page_config(layout="wide")

# Ocultar el padding y el menú de Streamlit (opcional, para aspecto más limpio)
hide_style = """
    <style>
    .block-container {
        padding: 0 !important;
    }
    header, footer, .stDeployButton {
        display: none;
    }
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Leer el archivo HTML local
with open("lenovo-r7.html", "r", encoding="utf-8") as f:
    html_content = "<hr><hr>"+f.read()

# Mostrar el HTML ocupando todo el espacio
components.html(html_content, height=800, width=None, scrolling=True)
