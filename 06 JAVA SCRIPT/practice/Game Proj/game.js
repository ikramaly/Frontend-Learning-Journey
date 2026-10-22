//We are trying to make a array for storing the value of the game.
let gameSeq =[];
let userSeq =[];

let started = false;
let level = 0;
let btns = ["red","yellow","green","purple"];

let H2 = document.querySelector("h2");
// let btn = document.querySelector(".btn");


document.addEventListener("keypress",function(event){
    if(started==false){
        console.log("Game is started..");
        started = true;
        levelUp();
    }
});
// btn flash func 
function gameFlash(btn){
    btn.classList.add("flash-color");
    setTimeout(function() {
        btn.classList.remove("flash-color");      
    }, 300);
};
//user btnflash 
function userFlash(btn){
    btn.classList.add("userFlash");
    setTimeout(function(){
        btn.classList.remove("userFlash");      
    }, 300);
}
// Level Up step by step.......
function levelUp(){
    userSeq = [];
    level++;
    H2.innerText = `Level : ${level}`;
    
    let ranIdx = Math.floor(Math.random()*4);
    let ranColor = btns[ranIdx];
    let ranBtn = document.querySelector(`.${ranColor}`);
    gameSeq.push(ranColor);
    gameFlash(ranBtn);
    console.log("gameSeq : ",gameSeq);
    

}
// check ans both user and game sequences are same or not..
function checkAns (idx){
    console.log(`Level : ${level}.`);
    
    if(userSeq[idx]==gameSeq[idx]){
        if(userSeq.length == gameSeq.length){
            setTimeout(levelUp,1000);
        }else{
            H2.innerText =`Game Over! Press any key to start.`;
        }
    }
    
}
//button press function by user
function btnPress(){
    // console.log("Button Was Pressed by user ",this);
    let btn = this;
    userFlash(btn);

    userColor = btn.getAttribute("id");
    userSeq.push(userColor);
    checkAns(userSeq.length-1);
};

let allBtns = document.querySelectorAll(".btn");
for(btn of allBtns){
    btn.addEventListener("click",btnPress);
};

function sequence(){
    console.log("gameSeq : ",gameSeq);
    console.log("userSeq : ",userSeq);
}


