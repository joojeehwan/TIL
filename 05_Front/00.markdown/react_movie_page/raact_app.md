

style.css를 사용해서

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import "./style.css"


ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);


```



이런식으로 사용하지 않을것임!

왜냐하면 모든 것에 대해서 통일되게 하고싶지 않음.





# xxx.module.css 

=> 와우 이건 정말 혁신스! 

```css
#Button.module.css

.btn {
  color: white;
  background-color: tomato;
}

```



```js
import PropTypes from "prop-types"
import styles from "./Button.module.css"

function Button({text}) {

  return <button
    className={styles.btn}>
    {text}
  </button> 
}

Button.propTypes = {
  text: PropTypes.string.isRequired
}

export default Button
```



이런식으로 모듈화 해서 사용이 가능,,! 

컴포넌트를 위한 독립적인 css를 만들 수 있음







----

# effect



state가 변화할때 나의 모든 컴포넌트는 다시 실행됨

하지만 그러고 싶지 않을떄,,, 바로 effect

렌더할때 한번만 실행되고 다음부터는 실행되고 싶지 않을때,,!



```js

import { useEffect, useState } from "react"

function App() {

  const [counter, setValue] = useState(0)
  const onClick = () => setValue((prev) => prev + 1)
  console.log("i run all the time")
  const iRunOnlyOnce = () => {
    console.log("i run only once. ")
  }
  useEffect(iRunOnlyOnce, [])
  return (
    <div>
      <h1> {counter}</h1>
      <button onClick={onClick}>click me</button>  
    </div>
  )
}

export default App;
 
```

api를 한번만 딱 호출하고 두번은 부르고 싶지 않으니깐 !







````js

import { useEffect, useState } from "react"

function App() {

  const [counter, setValue] = useState(0)
  const [keyword, setKeyword] = useState("")
  const onClick = () => setValue((prev) => prev + 1)
  const onChange = (event) => setKeyword(event.target.value)
  console.log("i run all the time")
  // const iRunOnlyOnce = () => {
  //   console.log("i run only once. ")
  // }
  useEffect(() => {
    console.log("call the api,,,")
  }, [])
  return (
    <div>
      <input value={keyword} onChange={onChange} type="text" placeholder="Search here..."/>
      <h1> {counter}</h1>
      <button onClick={onClick}>click me</button>  
    </div>
  )
}

export default App;
 
````



> 인풋을 만들어 이벤트 리스너와 연결하고 onChange 함수가 작동할때 argument로 
>
> event를 받는다. 그리고 그 이벤트테서 value를 꺼내 keyword state에 넣기!
>
> 그리고 그 keyword state를 인풋의 value로 사용함



----



keyword가 변화할때에만 검색이 하고 싶음

counter가 변할때에도 검색을 하고 싶은게 아니라! 





````js

import { useEffect, useState } from "react"

function App() {

  const [counter, setValue] = useState(0)
  const [keyword, setKeyword] = useState("")
  const onClick = () => setValue((prev) => prev + 1)
  const onChange = (event) => setKeyword(event.target.value)
  console.log("i run all the time")
  // const iRunOnlyOnce = () => {
  //   console.log("i run only once. ")
  // }
  useEffect(() => {
    console.log("call the api,,,")
  }, [])
  useEffect(() => {
    console.log("검색 : ", keyword)
  }, [keyword])
  return (
    <div>
      <input value={keyword} onChange={onChange} type="text" placeholder="Search here..."/>
      <h1> {counter}</h1>
      <button onClick={onClick}>click me</button>  
    </div>
  )
}

export default App;
 
````



이렇게 하면 `keyword`가 변화할때만 검색이 가능해져!





코드가 언제 시동될지 결정하는게 `useeffect`

=> 실행시키려는 것과 지켜보려는 것!





----



cleanup





## cf) 자바 스크립트 쓸떄 { }  여는 것 까먹지 않기.





코드를 아예 삭제(destory)힐때도 알고싶음





```js
import { useEffect, useState } from "react"

function Hello () {
  useEffect(() => {
    console.log("i'm created")
    return () => console.log("destoryed")
  }, [])
  return <h1>Hello</h1>
}

function App() {

  const [showing, setShowing] = useState(false)
  const onClick = () => setShowing((prev) => !prev)

  return ( 
  <div>
    {showing ? <Hello /> : null}
    <button onClick={onClick}> {showing ? "Hide" : "showing"} </button>

  </div>
  )
  }

export default App;
```

컴포넌트가 삭제될떄,,도,,

위에랑 아래랑 같음

````js
  function byFn() {
    console.log("bye")
  }

  function hiFn () {
    console.log("created")
    return byFn
  }
  useEffect(hiFn,[])
  
  #위아래 두개는 같은 것
  
    useEffect(() => {
    console.log("i'm created")
    return () => console.log("destoryed")
  }, [])
  
  
````







----





```js
useEffect(() => {
      console.log("hi")
    return () => console.log("bye")
  },[])

#위와 같은 방법을 사용하자

  useEffect(function() {
    console.log("hi")
    return function() {
      console.log("bye")
    }
  },[])
```

