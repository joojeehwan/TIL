# 불변성의 늪에서 구해줄 immer





그 전까지의 코드 

인덱스 리듀서



````js
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
````



포스트.js

````js
import shortId from "shortid"


export const initialState = {
  mainPosts: [{
    id: 1,
    User: {
      id: 1,
      nickname: '제로초',
    },
    content: '첫 번째 게시글 #해시태그 #익스프레스',
    Images: [{
      src: 'https://bookthumb-phinf.pstatic.net/cover/137/995/13799585.jpg?udate=20180726',
    }, {
      src: 'https://gimg.gilbut.co.kr/book/BN001958/rn_view_BN001958.jpg',
    }, {
      src: 'https://gimg.gilbut.co.kr/book/BN001998/rn_view_BN001998.jpg',
    }],
    Comments: [{
      User: {
        nickname: 'nero',
      },
      content: '우와 개정판이 나왔군요~',
    }, {
      User: {
        nickname: 'hero',
      },
      content: '얼른 사고싶어요~',
    }]
  },
  
],
  imagePaths: [],
  addPostLoading: false,
  addPostDone: false,
  addPostError: null,
  removePostLoading: false,
  removePostDone: false,
  removePostError: null,
  addCommentLoading: false,
  addCommentDone: false,
  addCommentError: null,
};


//액션의 이름을 변수로 뺴놓네?! 
// => 장점 리듀서에서 적을때 오타가 나면 알 수 있어서!
export const ADD_POST_REQUEST = "ADD_POST_REQUEST"
export const ADD_POST_SUCCESS = "ADD_POST_SUCCESS"
export const ADD_POST_FAILURE = "ADD_POST_FAILURE"

export const REMOVE_POST_REQUEST = 'REMOVE_POST_REQUEST';
export const REMOVE_POST_SUCCESS = 'REMOVE_POST_SUCCESS';
export const REMOVE_POST_FAILURE = 'REMOVE_POST_FAILURE';

export const ADD_COMMENT_REQUEST = 'ADD_COMMENT_REQUEST';
export const ADD_COMMENT_SUCCESS = 'ADD_COMMENT_SUCCESS';
export const ADD_COMMENT_FAILURE = 'ADD_COMMENT_FAILURE';

//동적 액션 creator
export const addPost = (data) => ({
  type: ADD_POST_REQUEST,
  data, 
})


export const addComment = (data) => ({
  type: ADD_COMMENT_REQUEST,
  data,
});

const dummyPost = (data) => ({
  id: data.id,
  content: data.content,
  User: {
    id: 1,
    nickname: '제로초',
  },
  Images: [],
  Comments: [],
});



const dummyComment = (data) => ({
  id: shortId.generate(),
  content: data,
  User: {
    id: 1,
    nickname: '제로초',
  },

})
const reducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_POST_REQUEST:
      return {
        ...state,
        addPostLoading: true, 
        addPostDone: false,
        addPostError: null, 
      }
    case ADD_POST_SUCCESS:
        return {
          ...state,
          mainPosts: [dummyPost(action.data), ...state.mainPosts],
          addPostLoading: false, 
          addPostDone: true, 
        }
    case ADD_POST_FAILURE:
      return {
        ...state, 
        addPostLoading: false, 
        addPostError: action.error, 
      }
    case REMOVE_POST_REQUEST:
      return {
        ...state,
        removePostLoading: true, 
        removePostDone: false,
        removePostError: null, 
      }
    case REMOVE_POST_SUCCESS:
        return {
          ...state,
          mainPosts: state.mainPosts.filter((v) => v.id !== action.data),
          removePostLoading: false, 
          removePostDone: true, 
        }
    case REMOVE_POST_FAILURE:
      return {
        ...state, 
        removePostLoading: false, 
        removePostError: action.error, 
      }
    // eslint-disable-next-line no-duplicate-case
    case ADD_COMMENT_REQUEST:
      return {
        ...state,
        addCommentLoading: true, 
        addCommentDone: false,
        addCommentError: null, 
      }
    case ADD_COMMENT_SUCCESS: {

      const postIndex = state.mainPosts.findIndex((v) => v.id === action.data.postId)
      const post = {...state.mainPosts[postIndex]}
      post.Comments = [dummyComment(action.data.content), ...post.Comments]
      const mainPosts = [...state.mainPosts]
      mainPosts[postIndex] = post
        return {
          ...state,
          //더미 포스트가 앞에 있어야 최신글이 위로! 
          //기존에 있던 게시글들도 있어야 하잖아! 그래서 ...state.main
          mainPosts,
          addCommentLoading: false, 
          addCommentDone: true, 
        }
    }
    case ADD_COMMENT_FAILURE:
      return {
        ...state, 
        addCommentLoading: false, 
        addCommentError: action.error, 
      }

    default:
      return {
        ...state
      }
  }
}


