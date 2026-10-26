import { useState } from "react"

export default function Form(){
    let [formData, setFormData] = useState({
        username : '',
        remarks : '',
        rating : '',
    });

    let handleInput = (event)=>{
        setFormData((currData)=>{
            return(
                {
                    ...currData,
                    [event.target.name] : event.target.value,
                }
            )
        })
    }
    let handleSubmit =(event)=>{
        event.preventDefault();
        setFormData((currData)=>{
            return{
                username : '',
                remarks : '',
                rating : '',
            }
        })
        console.log(formData);        
    }
    return(
        <form onSubmit={handleSubmit}>
            <label htmlFor="username">UserName : </label>
            <input 
                type="text"
                placeholder="UserName..." 
                id="username"
                name="username"
                value={formData.username}
                onChange={handleInput}
            /> <br /><br />
            <label htmlFor="remarks">Remarks : </label>
            <textarea 
                type="text"
                placeholder="Remarks...." 
                id="remarks"
                value={formData.remarks}
                name="remarks"
                onChange={handleInput}
            /> <br /> <br />
            <label htmlFor="rating">Rating : </label>
            <input 
                type="number"
                placeholder="Ratig...." 
                id="rating"
                value={formData.rating}
                name="rating"
                min={1}
                max={5}
                onChange={handleInput}
            /> <br /> <br />
            <button>Add Comment </button>
            
        </form>
    )
}