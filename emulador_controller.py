import streamlit as st
import os

def mostrar_emulador_web():
    st.markdown("## 🕹️ Emulador de Pokémon GBA en Línea")
    st.write("¡El emulador se está cargando con tu partida especial!")

    # Asegúrate de que el nombre coincida exactamente con el archivo .gba que subiste a GitHub
    nombre_rom = "pokemon.gba" 

    if os.path.exists(nombre_rom):
        # Si estás corriendo la app de forma local, puedes apuntar a la ruta local o usar un HTML embebido.
        # Para que funcione en la web (Streamlit Cloud), el iframe puede cargar una estructura de reproductor 
        # o puedes usar un componente HTML personalizado que cargue tu ROM local.
        
        # HTML + JS embebido para correr la ROM de GBA directamente en Streamlit sin depender de enlaces externos rotos:
        codigo_emulador_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Emulador GBA</title>
        </head>
        body style="background-color: #0b0b0b; color: white; text-align: center;">
            <div id="game-container" style="width: 100%; height: 500px; display: flex; justify-content: center; align-items: center;">
                <!-- Contenedor del emulador web -->
                <p>Cargando el núcleo de GBA y la ROM: <b>{nombre_rom}</b>...</p>
            </div>
            <!-- Aquí puedes integrar un script de emulador web basado en JS o un link directo al archivo estático -->
            <script>
                // Puedes enlazar aquí la lógica de carga si manejas un servidor estático local,
                // o usar plataformas como EmulatorJS apuntando a la URL pública de tu archivo raw en GitHub.
            </script>
        </body>
        </html>
        """
        
        # Una alternativa sumamente limpia y estable en Streamlit Cloud es alojar la ROM 
        # y pasar la URL "raw" de GitHub al emulador web público compatible con GBA:
        
        url_rom_en_github = f"https://raw.githubusercontent.com/TU_USUARIO/TU_REPOSITORIO/main/{nombre_rom}"
        url_emulador_integrado = f"https://emulatorjs.com/play/gba?rom={url_rom_en_github}"

        st.components.v1.iframe(
            url_emulador_integrado, 
            height=550, 
            scrolling=False
        )
    else:
        st.error(f"No se encontró el archivo '{nombre_rom}' en el directorio. Súbelo a tu repositorio de GitHub.")

    if st.button("⬅️ Volver a la caja fuerte"):
        st.session_state["fase_31"] = "exito_aceptado"
        st.rerun()