export default reducer
````



유저.js

````js
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
````





인덱스 사가

```js
import { all, fork } from 'redux-saga/effects';

import userSaga from './user';
import postSaga from './post'

export default function* rootSaga() {
  yield all([
    fork(userSaga),
    fork(postSaga)
  ]);
}
```



포스트 사가

```js
import axios from 'axios';
import shortId from 'shortid';
import {delay, all, takeLatest, fork, put } from "redux-saga/effects";
import 
{ ADD_COMMENT_FAILURE, 
  ADD_COMMENT_REQUEST, 
  ADD_COMMENT_SUCCESS, 
  ADD_POST_FAILURE, 
  ADD_POST_REQUEST, 
  ADD_POST_SUCCESS,
  REMOVE_POST_SUCCESS,
  REMOVE_POST_FAILURE,
  REMOVE_POST_REQUEST,

} from '../reducers/post';
import { ADD_POST_TO_ME } from '../reducers/user';



  function addPostAPI(data) {
    return axios.post('/api/post', data);
  }

function* addPost(action) {
  try {
    // const result = yield call(addPostAPI, action.data);
    yield delay(1000);
    const id = shortId.generate()
    yield put({
      type: ADD_POST_SUCCESS,
      data: {
        id, 
        content:action.data
      }
    });
    yield put({
      type: ADD_POST_TO_ME, 
      data: id,
    })
  } catch (err) {
    console.error(err);
    yield put({
      type: ADD_POST_FAILURE,
      error: err.response.data,
    });
  }
}

  function removePostAPI(data) {
    return axios.delete('/api/post', data);
  }

function* removePost(action) {
  try {
    // const result = yield call(addPostAPI, action.data);
    yield delay(1000);
    yield put({
      type: REMOVE_POST_SUCCESS,
      data: action.data
    });
    yield put({
      type: REMOVE_POST_OF_ME, 
      data: action.data,
    })
  } catch (err) {
    console.error(err);
    yield put({
      type: REMOVE_POST_FAILURE,
      error: err.response.data,
    });
  }
}

function addCommentAPI(data) {
  return axios.post(`/api/post/${data.postId}/comment`, data);
}

function* addComment(action) {
  try {
    // const result = yield call(addCommentAPI, action.data);
    yield delay(1000);
    yield put({
      type: ADD_COMMENT_SUCCESS,
      data: action.data
    });
  } catch (err) {
    yield put({
      type: ADD_COMMENT_FAILURE,
      data: err.response.data,
    });
  }
}


function* watchAddPost() {
  yield takeLatest(ADD_POST_REQUEST, addPost)
}


function* watchRemovePost() {
  yield takeLatest(REMOVE_POST_REQUEST, removePost)
}

function* watchAddComment() {
  yield takeLatest(ADD_COMMENT_REQUEST, addComment);
}


export default function* postSaga() {
  yield all([
    fork(watchAddPost),
    fork(watchAddComment),
    fork(watchRemovePost)
  ])
}
```



유저 사가

