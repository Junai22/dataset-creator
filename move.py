import os
import shutil

# Ruta del directorio principal
ruta_principal = "C:/Users/Administrator/Downloads/audio/Clips"

# Carpeta de destino para los archivos copiados
carpeta_destino = "C:/Users/Administrator/Downloads/audio/Zip"

# Obtener la lista de carpetas dentro del directorio principal
carpetas = [nombre_carpeta for nombre_carpeta in os.listdir(ruta_principal) if os.path.isdir(os.path.join(ruta_principal, nombre_carpeta))]

# Recorrer las carpetas
for carpeta in carpetas:
    # Ruta completa de la carpeta
    ruta_carpeta = os.path.join(ruta_principal, carpeta)
    
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(ruta_carpeta)
    
    # Recorrer los archivos y copiarlos a la carpeta de destino
    for archivo in archivos:
        ruta_origen = os.path.join(ruta_carpeta, archivo)
        ruta_destino = os.path.join(carpeta_destino, archivo)
        
        # Copiar el archivo a la carpeta de destino
        shutil.copy2(ruta_origen, ruta_destino)
        print(f"Archivo copiado: {ruta_origen} -> {ruta_destino}")
