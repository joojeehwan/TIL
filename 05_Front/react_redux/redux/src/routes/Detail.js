import React from "react";
import { useParams } from "react-router-dom";
import { connect } from "react-redux";

function Detail({toDo}) {
    const id = useParams()
    console.log(id)
    return (
        <>
        {toDo.id}
        Created at{toDo.id}
        </>
    )
}


const mapStateToProps = (state) => {

    return { toDo: state };
    }
export default connect(mapStateToProps)(Detail);



