import { HYDRATE } from "next-redux-wrapper"
import { combineReducers } from 'redux';

import user from './user';
import post from './post';



//액션을 함수를 통해서 동적으로 생성 할 수도 있음
//action creater


// changeNickname("neasdfa")
// ```
//   {
//     type:"CHANGE_NICKNAME",
//     data: "neasdfa"
//   }

// ```
// store.dispatch(changeNickname("sdfadfa"))

// //액션 부분
// const changeNickname = {
//   tpye: "CHANGE_NICKNAME", 
//   data: "sexyjeehwan"
// }

//리듀셔 부분
// (이전상태, 엑션) => 다음 상태
const rootReducers = combineReducers({
  index: (state = {}, action) => {
    switch (action.type) {
      case HYDRATE:
        console.log('HYDRATE', action)
        return { ...state, ...action.payload }
      default:
        return state;
    }
  },
  user,
  post,
})

export default rootReducers