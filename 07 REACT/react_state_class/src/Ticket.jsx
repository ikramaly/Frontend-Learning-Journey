import TicketNum from "./TicketNum";
import "./Ticket.css"

export default function Ticket({ticket}){
    return(
        <div className="Ticket"> 
            {/* <p>Now we will use the best method for generate the game.</p>
            <h4>Map Method </h4> */}

            { 
                ticket.map((num1, idx)=>(
                    <TicketNum num={num1} key={idx}/>
                ))
            }
        </div>
    );
}