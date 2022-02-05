import React from "react"
import { remove } from "../store"
import { connect } from "react-redux";
import { Link } from "react-router-dom"

//Home으로 부터 props text
//mapDispatchToProps으로 부터 props dispatch
//ownProps으로 부터 props id
const ToDo = ({text, onBtnClick, id}) => {

    return (
    <li>
        <Link to={`/${id}`}>
            {text}
        </Link>
            <button onClick={onBtnClick}>DEL</button>
    </li>
    )
}



function mapDispatchToProps(dispatch, ownProps) {
    return {
        onBtnClick: () => dispatch(remove(ownProps.id))
    }
}

export default connect(null, mapDispatchToProps)(ToDo);