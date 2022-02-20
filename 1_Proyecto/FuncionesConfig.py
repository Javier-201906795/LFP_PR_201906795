
class FuncionesConfig:

    ################################################################
    def __init__(self):
        self.dataconfig = "N/A"
        self.Nombre = "N/A"
        self.Grafica = "N/A"
        self.Titulo = "N/A"
        self.TituloX = "N/A"
        self.TituloY = "N/A"

    ################################################################
    def quitarcomillas(self, temptext):
        #Quitar ":"
        cont2 = -1
        for c in temptext:
            cont2 += 1
            if c == ":":
                break
        temptext = temptext[cont2 + 1:len(temptext)]    
        #Quitar """ comillas
        cont2 = -1
        for c in temptext:
            cont2 += 1
            if c == '"' or c=="'":
                break
        temptext = temptext[cont2 + 1:len(temptext)]  
        #Quitar """ comillas
        cont2 = -1
        for c in temptext:
            cont2 += 1
            if c == '"' or c=="'":
                break  
        temptext = temptext[0:cont2]  
        
        return temptext

    ################################################################

    def imprimir(self):
        print("Nombre: ", self.Nombre)
        print("Grafica: ", self.Grafica)
        print("Titulo: ", self.Titulo)
        print("TituloX: ", self.TituloX)
        print("TituloY: ", self.TituloY)

    ################################################################
    ################################################################
    def clasificador(self):
        #Texto Original
        dataconfig = self.dataconfig
        #Texto Minusculas
        dataconfigmin = dataconfig.lower()
        #Texto sin Espacios y en minusculas
        dataconfigsinespacios = ""
        for a in dataconfigmin:
                if a == '\n' or a == ' ':
                    pass
                else:
                    dataconfigsinespacios += a
        #print(dataconfig)
        #print(dataconfigmin)
        #print(dataconfigsinespacios)


        #Quitar "¿"
        cont = 0
        for c in dataconfigmin:
                cont += 1
                if c == "¿":
                    break
        #Temp Texto
        tempdataconfimin = dataconfigmin[cont:len(dataconfigmin)]
        #print(tempdataconfimin,"\n---------------------------\n")

        #Quitar "?>"
        cont = 0
        for d in tempdataconfimin:
                cont += 1
                if d == ">":
                    break
        #Temp Texto
        tempdataconfimin = tempdataconfimin[0:cont - 2]
        #print(tempdataconfimin,"\n||||||||||||||||||||\n")

        #Quitar "\n"
        cont = 0
        temptext = ""
        for e in tempdataconfimin:
            cont += 1
            if e == "\n":
                pass
            else:
                temptext += e
        

        #Separar ","
        listtemptext = temptext.split(",")
        #print(listtemptext)

        #Buscar Orden variables
        posicion = [-1,-1,-1,-1,-1]
        variable = ""
        cont0=-1
        for item in listtemptext:
            cont0+=1
            #print(item)
            #encontrar ":"
            cont1 = -1
            for c in item:
                cont1 += 1
                if c == ":":
                    break
            #Encontrar "nombre:"
            variable = item[cont1 - 6:cont1]
            if(variable == "nombre"):   
                #print("Se encontro nombre en la posicion:",cont0)
                #Guardar posicion
                posicion[0]=int(cont0)
            #Encontrar "grafica:"
            variable = item[cont1 - 7:cont1]
            if(variable == "grafica"):   
                #print("Se encontro grafica en la posicion:",cont0)
                #Guardar posicion
                posicion[1]=int(cont0)
            #Encontrar "titulo:"
            variable = item[cont1 - 6:cont1]
            if(variable == "titulo"):   
                #print("Se encontro titulo en la posicion:",cont0)
                #Guardar posicion
                posicion[2]=int(cont0)
            #Encontrar "titulox:"
            variable = item[cont1 - 7:cont1]
            if(variable == "titulox"):   
                #print("Se encontro titulox en la posicion:",cont0)
                #Guardar posicion
                posicion[3]=int(cont0)
            #Encontrar "tituloy:"
            variable = item[cont1 - 7:cont1]
            if(variable == "tituloy"):   
                #print("Se encontro tituloy en la posicion:",cont0)
                #Guardar posicion
                posicion[4]=int(cont0)
            #print(variable)
            
            
        #Guardar orden Variables
        # list | posicion
        #  0   |posicion Nombre
        #  1   |posicion Grafica
        #  2   |posicion Titulo
        #  3   |posicion Titulox
        #  4   |posicion Tituloy
        #print(posicion)
        

        ##[Obtener Nombre]
        #quitar comillas
        temptext = listtemptext[posicion[0]]
        self.Nombre = self.quitarcomillas(temptext)
        ##[Obtener Grafica]
        temptext = listtemptext[posicion[1]]
        self.Grafica = self.quitarcomillas(temptext)
        ##[Obtener Titulo]
        temptext = listtemptext[posicion[2]]
        self.Titulo = self.quitarcomillas(temptext)
        ##[Obtener Titulox]
        temptext = listtemptext[posicion[3]]
        self.TituloX = self.quitarcomillas(temptext)
        ##[Obtener Tituloy]
        temptext = listtemptext[posicion[4]]
        self.TituloY = self.quitarcomillas(temptext)
        
        
        #Imprimir datos
        #self.imprimir()


        
        
        return None

    

    ################################################################
    def setdataconfig(self,dataconfig):
        self.dataconfig = dataconfig

    ################################################################
    def getNombre(self):
        return self.Nombre

    def getGrafica(self):
        return self.Grafica

    def getTitulo(self):
        return self.Titulo

    def getTituloX(self):
        return self.TituloX
    
    def getTituloY(self):
        return self.TituloY
