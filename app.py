# ev_clase2\Scripts\activate  deactivate
# importar streamlit
# Probando como reniciar la conexion
import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_csv("data/match_result.csv")

def main():
    st.title("Trabajando con datos en Streamlit")
    st.dataframe(df)
    st.header("Usando table.")
    st.table(df)
    st.header("Usando json.")
    st.json({"clave":"valor"})

    codigo = """
    def saludando(nombre:
        print("Hola" + nombre))"""
    st.code(codigo, language= "python")

    # st.header("Este es el encabezado.")
    # st.subheader("Este es el sub-encabezado.")
    # st.text("Esto es un texno normal.")
    # nombre = "Mundo"
    # st.text(f"Hola {nombre}.")
    # st.markdown("# Esto es markdown 1")
    # st.markdown("## Esto es markdown 2")
    # st.markdown("### Esto es markdown 3")
    # st.markdown("#### Esto es markdown 4")
    # st.markdown("##### Esto es markdown 5")
    # st.success("Mensaje de exito.")
    # st.error("Error.")
    # st.warning("Mensaje de advertencia.")
    # st.info("Mensaje de información.")
    # st.exception("Msj control de exception")
    # st.write("Aca podemos poner el texto que querramos.")
    # st.write("### 1+3")


if __name__ == "__main__":
    main()