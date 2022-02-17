


class FuncionesData:
    ################################################################
    def __init__(self):
        self.datatexto1 = "N/A"
        ### [ Cordenadas Parametros ]
        ## [ Mes ]
        self.mes = "N/A"
        ## [ Año ]
        self.año = "N/A"

    ################################################################
    #Recive la informacion a procesar
    #--------------------------------
    def setdatatexto1(self, datatexto1):
        self.datatexto1 = datatexto1


    ################################################################

    def clasificador(self):

        
        ### [Obtener Mes]
        cont = 0
        for c in self.datatexto1:
            cont += 1
            if c == ":":
                break
        ## [Guardar  Mes ]
        cordmesfin = cont
        self.mes = self.datatexto1[0:cordmesfin - 1]

        

        ### [Obtener Año]
        #Texto nuevo
        temptext = self.datatexto1[cont + 1: len(self.datatexto1)]
        print(temptext)
        ## guarda el incio del segundo parametro
        cont = 0
        for c in temptext:
            cont += 1
            print(c)
            if c == "=":
                break
        ## [Guardar Cordenadas Mes ]
        cordañofin = cont
        self.año = temptext[0: cordañofin - 1 ]
        
        
    ################################################################

    def getMes(self):
        return self.mes

    ################################################################

    def getAño(self):
        return self.año
        

    
    