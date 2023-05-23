window.addEventListener('DOMContentLoaded',init,false);
function init(){
    var buttons = document.getElementsByTagName("a");
    for (var i = 0; i <  buttons.length; i++){
        buttons[i].addEventListener('click', setMenu, false);
    }
}

function setMenu(){
    hidePages();
    var sectionID =  "page-" + this.id;
    var selSection = document.getElementById(sectionID)
    selSection.style.display = 'block';
}

function hidePages(){
    var sections = document.getElementsByClassName('page')
    for (var p = 0; p < sections.length; p++){
        sections[p].style.display='none';
    }
}