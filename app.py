# ev_clase2\Scripts\activate  deactivate
# importar streamlit
# Probando como reniciar la conexion
import streamlit as st
import pandas as pd
from PIL import Image

# df = pd.read_csv("data/match_result.csv")

def main():
    st.title("Trabajando con Multimedia en Streamlit")

    img = Image.open("assets/OBRAS.png")
    st.image(img, use_container_width=True)

    img1 = "https://aula.sportsdatacampus.com/pluginfile.php?file=%2F1%2Ftheme_moove%2Flogo%2F1729159738%2FSDC_Hor_250.png"
    st.image(img1, use_container_width=True)

    with open("assets/2_PICK AL EJE.mp4", 'rb') as video_file:
        st.video(video_file, start_time=0)
    



    # posicion = st.selectbox("Seleccione una posicion",["Portero", "Defensa", "Mediocampista", "Delantero"])
    # st.write(f"La posicion seleccionada es: {posicion}")

    # opciones = st.multiselect("Seleccione una posicion",["Portero", "Defensa", "Mediocampista", "Delantero"])
    # st.write(f"La posicion seleccionada es: {opciones}")

    # edad = st.slider('Selecione su edad: ',
    #                 min_value=1, max_value=100, value=20, step=1)
    # st.write(f"Su edad es : {edad}")

    # nivel = st.select_slider(
    #     "Selecciones su nivel: ",
    #     ["Muy bajo", "Bajo", "Medio", "Alto", "Muy alto"])
    # st.write(f"Su nivel es: {nivel}")

    # opc = st.radio('Seleccione una opcion: ',["Portero", "Defensa", "Mediocampista", "Delantero"])
    # st.write(f'La opcion es: {opc}')

    # check = st.checkbox("Acepto las condiciones.")
    # if check:
    #     st.write("Has aceptado las condiciones")
    # else:
    #     st.write("No has aceptado las condiciones")

    # rta = st.button('Hola Nacho')
    # if rta:
    #     st.write('Que haces Nacho')
    #     st.write(rta)
    # else:
    #     st.write('-')
    #     st.write(rta)

    # tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

    # with tab1:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    # with tab2:
    #     st.header("A dog")
    #     st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    # with tab3:
    #     st.header("An owl")
    #     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
        


    # TRABAJANDO CON TABLAS.
    # st.dataframe(df)
    # st.header("Usando table.")
    # st.table(df)
    # st.header("Usando json.")
    # st.json({"clave":"valor"})

    # codigo = """
    # def saludando(nombre:
    #     print("Hola" + nombre))"""
    # st.code(codigo, language= "python")

    # TRABAJANDO CON TEXTO.
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