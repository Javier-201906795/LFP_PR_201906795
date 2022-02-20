

class FuncionesReporte:

    

    ################################################################
    def crearReporte(self,Mes, Año,Items, Nombre, Grafica, Titulo, TituloX, TituloY):

        print("\n ----------------------[ REPORTE ]-------------------------------------")
        #Imprimir Valores
        print("\n")
        print("Año: " + Año)
        print("Mes: " + Mes)
        for productos in Items:
            print(productos.imprimir())

        print("Nombre: ", Nombre)
        print("Grafica: ", Grafica)
        print("Titulo: ", Titulo)
        print("TituloX: ", TituloX)
        print("TituloY: ", TituloY)
        print("\n")


        

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

topnombre.innerHTML = '"""+ str(Items[0].nombre) +"""' 
topcantidad.innerHTML =  """+ str(Items[0].cantidad) +""" 
topprecio.innerHTML = 'Q '+"""+ str(Items[0].precio) +""" 
topvendido.innerHTML = 'Q '+ """+ str(Items[0].ventas) 
            #Producto Menos Vendido
            contenido += """
// Producto Menos Vendido

bottomnombre.innerHTML = '"""+ str(Items[len(Items)-1].nombre) +"""' 
bottomcantidad.innerHTML = """+ str(Items[len(Items)-1].cantidad) +""" 
bottomprecio.innerHTML = 'Q '+"""+ str(Items[len(Items)-1].precio) +""" 
bottomvendido.innerHTML  = 'Q '+""" + str(Items[len(Items)-1].ventas) 
            
            #Tabla datos
            
            listado = """[{nombre:"Paleta",cantidad: 25,precio:5.50},{nombre:"Paleta2",cantidad: 215,precio:52.50},{nombre:"Paleta3",cantidad: 5,precio:1.50}]"""    
            listado = "["
            for c in Items:
                listado += """{nombre:'"""+ str(c.nombre) +"""',cantidad:"""+ str(c.cantidad) + """,precio:"""+ str(c.precio) + """,cantidad:"""+ str(c.cantidad) + """,ventas:"""+str(c.ventas) + """},"""
            listado += "]"
            
            #print(listado)

            contenido += """
//Tabla
var listaproductos = """+ listado


            #Tabla Imprimir
            contenido += """
console.log(listaproductos)

//Limpiar Tabla
tablacuerpo.innerHTML = ''

for (var i = 0; i < listaproductos.length; i++){
    tablacuerpo.innerHTML += '<tr>'+
    '<th scope="row">'+(i+1)+'</th>' +
    '<td>'+listaproductos[i].nombre+'</td>' +
    '<td>Q '+listaproductos[i].precio+'</td>' +
    '<td>'+listaproductos[i].cantidad+'</td>' +
    '<td>Q '+listaproductos[i].ventas+'</td>' +
    '</tr>';
}"""

            f.write(contenido)
            f.close()
        except:
            print("Error al modicar archivo javascript")



        return None