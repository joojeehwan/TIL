![img](https://blog.kakaocdn.net/dn/cP2uAs/btqEsC1w2JK/OId33UPXr9sknzdWE1UjN1/img.png)

![img](https://blog.kakaocdn.net/dn/kycbq/btqErKFZGAS/cBYlSZkiEhfl7NiD9igNU0/img.png)



# **๐ Redux**

- ์๋ฐ์คํฌ๋ฆฝํธ ์ ํ๋ฆฌ์ผ์ด์์์ ์ฌ์ฉํ๋ ์ํ ๊ด๋ฆฌ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
- ์ ์ญ์ผ๋ก ์ํ ๊ด๋ฆฌ๋ฅผ ํ๊ฒ ๋  ๋ ํจ๊ณผ์ 
- ๊ด์ฌ์ฌ ๋ถ๋ฆฌ ์์น(SoC)์ ๋ฐ๋ฆ
- [reduxjs/redux](https://github.com/reduxjs/redux)
- install
  - `npm install redux`
  - `yarn add redux`

------

# **๐ createStore**

> **state(์ ํ๋ฆฌ์ผ์ด์์์ ์ฌ์ฉํ๋ ๋ฐ์ดํฐ)๋ฅผ ์ ์ฅํ  store ์์ฑ**

- store ๋ด์ฅํจ์
  - dispatch
  - getState
  - subscribe
- store ๋ง๋ค๊ธฐ

```
import { createStore } from 'redux';
const store = createStore();
// ๋ง์ฝ createStore ํจ์์ reducer ํจ์๋ฅผ ๋ฃ์ง ์๋๋ค๋ฉด?
// const store = create(reducer)
Uncaught Error: Expected the reducer to be a function.
```

> > createStore() ๋ฉ์๋์ reducer ์ธ์๋ฅผ ๋ฐ์ง ์๋๋ค๋ฉด ์์ธ ๋ฐ์

# **๐ reducer**

> **action์ ํด๊ฒฐํ๊ณ  ๋ณ๊ฒฝ๋ ํ์ฌ ์ํ๋ฅผ ๋ฐํ**

- reducer(state, action)
- ์ง์  ๊ตฌํํด์ผ ํ๋ ๋ถ๋ถ
- reducer๋ ์์ ํจ์ (์์ ํจ์๋ ํญ์ ์ถ๋ ฅ ๊ฐ์ด ๊ฐ์ ํจ์)

```
import { createStore } from 'redux';
const reducer = (state, action) => {
    // action ํ์์ ๋ฐ๋ฅธ state ์์ ํ๊ธฐ
    return state; // ์๋ก์ด ์ํ๋ฅผ ๋ฐํ
};

// store ์์ฑ
const store = createStore(reducer);
```

> > reducer ํจ์์๋ ์ ํ๋ฆฌ์ผ์ด์์์ ๊ด๋ฆฌํ  ๋ฐ์ดํฐ(state)์ state๋ฅผ ๋ณํ์ํฌ action์ด ํ์ํจ

# **๐ action**

> **state๋ฅผ ์ค์ง์ ์ผ๋ก ์์ **

- ํญ์ ๊ฐ์ฒด(Object) ํ์ ์ด์ด์ผ ํจ
- type ์์๋ฅผ ํ์์ ์ผ๋ก ๊ฐ์ง๊ณ  ์์ด์ผ ํจ

```
const ADD = 'ADD';
const MINUS = 'MINUS';
const actionAdd = { type: ADD }; // state๋ฅผ 1 ์ฆ๊ฐ์ํค๋ ์ก์
const actionMinus = { type: MINUS }; // state๋ฅผ 1 ๊ฐ์์ํค๋ ์ก์
```

> > action์ dispatch๋ฅผ ํตํด reducer์๊ฒ ์ ๋ฌํด์ค์ผ state๋ฅผ ์์ ํ๋ ์์์ด ์ด๋ฃจ์ด์ง

# **๐ dispatch**

> **reducer๋ฅผ ๋ถ๋ฌ์ ํ์ฌ state์ action์ ๋ฐ์์ํด(action์ reducer์๊ฒ ์ ๋ฌ)**

- dispatch(action)

```
...
const store = createStore(reducer);
...
store.dispatch(actionAdd);
```

state๋ฅผ 1 ์ฆ๊ฐ์ํด

# **๐ subscribe**

> **store๊ฐ ๋ณํ  ๋๋ง๋ค ํธ์ถ**

- subscribe(function(){})
- dispatch๊ฐ ์คํ๋  ๋๋ง๋ค subscribe์ ์ ๋ฌํ ํจ์๊ฐ ํธ์ถ๋จ

```
...
const store = createStore(reducer);
...
store.dispatch(actionAdd);
store.subscribe(()=>console.log(store.getState())) // getState๋ ํ์ฌ state๋ฅผ ํธ์ถํ๋ store ๋ด์ฅํจ์
```

> > 1 ์ฆ๊ฐ๋ state๊ฐ ์ถ๋ ฅ๋จ

# **๐จโ๐ป ์นด์ดํฐ ๊ตฌํ**

- ์ฆ๊ฐ ๋ฒํผ, ๊ฐ์ ๋ฒํผ์ ํตํด state ์์ ํ๊ธฐ

```js
/* count.js */

import { createStore } from 'redux';

// actionType
const ADD = 'ADD';
const MINUS = 'MINUS';

// reducer(์ด๊ธฐstate, action)
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

// store ์์ฑ
const countStore = createStore(reducer);

/* html span tag */
//const number = document.querySelector('span');
const onChangeState = () => {
    number.innerText = countStore.getState();
};
// store์ ๋ณํ๊ฐ ์์ ๋๋ง๋ค ํธ์ถ
countStore.subscribe(onChangeState);

const increased = () => {
    countStore.dispatch({ type: ADD });
};
const decreased = () => {
    countStore.dispatch({ type: MINUS });
};
// click ์ด๋ฒคํธ ๋ฐ์ ์ dispatch ์คํ

/* html tag id */
//const add = document.getElementById('add');
//const minus = document.getElementById('minus');
//add.addEventListener('click', increased);
//minus.addEventListener('click', decreased);
```



์ถ์ฒ: https://bbaktaeho-95.tistory.com/45 [Bbaktaeho]







https://data-jj.tistory.com/53