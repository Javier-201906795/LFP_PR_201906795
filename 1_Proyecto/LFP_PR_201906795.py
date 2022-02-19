#Librerias (Para abrir archivos)
from tkinter import filedialog, Tk
#Importaciones Funciones
from FuncionesGenerales import FuncionesGenerales
from FuncionesData import FuncionesData

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
        #Imprime
        print("\n----------------- [ .DATA ] ------------------------")
        print(text)
        print("------------------------------------------------ \n")
        return text

    
################################################################

def validardatos(mes, año, items):
    ## [Espacios Vacios] ##
    if (mes == "" or mes == " " or mes == "  "):
        print("En el archivo .data No se agrego el Mes, porfavor indicar el mes en el archivo .data")
    if (año == "" or año == " " or año == "  "):
        print("En el archivo .data No se agrego el Año, porfavor indicar el año en el archivo .data")
    if (items == []):
        print("No hay Productos a inspeccionar en el archivo .data")

    return None

################################################################
################################################################
#Main program
if __name__ == "__main__":

    #Importaciones
    Funcionesgenerales = FuncionesGenerales()
    Funcionesdata = FuncionesData()

    #Variables
    Mes = "N/A"
    Año = "N/A"
    Items = []
    
    ################
    Funcionesgenerales.mensajebienvenida()
    #[ Abrir archivo Data]#
    datatexto1 = abrirarchivodata()
    #[ Inspeccionar Elementos ]#
    if datatexto1 is not None:
        #Guardar Texto a inspeccionar 
        Funcionesdata.setdatatexto1(datatexto1)
        #Clasifica las variables
        Funcionesdata.clasificador()
        #Guardar Variables
        Mes = Funcionesdata.getMes()
        Año = Funcionesdata.getAño()
        Items = Funcionesdata.getItems()
        #Validar variables
        validardatos(Mes, Año, Items)
        
    else:
        print("El archivo no tiene ningun dato a inspeccionar")
    
    

    


    