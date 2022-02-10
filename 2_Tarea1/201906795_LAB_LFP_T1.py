#Librerias (Para abrir archivos)
from tkinter import filedialog, Tk

#Configuracion librerias explorador de archivos
def abrirarchivo():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Selecciona un archivo",
        #accede a la carpeta donde esta el archivo py
        initialdir =  "./",
        #tipo de archivo que puede seleccionar
        filetype = [
            ("Archivos LFP", "*.lfp"),
            ("Todos los archivos", "*.*")
        ]
    )

    #Leer archivo
    if archivo is None:
        print("No se selecciono ningun archivo" + "\n")
        return None
    else:
        #Devolver Texto del archivo
        txt = archivo.read()
        archivo.close()
        return txt


#Main program
if __name__ == "__main__":
    #cargar el archivo lfp con el texto a inspeccionar
    texto = abrirarchivo()

    #inspeccionarmos si existe algun texto
    if texto is not None:
        #si tiene mas de 0 caracteres
        if (len(texto)>0):
            print(texto)
        else:
            print("Error T2: No hay texto en el archivo seleccionado")
    else:
        print("Error T1: No se puede procesar \n")

    
