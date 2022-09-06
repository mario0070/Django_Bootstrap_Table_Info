
$(document).ready(function(){
    $("#mytable").DataTable({
      "aLengthMenu":[[3,5,10,25,-1],[3,5,10,25,"All"]],
      "iDisplayLength":3
    });
});


$(document).ready(function(){
    $("#contact").click(function(){
        $("main").load("contact/")
    });
});



$(document).ready(function(){
    $("#about").click(function(){
        $("main").load("about/")
    });
});

$(document).ready(function(){
    $("#messages").click(function(){
        $("main").load("messages/")
    });
});

$(document).ready(function(){
    $("#table").click(function(){
        $("main").load("table/")
    });
});

$(document).ready(function(){
    $("#create").click(function(){
        $("main").load("create/")
    });
});

var btn=document.getElementById("btn")
var links=document.getElementById("links")
var main=document.getElementById("main")
btn.addEventListener('click',()=>{
links.classList.toggle("valid")
main.classList.toggle("valid")

})