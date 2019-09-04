/**
 * Created by tarena on 19-5-9.
 */
function createXhr(){
    if(window.XMLHttpRequest)
        return new XMLHttpRequest();
    else
        return new ActiveXObject("Microsoft.XMLHTTP");
}
