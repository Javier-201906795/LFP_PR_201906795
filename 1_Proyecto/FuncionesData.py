


class FuncionesData:
    ################################################################
    def __init__(self):
        self.datatexto1 = "N/A"
        ### [ Cordenadas Parametros ]
        ## [ Mes ]
        self.cordmesini= 0
        self.cordmesfin= -1
        self.mes = "N/A"
        ## [ Año ]
        self.cordañoini= -1
        self.cordañofin= -1
        self.año = "N/A"

    ################################################################
    #Recive la informacion a procesar
    #--------------------------------
    def setdatatexto1(self, datatexto1):
        self.datatexto1 = datatexto1


    ################################################################
    # Consulta las cordenas almacenadas
    #--------------------------------
    def cordenadas(self):
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print ("░Cordenas Mes: ", self.cordmesini, " | ", self.cordmesfin)
        print ("░Cordenas Año ", self.cordañoini, " | ", self.cordañofin)
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    
    ################################################################

    def clasificador(self):

        
        ### [Obtener Mes]
        cont = 0
        for c in self.datatexto1:
            cont += 1
            print(c)
            if c == ":":
                break
        ## [Guardar Cordenadas Mes ]
        self.cordmesfin = cont

        

        ### [Obtener Año]
        ## guarda el incio del segundo parametro
        temp = cont + 1 
        cont = 0
        for c in self.datatexto1:
            cont += 1
            print(c)
            if c == "=":
                break
        ## [Guardar Cordenadas Mes ]
        self.cordañoini = temp
        self.cordañofin = cont
        
        
    ################################################################

    def getMes(self):
        self.mes = self.datatexto1[self.cordmesini:self.cordmesfin]
        return self.mes

    ################################################################

    def getAño(self):
        self.Año = self.datatexto1[self.cordañoini:self.cordañofin]
        return self.año
        

    
    