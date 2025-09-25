import streamlit as st
from rembg import remove
from PIL import Image
import io

# Título de la app
st.title("🖼️ BGRemover Pro – Limpia fondos de imágenes al instante")
st.write("Sube una imagen de producto y quita el fondo gratis. Ideal para e-commerce.")

# Upload de archivo
uploaded_file = st.file_uploader("Elige una imagen (PNG, JPG)", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Lee el archivo UNA vez en bytes (evita bugs de lectura doble)
    file_bytes = uploaded_file.read()
    
    if len(file_bytes) == 0:
        st.error("¡Ups! El archivo parece vacío o corrupto. Prueba con otra imagen.")
    else:
        try:
            # Carga la imagen original desde bytes
            image = Image.open(io.BytesIO(file_bytes))
            st.image(image, caption="Imagen original", use_container_width=True)
            
            # Procesa: quita fondo (rembg toma bytes directos)
            with st.spinner("Removiendo fondo... (tarda unos segs)"):
                output_bytes = remove(file_bytes)
                output_image = Image.open(io.BytesIO(output_bytes))
            
            # Muestra resultado
            st.image(output_image, caption="Imagen sin fondo", use_container_width=True)
            
            # Descarga
            st.download_button(
                label="Descargar imagen limpia",
                data=output_bytes,
                file_name="imagen_sin_fondo.png",
                mime="image/png"
            )
        except Exception as e:
            st.error(f"Error al procesar: {str(e)}. Asegúrate de que sea una imagen válida (no ZIP ni otros formatos).")
else:
    st.info("👆 Sube una imagen para empezar. Prueba con una foto de producto.")
