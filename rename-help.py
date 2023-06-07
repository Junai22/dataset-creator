import os

# Directorio donde se encuentran los archivos .wav
directorio = "C:/Users/Administrator/Downloads/audio/Acapella"

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Recorrer los archivos y renombrar los que tienen extensión .wav
for archivo in archivos:
    if archivo.endswith(".wav"):
        # Nuevo nombre de archivo con espacios reemplazados por guiones bajos
        nuevo_nombre = archivo.replace(" ", "_")
        
        # Ruta del archivo original y del archivo con el nuevo nombre
        ruta_original = os.path.join(directorio, archivo)
        ruta_nuevo = os.path.join(directorio, nuevo_nombre)
        
        # Renombrar el archivo
        os.rename(ruta_original, ruta_nuevo)
        print(f"Archivo renombrado: {ruta_original} -> {ruta_nuevo}")
