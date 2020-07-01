
function func()
{

var f=document.getElementById("fname");
var l=document.getElementByName("lname");
var u=document.getElementByName("uname");
var em=document.getElementByName("email");
var pass=document.getElementByName("pas");
var cpass=document.getElementByName("pas1");
var ph=document.getElementByName("phone");
var address=document.getElementByName("add");
if(f.value=="")
{
alert("No blank spacess are allowed here");
return false;
}else
{
alert("chal koi na");
return true;
}
}
