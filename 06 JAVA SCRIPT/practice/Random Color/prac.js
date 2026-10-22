let btn = document.querySelector('.btn');
console.log("check classList = ", btn.classList);
btn.classList.add("btn-hover");

let colorBox = document.querySelector(".color-box");

btn.addEventListener("click",()=>{
    console.log("random color : ",randomColor());
    let H1 = document.querySelector(".main-heading");
    H1.innerText = randomColor();

    let colorBox = document.querySelector(".color-box");
    colorBox.style.backgroundColor = randomColor();
 
    console.log("Color Updated Successfully.");
})

function randomColor(){
    let red = Math.floor(Math.random()*255)+1;
    let green = Math.floor(Math.random()*255)+1;
    let blue = Math.floor(Math.random()*255)+1;
    
    let color = `rgb(${red},${green},${blue})`;
    return color;    
}







