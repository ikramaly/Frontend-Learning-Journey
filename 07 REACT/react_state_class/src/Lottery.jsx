import { useState } from "react";
import { genTicketNum,sum } from "./helper"; // this is called helper function file in javascript.
import Ticket from "./Ticket";


export default function Lottery({n, winningSum}){
    let [ticket , setTicket] = useState([]);
    let isWinning = sum(ticket) === winningSum; // it will be set the true boolean value;

     

    function BuyTicket(){
        setTicket(genTicketNum(n));
    }
    // console.log(num);
    return(
        <div>
            <h2>Lottery Game </h2> <br />
            {/* now we will call the Ticket Components */}
            <Ticket ticket={ticket} />  <br /><br />

            <button onClick={BuyTicket}>Buy New Ticket </button> <br />
            <p>{isWinning && "Congrats you won the lottery!"}</p>

        </div>
    )
}