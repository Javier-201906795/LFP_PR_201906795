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

topnombre.innerHTML = 'producto 3' 
topcantidad.innerHTML =  170 
topprecio.innerHTML = 'Q '+15.0 
topvendido.innerHTML = 'Q '+ 2550.0
// Producto Menos Vendido

bottomnombre.innerHTML = 'producto 4' 
bottomcantidad.innerHTML = 0 
bottomprecio.innerHTML = 'Q '+50.0 
bottomvendido.innerHTML  = 'Q '+0.0
//Tabla
var listaproductos = [{nombre:'producto 3',cantidad:170,precio:15.0,cantidad:170,ventas:2550.0},{nombre:'producto 1',cantidad:33,precio:25.0,cantidad:33,ventas:825.0},{nombre:'producto 2',cantidad:10,precio:35.75,cantidad:10,ventas:357.5},{nombre:'producto 4',cantidad:0,precio:50.0,cantidad:0,ventas:0.0},]
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
}