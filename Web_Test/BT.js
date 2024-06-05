var currentImage=0;

function next(){
    if (currentImage>=3){
        currentImage=1;
    } else {
        currentImage=currentImage+1;
    }

    document.querySelector("#image").src="images/car"+currentImage+".jpeg"

}


// try example in Udemy video not working 
