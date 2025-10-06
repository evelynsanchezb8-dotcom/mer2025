import streamlit as st
import requests

# URL raw del archivo JSON en GitHub (reemplaza con el enlace a tu JSON)
GITHUB_JSON_URL = "https://raw.githubusercontent.com/tu_usuario/tu_repo/main/preguntas.json"

@st.cache_data
def cargar_preguntas(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    st.title("Quiz: Memoria, Estrés y Rendimiento Académico")

    preguntas = cargar_preguntas(GITHUB_JSON_URL)

    # Estado para manejar la pregunta actual, puntaje y si se respondió bien
    if "indice" not in st.session_state:
        st.session_state.indice = 0
    if "puntaje" not in st.session_state:
        st.session_state.puntaje = 0
    if "respondido" not in st.session_state:
        st.session_state.respondido = False

    # Mostrar pregunta actual
    if st.session_state.indice < len(preguntas):
        pregunta = preguntas[st.session_state.indice]
        st.subheader(f"Pregunta {st.session_state.indice + 1} de {len(preguntas)}")
        st.write(pregunta["pregunta"])

        opciones = pregunta["opciones"]
        respuesta_correcta = pregunta["respuesta_correcta"]

        # Para que la opción seleccionada se mantenga en la sesión
        if "seleccion" not in st.session_state:
            st.session_state.seleccion = None

        seleccion = st.radio("Selecciona una opción:", options=opciones, index=st.session_state.seleccion or 0)

        # Botón para enviar respuesta
        if st.button("Enviar respuesta"):
            indice_seleccion = opciones.index(seleccion)
            st.session_state.seleccion = indice_seleccion
            st.session_state.respondido = True

            if indice_seleccion == respuesta_correcta:
                st.session_state.puntaje += 1
                st.success("¡Respuesta correcta!")
            else:
                st.error("Respuesta incorrecta.")

            st.info(f"Justificación: {pregunta['justificacion']}")

        # Si ya respondieron correctamente, botón para siguiente pregunta
        if st.session_state.respondido:
            if st.session_state.seleccion == respuesta_correcta:
                if st.button("Siguiente pregunta"):
                    st.session_state.indice += 1
                    st.session_state.respondido = False
                    st.session_state.seleccion = None
            else:
                st.warning("Debes responder correctamente para avanzar.")

    else:
        # Fin del quiz
        st.success("¡Has terminado el quiz!")
        st.write(f"Tu puntaje final es: {st.session_state.puntaje} de {len(preguntas)}")
        porcentaje = (st.session_state.puntaje / len(preguntas)) * 100
        st.write(f"Porcentaje: {porcentaje:.2f}%")

        if st.button("Reiniciar quiz"):
            st.session_state.indice = 0
            st.session_state.puntaje = 0
            st.session_state.respondido = False
            st.session_state.seleccion = None

if __name__ == "__main__":
    main()
