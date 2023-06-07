import os

# Ruta del directorio principal
ruta_principal = "C:/Users/Administrator/Downloads/audio/Clips"

# Obtener la lista de carpetas dentro del directorio principal
carpetas = [nombre_carpeta for nombre_carpeta in os.listdir(ruta_principal) if os.path.isdir(os.path.join(ruta_principal, nombre_carpeta))]

# Recorrer las carpetas
for carpeta in carpetas:
    # Ruta completa de la carpeta
    ruta_carpeta = os.path.join(ruta_principal, carpeta)
    
    # Obtener el nombre de la carpeta
    nombre_carpeta = os.path.basename(ruta_carpeta)
    
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(ruta_carpeta)
    
    # Recorrer los archivos y renombrar los que cumplen el patrón
    for archivo in archivos:
        if archivo.startswith("clip"):
            # Obtener el número del archivo
            numero = archivo[4:]  # Se asume que el número comienza en el índice 4 hasta el final
            
            # Nuevo nombre de archivo con el nombre de la carpeta y el número
            nuevo_nombre = f"{nombre_carpeta}_{numero}"
            
            # Ruta del archivo original y del archivo con el nuevo nombre
            ruta_original = os.path.join(ruta_carpeta, archivo)
            ruta_nuevo = os.path.join(ruta_carpeta, nuevo_nombre)
            
            # Renombrar el archivo
            os.rename(ruta_original, ruta_nuevo)
            print(f"Archivo renombrado: {ruta_original} -> {ruta_nuevo}")
