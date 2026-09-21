import base64
from datetime import datetime
os = __import__("os")
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Caja Fuerte de Sorpresas", page_icon="🔒", layout="centered"
)


# --- FUNCIÓN PARA CONVERTIR IMAGEN A BASE64 ---
def obtener_base64_imagen(ruta_imagen):
  if os.path.exists(ruta_imagen):
    with open(ruta_imagen, "rb") as f:
      data = f.read()
    return base64.b64encode(data).decode("utf-8")
  return ""


# Convertimos las imágenes a base64
heart_base64 = obtener_base64_imagen("heart.png")
src_heart = (
    f"data:image/png;base64,{heart_base64}"
    if heart_base64
    else "https://via.placeholder.com/25"
)

gato_base64 = obtener_base64_imagen("gato_fondo.png")
src_gato = f"data:image/png;base64,{gato_base64}" if gato_base64 else ""

# --- DISEÑO VISUAL: FONDO NEGRO, GATO GIGANTE Y CORAZONES FLOTANTES ---
st.markdown(
    f"""
    <style>
    /* Fondo negro general de la aplicación */
    .stApp {{
        background-color: #0b0b0b;
        color: #ffffff;
    }}
    
    /* Gato gigante de fondo con transparencia */
    .gato-background {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 480px;
        opacity: 0.07; /* Muy sutil de fondo */
        z-index: 0;
        pointer-events: none;
    }}

    /* Asegurar que el contenido esté por encima del fondo */
    .block-container {{
        position: relative;
        z-index: 1;
    }}

    /* Estilo para las tarjetas de contenido estilo gamer/oscuro */
    .card {{
        background-color: rgba(22, 22, 22, 0.95);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #333333;
        box-shadow: 0 8px 20px rgba(0,0,0,0.8);
        margin-bottom: 20px;
    }}
    
    /* Títulos con estilo retro/pixel */
    h1, h3 {{
        color: #ff5252;
        font-family: 'Courier New', monospace;
        text-align: center;
    }}
    
    /* Estilo de los botones */
    .stButton>button {{
        background: linear-gradient(90deg, #ff5252 0%, #c62828 100%);
        color: white;
        border-radius: 25px;
        padding: 10px 25px;
        border: none;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(255, 82, 82, 0.3);
        width: 100%;
    }}
    .stButton>button:hover {{
        background: linear-gradient(90deg, #d32f2f 0%, #b71c1c 100%);
        color: white;
    }}

    /* Animación de corazones flotantes de fondo */
    @keyframes flotar {{
        0% {{ transform: translateY(0vh) scale(0.8); opacity: 0; }}
        50% {{ opacity: 0.7; }}
        100% {{ transform: translateY(-110vh) scale(1.2); opacity: 0; }}
    }}
    
    .corazon-pixel {{
        position: fixed;
        bottom: -10vh;
        width: 25px;
        height: 25px;
        animation: flotar 6s infinite linear;
        z-index: 1;
        user-select: none;
    }}
    </style>

    <!-- Gato gigante de fondo -->
    <img src="{src_gato}" class="gato-background">

    <!-- Corazones flotantes -->
    <img src="{src_heart}" class="corazon-pixel" style="left: 10%; animation-duration: 5s;">
    <img src="{src_heart}" class="corazon-pixel" style="left: 30%; animation-duration: 7s; animation-delay: 1.5s;">
    <img src="{src_heart}" class="corazon-pixel" style="left: 60%; animation-duration: 6s; animation-delay: 2.5s;">
    <img src="{src_heart}" class="corazon-pixel" style="left: 85%; animation-duration: 8s; animation-delay: 1s;">
""",
    unsafe_allow_html=True,
)


# --- FUNCIÓN PARA GUARDAR RESPUESTAS EN FORMATO SOLICITADO ---
def guardar_preferencia_formato(sorpresa, dia_elegido):
  # Formato: "sorpresa que quiere"; "dia elegido"
  registro = f'"{sorpresa}"; "{dia_elegido}"\n'
  with open("registro_sorpresas.csv", "a", encoding="utf-8") as f:
    f.write(registro)


# --- VERIFICACIÓN DE FECHA ---
hoy = datetime.now().strftime("%d-%m")
fecha_larga = datetime.now().strftime("%d/%m/%Y")

