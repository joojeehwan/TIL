export const initalState = {
  logInLoading: false, // 로그인 시도중
  logInDone: false,
  logInError: null,
  logOutLoading: false, // 로그아웃 시도중
  logOutDone: false,
  logOutError: null,
  signUpLoading: false,  //회원가입 시도중
  signUpDone: false, 
  signUpError: false,
  changeNicknameLoading: false, // 닉네임 변경 시도중
  changeNicknameDone: false,
  changeNicknameError: null, 
  me: null,
  signUpData: {},
  loginData: {},




}


export const LOG_IN_REQUEST = 'LOG_IN_REQUEST';
export const LOG_IN_SUCCESS = 'LOG_IN_SUCCESS';
export const LOG_IN_FAILURE = 'LOG_IN_FAILURE';

export const LOG_OUT_REQUEST = 'LOG_OUT_REQUEST';
export const LOG_OUT_SUCCESS = 'LOG_OUT_SUCCESS';
export const LOG_OUT_FAILURE = 'LOG_OUT_FAILURE';

export const SIGN_UP_REQUEST = 'SIGN_UP_REQUEST';
export const SIGN_UP_SUCCESS = 'SIGN_UP_SUCCESS';
export const SIGN_UP_FAILURE = 'SIGN_UP_FAILURE';

export const CHANGE_NICKNAME_REQUEST = 'CHANGE_NICKNAME_REQUEST';
export const CHANGE_NICKNAME_SUCCESS = 'CHANGE_NICKNAME_SUCCESS';
export const CHANGE_NICKNAME_FAILURE = 'CHANGE_NICKNAME_FAILURE';

export const FOLLOW_REQUEST = 'FOLLOW_REQUEST';
export const FOLLOW_SUCCESS = 'FOLLOW_SUCCESS';
export const FOLLOW_FAILURE = 'FOLLOW_FAILURE';

export const UNFOLLOW_REQUEST = 'UNFOLLOW_REQUEST';
export const UNFOLLOW_SUCCESS = 'UNFOLLOW_SUCCESS';
export const UNFOLLOW_FAILURE = 'UNFOLLOW_FAILURE';

export const ADD_POST_TO_ME = 'ADD_POST_TO_ME';
export const REMOVE_POST_OF_ME = 'REMOVE_POST_OF_ME';


const dummyUser = (data) => ({
  ...data,
  nickname: '지환주',
  id: 1,
  Posts: [{ id: 1 }],
  Followings: [{ nickname: '부기초' }, { nickname: 'Chanho Lee' }, { nickname: 'neue zeal' }],
  Followers: [{ nickname: '부기초' }, { nickname: 'Chanho Lee' }, { nickname: 'neue zeal' }],
});

export const loginRequestAction = (data) => {
  return {
    type: LOG_IN_REQUEST, 
    data,
  }
}
export const loginSuccessAction = (data) => {
  return {
    type: LOG_IN_SUCCESS, 
    data,
  }
}
export const loginFailureAction = (data) => {
  return {
    type: LOG_IN_FAILURE, 
    data,
  }
}

export const logoutRequestAction = () => {
  return {
    type: LOG_OUT_REQUEST, 
  
  }
}
export const logoutSuccessAction = () => {
  return {
    type: LOG_OUT_SUCCESS, 
  
  }
}
export const logoutFailureAction= () => {
  return {
    type: LOG_OUT_FAILURE, 
  
  }
}


//initalState의 depth를 생각하기
const reducer = (state = initalState, action) => {
  switch (action.type) {

    case LOG_IN_REQUEST:
      // return  {
      //   ...state, //처음 initalstate객체 핀것!
      //   user: { 
      //     ...state.user, //user객체 안의 것들이라!!
      //     isLoggedIn: true,
      //     user: action.data
      //   }
      // }
      console.log("reducer login")
      return  {
        ...state,
          logInLoading: true, 
          logInError: null,
          logInDone: false, 
      }
    case LOG_IN_SUCCESS:
      return  {
          ...state,
          logInLoading: false,
          logInDone: true,
          me: dummyUser(action.data)
      }

    case LOG_IN_FAILURE:
      return  {
        ...state,
        logInLoading: false,
        logInError: action.error,
      }
    case LOG_OUT_REQUEST:
      return  {
        ...state,
        logOutLoading: true,
        logOutDone: false,
        logOutError: null, 
      }
    case LOG_OUT_SUCCESS:
      return  {
        ...state,
        logOutLoading: false,
        logOutDone: true,
        me: null  
      }
    case LOG_OUT_FAILURE:
      return  {
        ...state,
        logOutLoading: false,
        logOutError: action.error
 
      }
    case SIGN_UP_REQUEST:
      return  {
        ...state,
        signUpLoading: true,
        signUpDone: false,
        signUpError: null, 
      }
    case SIGN_UP_SUCCESS:
      return  {
        ...state,
        signUpLoading: false,
        signUpDone: true,
      }
    case SIGN_UP_FAILURE:
      return  {
        ...state,
        signUpLoading: false,
        signUpError: action.error
 
      }

      case CHANGE_NICKNAME_REQUEST:
        return {
          ...state, 
          changeNicknameLoading: true, 
          changeNicknameError: null, 
          changeNicknameDone: false, 

        }
     
      case CHANGE_NICKNAME_SUCCESS:
          return {
            ...state, 
            changeNicknameLoading: false, 
            changeNicknameDone: true, 
          }
        
      case CHANGE_NICKNAME_FAILURE:
          return {
            changeNicknameLoading: false, 
            changeNicknameError: action.error
          }

      case ADD_POST_TO_ME:
        return {
          ...state, 
          me: {
            ...state.me,
            Posts: [{id: action.data}, ...state.me.Posts]
          }
        }
      case REMOVE_POST_OF_ME:
        return {
          ...state, 
          me: {
            ...state.me,
            Posts: state.me.Posts.filter((V) => v.id !== action.data)
          }
        }
       
      // return  {
      //   ...state, //처음 initalstate객체 핀것!
      //   user: { 
      //     ...state.user, //user객체 안의 것들이라!!
      //     isLoggedIn: false,
      //     user: null
      //   }
      // }

    default:
      return state
  }
}


export default reducer