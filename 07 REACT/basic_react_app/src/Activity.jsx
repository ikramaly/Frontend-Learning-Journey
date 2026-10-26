function Activity({userName,textColor}){
    let color = {color : textColor};
    return(
        <>
        <div>
            <h1 style={color}>UserName : {userName}</h1>
        </div>
        </>
    )
};

export default Activity;