```js
import { all, delay, fork, put, takeLatest } from 'redux-saga/effects';
import axios from 'axios';
import { 
  LOG_IN_FAILURE, 
  LOG_IN_REQUEST, 
  LOG_IN_SUCCESS, 
  LOG_OUT_FAILURE, 
  LOG_OUT_REQUEST, 
  LOG_OUT_SUCCESS,
  SIGN_UP_FAILURE,
  SIGN_UP_REQUEST,
  SIGN_UP_SUCCESS,
} from '../reducers/user';

function logInAPI(data) {
  return axios.post('/api/login', data);
}

function* logIn(action) {
  try {
    console.log('saga logIn');
    // const result = yield call(logInAPI);
    yield delay(1000);
    yield put({
      type: LOG_IN_SUCCESS,
      data: action.data,
    });
  } catch (err) {
    console.error(err);
    yield put({
      type: LOG_IN_FAILURE,
      error: err.response.data,
    });
  }
}

function logOutAPI() {
  return axios.post('/api/logout');
}

function* logOut() {
  try {
    // const result = yield call(logOutAPI);
    yield delay(1000);
    yield put({
      type: LOG_OUT_SUCCESS,
    });
  } catch (err) {
    console.error(err);
    yield put({
      type: LOG_OUT_FAILURE,
      error: err.response.data,
    });
  }
}

function signUpAPI() {
  return axios.post('/api/signUp');
}

function* signUp() {
  try {
    // const result = yield call(signUpAPI);
    yield delay(1000);
    yield put({
      type: SIGN_UP_SUCCESS,
    });
  } catch (err) {
    console.error(err);
    yield put({
      type: SIGN_UP_FAILURE,
      error: err.response.data,
    });
  }
}

function* watchLogIn() {
  yield takeLatest(LOG_IN_REQUEST, logIn);
}

function* watchLogOut() {
  yield takeLatest(LOG_OUT_REQUEST, logOut);
}

function* watchSignUp() {
  yield takeLatest(SIGN_UP_REQUEST, signUp);
}


export default function* userSaga() {
  yield all([
    
    fork(watchLogIn),
    fork(watchLogOut),
    fork(watchSignUp),
    
  ]);
}
```



포스트 폼 / 포스트 카드 폼

````
import React, {useRef, useCallback, useState, useEffect} from "react"
import {Form, Input, Button} from "antd"
import { useSelector, useDispatch } from 'react-redux';

import { addPost } from "../reducers/post";


const PostForm = () => {

    const dispatch = useDispatch()
    const [text, setText] = useState("")
    const { imagePaths, addPostLoading, addPostDone } = useSelector((state) => state.post);

    const imageInput = useRef()
    
    const onClickImageUpload = useCallback(() => {
      imageInput.current.click();
    }, [imageInput.current]);
    
    
    useEffect(() => {
      if (addPostDone) {
        setText('');
      }
    }, [addPostDone]);
    
    const onChangeText = useCallback((e) => {
      setText(e.target.value);
    }, []);

    const onSubmit = useCallback(() => {
      console.log("서브밋")
      dispatch(addPost(text));
    }, [text])
    

    return (
        <Form style={{ margin: '10px 0 20px' }} encType="multipart/form-data" onFinish={onSubmit}>
           <Input.TextArea value={text} onChange={onChangeText} maxLength={140} placeholder="어떤 신기한 일이 있었나요?" />
          <div>
            <input type="file" multiple hidden ref={imageInput}  />
            <Button onClick={onClickImageUpload}>이미지 업로드</Button>
            <Button type="primary" style={{ float: 'right' }} htmlType="submit">짹짹</Button>
          </div>
          <div>
          {imagePaths.map((v) => {
          return (
            <div key={v} style={{ display: 'inline-block' }}>
              <img src={v} style={{ width: '200px' }} alt={v} />
              <div>
                <Button>제거</Button>
              </div>
            </div>
          )
        })}
          </div>
        </Form>
    )

}

export default PostForm




-----------------------------------------

import { EllipsisOutlined, HeartOutlined, MessageOutlined, RetweetOutlined, HeartTwoTone } from "@ant-design/icons"
import PropTypes from 'prop-types';
import { Card, Popover, Button, Avatar, List, Comment } from "antd"
import React, {useCallback, useState}from "react"
import Link from 'next/link';
import { useSelector, useDispatch } from 'react-redux';

