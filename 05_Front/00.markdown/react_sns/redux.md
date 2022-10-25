redux - next -wrapper를 사용해서 reduex와 next를 같이 사용! 



리덕스를 써야 하는 이유?!



회원가입, 로그인,, 등의 공통적인 데이터 있음 => 로그인한 사람 정보, 로그인 여부 등등,, 여러 컴포넌트에서 공통적으로 쓰이는!

근데 이렇게 컴포넌트가 분리된채로 있으면 따로따로 데이터가 흩어져 있어야 한다.! 그렇게 하고 싶지 않으면 부보 컴포넌트가 있어야하고 자식으로 각각 보내줘야 한다,,,!



근데 이런 작업(부모 - 작업)이 귀찮기 때문에 중앙에서 하나로 관리해서! 컴포넌트로 뿌려주는게 바로 리덕스! 

`데이터들을 중앙저장소에서 하나로 모아주고 컴포넌트가 필요할때 쓸수 있게 끔!`





데이터 관리를 위해서,, 꼭 필요! 조금 규모가 크다면! 

리덕스(코드량은 많지만, 실수를 줄여준다), 모벡스, 컨텍스트 api()



----

**컨텍스트 api vs 리덕스**

=> **비동기를 지원하기 쉽냐 아니냐**

중앙저장소가 있으면, 서버에서 데이터를 많이 받음(항상 비동기)

데이터를 항상 받을 수 있는게 아니라,, 서버의 고장,, 등등 => **실패의 대비해야해!**



그래서 비동기는 3가지 단계를 가진다

`요청 , 성공, 실패`



근데 이것을 컨텍스트 api에서 구현할려면 직접다 구현해야 함,,! 



단점이,, useEffect에 많이 axios에서 요청 보내지! 

```js
useEffect(() => {
axios.get("data/")
	.then(()=> {
	setState(data)
	})
	.catch(()=> {
	setError(error)
	})
})
```



보통 이렇게 많이 하는데,,!

컴포넌트가,, 화면을 구성하는게 아니라, 다른 업무를 하게 되네?! 데이터 까지 다루네,,! 

웬만하면 컴포넌트에선 데이터 요청을 안하나느게,,! 별도의 모듈이나 라이브러리가 하느게!!



비동기 요청을 할때 컨텍스트 api를 직접 다 구현해야함,,! 



비동기 요청이 많다?! 리덕스를 쓰는게,,!!



----

