

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
        try:
            #Abre el archivo
            f = open('LFP_PR_201906795.js','w')
            #[Nuevo contenido]
            #Id del documento
            contenido = """// Producto TOP
topnombre = document.getElementById("topnombre");
topcantidad = document.getElementById("topcantidad");
topprecio = document.getElementById("topprecio");
topvendido = document.getElementById("topvendido");
// Producto Menos Vendido
bottomnombre = document.getElementById("bottomnombre");
bottomcantidad = document.getElementById("bottomcantidad");
bottomprecio = document.getElementById("bottomprecio");
bottomvendido = document.getElementById("bottomvendido");
//Tabla 
tablacuerpo = document.getElementById("tablacuerpo");"""
            #Producto Mas Vendido
            contenido += """// Producto TOP

topnombre.innerHTML = 'Tortrix' 
topcantidad.innerHTML = 5 
topprecio.innerHTML = 25.5 
topvendido.innerHTML = 50.05 """        
            #Producto Menos Vendido
            contenido += """// Producto Menos Vendido

bottomnombre.innerHTML = 'Chocolate' 
bottomcantidad.innerHTML = 1 
bottomprecio.innerHTML = 0.5 
bottomvendido.innerHTML = 0.5 """
            #Tabla datos
            contenido += """//Tabla
var listaproductos = [{nombre:"Paleta",cantidad: 25,precio:5.50},{nombre:"Paleta2",cantidad: 215,precio:52.50},{nombre:"Paleta3",cantidad: 5,precio:1.50}]"""
            #Tabla Imprimir
            contenido += """console.log(listaproductos)

//Limpiar Tabla
tablacuerpo.innerHTML = ''

for (var i = 0; i < listaproductos.length; i++){
    tablacuerpo.innerHTML += '<tr>'+
    '<th scope="row">'+(i+1)+'</th>' +
    '<td>'+listaproductos[i].nombre+'</td>' +
    '<td>Q '+listaproductos[i].precio+'</td>' +
    '<td>'+listaproductos[i].cantidad+'</td>' +
    '</tr>';
}"""

            f.write(contenido)
            f.close()
        except:
            print("Error al modicar archivo javascript")



        return None