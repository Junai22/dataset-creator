import os
import subprocess
import shutil

# Ruta de la carpeta de entrada con archivos .m4a
carpeta_entrada = "input/"

# Ruta de la carpeta de salida para las pistas vocales separadas
carpeta_salida = "output/"

# Ruta de la carpeta de destino para las pistas vocales renombradas
carpeta_destino = "tracks/"

# Crear la carpeta de salida si no existe
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# Obtener la lista de archivos .m4a en la carpeta de entrada
archivos_m4a = [archivo for archivo in os.listdir(carpeta_entrada) if archivo.endswith(".m4a")]

# Recorrer los archivos .m4a y separar las pistas vocales
for archivo_m4a in archivos_m4a:
    # Rutas de archivo de entrada y salida
    ruta_entrada = os.path.join(carpeta_entrada, archivo_m4a)
    ruta_salida = os.path.join(carpeta_salida, archivo_m4a)
    
    # Comando para separar las pistas vocales utilizando Spleeter
    comando = f"spleeter separate -o {carpeta_salida} {ruta_entrada}"
    
    # Ejecutar el comando en el sistema operativo
    subprocess.run(comando, shell=True)
    
    print(f"Pistas vocales separadas para: {archivo_m4a}")
    
    # Obtener el nombre de archivo original sin extensión
    nombre_original = os.path.splitext(archivo_m4a)[0]
    
    # Ruta de la carpeta de salida para la pista vocal renombrada
    carpeta_pista = os.path.join(carpeta_salida, nombre_original)
    
    # Ruta del archivo "vocals.wav"
    ruta_vocals = os.path.join(carpeta_pista, "vocals.wav")
    
    # Ruta de destino para la pista vocal renombrada
    ruta_destino = os.path.join(carpeta_destino, f"{nombre_original}.wav")
    
    # Copiar el archivo "vocals.wav" a la carpeta de destino con el nombre renombrado
    shutil.copy2(ruta_vocals, ruta_destino)
    
    print(f"Pista vocal renombrada copiada: {ruta_vocals} -> {ruta_destino}")
