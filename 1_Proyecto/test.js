
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
tablacuerpo = document.getElementById("tablacuerpo");


// Producto TOP

topnombre.innerHTML = 'Tortrix' 
topcantidad.innerHTML = 5 
topprecio.innerHTML = 25.5 
topvendido.innerHTML = 50.05 

// Producto Menos Vendido

bottomnombre.innerHTML = 'Chocolate' 
bottomcantidad.innerHTML = 1 
bottomprecio.innerHTML = 0.5 
bottomvendido.innerHTML = 0.5 

//Tabla

var listaproductos = [{nombre:"Paleta",cantidad: 25,precio:5.50},{nombre:"Paleta2",cantidad: 215,precio:52.50},{nombre:"Paleta3",cantidad: 5,precio:1.50}]

console.log(listaproductos)
console.log(listaproductos[0])
console.log(listaproductos[0].nombre)

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