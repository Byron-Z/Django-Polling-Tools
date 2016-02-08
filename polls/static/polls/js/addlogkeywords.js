$(document).ready(function() {  
    var MaxInputs = 10; //maximum input boxes allowed  
$("body").on("click",".buttom.Add", function(e){
    //var Inputs = $("#keyword00").clone(true);
    var Inputs = $(this).prev().clone(true);
    var x = parseInt($(this).siblings().last().attr('id').substr(-2, 1))+1;
    var replaceID = function () {
            var oldID = $(this).attr('id');
            var newID = $(this).attr('id').replace(oldID, oldID.slice(0,-2)+x+oldID.slice(-1));
            $(this).attr('id', newID);
            $(this).attr('name', newID);
        }
    Inputs.prepend('<br>');
    if(x <= MaxInputs) //max input box allowed  
    {
        var oldFormsetID = Inputs.attr('id');
        var newFormsetID = Inputs.attr('id').replace(oldFormsetID, oldFormsetID.slice(0,-2)+x+oldFormsetID.slice(-1));
        Inputs.attr('id', newFormsetID);
        Inputs.attr('class', newFormsetID);

        Inputs.find('input').each(replaceID)
        Inputs.find('select').each(replaceID)
        //$("input[id='" + $(this).attr('id') + "']")
        $(this).parent().append(Inputs.append('<input class="buttom Remove" name="Remove" id="Remove" value="X" type="button"/>'));
        x++; //text box increment
    }
return false;  
});

$("body").on("click",".buttom.Remove", function(e){ //user click on remove text  
        $(this).parent().remove(); //remove text box  
return false;  
}); 
});