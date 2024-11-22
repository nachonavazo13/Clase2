# ev_clase2\Scripts\activate  deactivate
# importar streamlit
import streamlit as st
import pandas as pd
from PIL import Image


def main():
    st.title("Mi primer app en Streamlit")
    st.header("Este es el encabezado.")
    st.subheader("Este es el sub-encabezado.")
    st.text("Esto es un texno normal.")
    nombre = "Mundo"
    st.text(f"Hola {nombre}.")
    st.markdown("# Esto es markdown 1")
    st.markdown("## Esto es markdown 2")
    st.markdown("### Esto es markdown 3")
    st.markdown("#### Esto es markdown 4")
    st.markdown("##### Esto es markdown 5")
    st.success("Mensaje de exito.")
    st.error("Error.")
    st.warning("Mensaje de advertencia.")
    st.info("Mensaje de información.")
    st.exception("Msj control de exception")
    st.write("Aca podemos poner el texto que querramos.")


if __name__ == "__main__":
    main()