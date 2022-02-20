// Producto TOP
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
tablacuerpo = document.getElementById("tablacuerpo");// Producto TOP

topnombre.innerHTML = 'producto 1' 
topcantidad.innerHTML =  33 
topprecio.innerHTML = 25.0 
topvendido.innerHTML = 825.0
// Producto Menos Vendido

bottomnombre.innerHTML = 'producto 4' 
bottomcantidad.innerHTML = 0 
bottomprecio.innerHTML = 50.0 
bottomvendido.innerHTML = 0.0
//Tabla
var listaproductos = mario[{nombre:"Paleta",cantidad: 25,precio:5.50},{nombre:"Paleta2",cantidad: 215,precio:52.50},{nombre:"Paleta3",cantidad: 5,precio:1.50}]
console.log(listaproductos)

//Limpiar Tabla
tablacuerpo.innerHTML = ''

for (var i = 0; i < listaproductos.length; i++){
    tablacuerpo.innerHTML += '<tr>'+
    '<th scope="row">'+(i+1)+'</th>' +
    '<td>'+listaproductos[i].nombre+'</td>' +
    '<td>Q '+listaproductos[i].precio+'</td>' +
    '<td>'+listaproductos[i].cantidad+'</td>' +
    '</tr>';
}