#Librerias (Para abrir archivos)
from cmath import exp
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
    mensaje = ""
    flagmes = False
    flagaño = False
    flagitems = False
    ## [Espacios Vacios] ##
    if (mes == "" or mes == " " or mes == "  "):
        flagmes = True
        mensaje += "En el archivo .data No se agrego el Mes, porfavor indicar el mes en el archivo .data"
    if (año == "" or año == " " or año == "  "):
        flagaño = True
        mensaje += "En el archivo .data No se agrego el Año, porfavor indicar el año en el archivo .data"
    if (items == []):
        flagitems = True
        mensaje += "No hay Productos a inspeccionar en el archivo .data"
    ## [Valida mes] ##
    if ( len(mes) > 11):
        flagmes = True
        mensaje += "El mes escrito no funciona favor revisarlo"
    ## [Validar Tipo] ##
    #Mes
    try:
        mes = int(mes)
        mensaje += "El mes debe de ser texto y no un numero"
        flagmes = True
    except:
        pass
    #Año
    try:
        año = str(año)
    except:
        mensaje += "El año debe de ser texto."
        flagaño = True
    #Items
    contador = -1
    for producto in items:
        contador += 1
        #Nombre
        try:
            producto.setnombre(str(producto.nombre))
        except:
            mensaje += "El nombre del producto No." + str(contador) + " No se puedo convertir a texto"
            flagitems = True
        #Costo
        try:
            if str(producto.precio) ==  " " or str(producto.precio) ==  "" or str(producto.precio) ==  "  " :
                producto.setprecio(float(0))
            producto.setprecio(float(producto.precio))
        except:
            mensaje += "El precio del producto No." + str(contador) + " No se puedo convertir a float"
            flagitems = True
        #Cantidad
        try:
            if str(producto.cantidad) ==  " " or str(producto.cantidad) ==  "" or str(producto.cantidad) ==  "  " :
                producto.setcantidad(int(0))

            producto.setcantidad(int(producto.cantidad))
        except:
            mensaje += "La cantidad del producto No." + str(contador) + " No se puedo convertir a entero porque no lo es."
            flagitems = True

    if flagitems == False and flagaño == False and flagmes == False:
        mensaje = "OK"
        print("Verificacion Terminada... [ OK ]")
    
    # #Imprimir Items
    # for product in items:
    #     print(product.imprimir())
    
    

    return mensaje

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
    
    cont = 0
    while True:
        ################
        Funcionesgenerales.mensajebienvenida()
        
        ## [ .DATA ] ##
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
            Validadormensaje = validardatos(Mes, Año, Items)
            print("Validador: ",Validadormensaje)
            if Validadormensaje == "OK":
                pass
            else:
                print("Error")
                break
        else:
            print("El archivo no tiene ningun dato a inspeccionar")
            break

        
        #Fin While
        cont += 1
        print(cont)
        if (cont >= 1):
            print("fin")
            break
    


    