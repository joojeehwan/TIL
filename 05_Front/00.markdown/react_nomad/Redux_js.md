![img](https://blog.kakaocdn.net/dn/cP2uAs/btqEsC1w2JK/OId33UPXr9sknzdWE1UjN1/img.png)

![img](https://blog.kakaocdn.net/dn/kycbq/btqErKFZGAS/cBYlSZkiEhfl7NiD9igNU0/img.png)



# **📚 Redux**

- 자바스크립트 애플리케이션에서 사용하는 상태 관리 라이브러리
- 전역으로 상태 관리를 하게 될 때 효과적
- 관심사 분리 원칙(SoC)을 따름
- [reduxjs/redux](https://github.com/reduxjs/redux)
- install
  - `npm install redux`
  - `yarn add redux`

------

# **📗 createStore**

> **state(애플리케이션에서 사용하는 데이터)를 저장할 store 생성**

- store 내장함수
  - dispatch
  - getState
  - subscribe
- store 만들기

```
import { createStore } from 'redux';
const store = createStore();
// 만약 createStore 함수에 reducer 함수를 넣지 않는다면?
// const store = create(reducer)
Uncaught Error: Expected the reducer to be a function.
```

> > createStore() 메서드에 reducer 인자를 받지 않는다면 예외 발생

# **📕 reducer**

> **action을 해결하고 변경된 현재 상태를 반환**

- reducer(state, action)
- 직접 구현해야 하는 부분
- reducer는 순수 함수 (순수 함수는 항상 출력 값이 같은 함수)

```
import { createStore } from 'redux';
const reducer = (state, action) => {
    // action 타입에 따른 state 수정하기
    return state; // 새로운 상태를 반환
};

// store 생성
const store = createStore(reducer);
```

> > reducer 함수에는 애플리케이션에서 관리할 데이터(state)와 state를 변화시킬 action이 필요함

# **📙 action**

> **state를 실질적으로 수정**

- 항상 객체(Object) 타입 이어야 함
- type 요소를 필수적으로 가지고 있어야 함

```
const ADD = 'ADD';
const MINUS = 'MINUS';
const actionAdd = { type: ADD }; // state를 1 증가시키는 액션
const actionMinus = { type: MINUS }; // state를 1 감소시키는 액션
```

> > action은 dispatch를 통해 reducer에게 전달해줘야 state를 수정하는 작업이 이루어짐

# **📘 dispatch**

> **reducer를 불러서 현재 state에 action을 발생시킴(action을 reducer에게 전달)**

- dispatch(action)

```
...
const store = createStore(reducer);
...
store.dispatch(actionAdd);
```

state를 1 증가시킴

# **📒 subscribe**

> **store가 변할 때마다 호출**

- subscribe(function(){})
- dispatch가 실행될 때마다 subscribe에 전달한 함수가 호출됨

```
...
const store = createStore(reducer);
...
store.dispatch(actionAdd);
store.subscribe(()=>console.log(store.getState())) // getState는 현재 state를 호출하는 store 내장함수
```

> > 1 증가된 state가 출력됨

# **👨‍💻 카운터 구현**

- 증가 버튼, 감소 버튼을 통해 state 수정하기

```js
/* count.js */

import { createStore } from 'redux';

// actionType
const ADD = 'ADD';
const MINUS = 'MINUS';

// reducer(초기state, action)
const reducer = (count = 0, action) => {
    switch (action.type) {
        case ADD:
            return count++;
        case MINUS:
            return count--;
        default:
            return count;
    }
};

// store 생성
const countStore = createStore(reducer);

/* html span tag */
//const number = document.querySelector('span');
const onChangeState = () => {
    number.innerText = countStore.getState();
};
// store에 변화가 있을 때마다 호출
countStore.subscribe(onChangeState);

const increased = () => {
    countStore.dispatch({ type: ADD });
};
const decreased = () => {
    countStore.dispatch({ type: MINUS });
};
// click 이벤트 발생 시 dispatch 실행

/* html tag id */
//const add = document.getElementById('add');
//const minus = document.getElementById('minus');
//add.addEventListener('click', increased);
//minus.addEventListener('click', decreased);
```



출처: https://bbaktaeho-95.tistory.com/45 [Bbaktaeho]







https://data-jj.tistory.com/53