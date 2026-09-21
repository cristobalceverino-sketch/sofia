from datetime import datetime
import os
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Un detalle para ti 💖", page_icon="🌻", layout="centered"
)

# --- DISEÑO VISUAL (CSS PERSONALIZADO) ---
# Esto cambia los colores, fuentes y le da un aspecto de tarjeta romántica y moderna
st.markdown(
    """
    <style>
    /* Fondo general de la aplicación */
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #f3e5f5 100%);
    }
    
    /* Estilo para las "tarjetas" de contenido */
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    
    /* Títulos principales */
    h1 {
        color: #d81b60;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Subtítulos */
    h3 {
        color: #880e4f;
    }
    
    /* Estilo de los botones */
    .stButton>button {
        background: linear-gradient(90deg, #ec407a 0%, #ab47bc 100%);
        color: white;
        border-radius: 25px;
        padding: 10px 25px;
        border: none;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(236, 64, 122, 0.3);
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #d81b60 0%, #8e24aa 100%);
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# --- FUNCIÓN PARA GUARDAR DATOS (Para tus planes futuros) ---
def guardar_dato_secreto(categoria, valor):
  fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
  registro = f"[{fecha_actual}] Categoria: {categoria} | Dato: {valor}\n"

  # Se guarda en un archivo de texto en tu proyecto
  with open("datos_sorpresas_futuras.txt", "a", encoding="utf-8") as f:
    f.write(registro)


# --- VERIFICACIÓN DE FECHA ---
hoy = datetime.now().strftime("%d-%m")
fecha_larga = datetime.now().strftime("%d/%m/%Y")

# Base de datos de sorpresas según el día del año
regalos_especiales = {
    "14-02": {
        "titulo": "¡Feliz San Valentín! 💖",
        "mensaje": (
            "Aunque todos los días son buenos para decirte lo mucho que"
            " vales, hoy toca recordártelo oficialmente. Eres de lo más bonito"
            " que tengo."
        ),
        "imagen": "https://images.unsplash.com/photo-1518199266791-5375a83190b7",
    },
    "21-09": {
        "titulo": "¡Feliz día de las flores amarillas! 🌻",
        "mensaje": (
            "Dicen que regalar flores amarillas significa que quieres que"
            " alguien se quede para siempre. Te hice este pequeño espacio"
            " digital porque iluminas mis días como nadie."
        ),
        "imagen": "https://images.unsplash.com/photo-1597848212624-a19eb35e2651",
    },
}

# --- INTERFAZ VISUAL ---
st.markdown("<h1>✨ Un rincón especial para ti ✨</h1>", unsafe_allow_html=True)
st.markdown(
    f"<p style='text-align: center; color: #666;'>📅 {fecha_larga}</p>",
    unsafe_allow_html=True,
)

# Contenedor principal con diseño de tarjeta
with st.container():
  st.markdown('<div class="card">', unsafe_allow_html=True)

  if hoy in regalos_especiales:
    regalo = regalos_especiales[hoy]
    st.balloons()  # Lluvia de globos visual en la pantalla
    st.subheader(regalo["titulo"])
    st.write(regalo["mensaje"])

    # Mostramos una imagen bonita relacionada con la fecha
    st.image(regalo["imagen"], use_container_width=True)
  else:
    st.subheader("💌 Mensaje de hoy")
    st.write(
        "Hoy es un día tranquilo, pero quiero recordarte que no hace falta una"
        " fecha especial para sorprenderte."
    )
    st.image(
        "https://images.unsplash.com/photo-1534447677768-be436bb09401",
        use_container_width=True,
    )

  st.markdown("</div>", unsafe_allow_html=True)

# --- SECCIÓN INTERACTIVA PARA GUARDAR DATOS (Tus planes futuros) ---
with st.container():
  st.markdown('<div class="card">', unsafe_allow_html=True)
  st.subheader("💡 Pequeño Buzón de Secretos")
  st.write(
      "Déjame saber un poquito más de ti para planear las siguientes"
      " sorpresas:"
  )

  # Pregunta 1: Guardar una preferencia (ej: su comida o dulce favorito)
  gusto_input = st.text_input(
      "¿Cuál es tu antojo o dulce favorito para nuestra próxima salida? 🍫"
  )
  if st.button("Guardar mi respuesta 🤫", key="btn_gusto"):
    if gusto_input:
      guardar_dato_secreto("Antojo Favorito", gusto_input)
      st.success("¡Guardado! (Ya tomé nota para la próxima 🤭).")
    else:
      st.warning("Escribe algo antes de guardar.")

  st.markdown("---")

  # Pregunta 2: Escoger una opción (para registrar datos estructurados)
  cancion_preferida = st.selectbox(
      "¿Qué tipo de música pega más con este momento?",
      [
          "Romántica / Tranquila 🎸",
          "Pop alegre 🎵",
          "Lo-Fi para relajarse ☕",
          "Sorpréndeme en la próxima 🎧",
      ],
  )
  if st.button("Registrar estilo musical ✨", key="btn_musica"):
    guardar_dato_secreto("Estilo Musical", cancion_preferida)
    st.success("¡Registrado con éxito!")

  st.markdown("</div>", unsafe_allow_html=True)