

class FuncionesReporte:

    ################################################################
    def hola(self):
        print("hola")
        return None

    ################################################################
    def javascriptdatos(self, dato1):
        print("Modificando javascript ... ")
        try:
            f = open('LFP_PR_201906795.js','w')

            mensaje = """mytexto = document.getElementById("mytext");
mytexto.innerHTML = 'Hola COMO ESTAS' """

            f.write(mensaje)
            f.close()
        except:
            print("Error al modicar archivo javascript")

        return None

    ################################################################
    def crearReporte(self):

        #Crear JAVASCRIPT
        self.javascriptdatos("dato1")
        return None