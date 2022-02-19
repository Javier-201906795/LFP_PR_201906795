
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
        dataconfig = self.dataconfig
        dataconfigmin = dataconfig.lower()
        print(dataconfig)
        print(dataconfigmin)
        return None

    ################################################################
    def setdataconfig(self,dataconfig):
        self.dataconfig = dataconfig
