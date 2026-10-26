function genTicketNum(n){
    // we will create the seprate array instead
    // of the create the individual var
    let arr = new Array(n);
    // we will enter the value of the array inside the arr
    for(let i=0; i<n; i++){
        arr[i] = Math.floor((Math.random())*10)+1;
        // this is called math random num generation.
    }
    return arr;
}// buy tickwt
// for sum the array 
function sum(arr){
    return arr.reduce((sum, currvalue)=>{
        return sum+currvalue;
    },0)// this is the current '0' value of the array.
};
export {genTicketNum, sum};