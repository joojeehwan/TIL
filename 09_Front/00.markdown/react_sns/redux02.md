[hydrate이해](https://helloinyong.tistory.com/315)

[Next.js의 Hydrate란?](https://helloinyong.tistory.com/315)

[개발 블로깅/Next.js](https://helloinyong.tistory.com/category/개발 블로깅/Next.js) 2021. 8. 8. 23:00

 



![img](https://blog.kakaocdn.net/dn/x6GHG/btrbCs6FUfa/nUGJFYA0H7K0EFMAqJHD61/img.jpg)



##  

##  

Next.js 프레임워크의 동작원리를 제대로 파악하고 있는 개발자라면 **Hydrate**에 대해선 이미 익숙한 용어일 것이다. 

그러나 Next.js의 주요 동작 방식 중 하나임에도, 눈에 잘 띄지 않아 놓치기도 쉬운 개념인 만큼, 한번 제대로 정리를 하고 넘어가보려고 한다.

 

Hydrate는 Server Side 단에서 렌더링 된 정적 페이지와 번들링된 JS파일을 클라이언트에게 보낸 뒤, 클라이언트 단에서 **HTML 코드와 React인 JS코드를 서로 매칭 시키는 과정**을 말한다.

 



![img](https://blog.kakaocdn.net/dn/RZ89B/btrbENofpfp/fBn3QJncluRPEBQNpeXjE1/img.png)출처: https://aboutmonica.com/blog/server-side-rendering-react-hydration-best-practices



 

이 과정이 왜 필요한지 간략하게 설명하기 위해, 우선 React에 대해 잠깐 얘기해보자.

 

### React의 웹 페이지 구성 원리

React는 JS파일만을 이용하여 웹 화면을 구성하는 원리를 가지고 있다. 그래서 실제 HTML 코드는 안에 내용이 하나도 없는 상태이다. (Client Side Rendering이 SEO에 적합하지 않은 이유이기도 하다.) 

 

```
// public/index.html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Title</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

 

위 코드는 처음 리액트 프로젝트 세팅할 때 많이 본 익숙한 HTML 코드일 것이다.

단순 뼈대만 있는 HTML document와 JS 파일들을 클라이언트로 모두 보낸 뒤, 클라이언트 단에서 JS 코드들을 통해 웹 화면을 렌더링 하며 페이지를 그리게 된다.

웹 페이지 렌더링을 한 뒤에도 페이지 내에서 동작하는 모든 이벤트 또한 자바스크립트로 인해 일어나게 된다.

 

 

```
// src/index.js

import React from "react";
import ReactDOM from "react-dom";
import App from './src/App';

ReactDOM.render(<App />, document.getElementById("root"));
```

 

위 코드처럼 public/index.html에는 아무 내용 없는 기본 뼈대만 있고, 나머지는 src/index.js의 자바스크립트 코드에서 모든 화면을 렌더링 한 뒤 HTML DOM 요소 중 root라는 아이디를 가진 엘리먼트를 찾아서 하위로 주입을 하게 된다.

 

### Next.js의 웹 페이지 구성 원리

Next.js는 클라이언트에게 웹 페이지를 보내기 전에 Server Side 단에서 미리 웹 페이지를 Pre-Rendering 한다. 그리고 Pre-Redering으로 인해 생성된 HTML document를 클라이언트에게 전송한다. 

그런데 이 시점에서 중요한 것은 아래 내용이다.

현재 클라이언트가 받은 웹 페이지는 단순히 웹 화면만 보여주는 HTML일 뿐이고, 자바스크립트 요소들이 하나도 없는 상태이다. 이는 웹 화면을 보여주고 있지만, 특정 JS 모듈 뿐 아니라 단순 클릭과 같은 이벤트 리스너들이 각 웹 페이지의 DOM 요소에 하나도 적용되어 있지 않은 상태임을 말한다.

 

그러면 이렇게 페이지만 보여주고 동작조차 하지 못하는 마치 빈 껍데기 같은 웹 페이지가 나중에는 어떻게 정상적으로 동작하게 되는 것일까.





Next.js Server에서는 Pre-Rendering된 웹 페이지를 클라이언트에게 보내고 나서, 바로 리액트가 번들링 된 자바스크립트 코드들을 클라이언트에게 전송한다. 

 



![img](https://blog.kakaocdn.net/dn/IKpSq/btrbvxzOgG8/dUjyHq88JuZSKEE8FVdqdK/img.png)



 

네트워크 탭을 보면, 맨 처음 응답받는 요소가 document Type의 파일이고, 이후에 React 코드들이 렌더링 된 JS 파일들이 Chunk 단위로 다운로드되는 것을 확인할 수 있다.

그리고 이 자바스크립트 코드들이 이전에 보내진 HTML DOM 요소 위에서 한번 더 렌더링을 하면서, 각자 자기 자리를 찾아가며 매칭이 된다.

이 과정을 **Hydrate**라고 부른다.

이것은 마치 자바스크립트 코드들이 DOM 요소 위에 물을 채우 듯 필요로 하던 요소들을 채운다 하여 Hydrate(수화)라는 용어를 쓴다고 한다.

 



![img](https://blog.kakaocdn.net/dn/Uwcdu/btrbwhjCZz8/tiZQdVqQFkyXDbkbuEorK0/img.gif)출처: https://qanda.ai/ko



 

아마 위의 GIF 이미지처럼 잠깐의 스타일 깜빡임이 Next.js에서 나타나는 일반적으로 많이 보는 현상일 것이다.

새롭게 페이지를 로딩할 때마다 약간 뒤늦게 스타일이 적용되는 듯한 이 과정이, HTML DOM 요소에 뒤늦게 자바스크립트가 동작하고 Hydration 돼서 나타나는 현상이다.



(정확하게는, 자바스크립트로 외부 서버에 웹폰트를 요청해서 받아오는데, Hydrate 이전에는 웹 폰트를 아직 요청하지 못해 적용되지 않아서이다.)

 

 

### Server에서 한번 렌더링하고 Client에서도 한번 더 렌더링 하면 비효율적인 렌더링 방식 아닌가요?

어쩌면 두번 렌더링 하는 것은 비효율적으로 보일 수 있다.

그러나 서버 단에서 빠르게 Pre-Rendering하고 유저에게 빠른 웹 페이지로 응답할 수 있다는 것에 더욱 큰 이점을 가져갈 수 있다. 심지어 이 Pre-Rendering 한 Document는 모든 자바스크립트 요소들이 빠진 굉장히 가벼운 상태이므로 클라이언트에게 빠른 로딩이 가능하다.
이는 같은 화면에 대해 두 번 렌더링이 일어난다는 단점을 보완하고도 남는다.

더 나아가서 클라이언트 단에서 자바스크립트가 렌더링을 할 때, 단지 각 DOM 요소에 자바스크립트 속성을 매칭 시키기 위한 목적이므로 실제 웹 페이지를 다시 그리는 과정까지는 하지 않는다.(Paint 함수 호출 X)

 

### Hydrate 과정은 Next.js에서만 일어나는 과정인가요?

사실 Hydrate는 Next.js에 종속된 동작이 아니라 *ReactDOM* 함수이다.

흔히 리액트 프로젝트 구축 시 초반에 꼭 작성해주는 *ReactDOM.render()* 함수와 잠깐 비교를 해보자.

```
ReactDOM.render(element, container, [callback]);
```

 

ReactDOM.render() 함수는 특정 컴포넌트를 두 번째 파라미터인 지정된 DOM 요소에 하위로 주입하여 렌더링을 처리해주는 함수이다. 
그리고 렌더링이 완료되면 특정 이벤트를 처리할 콜백 함수를 세 번째 파라미터로 넣어줄 수 있다.

 

```
ReactDOM.hydrate(element, container, [callback]);
```

 

ReactDOM.hydrate() 함수는 특정 컴포넌트를 두 번째 파라미터인 지정된 DOM 요소에 하위로 hydrate 처리만 한다. 이는 렌더링을 통해 새로운 웹 페이지를 구성할 DOM을 생성하는 것이 아니라, 기존 DOM Tree에서 해당되는 DOM 요소를 찾아 정해진 자바스크립트 속성(이벤트 리스너 등)들만 부착시키겠다는 말이다.

 

### Hydrate에 대해 우리가 신경 써야 할 것이 있을까요?

사실 그냥 웹 페이지 및 일반 Feature 개발만 한다면 이 과정을 몰라도 Next.js를 쓰는 것에 큰 문제는 없지만, 우선 원리는 알면 좋다.
그리고 나는 겪어보진 않았었는데, 어찌어찌 구글링 하다가 Next.js에서 Hydrate로 인해 발생하는 스타일 이슈 같은 게 있나 보다. 

이와 관련된 자세한 내용은 내가 봤던 아래 블로그 링크로 남겨둔다.

[ Next.JS hydration 스타일 이슈 피해가기Next.JS를 사용해 웹을 만들어가다보면, 어느 순간 Hydration 이슈를 마주치게 된다. 이번엔 그 상황이 언제, 왜 생겨나는지를 파악해보고, 이걸 피해가를 방법을 알아보자.fourwingsy.medium.com](https://fourwingsy.medium.com/next-js-hydration-스타일-이슈-피해가기-988ce0d939e7)

 

그리고 혹시나 Next.js 내에 Redux를 사용하게 된다면, 아마 **Next-Redux-Wrapper**라는 라이브러리를 이용하게 될 텐데, Reducer root Store에서 Hydrate를 처리해 주는 부분이 있다. 이는 Server Side 단에서 dispatch 했던 Store들을 클라이언트 단에서 그대로 사용할 수 있도록 Redux Store도 클라이언트 단에서 같이 Hydration이 필요하기 때문이다.

 

그리고 사실 지금와서 Hydrate에 대해 블로깅을 한 이유는, 이번에 웹 성능 최적화 작업을 하다가 이 Next.js Hydration에 대해 흥미로운 점을 발견하게 돼서 이에 대한 [블로깅(Partial Hydration에 대해)](https://helloinyong.tistory.com/316)을 하기 위해 미리 Hydrate에 대해 우선 정리를 했다.



----

redux dev tools

보통 diff(무엇이 바뀌엇나?!)와 state(데이터의 값)를 많이 사용 





---



## 리듀서 쪼개기!  => 경로 생각,,!

주의! //initalState의 depth를 생각하기

```js
   case "LOG_IN":
      //이게 처음 index에 있을 때!
       return  {
        ...state, //처음 initalstate객체 핀것!
         user: { 
           ...state.user, //user객체 안의 것들이라!!
           isLoggedIn: true,
           user: action.data
         }
       }
      
//아래와 같은 방식으로 변화해야 한다. 
      
        return  {
        ...state, //처음 initalstate객체 핀것!
          isLoggedIn: true,
          user: action.data
      }
```



----



리듀서를 합칠때  combineReducers를 사용해야한다! 함수라서 쉽지 않아서! 

````js
import { HYDRATE } from "next-redux-wrapper"
import { combineReducers } from 'redux';

import user from './user';
import post from './post';

const initalState = {
  user: {
   
  },
  post: {
  
  }
}


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
    //이 아래 부분은 ssr부분을 위해서! 하이드레이트 사용을 위해서! 
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

---

Applayout.js

````json
const isLoggedIn = useSelector((state) => state.user.isLoggedIn)
//이렇게도 가능! 구조분해 할당
const {isLoggedIn} = useSelector((state) => state.user)
````



----



## 포스트 폼 만들기



```js
export const initalState = {

  mainPosts: [{
    id: 1,
    User: {
      id: 1,
      nickname: '제로초',
    },
    content: '첫 번째 게시글',
    Images: [{
      src: 'https://bookthumb-phinf.pstatic.net/cover/137/995/13799585.jpg?udate=20180726',
    }, {
      src: 'https://gimg.gilbut.co.kr/book/BN001958/rn_view_BN001958.jpg',
    }, {
      src: 'https://gimg.gilbut.co.kr/book/BN001998/rn_view_BN001998.jpg',
    }]
  }],

}


```



왜 User랑 Images만 Comments만 대문자이냐?!

> 디비속에서 사용하는 시퀄라이져와 연관 어떤 정보와 다른 정보과 관련이 있으면
>
> 대문자로! 
>
> 유저랑 이미지스 커멘트는 다른정보와 합쳐줘서 이루어지기 떄문에! 



----



```js

//액션의 이름을 변수로 뺴놓네?! 
// => 장점 리듀서에서 적을때 오타가 나면 알 수 있어서!
const ADD_POST = "ADD_POST"
export const addPost = {
  type: "ADD_POST"
}

```



----

더미 포스트를 배열에 앞에다가 추가 하네?! 

=> 그래야 앞으로 추가 된다. 

불변성을 지키면서 변화되는 부분만 새로운 객체로 인식하게 끔! 

```js
const reducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_POST:
        return {
          ...state,
          //더미 포스트가 앞에 있어야 최신글이 위로! 
          mainPosts: [dummyPost, ...state.mainPosts],
          postAdded: true,
        }
    default:
      return state
  }
}
```



화면은 중요하지 않고! 데이터, 즉 `리두셔`부터 만들기! 



----



# 서버 개발자와 리덕스 데이터 구조는 미리 상의를 해야함,,! 



---



# useRef => 실제 DOM에 접근

[참고](https://yoonjong-park.tistory.com/entry/React-useRef-%EB%8A%94-%EC%96%B8%EC%A0%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%EA%B0%80)

React에서 useRef를 사용하는 경우는 다음과 같다.

useRef는 **리렌더링 하지 않는다.** **컴포넌트의 속성만 조회&수정**한다.

 

## 1. 컴포넌트에 focus를 위치시킬 필요가 있는 경우.

\- 예를 들어, 값을 여러개 일력하고 첫 번째 칸으로 이동해야 하는 경우 필요하다. 

```
//InputTest.js

import React, { useState, useRef } from 'react';

function InputTest() {
  const [text, setText] = useState('');
  const nameInput = useRef();

  const onChange = e => {
    setText(e.target.value)
  };

  const onReset = () => {
    setText('');
    nameInput.current.focus();
  };

  return (
    <div>
      <input
        name="name"
        onChange={onChange}
        value={text}
        ref={nameInput}
      />

      <button onClick={onReset}>초기화</button>
      <div>
        <b>내용: </b>
        {text}
      </div>
    </div>
  );
}

export default InputTest;
```

**const nameInput = useRef();
**: **Ref 객체**를 만들어준다.

 

**<input**

 **name="name"**

 **onChange={onChange}**

 **value={text}**

 **ref={nameInput}**

**/>
**: 선택하고 싶은 DOM에 속성으로 ref 값을 설정해준다.

 

**nameInput.current.focus();
**: Ref 객체의 current 값은 우리가 선택하고자 하는 DOM을 가리킨다.
 그리고 포커싱을 해주는 DOM API focus() 를 호출한다.





## 2. 속성 값을 초기화(clear)할 필요가 있는 경우.

\- 예를 들어, 카운터의 값을 0으로 초기화 할 필요가 있을 때. (타이머 0으로 만들기 같은...) 
\- setInterval 이나 setTimeout과 같은 함수는 clear 시켜주지 않으면 메모리를 많이 소모하기 때문이다.

```
// App.js

const RSPfunction = () => {
  const [result, setResult] = useState('');
  const [imgCoord, setImgCoord] = useState(rspCoords.바위);
  const [score, setScore] = useState(0);
  const interval = useRef();

  useEffect(() => { 
    interval.current = setInterval(changeHand, 100);
    return () => {
      clearInterval(interval.current);
    }
  }, [imgCoord]); 


//  코드 생략
```

 

## 3.useRef로 컴포넌트 안의 변수 관리하기

\- 컴포넌트의 속성 정보를 조회 & 수정할 때 (+리 렌더링을 하지 않으면서..)

useRef를 활용한 변수는 아래와 같은 곳에 쓰인다.

\- setTimeout, setInterval을 통해 만들어진 id
\- scroll 위치
\- 배열에 새 항목을 추가할 때 필요한 고유값 key

```
// App.js

import React, { useRef } from 'react';
import UserList from './UserList';

function App() {
  const users = [
    {
      id: 1,
      username: 'subin',
      email: 'subin@example.com'
    },
    {
      id: 2,
      username: 'user1',
      email: 'user1@example.com'
    },
    {
      id: 3,
      username: 'user2',
      email: 'user2@example.com'
    }
  ];

  const nextId = useRef(4);
  const onCreate = () => {
  
    // 배열에 새로운 항복 추가하는 로직 생략
    
    nextId.current += 1;
  };
  return <UserList users={users} />;
}

export default App;
```

 

**import React, { useRef } from 'react';
**: useRef 함수를 불러온다.

 

**const nextId = useRef(4);
**: 배열의 고유값 변수로 nextId를 설정해주고,

 useRef() 파라타미터로 다음 id가 될 숫자 4를 넣어준다.

 파라미터 값을 넣어주면 해당 값이 변수의 current 값이 된다.

 그리고 nextId 변수를 수정하거나 조회려면 .current 값을 수정하거나 조회한다.

 

**nextId.current += 1;
**: nㅍ변수에 1씩 더하여 업데이트를 한다.

 

공식문서에서 말하는

### Ref를 사용해야 할 때

Ref의 바람직한 사용 사례는 다음과 같습니다.

- 포커스, 텍스트 선택영역, 혹은 미디어의 재생을 관리할 때.
- 애니메이션을 직접적으로 실행시킬 때.
- 서드 파티 DOM 라이브러리를 React와 같이 사용할 때.

선언적으로 해결될 수 있는 문제에서는 ref 사용을 지양하세요.

예를 들어, Dialog 컴포넌트에서 open()과 close() 메서드를 두는 대신, isOpen이라는 prop을 넘겨주세요.



## => useRef를 통해 이미지 등록을 활성화 시킬 수 있구먼





````js
import React, {useRef, useCallback, useState } from "react"

const imageInput = useRef()


const onClickImageUpload = useCallback(() => {
    imageInput.current.click();
}, [imageInput.current]);


<Form style={{ margin: '10px 0 20px' }} encType="multipart/form-data" onFinish={onSubmit}>
    <Input.TextArea value={text} onChange={onChangeText} maxLength={140} placeholder="어떤 신기한 일이 있었나요?" />
          <div>
            <input type="file" multiple hidden ref={imageInput}  />
            <Button onClick={onClickImageUpload}>이미지 업로드</Button>
````



----

# 배열안에 jsx를 넣을때는 key값이 무조건 필요하다.





----



props 되는게 객체 일때 객체안의 값들의 조건을 좀더 명확하게 `shape`로 줄 수 있음. 좀더 꼼곰하게 검사가 가능

````js
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
````



----

# Optional Chaining

[참고](https://www.daleseo.com/js-optional-chaining/)

# [ES2020] ?. 연산자 - Optional Chaining

optional chaining을 지원하기 위해서 ES2020에서 추가된 문법인 `?.` 연산자에 대해서 알아보도록 하겠습니다.

## . 연산자를 통한 속성값 접근의 문제점

그동안 자바스크립트에서는 주로 `.` 연산자(chaining)를 사용해서 객체의 속성값에 접근했었습니다.

간단한 예로, `user` 객체의 `name` 속성의 `first` 속성값은 다음과 같이 접근할 수 있습니다.

```js
> user = {name: {first: "John", last: "Doe"}}
> user.name.first
'John'
```

하지만 이렇게 여러 단계로 이루어진 객체를 탐색할 때는 항상 `TypeError`가 발생할 확률이 생깁니다.

```js
> user.address.street
Uncaught TypeError: Cannot read property 'street' of undefined
```

이를 방지하기 위해서 일반적으로 다음과 같은 방어 로직을 넣게 되는데 보시다시피 코드가 지저분하게 됩니다.

```js
> user.address && user.address.street
undefined
```

그래서 기존에는 `lodash`와 같은 유틸리티 라이브러리를 이용하여 이 문제를 해결했었습니다. 😝

```js
import { get } from "lodash";

get(user, "address.street");
```

## ?. 연산자를 통한 안전한 속성값 접근

`?.` 연산자를 사용하면 지저분한 방어 로직이나 유틸리티 라이브러리 없이 안전하고 깔끔하게 속성값에 접근할 수 있습니다.

객체의 속성을 접근할 때 `.` 연산자 대신에 `?.` 연산자를 사용하면, 해당 객체가 nullish 즉, `undefined`나 `null`인 경우에 `TypeError` 대신에 `undefined`를 얻게 됩니다.



```js
> user?.name?.first
'John'
> user?.address?.street
undefined
```

`?.` 연산자는 배열이나 함수에서도 사용할 수 있습니다.

```js
> arr = null;
> arr?.[0]
undefined
> func = undefined
> func?.()
undefined
```

## ?? 연산자와 함께 사용하기

`?.` 연산자는 ES2020에서 함께 도입된 `??` 연산자와 함께 사용하면 더욱 시너지를 발휘합니다. nullish coalescing을 위해 사용되는 `??` 연산자에 대한 내용은 [관련 포스팅](https://www.daleseo.com/js-nullish-coalescing)를 참고 바랍니다.

```js
> user?.country ?? "Korea"
'Korea'
```

## 마치면서

2020년 현재 대부분의 최신 브라우저는 optional chaining을 지원하기 때문에 `?.` 연산자를 사용할 수 있습니다. Node.js의 경우 버전 14부터 지원하며, 그 이전 버전에서는 [Babel](https://www.daleseo.com/?tag=Babel)과 같은 트랜스파일러(transfiler)를 통해서 접해볼 수 있습니다.

optional chaining에 대한 좀 더 자세한 내용은 [관련 MDN 공식 문서](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)를 참고바라겠습니다.





----



헷갈리는 부분 



```js
 
내 아이디와 게시글 작성자 아이디가 나랑 같으면 수정/삭제가 가능하고 다르면 신고버튼만 가능
{id && post.User.id === id
                ? (
                  <>
                    <Button>수정</Button>
                    <Button type="danger">삭제</Button>
                  </>
                )
                : <Button>신고</Button>}
```



----



# tip



True <-> false 전환

**주로 클릭으로 인한 토글을 구현할 때 많이 사용함**



````js
 const onToggleLike = useCallback(() => {
    setLiked((prev) => !prev)
  }, [])
````





----

## 이 부분이 왜 필요하나?!  `<CommentForm post={post}/>`



````js
<div>    
	<CommentForm post={post}/>
    <List		
        header={`${post.Comments.length} 댓글`}
        itemLayout="horizontal"
        dataSource={post.Comments}
        renderItem={(item) => (~)


위의 두개가 CommentForm와 List가 하나의 div에서 같이 묶여서 렌더링 됨.
````

이 부분이 왜 필요하나?! 

**댓글을 작성할때 게시글에 속해있음. 게시글의 아이디를 받기 위해서** 





----



# 폼을 만드는 것은 꼭 앞으로는 라이브러리를 사용해서 하는게 좋음 

너무 반복되는 부분이 많음,,! 

ex) react-hook-form





----



> Q) img 태그에서 *role*="presentation"   을 추가하셨는데 기능이 뭔가요? 지워봐도 딱히 변화를 모르겠네요.

시각장애인을 위한 스크린 리더에 img가 이미지라는 사실을 숨겨버립니다. 이미지에 alt를 정확히 제공할 수 없다면 오히려 혼란을 주기때문입니다.



----



# 헷갈리는 부분  PostImages

````js
  const [showImagesZoom, setShowImagesZoom] = useState(false);

  const onZoom = useCallback(() => {
    setShowImagesZoom(true);
  }, []);

  const onClose = useCallback(() => {
    setShowImagesZoom(false);
  }, []);


{showImagesZoom && <ImagesZoom images={images} onClose={onClose} />}

// showImagesZoom의 값이 참이 되면 모달식으로  ImagesZoom 컴포넌트가 출력되는?! 

````







----

# 아니 왜 근데 굳이 ImgesZoom폴더를 만들어서 하는거지?! 



스타일드 컴포넌트 때문에!!

따로따로 만들어서! 



코드를 관리!! 아래의 2개의 js 파일이 하나의 컴포넌트 파일로 관리가 됨. 



```js
import React, { useState } from 'react';
import Slick from 'react-slick';
import PropTypes from 'prop-types';
import { Overlay, Header, CloseBtn, SlickWrapper, ImgWrapper, Indicator, Global } from './styles';


const ImagesZoom = ({images, onClose}) => {


  const [currentSlide, setCurrentSlide] = useState(0);
  return (
    <Overlay>
      <Global/>
      <Header>
        <h1>상세 이미지</h1>
        <CloseBtn onClick={onClose}></CloseBtn>
      </Header>
      <SlickWrapper>
        <div>
          <Slick
             initialSlide={0}
             afterChange={(slide) => setCurrentSlide(slide)}
             infinite
             arrows={false}
             slidesToShow={1}
             slidesToScroll={1}
          
          >
            {images.map((v) => (
                <ImgWrapper key={v.src}> 
                  <img src={v.src} alt={v.src}></img>
                </ImgWrapper>
            ))}
          </Slick>
          <Indicator>
            <div>
              {currentSlide + 1}
              {' '}
              /
              {images.length}
            </div>
          </Indicator>
        </div>
      </SlickWrapper>

    </Overlay>
  )

}


ImagesZoom.propTypes = {
  images: PropTypes.arrayOf(PropTypes.shape({
    src: PropTypes.string,
  })).isRequired,
  onClose: PropTypes.func.isRequired,
};

export default ImagesZoom;
```



````js
import styled, { createGlobalStyle } from 'styled-components';
import { CloseOutlined } from '@ant-design/icons';


export const Global = createGlobalStyle`
.slick-slide {
  display: inline-block;
}
.ant-card-cover {
  transform: none !important;
}
`
export const Overlay = styled.div`
position: fixed;
z-index: 5000;
top: 0;
left: 0;
right: 0;
bottom: 0;
`;

export const Header = styled.header`
height: 44px;
background: white;
position: relative;
padding: 0;
text-align: center;

& h1 {
  margin: 0;
  font-size: 17px;
  color: #333;
  line-height: 44px;
}

`

export const CloseBtn = styled(CloseOutlined)`
position: absolute;
right: 0;
top: 0;
padding: 15px;
line-height: 14px;
cursor: pointer;
`;


export const SlickWrapper = styled.div`
height: calc(100% - 44px);
background: #090909;
`



export const ImgWrapper = styled.div`
padding: 32px;
text-align: center;

& img {
  margin: 0 auto;
  max-height: 750px;
}
`

export const Indicator = styled.div`
text-align: center;

& > div {
  width: 75px;
  height: 30px;
  line-height: 30px;
  border-radius: 15px;
  background: #313131;
  display: inline-block;
  text-align: center;
  color: white;
  font-size: 15px;
}
`
````













---



캐로설을 react에선 react - slick을 사용해서 구현햇구먼,,! 





----



````js
import styled from 'styled-components';

const Overlay = styled.div`
  position: fixed;
  z-index: 5000;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
`;


#위의 `` 방식은 js방식!

함수를 부르는 방식이 func()이것도 있지만 func``이런것도 있는 것임! 
    
일반 함수 호출이랑 조금 내부의 방식은 다르긴 함! 
````







----



# 글로벌 스타일을 활용해서 다양한 css문제를 해결할 수 있음. 





```js
//거터 문제 해결

const Global = createGlobalStyle`
  .ant-row {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }
  
  .ant-col:first-child {
      padding-left: 0 !important;
  }
  
  .ant-col:last-child {
    padding-right: 0 !important;
  }
`;

//slick 약간 갇혀 있는거 해결

const Global = createGlobalStyle`
  .slick-slide {
    display: inline-block;
  }
  .ant-card-cover {
    transform: none !important;
  }
`
```





----





**더미데이터 구조 ㄱ잡는게 정말 중요,,!  문서화 하자!**





----





# 정규 표현식

해시태그를 찾는 정규 표현식



[참고](https://choonse.com/2021/07/27/184/)

```js
import React from 'react';
import Link from 'next/link';
import PropTypes from 'prop-types';

const PostCardContent = ({ postData }) => (
  <div>
    {postData.split(/(#[^\s#]+)/g).map((v) => {
      if (v.match(/(#[^\s]+)/)) {
        return (
          <Link
            href={{ pathname: '/hashtag', query: { tag: v.slice(1) } }}
            as={`/hashtag/${v.slice(1)}`}
            key={v}
          >
            <a>{v}</a>
          </Link>
        );
      }
      return v;
    })}
  </div>
);

PostCardContent.propTypes = {
  postData: PropTypes.string.isRequired,
};

export default PostCardContent;
```



**정규표현식(Regex)**은 검색 패턴을 지정하여 기호로 표시한 것입니다.

이 개념은 미국의 수학자인 Stephen Cole Kleene가 1950년대에 정의한 정규 언어(Regular Language)와 관련이 있으며, 정규표현식 문법은 1980년대 Perl에서부터 사용되기 시작했습니다.

주로 검색 또는 치환 작업에 사용되며, 현재 대부분의 프로그래밍 언어에서 정규표현식을 지원하거나 라이브러리를 통해 사용할 수 있습니다.

예를 들어 다음 문장에서 특정 조건에 따른 검색을 진행하고자 할 때, 정규표현식을 사용할 수 있습니다.

**The greatest danger for most of us is not that our aim is too high and we miss it, but that it is too low and we reach it.**

- too를 찾고자 할 때 -> /too/
  **The greatest danger for most of us is not that our aim is too high and we miss it, but that it is too low and we reach it.**
- 대소문자 구분 없이 t를 모두 찾고자 할 때 -> /t/-gi
  **The greatest danger for most of us is not that our aim is too high and we miss it, but that it is too low and we reach it.**
- d로 시작하는 단어 및 문자를 모두 찾고자 할 때 -> /[d]\w+/-gi
  **The greatest danger for most of us is not that our aim is too high and we miss it, but that it is too low and we reach it.**
- ea가 들어가는 단어를 찾고자 할 때 -> /[a-z]*ea[a-z]*/-i
  **The greatest danger for most of us is not that our aim is too high and we miss it, but that it is too low and we reach it.**



다음 사이트를 이용하면 의도한 대로 정규표현식이 작성되었는지 확인할 수 있어 매우 유용합니다.

[regexr.com](http://regexr.com/)

Expression 아래에 식을 삽입하고, 그 아래 상자에는 검색 대상이 될 텍스트를 입력하면 됩니다.

![img](https://i1.wp.com/choonse.com/wp-content/uploads/2021/07/image-1.png?resize=790%2C436&ssl=1)

그럼 먼저 표현식이 나타내는 의미에 대해 알아본 뒤, 자바스크립트에서 편리하게 사용하는 방법을 확인해 보겠습니다.



## 1. 정규표현식 기호의 종류

- / **.** / → 모든 문자
- / + / → 하나 이상의 문자
- / ? / → 0 개 또는 1개의 문자
- / ^ / → 해당 문자를 제외
- / – / → 범위 지정
- / * / → 0 개 또는 1개 이상의 문자
- / [ ] / → 집합 구성
- / { } / → 반복 횟수 지정
- / \ / → 이스케이프 문자
- / \d / → 모든 숫자
- / \D / → 숫자가 아닌 문자
- / \w / → 알파벳, 숫자, 밑줄_ 문자
- / \W / → 알파벳, 숫자, 밑줄_이 아닌 문자
- / \s / → 공백 문자
- / \S / → 공백이 아닌 문자
- / \n / → 줄 바꿈 문자

정규표현식의 가장 기본이 되는 기호와 의미는 위와 같으며, 위 기호의 사용법만 익힌다면 정규표현식의 기본적인 이해는 가능할 것입니다.

그럼 각 기호의 사용 예제를 통해 사용법을 익혀보도록 하겠습니다.



## 2. 기호의 의미

**\d \D \w \W \s \S \n**

정규 표현식에서 가장 기초가 되는 부분이므로 외워두면 유용하게 사용할 수 있습니다. d는 숫자, w는 영문자, 숫자, _, s는 공백, n은 줄바꿈을 의미하며, 각 단어의 대문자는 NOT(반대)을 의미합니다.

- **/ [\d]+ /** -> 숫자가 한 번 이상 반복되는 문자 검색
- **/ [\D] /** -> 숫자가 아닌 문자 검색(공백 포함)
- **/ \([\w]+\) /** -> 괄호가 포함된 문자, 숫자 검색
- **/ [\W]+ /** -> 영문자, 숫자, _ 가 아닌 문자 검색
- **/ \s /** -> 공백을 검색

[regexr.com](http://regexr.com/)에 검색할 대상이 되는 문장을 붙여 넣거나 직접 작성한 뒤 원하는 패턴으로 표현식을 직접 만들어보면 정규 표현식에 금방 익숙해질 수 있습니다.



**\ 이스케이프 Escape**

이스케이프란 무엇일까요? 키보드 왼쪽 상단에 있는 ESC 버튼이 이스케이프의 약자입니다. 바로 벗어나다는 뜻인데요.

여기서는 기존에 지정된 약속에서 벗어난다는 뜻으로 보면 됩니다.

예를 들어서 .(마침표, dot)의 경우 모든 문자를 의미하는 뜻으로 사용됩니다.

하지만 때로는 글자 그대로 마침표 기호를 의미하고 싶은 경우도 있는데요. 이 때 이스케이프 문자를 사용하면 ‘우리 약속했던 것에서 벗어나자’는 뜻으로 사용할 수 있습니다.

- **/ . /** -> 모든 문자를 의미. a, b, c, d, ?, !, @, , 등 모든 문자 중 하나를 의미
- **/ \. /** -> 오직 .(마침표)만을 의미
- **/ + /** -> 하나 이상의 문자를 의미
- **/ \+ /** ->오직 +(플러스)만을 의미

이스케이프는 매우 유용한 필수 기능이므로 이스케이프가 필요한 문자를 확인해 둘 필요가 있습니다.



**. + ? ^ – \***

정규 표현식에서 특정 기호는 특별한 의미를 갖습니다. 대표적인 기호의 사용법은 다음과 같습니다.

- **/ [a-zA-Z] /** -> 소문자 a~z 또는 대문자 A~Z 내 일치하는 영문자 검색
- **/ colou?r /** -> color 또는 colour를 검색
- **/ [\S]\*a[a-zA-Z]\* /** -> a가 들어가는 단어 검색
- **/ [^a-z ] /** -> a-z 또는 공백(space)이 아닌 문자 검색
- **/ [a-zA-Z]+[\d!@#\$%\^\*]+[\w]\* /** -> 영문자로 시작하여 반드시 숫자 또는 특수 기호를 포함하는 문자열 검색



**{ } 중괄호 curly brackets**

중괄호는 반복 횟수를 지정하며, 이를 사용하면 검색 패턴의 상세한 지정이 가능합니다.

중괄호에 하나의 숫자를 넣으면 전체 반복 횟수를 의미하며, 두 개의 숫자는 시작과 끝의 범위를 의미합니다.

예를 들어 {3}이면 패턴을 3번 반복하라는 의미를 가지며, {1, 3}은 범위 구간이 1에서 3까지임을 의미합니다.

{1, }과 같은 표현도 가능하며, 이는 + 기호와 같은 의미, 즉 하나 이상이라는 의미를 갖습니다.

- **/ [A]{3} /** -> A가 3번 반복되는 문자를 검색
- **/ [\d]{3,} /** -> 3자리 이상인 숫자를 검색
- **/ [A]{2,3} /** -> A가 2번에서 3번 반복되는 문자를 검색

반복 횟수만 지정하면 의도하지 않은 결과도 함께 검색되는 경우가 많아 하위표현식 및 전후방 탐색과 함께 사용하면 더욱 효과적인 패턴의 사용이 가능합니다.



**[ ] 대괄호 Brackets**

대괄호 내 기재된 기호로 검색할 패턴을 지정합니다. 기호를 직접 기입하거나 범위 지정 기호인 -를 사용해 검색 패턴을 지정할 수 있습니다.

- **[aAbBc]** -> a 또는 A 또는 b 또는 B 또는 c 문자를 하나 검색
- **[a-e]** -> a에서 e까지(a,b,c,d,e)의 범위 내 문자를 하나 검색
- **[^a-z]** -> 제외 문자인 ^가 있으므로 a-z 범위에 들어가지 않는 문자 또는 기호를 하나 검색
- **[?!@#$%^&\*()_]** -> 지정 기호 중 하나를 검색
- **[cC][a-z]** -> c 또는 C로 시작하여, a-z 중 하나로 끝나는 단어 검색

[ ] 내 기재된 기호는 하나의 문자 또는 하나의 기호를 대상으로 검색하므로 한 글자 이상을 검색하고 싶은 경우에는 +(하나 이상의 문자) 또는 *(0개 또는 1개 이상의 문자)를 붙여줘야 합니다.

- **[a-z]+** -> 한 개 이상의 a-z 문자를 검색(반드시 1 개 이상 존재하는 조건)
- **[A-Z]\*** -> 0 개 이상의 A-Z 문자를 검색(있을 수도 있고 없을 수도 있는 조건)

위 조건은 특정 구성을 갖는 문자열 검색에 효과적이며, 예를 들어 이메일 주소가 있습니다.

이메일 주소 형식인 abcd@xyz.com을 검색하기 위해서는 다음과 같은 검색 패턴을 사용할 수 있습니다.

**/[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+/**

패턴을 분석해 보겠습니다.

먼저 이메일의 아이디에 해당하는 부분은 영문자 및 숫자로 이루어질 수 있으므로 [a-zA-Z0-9]로 시작하고, 하나 이상의 문자이므로 +기호를 붙여줍니다.

아이디가 끝나는 부분에 @가 따라오므로 @를 기입하고, 뒤의 호스트 주소 역시 하나 이상의 영문자와 숫자로 지정합니다.

.com 형식의 주소이므로 .(마침표, dot)문자와 일치시키기 위해 이스케이프로 .(마침표, dot)을 지정해주고, 다시 하나 이상의 영문자를 지정하여 이메일 검색 패턴을 생성합니다.

아이디에 .(마침표, dot)이 들어가거나 호스트 주소가 .co.kr의 형식이 되는 경우에는 위 패턴에서 약간의 응용이 필요합니다.



------

## 3. 종합 정리

정규 표현식은 처음 보면 마치 외계어처럼 기존의 프로그래밍 언어와는 다른 모습을 하고 있습니다.

선뜻 다가가기 어렵거나 거부감이 들기도 하는데요. 알고나면 생각보다 간단하고 규칙적인 구조를 가지고 있어 마음이 놓이기도 하고 검색에 응용할 수 있는 부분이 많은 것을 깨닫습니다.

위에서 소개한 부분은 아주 기초적인 부분이며 대표적인 기능을 소개하기 위한 간략한 샘플 패턴이므로 정말 원하는 검색 패턴을 구현하기 위해서는 더 많은 기능을 익혀야 하고 검색 패턴도 보완되어야 할 부분이 많습니다.

추가 문의 사항이나 문제가 있는 부분은 댓글 남겨주세요.

감사합니다.



