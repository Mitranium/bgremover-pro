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
    # Carga la imagen original
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen original", use_column_width=True)
    
    # Procesa: quita fondo
    with st.spinner("Removiendo fondo... (tarda unos segs)"):
        input_bytes = io.BytesIO(uploaded_file.read())
        output_bytes = remove(input_bytes.read())
        output_image = Image.open(io.BytesIO(output_bytes))
    
    # Muestra resultado
    st.image(output_image, caption="Imagen sin fondo", use_column_width=True)
    
    # Descarga
    buf = io.BytesIO()
    output_image.save(buf, format='PNG')
    byte_im = buf.getvalue()
    st.download_button(
        label="Descargar imagen limpia",
        data=byte_im,
        file_name="imagen_sin_fondo.png",
        mime="image/png"
    )
else:
    st.info("👆 Sube una imagen para empezar. Prueba con una foto de producto.")
