function OvFun() {
   
    var ele = document.getElementsByName('ratingz');

    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
            //alert(6-ele[i].value)
            document.getElementById("testz").value
                = 6-ele[i].value;
    }
}
function InFun() {
   
    var ele = document.getElementsByName('rating');

    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
           // alert(6-ele[i].value)
            document.getElementById("testi").value
                = 6-ele[i].value;
    }
}
function ExFun() {
   
    var ele = document.getElementsByName('rating1');

    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
           // alert(6-ele[i].value)
            document.getElementById("test1").value
                = 6-ele[i].value;
    }
}
function recFun() {
   
    var ele = document.getElementsByName('flexRadioDefault');

    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
           // alert(ele[i].value)
            document.getElementById("testflexRadioDefault").value
                = ele[i].value;
    }

}
function fun(){
    var f=document.getElementById("testflexRadioDefault").value
    var s=document.getElementById("test1").value
    var t =document.getElementById("testi").value
    var fr=document.getElementById("testz").value
   // alert(f+' '+s+' '+t+' '+fr)
}
