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

topnombre.innerHTML = 'Pepsi + Seven Up' 
topcantidad.innerHTML =  305 
topprecio.innerHTML = 'Q '+39.99 
topvendido.innerHTML = 'Q '+ 12196.95
// Producto Menos Vendido

bottomnombre.innerHTML = 'Pimentones cheika' 
bottomcantidad.innerHTML = 52 
bottomprecio.innerHTML = 'Q '+10.6 
bottomvendido.innerHTML  = 'Q '+551.1999999999999
//Tabla
var listaproductos = [{nombre:'Pepsi + Seven Up',cantidad:305,precio:39.99,cantidad:305,ventas:12196.95},{nombre:'Toallas de Cocina Jumbo Pack',cantidad:99,precio:85.0,cantidad:99,ventas:8415.0},{nombre:'Pepsi Jumbo',cantidad:425,precio:17.5,cantidad:425,ventas:7437.5},{nombre:'Pepsi Light',cantidad:417,precio:15.69,cantidad:417,ventas:6542.73},{nombre:'Toallas Humedas Desinfectantes',cantidad:300,precio:20.0,cantidad:300,ventas:6000.0},{nombre:'Gatorade fresa-kiwi',cantidad:542,precio:8.9,cantidad:542,ventas:4823.8},{nombre:'Salsa Bolognesa',cantidad:133,precio:35.0,cantidad:133,ventas:4655.0},{nombre:'Queso crema natural',cantidad:154,precio:28.5,cantidad:154,ventas:4389.0},{nombre:'Pasta precocinada',cantidad:175,precio:23.9,cantidad:175,ventas:4182.5},{nombre:'Air Wick aparato + repuesto',cantidad:87,precio:40.0,cantidad:87,ventas:3480.0},{nombre:'Ades jugo surtido',cantidad:88,precio:25.75,cantidad:88,ventas:2266.0},{nombre:'Air Wick flores de magnolia',cantidad:171,precio:12.25,cantidad:171,ventas:2094.75},{nombre:'Air Wick suavidad algodón',cantidad:141,precio:12.25,cantidad:141,ventas:1727.25},{nombre:'Queso crema con pimienta',cantidad:76,precio:21.45,cantidad:76,ventas:1630.2},{nombre:'Aromatizante Glade Paraiso Azul',cantidad:63,precio:23.45,cantidad:63,ventas:1477.35},{nombre:'Aromatizante Glade Hawaiian Breeze',cantidad:62,precio:23.45,cantidad:62,ventas:1453.8999999999999},{nombre:'Aromatizante Glade Manzana y Canela',cantidad:61,precio:23.45,cantidad:61,ventas:1430.45},{nombre:'Queso crema light',cantidad:67,precio:20.0,cantidad:67,ventas:1340.0},{nombre:'Pimenton ahumado',cantidad:96,precio:12.75,cantidad:96,ventas:1224.0},{nombre:'Gatorade mandarina',cantidad:129,precio:8.9,cantidad:129,ventas:1148.1000000000001},{nombre:'Pepino agridulce',cantidad:78,precio:13.33,cantidad:78,ventas:1039.74},{nombre:'Agua Juniper quinua botella',cantidad:96,precio:10.5,cantidad:96,ventas:1008.0},{nombre:'Ades soya jugo naranja',cantidad:175,precio:4.75,cantidad:175,ventas:831.25},{nombre:'Queso Emmental',cantidad:32,precio:25.0,cantidad:32,ventas:800.0},{nombre:'Pimentones cheika',cantidad:52,precio:10.6,cantidad:52,ventas:551.1999999999999},]
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