import PostImages from "./PostImages";
import CommentForm from "./CommentForm";
import PostCardContent from "./PostCardContent";

import styled from 'styled-components';
import { REMOVE_POST_REQUEST } from "../reducers/post";

const CardWrapper = styled.div`
  margin-bottom: 20px;
`;


const PostCard = ({ post }) => {

  const dispatch = useDispatch()
  const {removePostLoding} = useSelector((state) => state.post)
  const [commentFormOpened, setCommentFormOpened] = useState(false)
  const [liked, setLiked] = useState(false);

  const onToggleLike = useCallback(() => {
    setLiked((prev) => !prev)
  }, [])

  const onToggleComment = useCallback(() => {
    setCommentFormOpened((prev) => !prev);
  }, []);

  const onRemovePost = useCallback(() => {
    dispatch({
      type: REMOVE_POST_REQUEST,
      data: post.id
    })
  }, [])

  const id = useSelector((state) => state.user.me?.id)
  return (

    <CardWrapper key={post.id}>
      <Card
        cover={post.Images[0] && <PostImages images={post.Images} />}
        actions={[
          <RetweetOutlined key="retweet"/>,
          liked
            ? <HeartTwoTone twoToneColor="#eb2f96" key="heart" onClick={onToggleLike} />
            : <HeartOutlined key="heart" onClick={onToggleLike} />,
          <MessageOutlined key="message" onClick={onToggleComment}/>,
          <Popover
          key="ellipsis"
          content={(
            <Button.Group>
              {id && post.User.id === id
                ? (
                  <>
                    <Button>수정</Button>
                    <Button type="danger" onClick={onRemovePost} loading={removePostLoding}>삭제</Button>
                  </>
                )
                : <Button>신고</Button>}
            </Button.Group>
          )}
            
            
            >
              <EllipsisOutlined/>
          </Popover>
        ]}
      >
      <Card.Meta
          avatar={<Avatar>{post.User.nickname[0]}</Avatar>}
          title={post.User.nickname}
          description={<PostCardContent postData={post.content} />}
      />
      </Card>

      {commentFormOpened && (
      <div>
        <CommentForm post={post}/>
        <List
          header={`${post.Comments.length} 댓글`}
          itemLayout="horizontal"
          dataSource={post.Comments}
          renderItem={(item) => (
            <li>
              <Comment
                author={item.User.nickname}
                avatar={(
                  <Link href={{ pathname: '/user', query: { id: item.User.id } }} as={`/user/${item.User.id}`}>
                    <a><Avatar>{item.User.nickname[0]}</Avatar></a>
                  </Link>
                )}
                content={item.content}
              />
            </li>
          )}
        
        />
      </div>)}

    </CardWrapper>

  )

}

PostCard.propTypes = {
  post: PropTypes.shape({
    id: PropTypes.number,
    User: PropTypes.object,
    content: PropTypes.string,
    createdAt: PropTypes.object,
    Comments: PropTypes.arrayOf(PropTypes.any),
    Images: PropTypes.arrayOf(PropTypes.any),
  }),
}


export default PostCard


````







----

# 리듀서란?!

이전 상태를 액션을 통해 다음 상태로 만들어내는 함수(불변성은 지키면서)

이머에서 드래프트는 불변성에 상관없이 막 바꾸어도 된다. 

이머가 알아서 스테이트를 불변성 지켜서 다음 상태로 전환해준다.

이머를 쓰면 불변성을 오히려 안지켜야 한다! 





----



# 리덕스 toolkit

스위치문을 효율적으로 줄여준다.

=> immer랑 같이 사용하는 부분 확인! 

https://github.com/ZeroCho/react-nodebird/tree/master/toolkit/front

# swr, 



---

# js 배열 합치기



## **배열 합치기 3가지 방법**

> \1. concat() 함수
> \2. ... spread operator (전개 연산자) 
> \3. push() 함수와 spread operator

 

