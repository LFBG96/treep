
var a = document.getElementsByClassName('content')
var d = document.getElementsByClassName('d')
var cont = a.length
localStorage.clear()
  






function checar (){
    
    var cat = document.getElementsByName('categoria')
    var natureza = '';
    var praia = '';
    var gastronomia = '';
    var cultura = '';

    
    
    
    
    for(var i = 0; i < cat.length; i++){
        //console.log(cat[i].value)
        if(cat[i].checked){
            //localStorage.setItem('mds','asoansoai')
            if (cat[i].value == 'natureza'){
                
                natureza = cat[i].value
                localStorage.setItem('natureza',natureza)
            }
            if(cat[i].value == 'praia'){
                //v = prai[i].value
                //console.log(cat[i].value)
                praia = cat[i].value
                localStorage.setItem('praia',praia)
            }
            if(cat[i].value =='gastronomia'){
                gastronomia = cat[i].value
                //console.log(cat[i].value)
                localStorage.setItem('gastronomia',gastronomia)

            }
            if(cat[i].value =='cultura'){
                cultura = cat[i].value
                //console.log(cat[i].value)
                localStorage.setItem('cultura',cultura)

            }
            
            //localStorage.setItem('nao','não entrou')
        }
}
    
}
function btn(){
    //localStorage.setItem('a','soso')
    //console.log(localStorage.getItem('nao'))
    console.log(localStorage.getItem('natureza'))
    console.log(localStorage.getItem('praia'))
    console.log(localStorage.getItem('gastronomia'))
    console.log(localStorage.getItem('cultura'))

    localStorage.clear()
    console.log(localStorage.length)
    //console.log(localStorage.getItem('mds'))
    
}
