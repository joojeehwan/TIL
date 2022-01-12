import { createStore } from "redux";

const add = document.getElementById("add")
const minus = document.getElementById("minus")
const number = document.querySelector("span")

// const countModifer = (count = 0) => {

//   return count
// }

const ADD = "ADD";
const MINUS = "MINUS";
number.innerText = 0
const countModifier = (count = 0, action) => {

  switch (action.type) {
    case ADD:
      return count + 1;
    case MINUS:
      return count - 1;
    default:
      return count;
  }
};



const countStore = createStore(countModifier);

const onChange = () => {
  number.innerText = countStore.getState()
}
countStore.subscribe(onChange)

add.addEventListener("click", () => countStore.dispatch({type:ADD}))
minus.addEventListener("click", () => countStore.dispatch({type:MINUS}))






// const updateText = () => {
//   number.innerText = count
//   updateText()
// }

// const handleAdd = () => {
//   count = count += 1
//   updateText()
// }

// const handleminus = () => {
//   count = count -= 1
//   updateText()
// }



// add.addEventListener("click", handleAdd)
// minus.addEventListener("click", handleminus)