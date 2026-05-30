import os
import shutil

def organizar_carpeta(ruta_carpeta):
    # Diccionario con las extensiones y sus carpetas correspondientes
    extensiones_carpetas = {
        'Documentos': ['.docx', '.txt', '.xlsx', '.pptx'],
        'PDFs': ['.pdf'],
        'Imagenes': ['.jpg', '.jpeg', '.png', '.gif'],
        'Instaladores': ['.exe', '.msi', '.dmg']
    }

    # Verificar si la ruta existe
    if not os.path.exists(ruta_carpeta):
        print(f"La ruta {ruta_carpeta} no existe.")
        return

    # Recorrer los archivos de la carpeta
    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        
        # Saltarse si es una carpeta
        if os.path.isdir(ruta_archivo):
            continue
            
        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo)
        extension = extension.lower()

        # Buscar a qué carpeta pertenece el archivo
        movido = False
        for nombre_carpeta, extensiones in extensiones_carpetas.items():
            if extension in extensiones:
                # Crear la carpeta de destino si no existe
                carpeta_destino = os.path.join(ruta_carpeta, nombre_carpeta)
                os.makedirs(carpeta_destino, exist_ok=True)
                
                # Mover el archivo
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                print(f"Movido: {archivo} -> {nombre_carpeta}/")
                movido = True
                break
        
        if not movido:
            print(f"No se clasificó: {archivo} (extensión no registrada)")

if __name__ == "__main__":
    # Puedes cambiar '.' por la ruta de la carpeta que quieras organizar
    ruta_a_organizar = "./mi_carpeta_desordenada"
    
    # Crear una carpeta de prueba por si acaso
    os.makedirs(ruta_a_organizar, exist_ok=True)
    print(f"Organizando la carpeta: {ruta_a_organizar}")
    organizar_carpeta(ruta_a_organizar)