[참고](https://velog.io/@jehjong/Next.js%EC%97%90%EC%84%9C-Redux%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-Redux-wrapper)

리덕스 원리 이해!



# 중앙데이타저장소 Store

- 컴포넌트에서 공통적으로 쓰이는 데이타가 흩어져있기 때문에 부모 컴포넌트에서 데이타를 받아서 자식 컴포넌트에게 각각 보내줘야한다
- 컴포넌트끼리 데이타를 전달하는 과정도 매우 복잡하고 오류가 발생하기도 쉽다.
  ![img](https://media.vlpt.us/images/jehjong/post/c0ea2123-6225-44d7-91b1-94a46e16d2e9/image.png)
- 규모가 있는 서비스라면 중앙데이타저장소 Store를 최소 한 개 만들어 중앙에서 모든 데이타를 관리하고 보내주는 것이 편하다
- 중앙데이타저장소는 Redux, React의 contextedAPI, Mobax, Apolo 등이 있다

### Redux

- **Redux**는 원리가 간단하고 모든 수정사항을 기록한다.
- 모든 히스토리가 기록되어 에러 추적이 쉽고 안정적이다.
- 하지만 코드량이 많아진다.
- 중앙은 앱이 커지면 데이타를 쪼개는 작업이 필요한데 Redux는 reducer들을 쪼개는 기능을 제공해주어 편리하다 (reducer란 전달받은 action에 따라 상태를 어떻게 업데이트할지 정의해주는 함수)
- 사용법이 쉬워 초보자에게 추천되지만 전체적으로 가장 많이 사용되는 라이브러리기도 하다

### Mobax

- **Mobax**는 코드량이 매우 적어 생산성을 높일 수 있다
- 하지만 실수를 했을 때 추적이 어렵다
- 초보를 벗어나면 생산성을 위해 추천되는 라이브러리지만 Redux보다는 사용률이 낮다

### Context API

- 앱 규모가 작을 때 권장된다
- 큰 규모의 프로젝트는 차라리 리덕스나 모백스를 사용하는 것이 낫다
  - 중앙데이타저장소는 서버에서 데이타를 받아오는데 이 과정은 비동기다
  - 서버가 고장나거나 네트워크 에러가 생기면 데이타가 안 올수 있다
  - 실패에 대비하기위해 요청, 성공, 실패 3단계를 직접 구현해야한다.
  - 3단계 구현 코드를 컴포넌트마다 넣어줘야해 의도치 않은 코드 중복이 발생
  - 위의 코드만 밖으로 따로 빼낼 수 있지만 비동기 요청이 많으면 **context API도 리덕스와 모백스와 비슷해진다**
  - 따라서 리덕스나 모백스 등이 알아서 처리해주는 것이 편하다

```javascript
	useEffect(() => {
    	axios.get('/data')
      		.then(() => {
        		setState(data);
        })
      		.catch(() => {
        		setError(error);
        })
    })
```

------

# Redux && redux-wrapper

## 설치

- 넥스트가 설치되어있는 `front` 디렉토리에서 리덕스 설치
  `npm i redux`
- Redux의 손쉬운 사용을 위해 redux-wrapper 설치 (Redux와 사용법이 약간 다르다)
  `npm i next-redux-wrapper`
- `front/store/configureStore.js` 파일 생성

```javascript
      import { createWrapper } from 'next-redux-wrapper';
      import {createStore} from 'redux';

      const configureSotre = () => {
        const store = createStore(reducer);
        return store;
      };

      const wrapper = createWrapper(configureSotre, {
        debug: process.env.NODE_ENV === 'development,'
      });

      export default wrapper;
```

- ```
  _app.js
  ```

   

  파일 수정

  - wrapper 불러오기
  - wrapper를 사용해서 내보내기
  - Nodebird는 앱 이름

```javascript
	import wrapper from '../store/configureStore.js`
	.
	.
    	.
    	export default wrapper.withRedux(Nodebird);
	//wrapper로 감싸줘야 프로젝트의 모든 컴포넌트와 페이지에 적용된다
```

- 예전에는 `_app.js`의 return 내부를 `Provider`로 감싸야했는데 지금은 redux가 알아서 감싸주니 비워두어야한다 (사용자가 감싸면 중복되어 에러 발생)

```javascript
	//before
	return (
            <Provider store={store}>
            </Provider>
    	);


	//from redux@6
	return (
            <>
            </>
    	);
```

------

## Redux의 원리

### 진행 과정

![img](https://media.vlpt.us/images/jehjong/post/bfcd7132-0fb1-4a88-ae55-b0885c6b2ca7/image.png)

> 1. 앱의 상태를 객체 형식으로 작성한다 **state** (좌)
>
> 2. 변경하고 싶은 내용 action 으로 만든다 (우)
>
>        - **action**의 이름을 적는 `type`
>   - 변경사항을 적는 `data`
> 
>3. **action**을 **dispatch**한다
> 
>4. dispatch된  action을 reducer에 따라 처리한다 (아래)
> 
> 
>   - **reducer**는 **action** 어떻게 처리할지 정의해준다
>    - 예를 들어 `switch`를 값을 변경해주는 것이다
>   - `case`에 **action**의 `type`을 적어준다
>    - 바꾸고싶은 값에 `action.data`를 넣어준다

- #### 중앙관리저장소에 앱의 전체 상태를 하나의 객체로 표현한다

```javascript
{
  name: 'zerocho',
  age: '27',
  password: 'babo'
}
```

- #### action을 생성해서 무엇으로 변경할지 적어준다

  - 변경사항마다 action을 만들어줘야한다

```javascript
  {
    type: 'CHANGE_NICKNAME' // action이름
    data: 'boogicho' // 변경될 데이타값
  }
  {
    type: 'CHANGE_AGE'
    data: 30,
  }
```

- #### action을 dispatch하면 reducer에 따라 중앙저장소의 데이타가 변경된다

- #### reducer에 데이타를 어떻게 변경해야하는지 정의해준다

```javascript
  switch (action.type) {
    case 'CHANGE_NICKNAME':	//action의 type
      return {			//새로운 객체를 리턴
        ...state,			//유지할 state들은 그대로 사용
        name: action.data,		//변경할 state를 action.data로 바꿔준다
      }
    case 'CHANGE_AGE':		//또 다른 action 처리를 정의
      return {
        ...state,
        age: action.data,
      }
  }
```

- #### 중앙저장소의 데이타가 reducer가 정의한대로 변경되면 해당 데이타를 갖다 쓰는 컴포넌트의 모든 데이타가 변경된다

  - 지정한 데이타만 변경된 채로 새로운 객체가 만들어지고 그 객체를 가져다 쓰는 방식이다

### 장단점

- 변경할 때마다 action과 reducer를 하나씩 추가해줘야해서 코드량이 많아진다
- action 하나하나가 Redux에 기록이 되어 그 내역을 보고 버그를 찾기가 매우 쉽다
- 개발 변경사항을 거꾸로 거슬러 올라가며 개발사항을 테스트하기 쉽다

### 새로운 객체를 만드는 이유

- reducer에서는 매번 일부만 수정된 **새로운 객체를 반환**한다.

```javascript
    return { //새로운 객체 반환
      ...state,
      name: action.data,
    }
```

> #### JavaScript에서 참조한 두 객체는 같은데 Redux는 매번 새로운 객체를 만들기 때문에 서로 다른 객체이다
>
> ```javascript
> {} === {} //false
> 
> 
> const a = {};
> const b = a;
> a === b //true
> ```

- 이렇게 새로운 객체를 만들면 **변경 전과 후를 모두 기록**할 수 있다

```javascript
    //새로운 객체 만들기
    const prev = { name: 'zerocho' }
    const next = { name: 'boogicho' }


    ---
    //기존 객체 참조
    const next = prev;
    next.name = 'bbogicho';

    prev.name; // boogicho
```

### 객체 내의 바뀌지않는 데이타는 예전 것 참조

```javascript
    return {
      ...state, // 바뀌지않는 부분은 예전 것 참조
      name: action.data,
    }
```

- 일일히 입력하며 작업량이 많아지는 것을 방지
- 메모리 관리를 위해
  - action하나를 실행할 때마다 새로운 객체가 생기기 때문에 메모리가 많이 필요하다
  - 바뀌는 데이타만 새로 만들고 유지하는 데이타는 참조하는 방식으로 진행

```javascript
    const next = { b: 'c' };
    const prev = { a: next };
    const next = { ...prev};

    prev.a === next.a //true
    prev === next //false
```

- 유지되는 데이타 `a`는 예전 것을 참조했기에 같은 객체로 본다

----

## React가 렌더되는 경우

React가 렌더 되는 경우는 다음과 같다.

1. state나 props가 변경되었을 때
2. `forceUpdate()`를 실행했을 때
3. 부모 컴포넌트가 렌더링 되었을 때

이번 글에서 주목해야할 것은 1번이다. React는 state나 props가 변경되었을 경우에만 리렌더가 된다.

React는 어떻게 state나 props의 변경을 감지할 수 있을까? 먼저 자바스크립트 각 데이터 타입이 어떻게 변경 되는지 알아보자.

## 자바스크립트 데이터 타입

자바스크립트는 크게 원시 타입과 참조 타입으로 나뉜다.

### 원시 타입(Primitive Type)

원시 타입에는 문자열, 숫자, Boolean, null, undefined가 있으며 이는 변경 불가능한(immutable) 값이다.

```js
const str = 'hello'

console.log(str[0]) // output: 'h'
str[0] = 'w' // 에러가 뜨지 않음

console.log(str) // output: 'hello', 바뀌지 않음
```

비록 `str[0] = 'w'`로 했을 때 아무런 에러가 뜨지 않았지만, 다시 str를 콘솔로 찍어보니 바뀌지 않은 것을 확인할 수 있다. 이처럼 원시 타입은 변경 불가능하다.



### 참조 타입(Reference/Object Type)

참조 타입에는 함수, 객체, 배열이 있으며 변경 가능한(mutable) 값이다.

```
배열의 변경
const fruits = ['apple', 'banana']

fruits.push('mango')
console.log(fruits) // output: ['apple', 'banana', 'mango']
객체의 변경
const profile = { name: 'kmj' }

profile.name = 'howdy-mj'
profile.gender = 'female'
console.log(profile) // output: { name: 'howdy-mj', gender: 'female' }
```

이처럼 참조 타입은 바로 값이 바뀌는 것을 확인할 수 있다. 하지만 React, Redux는 해당 값이 변경 되지 않았다고 판단할 것이다. 밑의 예시를 보자.

```js
const num = [1, 2, 3]

num === num // output: true
num === [1, 2, 3] // output: false
```

분명 `num`과 `[1, 2, 3]`은 같지만, 자바스크립트는 두 개의 값이 다르다고 알려주고 있다. 이는 참조 타입이 메모리 주소를 ‘참조’하기 때문이다. (해당 내용은 나중에 새로운 글에서 자세히 작성해보겠다. 우선 밑의 핵심 요약을 보면 감을 잡을 수 있을거라 생각한다)



### 핵심 요약

원시 타입은 **워드 파일의 복사본을 만든것 처럼, 해당 값을 복사하면 서로가 독립된 값**을 가진다.

```js
var title = '마지막'
var final = title

title = '진짜 마지막'

console.log(title) // output: '진짜 마지막'
console.log(final) // output: '마지막'
```

이처럼 final은 처음에 복사한 title 값을 그대로 가져온 반면, title은 나중에 변경된 값으로 찍힌다.

참조 타입은 **만약 내가 구글 드라이브에 동기화된 파일을 수정하면, 다른 사람 것에서도 자동으로 변경**된다. 단, url 주소는 동일하다.

```js
const profile = { name: 'kmj' }
const copy = profile

profile.name = 'howdy-mj'

console.log(profile) // output: { name: 'howdy-mj' }
console.log(copy) // output: { name: 'howdy-mj' }
```

profile.name을 바꾸자, 기존의 profile과 copy 모두 바뀐 것을 확인할 수 있다.

이렇듯 참조 타입은 값이 바뀌어도 메모리(쉽게 말하면 url) 주소가 똑같기 때문에 React는 데이터가 변경된 것을 알아차리지 못한다. 따라서, 메모리 주소를 바꾸어 React에게 데이터가 변경되었다고 알려주어야 한다. 이는 Redux에서도 똑같이 작용한다.

## Redux의 state 변경 감지 코드

보통 redux를 사용하면,

```js
import { combineReducers } from 'redux'

const songsReducer = () => {
  return [
    { title: '소주 한잔', duration: '4:51' },
    { title: 'Memories', duration: '3:10' },
    { title: '널 좋아하나봐', duration: '3:44' },
    { title: '거짓말이라도 해서 널 보고싶어', duration: '3:48' },
  ]
}

const selectedSongReducer = (selectedSong = null, action) => {
  if (action.type === 'SONG_SELECTED') {
    return action.payload
  }
  return selectedSong
}

export default combineReducers({
  songs: songsReducer,
  selectedSong: selectedSongReducer,
})
```

위와 같은 형태로 모든 reducers를 `combineReducers로` 모아 store에 알려준다.

이때, [combineReducers](https://github.com/reduxjs/redux/blob/master/src/combineReducers.ts) 코드를 보면 Redux가 어떻게 state의 변화를 감지하는지 알 수 있다.

```ts
// ...
let hasChanged = false
const nextState: StateFromReducersMapObject<typeof reducers> = {}
for (let i = 0; i < finalReducerKeys.length; i++) {
  const key = finalReducerKeys[i]
  const reducer = finalReducers[key]
  const previousStateForKey = state[key] // 기존 reducer
  const nextStateForKey = reducer(previousStateForKey, action) // action이 발생한 후, 새로운 reducer
  if (typeof nextStateForKey === 'undefined') {
    // reducers의 return이 undefined이거나 비어있을 때 에러가 나는 이유
    const errorMessage = getUndefinedStateErrorMessage(key, action)
    throw new Error(errorMessage)
  }
  nextState[key] = nextStateForKey
  hasChanged = hasChanged || nextStateForKey !== previousStateForKey  // 만약 nextState와 previousState가 달라질 경우, hasChanged는 true로 바뀜
}
hasChanged = hasChanged || finalReducerKeys.length !== Object.keys(state).length// 만약 combineReducer안의 reducer의 개수가 기존과 달라질 경우, hasChange는 true로 바뀜
return hasChanged ? nextState : state // hasChanged가 true라면 새로운 state를 아니라면 기존 state를 반환
```

따라서, Redux에서 state를 바꾸는 가장 올바른 방법은 메모리 주소를 바꾸는 것이다.

위의 예시를 다시 가져와보자.

```js
배열의 변경
const fruits = ['apple', 'banana']

// 틀린 방법
fruits.push('mango')
fruits.pop()
fruits[0] = 'peach'

// 올바른 방법
[...state, 'mango']
fruits.filter(fruit => fruit !== 'mango')
fruits.map(fruit => fruit === 'apple' ? 'peach' : fruit)
객체의 변경
const profile = { name: 'kmj' }

// 틀린 방법
profile.name = 'howdy-mj'
profile.gender = 'female'
delete profile.gender

// 올바른 방법
{ ...state, name: 'howdy-mj' }
{ ...state, gender: 'female' }
_.omit(state, 'gender') // lodash로 제거
```

이러한 번거로움을 없애고자 [immer](https://immerjs.github.io/immer/docs/introduction) 혹은 [immutable-js](https://immutable-js.github.io/immutable-js/) 라이브러리를 사용한다.

아니면 바로 immutable update logic이 있어 바로 state를 변경할 수 있도록 만들어진 [Redux Toolkit](https://redux-toolkit.js.org/)을 사용할 수도 있다.





----





# 비구조화 할당

[참고](https://yuddomack.tistory.com/entry/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EB%AC%B8%EB%B2%95-%EB%B9%84%EA%B5%AC%EC%A1%B0%ED%99%94-%ED%95%A0%EB%8B%B9)

 **복사(copy)** 



전개 연산자를 사용하여 배열, 객체의 깊은 복사를 할 수 있습니다.

```
var arr = [1,2,3];
var copy1 = arr;
var [...copy2] = arr;
var copy3 = [...arr];

arr[0] = 'String';
console.log(arr); // [ 'String', 2, 3 ]
console.log(copy1); // [ 'String', 2, 3 ]
console.log(copy2); // [ 1, 2, 3 ]
console.log(copy3); // [ 1, 2, 3 ]
```

얕은 복사인 copy1은 arr을 참조하기 때문에 0번 요소가 변경되었지만 전개 연산자를 사용한 copy2, copy3는 깊은 복사가 된 것을 볼 수 있습니다.



객체 역시 전개 연산자로 깊은 복사를 사용할 수 있습니다.

무엇보다도 강력한 점은 복사와 함께 새로운 값을 할당할 수 있다는 점 입니다.

```
var prevState = {
  name: "yuddomack",
  birth: "1996-11-01",
  age: 22
};

var state = {
  ...prevState,
  age: 23
};

console.log(state); // { name: 'yuddomack', birth: '1996-11-01', age: 23 }
```

위와 같이 ...prevState를 사용하여 기존 객체를 복사함과 동시에 age키에 새로운 값(23)을 할당할 수 있습니다.

리액트의 props나 state처럼 이전 정보를 이용하는 경우 유용하게 사용할 수 있습니다.







----



스토어? 스테이트와 리듀서를 포함하는 것! 

## **위의 그림을 그대로 표현한 것**

```js
//reducers.index.js

const initalState = {
  name:"joojeehwan", 
  age:29,
  password: "ghks7683!!"
}


//액션 부분
const changeNickname = {
  tpye: "CHANGE_NICKNAME", 
  data: "sexyjeehwan"
}

//리듀셔 부분
// (이전상태, 엑션) => 다음 상태
const rootReducers = ((state = initalState, action) => {
    switch(action.type) {
        case "CHANGE_NICKNAME":
          return  {
            ...state,
            name: action.data
          }
    }
})

export default rootReducers



//store.configureStroe.js

import {createWrapper} from "next-redux-wrapper"
import {createStore} from "redux"


const configureStore = () => {

  const store = createStore(reducer)
  store.dispatch({
    tpye: "CHANGE_NICKNAME", 
    data: "sexyjeehwan"
  })
  return store
}

const wrapper = createWrapper(configureStore,
   {debug: process.env.NODE_ENV === "development"})

export default wrapper
```





액션을 그때그떄 만드는,,!  **action Creactor**



````js
//액션을 함수를 통해서 동적으로 생성 할 수도 있음
//action creater

const changeNickname = (data) => {
  return {
    type: "CHANGE_NICKNAME", 
    data,
  }
}

changeNickname("neasdfa")
```
위에 적은 게 아래와 같은 뜻!
  {
	
    type:"CHANGE_NICKNAME",
    data: "neasdfa"
  }

```
store.dispatch(changeNickname("sdfadfa"))
````



---



## 비동기 action creactor => 이건 redux saga 에서



----



리덕스를 쓰니깐 useState의 기능을 쓸일이 되게 줄어든다! 



1. AppLayOut 변화

```js
import React from 'react';
import PropTypes from "prop-types"
import Link from "next/link"
import {Menu, Input, Row, Col} from "antd"
import 'antd/dist/antd.css'
import LoginForm from "../components/LoginForm"
import UserProfile from "../components/UserProfile"
import styled from "styled-components"
import {useSelector} from "react-redux"

const SearchInput = styled(Input.Search)`
  vertical-align: middle;
`

const AppLayout = ({children}) => {

  //const [isLoggedIn, setIsLoggedIn] = useState(false)

  return (
    <div>
      <Menu mode='horizontal'>
        <Menu.Item>
         <Link href="/"><a>노드버드</a></Link>
        </Menu.Item>
        <Menu.Item>
        <Link href="/profile"><a>프로필</a></Link>
        </Menu.Item>
        <Menu.Item>
          <SearchInput enterButton />
        </Menu.Item>
        <Menu.Item>
          <Link href="/signup"><a>회원가입</a></Link>
        </Menu.Item>
      </Menu>
      <Row gutter={8}>
        <Col xs={24} md={6}>
          {isLoggedIn ? <UserProfile setIsLoggedIn={setIsLoggedIn} /> : <LoginForm setIsLoggedIn={setIsLoggedIn} />}
        </Col>
        <Col xs={24} md={12}>
           {children} 
        </Col>
        <Col xs={24} md={6}>
          <a href='https://velog.io/@meanstrike' target="_blank" rel='noreferrer noopener'>Made by jeehwan</a>
        </Col>
      </Row>
    </div>
  )
}





AppLayout.propTypes = {
  children: PropTypes.node.isRequired,

}

export default AppLayout
```



````js
import React from 'react';
import PropTypes from "prop-types"
import Link from "next/link"
import {Menu, Input, Row, Col} from "antd"
import 'antd/dist/antd.css'
import LoginForm from "../components/LoginForm"
import UserProfile from "../components/UserProfile"
import styled from "styled-components"
import {useSelector} from "react-redux"

const SearchInput = styled(Input.Search)`
  vertical-align: middle;
`

const AppLayout = ({children}) => {

  const isLoggedIn = useSelector((state) => state.user.isLoggedIn)

  //const [isLoggedIn, setIsLoggedIn] = useState(false)

  return (
    <div>
      <Menu mode='horizontal'>
        <Menu.Item>
         <Link href="/"><a>노드버드</a></Link>
        </Menu.Item>
        <Menu.Item>
        <Link href="/profile"><a>프로필</a></Link>
        </Menu.Item>
        <Menu.Item>
          <SearchInput enterButton />
        </Menu.Item>
        <Menu.Item>
          <Link href="/signup"><a>회원가입</a></Link>
        </Menu.Item>
      </Menu>
      <Row gutter={8}>
        <Col xs={24} md={6}>
          {isLoggedIn ? <UserProfile /> : <LoginForm />}
        </Col>
        <Col xs={24} md={12}>
           {children} 
        </Col>
        <Col xs={24} md={6}>
          <a href='https://velog.io/@meanstrike' target="_blank" rel='noreferrer noopener'>Made by jeehwan</a>
        </Col>
      </Row>
    </div>
  )
}



export default AppLayout
````



> **가장 큰 변화 props를 굳이 안해도 된다! 부모-자식간의  proops 왜냐면 그냥 중아에서 갖다가 쓰니깐!** 
>
> 그리고  `import {useDispatch} from "react-redux"` 사용해서 dispatch!



````js
/* eslint-disable react/prop-types */
import React,{useCallback, useMemo} from "react"
import {Form, Input, Button} from "antd"
import Link from "next/link"
import styled from "styled-components"
import {useDispatch} from "react-redux"

import useinput from "../hooks/useinput"
import { loginAction } from "../reducers"



const ButtonWrapper = styled.div`
  margin-top: 10px;
`


const FormWrapper = styled(Form)`
  padding: 10px;
`

const LoginForm = ( ) => {

    const dispatch = useDispatch()
    const [id, onChangeId] = useinput("")
    const [password, onChangePassword] = useinput("")

    // const [id, setId] = useState("")
    // const onChangeId = useCallback((e) => {
    //   setId(e.target.value)
    // }, [])
    
    // const [passwrod, setPassword] = useState("")
    // const onChangePasswrod = useCallback((e) => {
    //   setPassword(e.target.value)
    // }, [])

    const onSubmitForm = useCallback(() => {
          console.log(id, password)
          dispatch(loginAction({id, password}))
    }, [id, password])

    const style = useMemo(() => ({marginTop: 10}), [])
    return (
      <FormWrapper onFinish={onSubmitForm}>
        <div>
          <label htmlFor="user-id"></label> 
          <br />
          <Input name="user-id" value={id} onChange={onChangeId} required/>
        </div>
        <div>
          <label htmlFor="user-password"></label> 
            <br />
            <Input 
            name="user-password" 
            type="password"
            value={password} 
            onChange={onChangePassword} 
            required
            />
        </div>
        <ButtonWrapper style={style}>
          <Button type="primary" htmlType="submit" loading={false}>로그인</Button>
          <Link href="/signup"><a><Button>회원가입</Button></a></Link>
        </ButtonWrapper>
      </FormWrapper>
    )
}

// LoginForm.propTypes = {
//   setIsLoggedIn: PropTypes.func.isRequired,
// }


export default LoginForm
````



```js
import React, { useCallback } from 'react';
import {Card, Avatar, Button} from "antd"
import {useDispatch} from "react-redux"

import {logoutAction} from "../reducers"

// eslint-disable-next-line react/prop-types
const UserProfile = () => {

  const dispatch = useDispatch()

  
  const onLogOut = useCallback(() => {
    dispatch(logoutAction())
  })
  return(
    <Card
      actions= {[
        <div key="twit">쨱쨱<br />0</div>, 
        <div key="followings">팔로잉<br />0</div>, 
        <div key="followers">팔로워<br />0</div>
      ]}
      >
        <Card.Meta
          Avatar={<Avatar>JH</Avatar>}
          title="jeehwan"
        />
        <Button onClick={onLogOut}>로그아웃</Button>
    </Card>
  )
}

export default UserProfile
```



```js
const initalState = {
  user: {
    isLoggedIn: false,
    user: null,
    signUpData: {},
    loginData: {},
  },
  post: {
    mainPosts: [],
  }
}


//액션을 함수를 통해서 동적으로 생성 할 수도 있음
//action creater

export const loginAction = (data) => {
  return {
    type: "LOG_IN", 
    data,
  }
}
export const logoutAction = () => {
  return {
    type: "LOG_OUT", 
  
  }
}

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
const rootReducers = ((state = initalState, action) => {
    switch(action.type) {
        case "LOG_IN":
          return  {
            ...state, //처음 initalstate객체 핀것!
            user: { 
              ...state.user, //user객체 안의 것들이라!!
              isLoggedIn: true,
              user: action.data
            }
          }
        case "LOG_OUT":
          return  {
            ...state, //처음 initalstate객체 핀것!
            user: { 
              ...state.user, //user객체 안의 것들이라!!
              isLoggedIn: false,
              user: null
            }
          }
          default: return state
    }
})

export default rootReducers
```