------

 

##  **1. concat() 함수** 

> array.**concat**([value1[, value2[, ...[, valueN]]]])

concat() 함수는

파라미터로 받은 배열이나 값들을 기존의 배열에 합쳐서,

새로운 배열을 만들어서 리턴합니다.

 

 **파라미터** 

**value1~valueN**

기존 배열에 합칠 배열 또는 값

 

 **리턴값** 

기존 배열(array)와 파라미터로 받은 값(value1~valuneN)을 합쳐서 새로 만든 배열

 

###  **예제** 

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="265" width="100%" name="cp_embed_1" scrolling="no" src="https://codepen.io/hianna/embed/oNbOWYY?height=265&amp;theme-id=dark&amp;default-tab=js%2Cresult&amp;user=hianna&amp;slug-hash=oNbOWYY&amp;pen-title=%EB%B0%B0%EC%97%B4&amp;name=cp_embed_1" title="배열" loading="lazy" id="cp_embed_oNbOWYY" style="max-width: 100%; width: 595.763px; overflow: hidden; display: block;"></iframe>

 

 **const newArr = arr.concat('a', ['b', 'c'], 'abc');** 

arr.concat()에 3개의 파라미터를 전달하여

3개의 값을 가진 배열 arr와 파라미터를 합쳤습니다.

arr : [1, 2, 3]

첫번째 : 'a'

두번째 : ['b', 'c']

세번째 : 'abc'

 

concat() 함수는 arr와 전달받은 파라미터들을 합쳐서 

"새로운 배열"을 생성하여 리턴합니다.

이 때, 파라미터가 배열인 경우, 배열 안의 원소들을 꺼내여 새로운 배열에 포함시킵니다.

그래서, 새로운 배열(newArr)의 길이는 6이 아닌 7이 됩니다.

원본인 arr의 값은 변하지 않습니다.

 

 

##  **2. ... spread operator (전개연산자)** 

ES6에서 제공하는 spread operator(...)를 사용하여 배열을 이어 붙일 수 있습니다.

 

 **spread operator(...)** 

spread operator는 한글로 전개 연산자라고도 합니다.

spread operator는 배열과 객체 등 여러 곳에서 사용할 수 있지만,

여기서는 배열에서 사용하는 방법만 간단히 설명합니다.

 

배열에서 spread operator는 배열의 원소들을 분해해서 개별요소로 만들어줍니다.

설명보다는 예제를 보는 것이 더 이해하기 쉽습니다.

 

###  **배열 합치기 예제 (spread operator)** 

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="323" width="100%" name="cp_embed_2" scrolling="no" src="https://codepen.io/hianna/embed/BajERmP?height=323&amp;theme-id=dark&amp;default-tab=js%2Cresult&amp;user=hianna&amp;slug-hash=BajERmP&amp;pen-title=%EB%B0%B0%EC%97%B4&amp;name=cp_embed_2" title="배열" loading="lazy" id="cp_embed_BajERmP" style="max-width: 100%; width: 595.763px; overflow: hidden; display: block;"></iframe>

위의 예제에서 '...' 기호는 spread operator(전개연산자) 입니다.

 

**...arr1, ...arr2, ...arr3**

spread operator ... 은 arr1의 원소들을 쪼개어 개별요소인 1, 2, 3을 리턴합니다.

...arr2는 개별요소인 4, 5, 6을 리턴합니다.

...arr3은 개별요소인 7, 8, 9를 리턴합니다.

 

**newArr는**

이렇게 쪼개진 개별 요소들을 인자로 가지는 새로운 배열입니다.

 

spread operator(전개연산자) 사용이 익숙하다면

매우 간결하게 배열을 합칠 수 있습니다.

spread operator는 이 이외에도 여러가지 방법으로 다양하게 사용됩니다.

자세한 사항은 다음에 spread operator를 다루는 다른 포스팅에서 설명하도록 하겠습니다.

 

 

##  **3. push() 함수와 spread operator** 

