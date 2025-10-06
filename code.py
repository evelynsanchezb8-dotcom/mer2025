import streamlit as st

# Preguntas, opciones, respuestas y justificaciones embebidas directamente en el código
PREGUNTAS = [
    {
        "pregunta": "¿Cómo afecta el estrés crónico a la memoria de trabajo durante el estudio?",
        "opciones": [
            "La mejora significativamente porque aumenta la concentración.",
            "No tiene ningún efecto.",
            "La deteriora porque afecta la función del hipocampo.",
            "Solo afecta la memoria a largo plazo."
        ],
        "respuesta_correcta": 2,
        "justificacion": "El estrés crónico libera cortisol, que puede dañar el hipocampo, afectando la memoria de trabajo y la capacidad para retener información."
    },
    {
        "pregunta": "¿Cuál es el impacto del estrés agudo en la recuperación de información durante un examen?",
        "opciones": [
            "Mejora la recuperación porque aumenta la alerta.",
            "Dificulta la recuperación porque genera ansiedad.",
            "No afecta la recuperación de información.",
            "Solo afecta la memoria a largo plazo."
        ],
        "respuesta_correcta": 1,
        "justificacion": "El estrés agudo puede generar ansiedad que bloquea la recuperación de información, aunque aumenta la alerta."
    },
    {
        "pregunta": "¿Qué tipo de memoria suele verse más afectada por el estrés en contextos académicos?",
        "opciones": [
            "Memoria sensorial.",
            "Memoria a largo plazo.",
            "Memoria de trabajo.",
            "Memoria implícita."
        ],
        "respuesta_correcta": 2,
        "justificacion": "La memoria de trabajo es especialmente vulnerable al estrés, manejando información temporal para tareas cognitivas."
    },
    {
        "pregunta": "¿Cómo puede el estrés moderado afectar el rendimiento académico?",
        "opciones": [
            "Puede mejorar el rendimiento al aumentar la motivación.",
            "Siempre empeora el rendimiento.",
            "No tiene ningún efecto.",
            "Solo afecta el rendimiento en deportes."
        ],
        "respuesta_correcta": 0,
        "justificacion": "Un nivel moderado de estrés puede aumentar la motivación y la concentración, mejorando el rendimiento."
    },
    {
        "pregunta": "¿Qué hormona relacionada con el estrés tiene un impacto negativo en la memoria?",
        "opciones": [
            "Dopamina.",
            "Cortisol.",
            "Serotonina.",
            "Adrenalina."
        ],
        "respuesta_correcta": 1,
        "justificacion": "El cortisol afecta negativamente la función del hipocampo, dañando la memoria."
    },
    {
        "pregunta": "¿Cuál es una estrategia efectiva para minimizar el impacto del estrés en la memoria durante los estudios?",
        "opciones": [
            "Estudiar toda la noche sin descanso.",
            "Realizar ejercicios de relajación y pausas.",
            "Ignorar el estrés.",
            "Aumentar el consumo de cafeína sin límite."
        ],
        "respuesta_correcta": 1,
        "justificacion": "Las pausas y técnicas de relajación reducen el estrés y mejoran la función cognitiva."
    },
    {
        "pregunta": "¿Qué ocurre con la memoria cuando el estrés es muy alto durante un examen?",
        "opciones": [
            "Se optimiza porque el cuerpo libera energía.",
            "Se bloquea debido a la ansiedad extrema.",
            "No cambia.",
            "Solo mejora la memoria a corto plazo."
        ],
        "respuesta_correcta": 1,
        "justificacion": "El estrés extremo genera ansiedad que puede bloquear la recuperación de información almacenada."
    },
    {
        "pregunta": "¿Cómo puede el estrés afectar la consolidación de la memoria después de estudiar?",
        "opciones": [
            "Facilita la consolidación porque el cuerpo está alerta.",
            "Dificulta la consolidación porque afecta el sueño.",
            "No afecta la consolidación.",
            "Solo afecta la memoria sensorial."
        ],
        "respuesta_correcta": 1,
        "justificacion": "El estrés puede interferir con el sueño, necesario para consolidar la memoria, dificultando el aprendizaje."
    },
    {
        "pregunta": "¿Cuál es una consecuencia del estrés prolongado en estudiantes?",
        "opciones": [
            "Aumento del rendimiento académico.",
            "Deterioro de la función cognitiva y memoria.",
            "Mejora de la creatividad.",
            "Ninguna, se adaptan fácilmente."
        ],
        "respuesta_correcta": 1,
        "justificacion": "El estrés prolongado deteriora la función cognitiva y la memoria."
    },
    {
        "pregunta": "¿Qué factor puede moderar el impacto del estrés sobre la memoria en estudiantes?",
        "opciones": [
            "La cantidad de horas de estudio sin descanso.",
            "El nivel de apoyo social y emocional.",
            "La cantidad de café consumido.",
            "La edad únicamente."
        ],
        "respuesta_correcta": 1,
        "justificacion": "El apoyo social y emocional ayuda a manejar el estrés, reduciendo su impacto negativo."
    }
]

def main():
    st.title("Quiz: Memoria, Estrés y Rendimiento Académico")

    if "indice" not in st.session_state:
        st.session_state.indice = 0
    if "puntaje" not in st.session_state:
        st.session_state.puntaje = 0
    if "respondido" not in st.session_state:
        st.session_state.respondido = False
    if "seleccion" not in st.session_state:
        st.session_state.seleccion = None

    if st.session_state.indice < len(PREGUNTAS):
        pregunta = PREGUNTAS[st.session_state.indice]
        st.subheader(f"Pregunta {st.session_state.indice + 1} de {len(PREGUNTAS)}")
        st.write(pregunta["pregunta"])

        opciones = pregunta["opciones"]
        respuesta_correcta = pregunta["respuesta_correcta"]

        seleccion = st.radio("Selecciona una opción:", options=opciones, index=st.session_state.seleccion or 0)

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

        if st.session_state.respondido:
            if st.session_state.seleccion == respuesta_correcta:
                if st.button("Siguiente pregunta"):
                    st.session_state.indice += 1
                    st.session_state.respondido = False
                    st.session_state.seleccion = None
            else:
                st.warning("Debes responder correctamente para avanzar.")

    else:
        st.success("¡Has terminado el quiz!")
        st.write(f"Tu puntaje final es: {st.session_state.puntaje} de {len(PREGUNTAS)}")
        porcentaje = (st.session_state.puntaje / len(PREGUNTAS)) * 100
        st.write(f"Porcentaje: {porcentaje:.2f}%")

        if st.button("Reiniciar quiz"):
            st.session_state.indice = 0
            st.session_state.puntaje = 0
            st.session_state.respondido = False
            st.session_state.seleccion = None

if __name__ == "__main__":
    main()
