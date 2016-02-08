
var getAppOptions = function (appid){  
    $.ajax({   
        type: "GET",
        url: "/index.html?appid=" + appid,       
        dataType:'json',   
        success: function(data){
            var MangerOptions = document.getElementById("manager");
            var OwnerOptions = document.getElementById("ownership");
            var PriOptions = document.getElementById("priority");
            //alert(JSON.stringify(data));
            if (data.length > 0 ) {
                var info = data[0].text;
                for (i=0 ; i < MangerOptions.options.length ; i++ ) {
                    if (MangerOptions.options[i].text === info) {
                        MangerOptions.options[i].setAttribute('selected','true');
                        break;
                    }
                }
                var info = data[1].text;
                for (i=0 ; i < OwnerOptions.options.length ; i++ ) {
                    if (OwnerOptions.options[i].text === info) {
                        OwnerOptions.options[i].setAttribute('selected','true');
                        break;
                    }
                }
                var info = data[2].text;
                for (i=0 ; i < PriOptions.options.length ; i++ ) {
                    if (PriOptions.options[i].text === info) {
                        PriOptions.options[i].setAttribute('selected','true');
                        break;
                    }
                } 
            }
        }    
    });
}  
