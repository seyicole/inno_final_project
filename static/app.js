function darkMode(){
    let element = document.body;
    let text = document.getElementsByClassName('text')

    let state = localStorage.getItem("state")

    element.classList.toggle('dark-mode')

    for(const i of text){
        i.classList.toggle('dark-mode')
    }

    if(state !=='dark'){
        localStorage.setItem('state', 'dark')
    }else{
        localStorage.setItem('state', 'light')
    }
}

function storeMode(){
    let element = document.body;
    let text = document.getElementsByClassName('text')

    let state = localStorage.getItem("state")

    if(state =="dark"){
        element.classList.toggle('dark-mode')
    }

    element.classList.toggle('dark-mode')

    for(const i of text){
        i.classList.toggle('dark-mode')
    }
}