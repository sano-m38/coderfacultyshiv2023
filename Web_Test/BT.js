var currentImage=0;

function next(){
    if (currentImage>=2){
        currentImage=0;
    } else {
        currentImage++;
}

    Document.querySelector("#image").src="images/"+currentImage+".jpeg"

}


// try example in Udemy video not working 
