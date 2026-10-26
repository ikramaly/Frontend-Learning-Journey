export default function Button(){
    return(
        <div>
            <button onClick={Hello}> Click Me!</button>
            <p onMouseOver={Over}>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima commodi sapiente esse recusandae tempore, dolores voluptatem quis harum magnam, voluptates et, incidunt maxime! Similique, alias voluptatum perspiciatis pariatur amet enim?
            </p>
        </div>
    )
};

function Hello(){
    console.log("Hello To All.");
}
function Over(){
    console.log("We Over the mouse on the paragraph.")
}