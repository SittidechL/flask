let toggle = document.querySelector(".toggle");
let text = document.querySelector(".text");

function Animatedtoggle(){
    toggle.classList.toggle("active");

    if(toggle.classList.contains("active")){
        text.innerHTML = "ON";
    }
    else{
        text.innerHTML = "OFF";
    }   

}