import matplotlib.pyplot as plt

class FuncionesGrafica:

    def hola(self):
        print("Bienvenidos")
        return None


    def graficadebarras(self):
        # Datos Gráfica de Barras
        ejeXB = ['Alberto','Kevin','María','Josué','Carolina','Michelle']
        ejeYB = [100, 75, 105, 59, 73, 68]
        # Datos Gráfica de Líneas
        ejeXL = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado']
        ejeYL = [100*3, 75*3, 105*3, 59*3, 73*3, 68*3]

        plt.rcdefaults()
        figB, axB = plt.subplots()
        figL, axL = plt.subplots()

        # GRÁFICA DE BARRAS
        axB.bar(ejeXB, ejeYB) # Datos de los ejes de la gráfica de barras, se usa función bar()

        axB.set_xlabel('Empleados') # Titulos de los ejes
        axB.set_ylabel('Llamadas')

        axB.grid(axis='y', color='lightgray', linestyle='dashed')
        axB.set_title('Desempeño x Empleado Call-Center')

        figB.savefig('./graficaBarras.png')
        return None

    def creargrafica(self, Mes, Año, productos, Nombre, Grafica, Titulo, TituloX, TituloY):
        
        self.graficadebarras()
        
        return None