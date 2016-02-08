$(document).ready(function() {  
  
var MaxInputs       = 8; //maximum input boxes allowed  
var InputsWrapper   = $("#InputsWrapper"); //Input boxes wrapper ID  
var AddButton       = $("#AddForm"); //Add button ID 


var x = InputsWrapper.length; //initlal text box count  

$(AddButton).click(function (e)  //on add input button click  
{  
        var Inputs = $("#Inputs0").clone(true)
        var replaceID1 = function () {
                var oldID = $(this).attr('id');
                var newID = $(this).attr('id').replace(oldID, oldID.slice(0,-1)+x);
                $(this).attr('id', newID);
                $(this).attr('class', newID);
            }

        var replaceID2 = function () {
                var oldID = $(this).attr('id');
                var newID = $(this).attr('id').replace(oldID, oldID.slice(0,-1)+x);
                $(this).attr('id', newID);
                $(this).attr('name', newID);
            }

        if(x <= MaxInputs) //max input box allowed  
        {
            var oldDivID = Inputs.attr('id');
            var newDivID = Inputs.attr('id').replace(oldDivID, oldDivID.slice(0,-1)+x);
            Inputs.attr('id', newDivID);
            Inputs.attr('class', newDivID);

            Inputs.find('input').each(replaceID2)
            Inputs.find('select').each(replaceID2)
            Inputs.find('textarea').each(replaceID2)
            Inputs.find('div').each(replaceID1)
            Inputs.find('formset').each(replaceID1)
            $(InputsWrapper).append(Inputs.append('<br><input class="buttom Remove" name="Remove" id="Remove" value="Remove" type="button" style="position:relative;left:150px;"/>'));
            x++; //text box increment  
        }
return false;  
});  
  
$("body").on("click",".buttom.Remove", function(e){ //user click on remove text  
        if( x > 1 ) {  
                $(this).parent().remove(); //remove text box  
                x--; //decrement textbox  
        }  
return false;  
});   
  
});  