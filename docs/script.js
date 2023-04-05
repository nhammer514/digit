window.addEventListener('DOMContentLoaded',init,false);
function init(){
    var buttons = document.getElementsByTagName("button");
    for (var i = 0; i <  buttons.length; i++){
        buttons[i].addEventListener('click', toggle, false);
    }
}

function setMenu(){
    hidePages();
    var sectionID =  "page-" + this.id;
    var selSection = document.getElementById(sectionID)
    selSection.style.display = 'block';
}

function toggle(){
    var sectionID =  "section-" + this.id;
    var selSection = document.getElementById(sectionID);
    if (selSection.style.display == 'block'){
        selSection.style.display = 'none';
    }
    else{
        selSection.style.display = 'block';
    }
}

function hidePages(){
    var sections = document.getElementsByClassName('page')
    for (var p = 0; p < sections.length; p++){
        sections[p].style.display='none';
    }
}