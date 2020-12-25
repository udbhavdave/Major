function onClick(element) {
    document.getElementById("img01").src = element.src;
    document.getElementById("modal01").style.display = "block";
  }



var _validFileExtensions = [".jpg", ".jpeg", ".png"]; 

function change(){
    // var fu1 = document.getElementById("fle").value;
    var arrInputs = document.getElementsByTagName("input");
    
    for (var i = 0; i < arrInputs.length; i++) {
        var oInput = arrInputs[i];
        if (oInput.type == "file") {
            var sFileName = oInput.value;
            if (sFileName.length > 0) {
                var blnValid = false;
                for (var j = 0; j < _validFileExtensions.length; j++) {
                    var sCurExtension = _validFileExtensions[j];
                    if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                        blnValid = true;
                        break;
                    }
                }
                
                if (!blnValid) {
                    var msg="Sorry, Selected file is invalid, allowed extensions are: " + _validFileExtensions.join(", ");
                    document.getElementById("msg").innerHTML = msg;
                    var dis=sFileName.substr(sFileName.lastIndexOf('\\') + 1);
                    document.getElementById("file-return").innerHTML = "";
                    return false;
                }
            }
        }
    }
    var dis=sFileName.substr(sFileName.lastIndexOf('\\') + 1);
    document.getElementById("file-return").innerHTML = dis;
    document.getElementById("msg").innerHTML = "";
    return true;
    
}

  
function Validate(oForm) {
    if( document.getElementById("fle").files.length == 0 ){
        document.getElementById("msg").innerHTML = "Please Select The File!";
        document.getElementById("smsg").innerHTML = "";
        return false;
    }
    var arrInputs = document.getElementsByTagName("input");
    
    for (var i = 0; i < arrInputs.length; i++) {
        var oInput = arrInputs[i];
        if (oInput.type == "file") {
            var sFileName = oInput.value;
            if (sFileName.length > 0) {
                var blnValid = false;
                for (var j = 0; j < _validFileExtensions.length; j++) {
                    var sCurExtension = _validFileExtensions[j];
                    if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                        blnValid = true;
                        break;
                    }
                }
                
                if (!blnValid) {
                    var msg="Sorry, Selected file is invalid, allowed extensions are: " + _validFileExtensions.join(", ");
                    document.getElementById("msg").innerHTML = msg;
                    return false;
                }
            }
        }
    }
    var dis=sFileName.substr(sFileName.lastIndexOf('\\') + 1);
    document.getElementById("file-return").innerHTML = dis;
    document.getElementById("msg").innerHTML = "";
    show();
    return true;
}

function show(){
    $('#spinner').show();
}

function hide(){
    $('#spinner').hide();
}
