import { createStore } from "redux";
import { createAction, createReducer, configureStore, createSlice} from "@reduxjs/toolkit"



// const ADD = "ADD";
// const DELETE = "DELETE";


// export const addToDo = text => {
//   return {
//     type: ADD,
//     text
//   };
// };

// export const deleteToDo = id => {
//   return {
//     type: DELETE,
//     id: parseInt(id)
//   };
// };

 // const reducer = (state = [], action) => {
//   switch (action.type) {
//     case addToDo.type:
//       console.log(action)
//       return [{ text: action.payload, id: Date.now() }, ...state];
//     case deleteToDo.type:
//       return state.filter(toDo => toDo.id !== action.payload);
//     default:
//       return state;
//   }
// };



// const addToDo = createAction("ADD")
// const deleteToDo = createAction("DELETE")



// 불변성을 지키지 않아도 됨
// const reducer = createReducer([],  {

//     [addToDo]: (state, action) => {
//       state.push({text: action.payload, id: Date.now() });
//     },
//     [deleteToDo]: (state, action) => 
//       state.filter(toDo => toDo.id !== action.payload)


// })


//액션 + 리듀서
const toDos = createSlice({
  name:"toDoReducer", 
  initialState: [],
  reducers: {
    add: (state, action) => {
      state.push({text: action.payload, id: Date.now() });
  }, 
    remove: (state, action) => 
    state.filter(toDo => toDo.id !== action.payload)
  }
})

//그냥 알아서 리듀서를!
// const store = configureStore({reducer: toDos.reducer});


// export const actionCreators = {
//     addToDo,
//     deleteToDo
//   };
  
export const {add, remove} = toDos.actions

export default configureStore({reducer: toDos.reducer});