//-------------------------------------------------------------
var natureza = localStorage.getItem('natureza')
var gastronomia = localStorage.getItem('gastronomia')
var praia = localStorage.getItem('praia')
var cultura = localStorage.getItem('cultura')

var v = 0;


console.log(localStorage.getItem('natureza'))
console.log(localStorage.getItem('praia'))
console.log(localStorage.getItem('gastronomia'))
console.log(localStorage.getItem('cultura'))

/*var prai = document.getElementsByName('praia')

for(var i = 0; i < prai.length; i++){
    if(prai[i].checked){
        if (prai[i].value == 3){
            console.log(prai[i].value)
            a = prai[i].value
            
        }
        if(prai[i].value == 1){
            v = prai[i].value
        }
    }
}
console.log("valor de A:"+a)
*/
window.onload = function () { 
var b = document.getElementById('id_gastronomia').style.display
console.log(b)

if(!natureza){
    document.getElementById('id_natureza').style.display = 'none';
    document.getElementById('natureza').style.display = 'none';

}
else{
    document.getElementById('id_natureza').style.display = 'block';
    document.getElementById('natureza').style.display = 'block';


}
if(!gastronomia){
    document.getElementById('id_gastronomia').style.display = 'none';
    document.getElementById('gastronomia').style.display = 'none';

}
else{
    document.getElementById('id_gastronomia').style.display = 'block';
    document.getElementById('gastronomia').style.display = 'block';


}
if(!praia){
    document.getElementById('id_praia').style.display = 'none';
    document.getElementById('praia').style.display = 'none';

}
else{
    document.getElementById('id_praia').style.display = 'block';
    document.getElementById('praia').style.display = 'block';


}
if(!cultura){
    document.getElementById('id_cultura').style.display = 'none';
    document.getElementById('cultura').style.display = 'none';

}
else{
    document.getElementById('id_cultura').style.display = 'block';
    document.getElementById('cultura').style.display = 'block';


}


//-------------------------------------------------------------

//alert(gastronomia)
} 

