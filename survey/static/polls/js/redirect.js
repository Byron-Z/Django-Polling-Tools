$(document).ready(function() {  
    logurl = window.location.search.substring(1);
    $("form").on("click",".buttom.skip", function(e){ 
        window.location.href='log.html?'+logurl;
        return false;  
    });

    $("form").on("click",".buttom.finish", function(e){
        window.location.href='confirm.html';
        return false;  
    });  
});  
