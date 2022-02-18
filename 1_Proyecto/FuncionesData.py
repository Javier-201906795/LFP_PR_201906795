


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
        #print(temptext)
        ##encontrar "="
        cont = 0
        for c in temptext:
            cont += 1
            if c == "=":
                break
        ## [Guardar Año ]
        cordañofin = cont
        self.año = temptext[0: cordañofin - 1 ]

        ### [Obtener Items]
        ### [Ingresar al array] "("
        #Texto nuevo
        temptext = temptext[cont + 1: len(temptext)]
        ##encontrar "("
        cont = 0
        for c in temptext:
            cont += 1
            if c == "(":
                break
        ###[Obtenr item]
        items = []
        contadorwhile = 0

        while True:    

            temptext = temptext[cont + 1: len(temptext)]
            ##encontrar inicio item "["
            cont = 0
            for c in temptext:
                cont += 1
                if c == "[":
                    break
            
            ## [ NOMBRE ] ##
            # Temp Text
            temptext = temptext[cont: len(temptext)]
            ##encontrar ","
            cont = 0
            for c in temptext:
                cont += 1
                if c == ",":
                    break
            #Guardar item Nombre
            itemnombre = temptext[1: cont - 2]
            print("Nombre: ", itemnombre)

            ## [ PRECIO ] ##
            # Temp Text
            temptext = temptext[cont: len(temptext)]
            ##encontrar ","
            cont = 0
            for c in temptext:
                cont += 1
                if c == ",":
                    break
            #Guardar item Precio
            itemprecio = temptext[0: cont - 1]
            print("Precio: ", itemprecio)

            ## [ CANTIDAD ] ##
            # Temp Text
            temptext = temptext[cont: len(temptext)]
            ##encontrar ","
            cont = 0
            for c in temptext:
                cont += 1
                if c == "]":
                    break
            #Guardar item Cantidad
            itemcantidad = temptext[0: cont - 1]
            print("Cantidad: ", itemcantidad)

            # print("||||||||||")
            # print(temptext,"\n")
        

            

            
            #[ TempText Quitar espacios]
            temptextsinespacios = ""
            for a in temptext:
                if a == '\n' or a == ' ':
                    pass
                else:
                    temptextsinespacios += a

            
            ## [ Fin WHILE ] ##
            
            #Juntar ultimos 3 caracteres
            verificar = temptextsinespacios[len(temptextsinespacios) - 3:len(temptextsinespacios)]                    
            
            #Verificar ultimos 3 caracters son Finales "];)"
            if (len(temptextsinespacios) < 4):
                if (verificar == "];)"):
                    print("FIN")
                    break


            
            

        
        
        
    ################################################################

    def getMes(self):
        return self.mes

    ################################################################

    def getAño(self):
        return self.año
        

    
    