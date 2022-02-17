#Librerias (Para abrir archivos)
from tkinter import filedialog, Tk
#Importaciones Funciones
from FuncionesGenerales import FuncionesGenerales
from Modulos import Modulos

################################################################
#Configuracion librerias explorador de archivos
def abrirarchivodata():
    #Mesaje
    print("Selecciona el archivo .data y cargalo en el programa")
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Selecciona un archivo",
        #accede a la carpeta donde esta el archivo py
        initialdir =  "./",
        #tipo de archivo que puede seleccionar
        filetype = [
            ("Archivos DATA", "*.data"),
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

################################################################
################################################################
#Main program
if __name__ == "__main__":

    #Importaciones
    Funcionesgenerales = FuncionesGenerales()
    Funciones = Modulos()

    

    
    Funcionesgenerales.mensajebienvenida()
    
    datatexto1 = abrirarchivodata()

    print(datatexto1)


    