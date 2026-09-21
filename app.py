import base64
from datetime import datetime
import os
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


# Convertimos la imagen 'heart.png' a base64
heart_base64 = obtener_base64_imagen("heart.png")
src_imagen = (
    f"data:image/png;base64,{heart_base64}"
    if heart_base64
    else "https://via.placeholder.com/25"
)

# --- DISEÑO VISUAL: FONDO NEGRO Y CORAZONES FLOTANTES ---
st.markdown(
    f"""
    <style>
    /* Fondo negro general de la aplicación */
    .stApp {{
        background-color: #0b0b0b;
        color: #ffffff;
    }}
    
    /* Estilo para las tarjetas de contenido estilo gamer/oscuro */
    .card {{
        background-color: #161616;
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
        50% {{ opacity: 0.9; }}
        100% {{ transform: translateY(-110vh) scale(1.2); opacity: 0; }}
    }}
    
    .corazon-pixel {{
        position: fixed;
        bottom: -10vh;
        width: 25px;
        height: 25px;
        animation: flotar 6s infinite linear;
        z-index: 999;
        user-select: none;
    }}
    </style>

    <!-- Corazones flotantes usando la imagen en Base64 -->
    <img src="{src_imagen}" class="corazon-pixel" style="left: 10%; animation-duration: 5s;">
    <img src="{src_imagen}" class="corazon-pixel" style="left: 30%; animation-duration: 7s; animation-delay: 1.5s;">
    <img src="{src_imagen}" class="corazon-pixel" style="left: 60%; animation-duration: 6s; animation-delay: 2.5s;">
    <img src="{src_imagen}" class="corazon-pixel" style="left: 85%; animation-duration: 8s; animation-delay: 1s;">
""",
    unsafe_allow_html=True,
)


# --- FUNCIÓN PARA GUARDAR DATOS (Para tus planes futuros) ---
def guardar_dato_secreto(categoria, valor):
  fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
  registro = f"[{fecha_actual}] Categoria: {categoria} | Dato: {valor}\n"

  with open("datos_sorpresas_futuras.txt", "a", encoding="utf-8") as f:
    f.write(registro)


# --- VERIFICACIÓN DE FECHA ---
hoy = datetime.now().strftime("%d-%m")
fecha_larga = datetime.now().strftime("%d/%m/%Y")

# ==============================================================================
# AQUÍ PUEDES PERSONALIZAR LAS FECHAS, CONTRASEÑAS, TÍTULOS Y MENSAJES A TU GUSTO
# ==============================================================================
calendario_sorpresas = {
    "14-02": {
        "titulo": "San Valentin",
        "password": "tu_contraseña_aqui",  # Cambia por tu clave secreta
        "mensaje": "Escribe aqui tu mensaje personalizado para esta fecha.",
        "video": "video_san_valentin.mp4",
    },
    "21-09": {
        "titulo": "Dia de las Flores Amarillas",
        "password": "Te_Amo",  # Cambia por tu clave secreta
        "mensaje": (
            "Me gustas hace mucho tiempo y la verdad pense en hacer algo especial para ti. "
            " asi que aqui tienes tu primer sorpresa, espero que te guste y que la disfrutes mucho. Con amor, cristobal."
        ),
        "video": (  # Nombre de tu video subido a GitHub (ej: caramelldansen.mp4)
            "video_flores_amarillas.mp4"
        ),
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

    # Input de contraseña
    clave_ingresada = st.text_input("Ingresa la contraseña:", type="password")

    if st.button("Desbloquear sorpresa"):
      if clave_ingresada == regalo["password"]:
        st.success("Contraseña correcta. Desbloqueando regalo...")
        st.balloons()
        st.write(regalo["mensaje"])

        # Reproductor de video personalizado
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
        st.error("Contraseña incorrecta. Intentalo de nuevo.")

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

# --- SECCIÓN INTERACTIVA PARA GUARDAR DATOS (Tus planes futuros) ---
with st.container():
  st.markdown('<div class="card">', unsafe_allow_html=True)
  st.subheader("Buzón de Secretos")
  st.write("Déjame saber un poquito más para planear las siguientes sorpresas:")

  gusto_input = st.text_input("Escribe algo que te guste para la proxima:")
  if st.button("Guardar mi respuesta", key="btn_gusto"):
    if gusto_input:
      guardar_dato_secreto("Preferencia", gusto_input)
      st.success("Guardado con exito.")
    else:
      st.warning("Escribe algo antes de guardar.")

  st.markdown("---")

  opcion_preferida = st.selectbox(
      "Elige una opcion:",
      [
          "navidad",
          "Año Nuevo",
          "San Valentin",
          "Cumpleaños",
      ],
  )
  if st.button("Registrar seleccion", key="btn_opcion"):
    guardar_dato_secreto("Seleccion", opcion_preferida)
    st.success("Registrado con exito.")

  st.markdown("</div>", unsafe_allow_html=True)