import { useEffect, useState } from "react"

export default function Counter(){
    
    let [countx, setCountx] = useState(0);
    let [county, setCounty] = useState(0);
    let intCountx = ()=>{
        setCountx((currCount)=>{
            return currCount+=1;
        });
    };
    // but we want to use sideEffect();
    useEffect(function Printsome(){
        console.log("UseEffect X");
    }, [countx]);
 
    let intCounty = ()=>{
        setCounty((currCount)=>{
            return currCount+=1;
        });      
    }; 
    // but we want to use sideEffect();
    useEffect(function Printsome(){
        console.log("UseEffect Y");
    },[])

    return(
        <div>  
            <h3>Countx = {countx}</h3>
            <button onClick={intCountx}>+1</button>
            <h3>County = {county}</h3>
            <button onClick={intCounty}>+1</button>
        </div>
    )
}