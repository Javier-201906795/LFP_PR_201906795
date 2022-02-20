import matplotlib.pyplot as plt

class FuncionesGrafica:

    def hola(self):
        print("Bienvenidos")
        return None

    ################################################################
    def graficadebarras(self, Mes, Año, productos, Nombre, Grafica, Titulo, TituloX, TituloY):
        # Datos Gráfica de Barras
        ejeXB = []
        #Agrega los nombres a un nuevo array
        for c in productos:
            ejeXB.append(str(c.nombre))

        print(ejeXB)
        
        ejeYB = []
        #Agrega las ventas en un nuevo array
        for c in productos:
            ejeYB.append(float(c.ventas))

        print(ejeYB)

        plt.rcdefaults()
        figB, axB = plt.subplots()
        figL, axL = plt.subplots()

        # GRÁFICA DE BARRAS
        axB.bar(ejeXB, ejeYB) # Datos de los ejes de la gráfica de barras, se usa función bar()

        axB.set_xlabel(str(TituloX).upper()) # Titulos de los ejes
        axB.set_ylabel(str(TituloY).upper()) # Titulos de los

        axB.grid(axis='y', color='lightgray', linestyle='dashed')
        axB.set_title(str(Titulo).upper())

        docnombre = "./"+str(Nombre)+".png"
        figB.savefig(str(docnombre))
        return None

    ################################################################
    def graficaLineas(self, Mes, Año, productos, Nombre, Grafica, Titulo, TituloX, TituloY):
        # Datos Gráfica 
        ejeXL = []
        #Agrega los nombres a un nuevo array
        for c in productos:
            ejeXL.append(str(c.nombre))

        print(ejeXL)
        
        ejeYL = []
        #Agrega las ventas en un nuevo array
        for c in productos:
            ejeYL.append(float(c.ventas))

        print(ejeYL)

        plt.rcdefaults()
        figL, axL = plt.subplots()

        # GRÁFICA DE LÍNEAS
        axL.plot(ejeXL, ejeYL) # Configuración de los ejes de la gráfica de lineas, se usa función plot()

        # Titulos de los ejes
        axL.set_xlabel(str(TituloX).upper(), fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'blue'})
        axL.set_ylabel(str(TituloY).upper(), fontdict = {'fontweight':'bold', 'fontsize':13, 'color':'red'})

        axL.grid(axis='y', color='darkgray', linestyle='dashed')
        axL.set_title(str(Titulo).upper())

        docnombre = "./"+str(Nombre)+"2.png"
        figL.savefig(str(docnombre))
        return None

    ################################################################
    ################################################################
    def creargrafica(self, Mes, Año, productos, Nombre, Grafica, Titulo, TituloX, TituloY):
        
        #self.graficadebarras(Mes, Año, productos, Nombre, Grafica, Titulo, TituloX, TituloY)
        
        #self.graficaLineas(Mes, Año, productos, Nombre, Grafica, Titulo, TituloX, TituloY)

        if(str(Grafica).lower() == "barras"):
            self.graficadebarras(Mes, Año, productos, Nombre, Grafica, Titulo, TituloX, TituloY)

        if(str(Grafica).lower() == "lineas"):
            self.graficaLineas(Mes, Año, productos, Nombre, Grafica, Titulo, TituloX, TituloY)

        return None