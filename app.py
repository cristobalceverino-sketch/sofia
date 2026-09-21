import base64
import random
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
        opacity: 0.07;
        z-index: 0;
        pointer-events: none;
    }}

    .block-container {{
        position: relative;
        z-index: 1;
    }}

    .card {{
        background-color: rgba(22, 22, 22, 0.95);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #333333;
        box-shadow: 0 8px 20px rgba(0,0,0,0.8);
        margin-bottom: 20px;
    }}
    
    h1, h3 {{
        color: #ff5252;
        font-family: 'Courier New', monospace;
        text-align: center;
    }}
    
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

    /* Animaciones de ataque para los sprites */
    @keyframes atornillar-jugador {{
        0% {{ transform: translateX(0); }}
        50% {{ transform: translateX(30px) scale(1.05); }}
        100% {{ transform: translateX(0); }}
    }}
    
    @keyframes atornillar-rival {{
        0% {{ transform: translateX(0); }}
        50% {{ transform: translateX(-30px) scale(1.05); }}
        100% {{ transform: translateX(0); }}
    }}

    .sprite-animado-jugador {{
        animation: atornillar-jugador 0.4s ease;
    }}

    .sprite-animado-rival {{
        animation: atornillar-rival 0.4s ease;
    }}

    /* Consola pequeña y discreta para el último ataque del rival */
    .consola-rival {{
        background-color: #111;
        border: 2px solid #ff5252;
        border-radius: 8px;
        padding: 10px 15px;
        font-family: 'Courier New', monospace;
        font-size: 13px;
        color: #ff8a80;
        margin-bottom: 15px;
        text-align: center;
        box-shadow: inset 0 0 10px rgba(255, 82, 82, 0.2);
    }}

    /* Animación de corazones flotantes normales */
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

    <img src="{src_gato}" class="gato-background">

    <!-- Corazones flotantes de fondo base -->
    <img src="{src_heart}" class="corazon-pixel" style="left: 10%; animation-duration: 5s;">
    <img src="{src_heart}" class="corazon-pixel" style="left: 30%; animation-duration: 7s; animation-delay: 1.5s;">
    <img src="{src_heart}" class="corazon-pixel" style="left: 60%; animation-duration: 6s; animation-delay: 2.5s;">
    <img src="{src_heart}" class="corazon-pixel" style="left: 85%; animation-duration: 8s; animation-delay: 1s;">
