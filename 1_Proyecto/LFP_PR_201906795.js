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

topnombre.innerHTML = 'Chocolates Milk' 
topcantidad.innerHTML =  22 
topprecio.innerHTML = 'Q '+7.5 
topvendido.innerHTML = 'Q '+ 165.0
// Producto Menos Vendido

bottomnombre.innerHTML = 'Gansito' 
bottomcantidad.innerHTML = 0 
bottomprecio.innerHTML = 'Q '+5.25 
bottomvendido.innerHTML  = 'Q '+0.0
//Tabla
var listaproductos = [{nombre:'Chocolates Milk',cantidad:22,precio:7.5,cantidad:22,ventas:165.0},{nombre:'Cocacola',cantidad:25,precio:5.0,cantidad:25,ventas:125.0},{nombre:'Nachos',cantidad:5,precio:2.5,cantidad:5,ventas:12.5},{nombre:'Tortrix',cantidad:10,precio:1.0,cantidad:10,ventas:10.0},{nombre:'Bombones',cantidad:0,precio:1.5,cantidad:0,ventas:0.0},{nombre:'Gansito',cantidad:0,precio:5.25,cantidad:0,ventas:0.0},]
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