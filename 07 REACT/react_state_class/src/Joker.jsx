import js from "@eslint/js";
import { useEffect, useState } from "react";

export default function Joker(){
    const URL = "https://official-joke-api.appspot.com/random_joke";
    let [joke, setJoke]=useState({});
    const getNewJoke = async ()=>{
        let response = await fetch(URL);
        // Now we will convert into the json response
        let jsonResponse = await response.json();
        console.log(jsonResponse.setup);
        console.log(jsonResponse.punchline);
        // return jsonResponse;
        setJoke({
            setup: jsonResponse.setup,
            punchline: jsonResponse.punchline
        });
    };
    useEffect(()=>{
        async function getNewJoke(){
            let response = await fetch(URL);
            // Now we will convert into the json response
            let jsonResponse = await response.json();
            setJoke({
                setup: jsonResponse.setup,
                punchline: jsonResponse.punchline
            });
        };
        getNewJoke();
    },[])
 
    return(
        <div>
            <h3>Joker!</h3>
            <h4>{joke.setup}</h4>
            <p>{joke.punchline}</p> <br />
            <button onClick={getNewJoke}>Get New Joke!</button>
        </div>
    )
}