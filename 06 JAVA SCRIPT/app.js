// let h1 = document.querySelector("h1");
// function changeColor(color,delay){
//     return new Promise((resolve, reject)=>{
//         setTimeout(() => {
//         h1.style.color = color;
//         // let num = Math.floor(Math.random()*8)+1;
//         // if(num>7){
//         //     reject("Weak Connection.");
//         // }
//         console.log(`color changed successfully : ${color}.`)
//         resolve("Color Changed !");
//     }, delay);
//     });

// };

// async function colorChanged(){
//     try{
//         await changeColor("red",1000);
//         await changeColor('green',1000);
//         await changeColor("blue",1000);
//         await changeColor("pink",1000);
//         await changeColor("orange",1000,i);
//         await changeColor("purple",1000);
//     }catch(error){
//         console.log('Error Cought');
//         console.log(error);
//     }
//     let a = 29;
//     console.log(a+34);
    

// };
// colorChanged();
// // function getNum(){
// //     return new Promise((resolve,rejected)=>{
// //         setTimeout(() => {
// //             let num = Math.floor(Math.random()*10)+1;
// //             console.log("num : ",num);
// //             resolve("Promise Resolved.");
// //         }, 1000);
// //     })
// // };
// // async function deepo(){
// //     await getNum();
// //     await getNum();
// //     await getNum();
// //     // await console.log(getNum());
// //     getNum();
// //     getNum();
// // };
// // deepo();

// let json ='{"fact":"The average cat food meal is the equivalent to about five mice.","length":63}';
// // console.log(json);

// let jsonParseData = JSON.parse(json); 

// console.log(jsonParseData);

// console.log("Now we will convert into the JSON OBject data into JSON Data.");

// let jsonData = JSON.stringify(jsonParseData);
// // console.log(jsonData);

// let urll = "https://catfact.ninja/fact";
// // fetch(urll).then((res)=>{
// //     console.log("Res : ",res);
// //     return res.json();
// // }).then((data)=>{
// //     console.log("Data1 = ",data.fact);
// //     return fetch(urll);
// // }).then((res2)=>{
// //     console.log("Res2 : ",res2)
// //     return res2.json(); 
// // }).then((data2)=>{
// //     console.log("Data2 : ",data2.fact)
// // })
// // .catch((err)=>{
// //     console.log("Error : ",err)
// // });
// async function getFact() {
//     try{
//         let res = await axios.get(urll);
//         console.log(res.data.fact);
        
//     }catch(e){
//         console.log("Error : ",e);
//     }    
    
// }
// let urll = "https://catfact.ninja/fact";
// let urllll = "https://dog.ceo/api/breeds/image/random";
// let btn = document.querySelector("button");
// let para = document.querySelector("#para");
// let img = document.querySelector("#img");


// btn.addEventListener("click",()=>{
//     console.log("Button was clicked.");
//     getFact();  
// })
// async function getFact() {
//         try {
//             let res = await axios.get(urll);
//             console.log("res.data.fact : ",res.data.fact);
//             para.innerText = res.data.fact;

//             let dogRes = await axios.get(urllll);
//             console.log(dogRes);
//             console.log(dogRes.data.message);
//             img.setAttribute("src",dogRes.data.message);
//             console.log("Image print succcessfully.");
            

//         } catch (error) {
//             console.log("Error : ",error);
//         }        
//     }

let urll3 = "https://icanhazdadjoke.com/";
// console.log(fetch(urll3));
async function getjoke2() {
    let congig = {headers : {Accept : "application/json"}};
    let res = await axios.get(urll3,congig)
    console.log("JOKE : ",res.data.joke);
};

