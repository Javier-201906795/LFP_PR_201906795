
class FuncionesConfig:

    ################################################################
    def __init__(self):
        self.dataconfig = "N/A"
        self.Nombre = "N/A"
        self.Grafica = "N/A"
        self.Titulo = "N/A"
        self.TituloX = "N/A"
        self.TituloY = "N/A"

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
        print(tempdataconfimin,"\n---------------------------\n")

        #Quitar "?>"
        cont = 0
        for d in tempdataconfimin:
                cont += 1
                if d == ">":
                    break
        #Temp Texto
        tempdataconfimin = tempdataconfimin[0:cont - 2]
        print(tempdataconfimin,"\n||||||||||||||||||||\n")

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
        print(listtemptext)

        #Buscar nombre
        variable = ""
        for item in listtemptext:
            print(item)
            #encontrar ":"
            for c in item:
                if c == ":":
                    break
            #Extraer "nombre:"
            
            
            

        



        
        
        return None

    ################################################################
    def setdataconfig(self,dataconfig):
        self.dataconfig = dataconfig
