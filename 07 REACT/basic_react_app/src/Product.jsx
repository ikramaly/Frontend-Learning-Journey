
function Product({title}){
    return(
        <div id="Product">
            <h4>{title}</h4>
            <Price oldPrice={}/>
        </div>
    )
}
export default Product;
import Price from "./Price";
import "./Product.css";