calendario_sorpresas = {
    "14-02": {
        "titulo": "San Valentín",
        "password": "tu_contraseña_aqui",
        "mensaje": "Escribe aquí tu mensaje personalizado para esta fecha.",
        "video": "video_san_valentin.mp4",
    },
    "21-09": {
        "titulo": "Día de las Flores Amarillas",
        "password": "Te_Amo",
        "mensaje": (
            "Me gustas hace mucho tiempo y la verdad pensé en hacer algo"
            " especial para ti. Así que aquí tienes tu primera sorpresa,"
            " espero que te guste y que la disfrutes mucho. Con amor, Cristóbal."
        ),
        "video": "video_flores_amarillas.mp4",
    },
}

# --- INTERFAZ VISUAL PRINCIPAL ---
st.markdown("<h1>Caja Fuerte de Sorpresas</h1>", unsafe_allow_html=True)
st.markdown(
    f"<p style='text-align: center; color: #888;'>Fecha actual: {fecha_larga}</p>",
    unsafe_allow_html=True,
)

# Verificar si hoy hay sorpresa programada
if hoy in calendario_sorpresas:
  regalo = calendario_sorpresas[hoy]

  with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(regalo["titulo"])
    st.write(
        "Hay una sorpresa bloqueada para hoy. Introduce la contraseña secreta"
        " para abrirla."
    )

    clave_ingresada = st.text_input("Ingresa la contraseña:", type="password")

    if st.button("Desbloquear sorpresa"):
      if clave_ingresada == regalo["password"]:
        st.success("Contraseña correcta. Desbloqueando regalo...")
        st.balloons()
        st.write(regalo["mensaje"])
        try:
          st.video(regalo["video"])
        except Exception:
          st.warning(
              "No se encontró el archivo de video. Asegúrate de subirlo a"
              " GitHub con el mismo nombre."
          )
      elif clave_ingresada == "":
        st.warning("Por favor, introduce una contraseña.")
      else:
        st.error("Contraseña incorrecta. Inténtalo de nuevo.")
    st.markdown("</div>", unsafe_allow_html=True)

else:
  with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Zona de espera")
    st.write(
        "Hoy es un día tranquilo y no hay cajas fuertes abiertas. Vuelve en"
        " otra fecha especial para descubrir nuevas sorpresas."
    )
    st.markdown("</div>", unsafe_allow_html=True)

# --- SECCIÓN INTERACTIVA: BUZÓN DE SECRETOS ---
with st.container():
  st.markdown('<div class="card">', unsafe_allow_html=True)
  st.subheader("Buzón de Secretos")
  st.write(
      "Cuéntame qué te gustaría para la próxima sorpresa y elige el día"
      " especial:"
  )

  gusto_input = st.text_input(
      "¿Qué sorpresa te gustaría para la próxima?:",
      placeholder="Ej. Una cena, un viaje, chocolates...",
  )
  opcion_preferida = st.selectbox(
      "Elige el día u ocasión preferida:",
      ["Navidad", "Año Nuevo", "San Valentín", "Cumpleaños", "Aniversario"],
  )

  if st.button("Guardar mi respuesta", key="btn_guardar_secreto"):
    if gusto_input:
      guardar_preferencia_formato(gusto_input, opcion_preferida)
      st.success("¡Guardado con éxito! ❤️")
    else:
      st.warning("Por favor escribe algo antes de guardar.")

  st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# PANEL OCULTO PARA EL CREADOR (REVISAR Y DESCARGAR RESPUESTAS)
# ==============================================================================
with st.expander("🛠️ Panel de creador (Oculto)"):
  pass_admin = st.text_input(
      "Clave de administrador:", type="password", key="admin_pass"
  )

  # Cambia 'cristobal123' por la contraseña que tú prefieras
  if pass_admin == "cristobal123":
    st.success("¡Acceso concedido!")

    if os.path.exists("registro_sorpresas.csv"):
      with open("registro_sorpresas.csv", "r", encoding="utf-8") as f:
        contenido = f.read()

      if contenido.strip():
        st.write("### Respuestas registradas hasta ahora:")
        st.code(contenido, language="text")

        with open("registro_sorpresas.csv", "rb") as archivo_csv:
          st.download_button(
              label="📥 Descargar archivo CSV para Drive",
              data=archivo_csv,
              file_name="registro_sorpresas.csv",
              mime="text/csv",
          )
      else:
        st.info(
            "El archivo está vacío, aún no hay respuestas guardadas por este"
            " medio."
        )
    else:
      st.warning(
          "Aún no se ha creado el archivo de registro (nadie ha enviado nada"
          " todavía)."
      )
  elif pass_admin != "":
    st.error("Contraseña incorrecta.")