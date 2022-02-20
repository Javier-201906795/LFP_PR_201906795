#Librerias (Para abrir archivos)
from cmath import exp
from tkinter import filedialog, Tk, Label, Button

#Importaciones Funciones
from FuncionesGenerales import FuncionesGenerales
from FuncionesData import FuncionesData
from FuncionesConfig import FuncionesConfig
from FuncionesReporte import FuncionesReporte
from FuncionesGrafica import FuncionesGrafica


#Variables Globales
Mes = "N/A"
Año = "N/A"
Items = []

Nombre = "N/A"
Grafica = "N/A"
Titulo = "N/A"
TituloX = "N/A"
TituloY = "N/A"

################################################################
def abrirarchivodata():
    try:
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
    
    except:
        print("Error al cargar el archivo .data")

    
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
            if str(producto.nombre) ==  " " or str(producto.nombre) ==  "" or str(producto.nombre) ==  "  " :
                producto.setnombre("Sin nombre")
                flagitems = True
                mensaje += "El nombre del producto No." + str(contador) + " esta Vacio" 

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
def imprimirdata():
    print("\n")
    print("Año: " + Año)
    print("Mes: " + Mes)
    for productos in Items:
        print(productos.imprimir())
    print("\n")

################################################################
def imprimirconfiguracion():
    print("\n")
    print("Nombre: ", Nombre)
    print("Grafica: ", Grafica)
    print("Titulo: ", Titulo)
    print("TituloX: ", TituloX)
    print("TituloY: ", TituloY)
    print("\n")

################################################################
def abrirarchivoconfig():
    try:
        archivo = filedialog.askopenfilename(
        title = "Selecciona un archivo",
        #accede a la carpeta donde esta el archivo 
        initialdir =  "./",
        #tipo de archivo que puede seleccionar
        filetype = [
            ("Archivos DATA", "*.lfp"),
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
            print("\n----------------- [ .LFP ] ------------------------")
            print(text)
            print("------------------------------------------------ \n")
            return text
    
    except:
        print("Error al cargar el archivo .lfp")

    
################################################################
def ordenaritems():

    print("\n################################################################")
    #1.0 llenar array 
    lengtharreglo = len(Items)
    arrayfiltro  = []
    #2.0 nuevo arrego Items 
    for item in Items:
        item.getventas()
        arrayfiltro.append(item)

    
    # { ORDENAMIENTO METODO BURBUJA }        
    #1.0 Ordenar por Like
    temp = 0
    #2.0 obtiene el largo del arreglo
    lengtharreglo = len(arrayfiltro)
    #2.1 reccorrre el array
    for h in range(lengtharreglo-1,0,-1):
        for i in range(h):
            #Valida si es mayor
            if int(arrayfiltro[i].ventas) < int(arrayfiltro[i+1].ventas):
                temp = arrayfiltro[i]
                arrayfiltro[i] =arrayfiltro[i+1]
                arrayfiltro[i+1] = temp
    print("fin ordenamiento por metodo burbuja")


    
    
    

    print("\n################################################################")
    return arrayfiltro

################################################################
################################################################
#Main program
if __name__ == "__main__":

    #Importaciones
    Funcionesgenerales = FuncionesGenerales()
    Funcionesdata = FuncionesData()
    Funcionesconfig = FuncionesConfig()
    Funcionesreporte = FuncionesReporte()
    Funcionesgrafica = FuncionesGrafica()

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
                print("Error al validar Datos en el archivo .data")
                break
            #Imprimir informacion .data
            imprimirdata()
        else:
            print("El archivo .data no tiene ningun dato a inspeccionar")
            break

        ## [ LFP ] ##
        #Abrir archivo config lfp
        dataconfig = abrirarchivoconfig()
        if dataconfig is not None:
            #Guardar Informacion lfp
            Funcionesconfig.setdataconfig(dataconfig)
            #Clasificar las variables dentro del .lfp
            Funcionesconfig.clasificador()
            #Guarda las Variables
            Nombre = Funcionesconfig.getNombre()
            Grafica = Funcionesconfig.getGrafica()
            Titulo = Funcionesconfig.getTitulo()
            TituloX = Funcionesconfig.getTituloX()
            TituloY = Funcionesconfig.getTituloY()
            imprimirconfiguracion()
        else:
            print("El archivo .lfp no tiene ningun data a inspeccionar")

        
        ## [ REPORTE ] ##
        #Ordena los Productos 
        arrayfiltro = ordenaritems()
        #Crea el reporte
        Funcionesreporte.crearReporte(Mes, Año,arrayfiltro, Nombre, Grafica, Titulo, TituloX, TituloY)


        ## [ GRAFICA ] ##
        Funcionesgrafica.creargrafica(Mes, Año,arrayfiltro, Nombre, Grafica, Titulo, TituloX, TituloY)

        
        #Fin While
        seleccion = input("Desea cargar otros archivos? S/N\n")
        print(str(seleccion))
        if(str(seleccion) == "N" or str(seleccion) == "n" ):
            break

        #ciclo while infinito
        cont += 1
        if (cont >= 20):
            break
    


    