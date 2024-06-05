var currentIndex=0;
var images=[ "game1.jpg" , "game2.jpg" , "game3.jpg"];
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


// var currentImage=0;

// function next(){
//     if (currentImage>=3){
//         currentImage=1;
//     } else {
//         currentImage=currentImage+1;
//     }

//     document.querySelector("#image").src="images/game1"+currentImage+".jpeg"

// }



