""",
    unsafe_allow_html=True,
)


# --- FUNCIÓN PARA GUARDAR RESPUESTAS ---
def guardar_preferencia_formato(sorpresa, dia_elegido):
  registro = f'"{sorpresa}"; "{dia_elegido}"\n'
  with open("registro_sorpresas.csv", "a", encoding="utf-8") as f:
    f.write(registro)


# --- VERIFICACIÓN DE FECHA REAL ---
fecha_real = datetime.now().strftime("%d-%m")
fecha_larga = datetime.now().strftime("%d/%m/%Y")

# ==============================================================================
# CALENDARIO DE SORPRESAS
# ==============================================================================
calendario_sorpresas = {
    "14-02": {
        "tipo": "normal",
        "titulo": "San Valentín",
        "password": "tu_contraseña_aqui",
        "mensaje": "Escribe aquí tu mensaje personalizado para esta fecha.",
        "video": "video_san_valentin.mp4",
    },
    "21-09": {
        "tipo": "normal",
        "titulo": "Día de las Flores Amarillas",
        "password": "Te_Amo",
        "mensaje": (
            "Me gustas hace mucho tiempo y la verdad pensé en hacer algo"
            " especial para ti. Así que aquí tienes tu primera sorpresa,"
            " espero que te guste y que la disfrutes mucho. Con amor, Cristóbal."
        ),
        "video": "video_flores_amarillas.mp4",
    },
    "31-10": {
        "tipo": "pareja",
        "titulo": "???",
        "password": "???",
        "poema": (
            '"Desde que te vi senti algo especial en ti,<br>'
            "llegaste a mi vida y todo se volvio mucho mas colorido.<br>"
            "Eres la luz de mis días,<br>"
            'Eres como el sol o la luna una vez miro su esplendor ya no puedo mirar nada mas ."<br><br>'
            "<b>— Con amor, Cristóbal</b>"
        ),
        "pregunta": (
            "Después de todo este tiempo (242 dias) ... ¿Puedo ser tu novio?"
        ),
        "frases_no": [
            "No",
            "¿Segura?",
            "Piénsalo bien...",
            "¡Dale al otro botón!",
            "Te vas a arrepentir :O",
            "Imposible aceptar esto",
            "¡El botón de al lado es mejor!",
        ],
        "musica_romantica": "musica_romantica.mp3",
        "musica_triste": "musica_triste.mp3",  # Canción triste al agotar los No
        "musica_batalla": "musica_pokemon.mp3",
        "pokemon_jugador": "Pikachu",
        "sprite_jugador": (
            "https://play.pokemonshowdown.com/sprites/gen5/pikachu.png"
        ),
        "pokemon_rival": "Sylveon",
        "sprite_rival": (
            "https://play.pokemonshowdown.com/sprites/gen5/sylveon.png"
        ),
        "sprite_premio": (
            "https://play.pokemonshowdown.com/sprites/gen5/jigglypuff.png"
        ),
        "pokemon_premio": (
            "¡Has ganado, aquí está tu premio! Una cita especial o regalito"
            " por desbloquear mi corazón."
        ),
    },
}

# --- INTERFAZ VISUAL PRINCIPAL ---
st.markdown("<h1>Caja Fuerte</h1>", unsafe_allow_html=True)

# ==============================================================================
# PANEL OCULTO PARA EL CREADOR (ADMINISTRADOR)
# ==============================================================================
with st.expander("Panel de creador (Oculto)"):
  pass_admin = st.text_input(
      "Clave de administrador:", type="password", key="admin_pass"
  )

  if pass_admin == "NEOX":
    st.success("¡Acceso concedido!")

    st.markdown("---")
    st.subheader("Herramientas de Prueba")

    modo_prueba = st.selectbox(
        "Selecciona qué fecha quieres probar:",
        [
            "Fecha real (Automática)",
            "14-02 (San Valentín)",
            "21-09 (Flores Amarillas)",
            "31-10 (Pregunta de Pareja)",
            "Día sin sorpresas (Zona de espera)",
        ],
    )

    if modo_prueba == "14-02 (San Valentín)":
      hoy = "14-02"
    elif modo_prueba == "21-09 (Flores Amarillas)":
      hoy = "21-09"
    elif modo_prueba == "31-10 (Pregunta de Pareja)":
      hoy = "31-10"
    elif modo_prueba == "Día sin sorpresas (Zona de espera)":
      hoy = "00-00"
    else:
      hoy = fecha_real

    st.markdown("---")
    st.subheader("Gestión de Respuestas")

    if os.path.exists("registro_sorpresas.csv"):
      with open("registro_sorpresas.csv", "r", encoding="utf-8") as f:
        contenido = f.read()

      if contenido.strip():
        st.write("### Respuestas registradas hasta ahora:")
        st.code(contenido, language="text")

        with open("registro_sorpresas.csv", "rb") as archivo_csv:
          st.download_button(
              label="Descargar archivo CSV para Drive",
              data=archivo_csv,
              file_name="registro_sorpresas.csv",
              mime="text/csv",
          )

        if st.button("🗑️ Borrar todas las respuestas registradas"):
          with open("registro_sorpresas.csv", "w", encoding="utf-8") as f:
            f.write("")
          st.success("¡El archivo de respuestas ha sido limpiado con éxito!")
          st.rerun()
      else:
        st.info("El archivo está vacío, no hay respuestas guardadas.")
    else:
      st.warning("Aún no se ha creado el archivo de registro.")
  else:
    hoy = fecha_real
    if pass_admin != "":
      st.error("Contraseña incorrecta.")

st.markdown(
    f"<p style='text-align: center; color: #888;'>Fecha actual simulada: {hoy}</p>",
    unsafe_allow_html=True,
)

# Verificar si hoy hay sorpresa programada
if hoy in calendario_sorpresas:
  regalo = calendario_sorpresas[hoy]

  with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(regalo["titulo"])

    # SI ES LA FECHA ESPECIAL DE PAREJA (31 DE OCTUBRE)
    if regalo.get("tipo") == "pareja":
      if "fase_31" not in st.session_state:
        st.session_state["fase_31"] = "bloqueado"

      # 1. FASE DE CONTRASEÑA
      if st.session_state["fase_31"] == "bloqueado":
        st.write(
            "Hay una caja misteriosa bloqueada para hoy. Introduce la contraseña"
            " secreta para descubrir lo que hay dentro..."
        )
        clave_ingresada = st.text_input("Ingresa la contraseña:", type="password")

        if st.button("Desbloquear sorpresa"):
          if clave_ingresada == regalo["password"]:
            st.session_state["fase_31"] = "poema"
            st.rerun()
          else:
            st.error("Contraseña incorrecta. ¡Inténtalo de nuevo!")

      # 2. FASE DEL POEMA Y PREGUNTA
      elif st.session_state["fase_31"] in [
          "poema",
          "exito_aceptado",
          "rechazo_final",
      ]:
        if st.session_state["fase_31"] == "rechazo_final":
          try:
            st.audio(regalo["musica_triste"], autoplay=True, loop=True)
          except Exception:
            pass
        else:
          try:
            st.audio(regalo["musica_romantica"], autoplay=True, loop=True)
          except Exception:
            pass

        st.success("¡Contraseña correcta! Desbloqueando momento especial...")

        st.markdown("---")
        st.markdown("### Una pequeña cuenta regresiva hacia tu corazón...")
        st.info(
            "Cada segundo que pasa desde que nos conocimos ha valido la pena"
            " por completo..."
        )

        st.markdown("---")
        st.markdown("### Para ti, con todo mi amor:")
        st.markdown(
            f"""
            <div style='text-align: center; font-style: italic; color: #ff8a80; font-size: 18px; line-height: 1.6;'>
                {regalo["poema"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")
        st.markdown("### La Pregunta Más Importante...")
        st.write(regalo["pregunta"])

        if st.session_state["fase_31"] == "exito_aceptado":
          st.success(
              "¡Has aceptado ser mi novio! Tu respuesta ya ha sido guardada"
              " con éxito."
          )
          st.write(
              "¿Quieres pasar el rato y jugar una batalla Pokémon de bonificación"
              "?"
          )
          if st.button("¡Iniciar Combate Pokémon!"):
            st.session_state["fase_31"] = "batalla_pokemon"
            st.session_state["hp_rival"] = 100
            st.session_state["hp_usuario"] = 100
            st.session_state["ultimo_movimiento_rival"] = (
                "¡El combate está por empezar!"
            )
            st.session_state["animacion_sprite"] = "ninguna"
            st.rerun()

        elif st.session_state["fase_31"] == "rechazo_final":
          st.warning(
              "Has presionado el último 'No'... aunque duele, respeto tu"
              " decisión. ¡Gracias por llegar hasta aquí y por todo este tiempo"
              " juntos!"
          )
          st.write(
              "*(Se ha registrado tu respuesta final en el sistema con una"
              " melodía nostálgica)*"
          )

        else:
          if "contador_no" not in st.session_state:
            st.session_state["contador_no"] = 0

          frases_no = regalo["frases_no"]
          indice_actual = st.session_state["contador_no"]
          texto_actual_no = frases_no[min(indice_actual, len(frases_no) - 1)]

          ancho_si = min(2 + (st.session_state["contador_no"] * 2), 10)
          ancho_no = max(4 - st.session_state["contador_no"], 1)

          col1, col2 = st.columns([ancho_si, ancho_no])

          with col1:
            if st.button("¡SÍ, QUIERO!"):
              guardar_preferencia_formato(
                  "Aceptó ser mi novio", "31 de Octubre"
              )
              st.session_state["fase_31"] = "exito_aceptado"
              st.rerun()

          with col2:
            if st.button(texto_actual_no, key="btn_rechazo"):
              # Validar si es el último botón de "No" de la lista
              if indice_actual >= len(frases_no) - 1:
                guardar_preferencia_formato(
                    "Dijo que NO hasta el final", "31 de Octubre"
                )
                st.session_state["fase_31"] = "rechazo_final"
              else:
                st.session_state["contador_no"] += 1
              st.rerun()

      # 3. FASE DE LA BATALLA POKÉMON CON CONSOLA Y ANIMACIÓN DE SPRITES
      elif st.session_state["fase_31"] == "batalla_pokemon":
        try:
          st.audio(regalo["musica_batalla"], autoplay=True, loop=True)
        except Exception:
          pass

        st.markdown("## COMBATE POKÉMON DIFÍCIL")
        st.write(
            f"¡Un **{regalo['pokemon_rival']}** salvaje muy fuerte apareció!"
        )

        hp_r = st.session_state["hp_rival"]
        hp_u = st.session_state["hp_usuario"]

        st.markdown(
            f"""
            <div class="consola-rival">
                🖥️ CONSOLA RIVAL: {st.session_state.get('ultimo_movimiento_rival', 'Esperando movimiento...')}
            </div>
            """,
            unsafe_allow_html=True,
        )

        anim = st.session_state.get("animacion_sprite", "ninguna")
        clase_jugador = (
            "sprite-animado-jugador" if anim == "jugador" else ""
        )
        clase_rival = "sprite-animado-rival" if anim == "rival" else ""

        col_sprite_r, col_info_r = st.columns([1, 2])
        with col_sprite_r:
          st.markdown(
              f'<div class="{clase_rival}">', unsafe_allow_html=True
          )
          st.image(regalo["sprite_rival"], width=120)
          st.markdown("</div>", unsafe_allow_html=True)
        with col_info_r:
          st.markdown(f"**Rival: {regalo['pokemon_rival']} (Lv. 50)**")
          st.text(f"HP: {hp_r}%")

        st.markdown("---")

        col_info_u, col_sprite_u = st.columns([2, 1])
        with col_info_u:
          st.markdown(f"**Tu equipo: {regalo['pokemon_jugador']} (Lv. 50)**")
          st.text(f"HP: {hp_u}%")
        with col_sprite_u:
          st.markdown(
              f'<div class="{clase_jugador}">', unsafe_allow_html=True
          )
          st.image(regalo["sprite_jugador"], width=120)
          st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.write("### Elige tu movimiento (4 Ataques reales):")

        def procesar_turno_jugador(danio_jugador):
          st.session_state["hp_rival"] -= danio_jugador
          st.session_state["animacion_sprite"] = "jugador"

          if st.session_state["hp_rival"] <= 0:
            st.session_state["hp_rival"] = 0
            st.session_state["fase_31"] = "victoria"
          else:
            ataques_rival = [
                ("Fuerza Lunar", 20),
                ("Voz Cautivadora", 15),
                ("Besos Drenaje", 25),
                ("Rapidez", 18),
            ]
            nombre_atq, danio_atq = random.choice(ataques_rival)
            st.session_state["hp_usuario"] -= danio_atq
            st.session_state["animacion_sprite"] = "rival"
            st.session_state["ultimo_movimiento_rival"] = (
                f"¡{regalo['pokemon_rival']} usó {nombre_atq} y te causó"
                f" {danio_atq}% de daño!"
            )

            if st.session_state["hp_usuario"] <= 0:
              st.session_state["hp_usuario"] = 0
              st.session_state["fase_31"] = "derrota"
          st.rerun()

        col_atq1, col_atq2 = st.columns(2)
        with col_atq1:
          if st.button("Impactrueno"):
            procesar_turno_jugador(20)

          if st.button("Ataque Rápido"):
            procesar_turno_jugador(15)

        with col_atq2:
          if st.button("Cola Férrea"):
            procesar_turno_jugador(30)

          if st.button("Rayo"):
            procesar_turno_jugador(35)

      # 4. FASE DE DERROTA EN LA BATALLA
      elif st.session_state["fase_31"] == "derrota":
        st.error(
            f"¡Tu {regalo['pokemon_jugador']} se quedó sin energía contra"
            f" {regalo['pokemon_rival']}!"
        )
        if st.button("Reintentar Combate"):
          st.session_state["hp_rival"] = 100
          st.session_state["hp_usuario"] = 100
          st.session_state["ultimo_movimiento_rival"] = (
              "¡Nuevo intento de combate!"
          )
          st.session_state["fase_31"] = "batalla_pokemon"
          st.rerun()

      # 5. FASE DE VICTORIA (MUESTRA SPRITE SELECCIONADO Y PREMIO)
      elif st.session_state["fase_31"] == "victoria":
        st.balloons()
        st.markdown(
            f"<h2 style='text-align: center; color: #ff5252;'>¡VICTORIA!</h2>",
            unsafe_allow_html=True,
        )

        col_img_premio, col_txt_premio = st.columns([1, 2])
        with col_img_premio:
          st.image(regalo["sprite_premio"], width=130)
        with col_txt_premio:
          st.success(regalo["pokemon_premio"])

        st.markdown("---")
        st.write(
            "¡Muchas gracias por aceptar ser mi novio! Eres lo mejor de mi"
            " mundo."
        )

    else:
      # DÍAS NORMALES
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
      placeholder="Ej. Un poema, Un regalo, etc...",
  )
  opcion_preferida = st.selectbox(
      "Elige el día u ocasión preferida:",
      ["Navidad", "Año Nuevo", "San Valentín", "Cumpleaños"],
  )

  if st.button("Guardar mi respuesta", key="btn_guardar_secreto"):
    if gusto_input:
      guardar_preferencia_formato(gusto_input, opcion_preferida)
      st.success("¡Guardado con éxito!")
    else:
      st.warning("Por favor escribe algo antes de guardar.")

  st.markdown("</div>", unsafe_allow_html=True)