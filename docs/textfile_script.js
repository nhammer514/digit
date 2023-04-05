window.addEventListener('DOMContentLoaded',init,false);
function init(){
    var buttons = document.getElementsByTagName("button");
    for (var i = 0; i <  buttons.length; i++){
        buttons[i].addEventListener('click', toggle, false);
    }
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