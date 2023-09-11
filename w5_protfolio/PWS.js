// alert("this is an alert");              // this will not work in for the preview button 


var currentIndex=0;
var images=[ "Ghost of Tsushima1.jpg" , "STAR WARS.jpg" , "Ghost of Tsushima2.jpg" , "Marvel's spider-man.jpg"];
function next(){
    if (currentIndex>=2){
        currentIndex=0;
    }else{
        currentIndex=currentIndex+1;
    }
    
    var GP =document.getElementById("GP");
    GP .setAttribute("src",images[currentIndex]);
    console.log("swapped image");
}         



















