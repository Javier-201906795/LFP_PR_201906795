#Librerias (Para abrir archivos)
from tkinter import filedialog, Tk
#Importaciones Funciones
from FuncionesGenerales import FuncionesGenerales

################################################################
def abrirarchivodata():
    archivo = filedialog.askopenfilename(
        title = "Selecciona un archivo",
        #accede a la carpeta donde esta el archivo 
        initialdir =  "./",
        #tipo de archivo que puede seleccionar
        filetype = [
            ("Archivos DATA", "*.data"),
            ("Todos los archivos", "*.*")
        ]
    )


    if archivo is None:
        print("No se selecciono ningun archivo" + "\n")
        return None
    else:
        #Abre el archivo
        with open(archivo, 'r', encoding='utf8') as file:
            text = file.read()
            file.close()
        return text

    
################################################################
################################################################
#Main program
if __name__ == "__main__":

    #Importaciones
    Funcionesgenerales = FuncionesGenerales()

    
    ################
    Funcionesgenerales.mensajebienvenida()
    #[ Abrir archivo Data]#
    datatexto1 = abrirarchivodata()
    print(datatexto1)

    


    