spread operator를 사용하면 push() 함수를 이용해서도 여러 개의 배열을 하나로 합칠 수 있습니다.

 

push() 함수에 대해서는 아래의 포스팅을 참조하세요.

[[Javascript\] 배열 앞, 뒤에 값 추가, 삭제하기 (1)](https://hianna.tistory.com/395)

 

###  **push() 함수로 배열 합치기** 

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="265" width="100%" name="cp_embed_3" scrolling="no" src="https://codepen.io/hianna/embed/dyGLWmR?height=265&amp;theme-id=dark&amp;default-tab=js%2Cresult&amp;user=hianna&amp;slug-hash=dyGLWmR&amp;pen-title=%EB%B0%B0%EC%97%B4&amp;name=cp_embed_3" title="배열" loading="lazy" id="cp_embed_dyGLWmR" style="max-width: 100%; width: 595.763px; overflow: hidden; display: block;"></iframe>

push() 함수를 사용하여 배열을 합치면

파라미터로 전달 된 배열을 하나의 원소로 처리합니다.

따라서, 위 예제에서 파라미터로 전달 된 배열은 arr1의 4번째 원소가 됩니다.

따라서, arr1의 길이는 6이 아니라 4가 됩니다.

 

push() 함수를 사용하여, 두 여러개의 배열을 합칠 때, 

concat() 함수를 사용한 것과 같이

파라미터로 전달 된 배열의 원소 각각을 새로운 배열에 넣어서 합치기 위해서는

spread operator(...)를 사용해야 합니다.

 

###  **push() 함수와 spread operator(...)로 배열 합치기** 

<iframe allowfullscreen="true" allowpaymentrequest="true" allowtransparency="true" class="cp_embed_iframe " frameborder="0" height="324" width="100%" name="cp_embed_4" scrolling="no" src="https://codepen.io/hianna/embed/ExPJmOg?height=324&amp;theme-id=dark&amp;default-tab=js%2Cresult&amp;user=hianna&amp;slug-hash=ExPJmOg&amp;pen-title=%EB%B0%B0%EC%97%B4&amp;name=cp_embed_4" title="배열" loading="lazy" id="cp_embed_ExPJmOg" style="max-width: 100%; width: 595.763px; overflow: hidden; display: block;"></iframe>

**arr1.push(...arr2)**

spread operator(...)은 배열의 원소들을 쪼개어 각각의 개별요소를 반환한다고 하였습니다.

그래서 위 예제에서는

파라미터로 전달되는 배열(arr2)에 spread operator를 사용하여

arr2의 원소들을 각각 쪼개주었습니다.

spread operator를 사용함으로써, 이 표현식은

**arr1. push(4, 5, 6)**

와 같은 효과를 가지게 됩니다.





----

# Array () vs new Array() => 같은 것!

>
>
>When `Array` is called as a function rather than as a constructor, it creates and initialises a new Array object. Thus the function call `Array(…)` is equivalent to the object creation expression `new Array(…)` with the same arguments.
>
>Array가 생성자가 아닌 함수로 호출되면 새로운 Array 객체를 생성하고 초기화합니다. 따라서 함수 호출 Array(…)는 동일한 인수를 가진 객체 생성 표현식 new Array(…)와 동일합니다.



---

## map 사용법

map을 사용하는 방법은 callbackfn을 통해 주어진 3개의 인자(요소 값, index, 순회하는 대상 객체)를 사용해 새로운 값을 만드는 함수를 등록하는 것입니다.

```js
const numbers = [1];

numbers.map((number, index, source) => {

    // number: 요소값
    // index: source에서 요소의 index
    // source: 순회하는 대상

    console.log(number);
    // 1

    console.log(index);
    // 0

    console.log(source);
    // [1]

    return number * number;
});
```





----

# 인피니티 스크롤



````js

사가
function* loadPosts(action) {
  try {
    // const result = yield call(loadPostsAPI, action.data);
    yield delay(1000);
    yield put({
      type: LOAD_POSTS_SUCCESS,
      data: generateDummyPost(10),
    });
  } catch (err) {
    console.error(err);
    yield put({
      type: LOAD_POSTS_FAILURE,
      data: err.response.data,
    });
  }
}

요기서 10개 만들고

리듀서
 case LOAD_POSTS_SUCCESS:
      draft.loadPostsLoading = false;
      draft.loadPostsDone = true;
      draft.mainPosts = action.data.concat(draft.mainPosts);
      draft.hasMorePosts = draft.mainPosts.length < 50;
      break;

만들어진 10개의 값이 action.data의 값으로 가고, 그게 이제 원래있던 것과 합쳐진다! 
````



스크롤이 끝에 갔을때, 추가 할 수 있도록

**#주의** 

**useEffect에서 윈도우.이벤트리스너를 할때 반드시 return 을 적어줘야 한다! 리턴해서 윈도우.리무브이벤트리스너 사용해야 함.**

안하면 데이터가 계속 누적됨. 

```js
  //인피니티 스크롤 구현
  useEffect(() => {

    function onScroll() {
      console.log(window.scrollY, document.documentElement.clientHeight, document.documentElement.scrollHeight)
    }

    window.addEventListener("scroll", onScroll)
    return () => {
      window.removeEventListener("scroll", onScroll)
    }

  }, [])
```

scrollY : 얼마나 내렸는지

clientHeight: 화면 보이는 길이

scrollHeight: 총 길이





```js
 const isFollowing = me?.Followings.find((v) => v.id === post.User.id);
```



내가 팔로우 하고 있는 살마들 중에서 그 게시글의 id와 같으네 있다면 이미 내가 팔로우 하고 있는 사람





----





**우선 간단하게 논리 연산자 코드는 총 3가지로 분류됩니다.**

 

| 연산자   | 표기법 | 구문                   | 구문 치환             | 설명                                                         |
| -------- | ------ | ---------------------- | --------------------- | ------------------------------------------------------------ |
| 논리 AND | &&     | example1 && example2   | example1 AND example2 | example1 이 true 인 경우 example2 을 반환하고 그렇지 않은 경우 example1을 반환 |
| 논리 OR  | \|\|   | example1 \|\| example2 | example1 OR example2  | example1 이 true 인 경우 example1 을 반환하고 그렇지 않은 경우 example2을 반환 |
| 논리 NOT | !      | !example1              | NOT example1          | example1 이 true 인 경우 false를 반환하고 그렇지 않은 경우 true 를 반환 |

 

간단하게 예시로 살펴보면 아래와 같습니다. ( 문법 예시는 MDN 예시가 가장 무난하여 공유드립니다. )

 

**[논리 AND ( && ) 예시]**

```js
a1 = true  && true       // t && t returns true
a2 = true  && false      // t && f returns false
a3 = false && true       // f && t returns false
a4 = false && (3 == 4)   // f && f returns false
a5 = 'Cat' && 'Dog'      // t && t returns "Dog"
a6 = false && 'Cat'      // f && t returns false
a7 = 'Cat' && false      // t && f returns false
a8 = ''    && false      // f && f returns ""
a9 = false && ''         // f && f returns false
```

 

**[논리 OR ( || ) 예시]**

```js
o1 = true  || true       // t || t returns true
o2 = false || true       // f || t returns true
o3 = true  || false      // t || f returns true
o4 = false || (3 == 4)   // f || f returns false
o5 = 'Cat' || 'Dog'      // t || t returns "Cat"
o6 = false || 'Cat'      // f || t returns "Cat"
o7 = 'Cat' || false      // t || f returns "Cat"
o8 = ''    || false      // f || f returns false
o9 = false || ''         // f || f returns ""
o10 = false || varObject // f || object returns varObject
```

 

**[논리 NOT ( ! ) 예시]**

```js
n1 = !true               // !t returns false
n2 = !false              // !f returns true
n3 = !''                 // !f returns true
n4 = !'Cat'              // !t returns false
```



----

삭제시에 불변성을 안지킬려먼 splice가 맞음





----

