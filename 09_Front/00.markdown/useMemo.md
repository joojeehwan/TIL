useMemo

## 이건 알아두세요!

- 함수형 컴포넌트는 그냥 함수입니다. 다시 한 번 강조하자면 함수형 컴포넌트는 단지 jsx를 반환하는 함수이죠.
- 컴포넌트가 렌더링 된다는 것은 누군가가 그 함수(컴포넌트)를 호출하여서 실행되는 것을 말합니다. 함수가 실행될 때마다 내부에 선언되어 있던 표현식(변수, 또다른 함수 등)도 매번 다시 선언되어 사용됩니다.
- 컴포넌트는 자신의 state가 변경되거나, 부모에게서 받는 props가 변경되었을 때마다 리렌더링 됩니다. 심지어 하위 컴포넌트에 최적화 설정을 해주지 않으면 부모에게서 받는 props가 변경되지 않았더라도 리렌더링 되는게 기본입니다.
  (-[[짤막글\]react.memo](https://velog.io/@kysung95/짤막글-React.memo)편 참조 )

## 렌더링 최적화

기본적으로 react는 부모 component로부터 받는 state,props가 변동될 경우 rerendering됩니다. 당연한 것이죠. 하지만 여기에는 분명한 문제가 존재합니다.

> 예를들어 state,props가 여러가지라면?
> state1, state2, state3이 존재하는 상태에서 state1을 변경시켜주었는데 state2, state3도 재계산된다면??
> 이것이 과연 좋은 rerendering일까요??

useMemo와 useCallback은 이러한 고민을 가질 개발자들을 위해 탄생했다고 보시면 됩니다.
둘이 비슷한 개념이기에 많은 FE 면접에서 useMemo와 useCallback의 차이점을 물어보곤 하죠.
이번 useMemo 포스팅과 다음번에 올라올 useCallback 포스팅을 잘 보시면 이러한 질문에 잘 대처하실 수 있으리라 생각합니다:)

## useMemo 사용법

자 간단한 코드를 작성해보겠습니다.
파일 구성은 App.js와 ShowState.js로 구성되어있습니다.

```jsx
//App.js

import React, { useState } from "react";
import ShowState from "./ShowState";

const App = () => {
  const [number, setNumber] = useState(0);
  const [text, setText] = useState("");

  const increaseNumber = () => {
    setNumber((prevState) => prevState + 1);
  };

  const decreaseNumber = () => {
    setNumber((prevState) => prevState - 1);
  };

  const onChangeTextHandler=(e)=>{
    setText(e.target.value);
  }

  return (
    <div className="App">
      <div>
        <button onClick={increaseNumber}>+</button>
        <button onClick={decreaseNumber}>-</button>
        <input
          type="text"
          placeholder="Last Name"
          onChange={onChangeTextHandler}
        />
      </div>
      <ShowState number={number} text={text} />
    </div>
  );
};

export default App;
```

이제 App으로부터 number과 text를 내려받는 ShowState 컴포넌트를 만들어보겠습니다.

```jsx
//ShowState.js

import React from "react";
import "./styles.css";

const getNumber = (number) => {
  console.log("숫자가 변동되었습니다.");
  return number;
};

const getText = (text) => {
  console.log("글자가 변동되었습니다.");
  return text;
};

const ShowState = ({ number, text }) => {
  const showNumber = getNumber(number);
  const showText = getText(text);

  return (
    <div className="info-wrapper">
      {showNumber} <br />
      {showText}
    </div>
  );
};

export default ShowState;
```

코드 쉽게 이해되시죠??
이제 해당 페이지에서 +,- 버튼을 눌러 number 값을 바꾸어보기도하고 input창에서 text를 변경시켜보기도 해볼까요?.

그렇게 하시면 아마 이러한 console을 보실겁니다.

> **숫자**가 변동되었습니다.
> **글자**가 변동되었습니다.

어떤게 문제인지 아시겠죠? 저희는 숫자만 변경하였는데도 위의 두개의 문장이 console에 뜨는 것을 볼 수 있습니다.
잘 모르시는 분이봐도 이건 분명 문제가 있다고 생각할겁니다.

> 변경하고자 하는 state에 해당되지 않는 함수도 덩달아 실행된다니.. 이거 너무 비효율적이고 낭비아닌가요?
> **우리는 이럴 때 useMemo를 사용합니다!**

ShowState 컴포넌트 내에서 useMemo를 사용해보겠습니다.

```null
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

> **react 공식홈페이지에 나와있는대로 적용하면 됩니다.** 여기서 우리가 memoization 할 값은 **showNumber**과 **showText**임으로 그대로 적용시켜주겠습니다.

```jsx
//ShowState.js

import React,{useMemo} from "react";
import "./styles.css";

const getNumber = (number) => {
  console.log("숫자가 변동되었습니다.");
  return number;
};

const getText = (text) => {
  console.log("글자가 변동되었습니다.");
  return text;
};

const ShowState = ({ number, text }) => {
  const showNumber = useMemo(()=>getNumber(number),[number]);
  const showText = useMemo(()=>getText(text),[text]);

  return (
    <div className="info-wrapper">
      {showNumber} <br />
      {showText}
    </div>
  );
};

export default ShowState;
```

적용방법이 상당히 간단합니다. 이제 아까처럼 +,- 버튼을 눌러보거나 input 창에 글을 입력해볼까요?

어떤가요?
**숫자가 변경될 때는 '숫자가 변동되었습니다.'** 라는 console만
**글자가 변경될 때는 '글자가 변동되었습니다.'** 라는 console만 뜨죠??

이렇게 useMemo의 사용법에 대해 알아보았습니다.
물론 현재 제가 예시로 작성한 코드에서 useMemo의 사용 유무는 성능에 큰 영향을 주진 않을겁니다. 굉장히 간단한 계산들로만 이루어져 있기 때문이죠.

> react 공홈에서 예시로 든 코드를 보면 computeExpensiveValue라는 함수가 들어가있죠? 이처럼 **memoization되는 값의 재계산 로직이 expensive한 경우, 즉 복잡한 계산일 경우에 useMemo를 사용하는 것이 추천**되고 이런 경우에는 성능상 큰 이점으로 작용한답니다.

## 마무리

이번 포스팅에서는 useMemo에 대해 알아보았는데요.
아마 내일은 **useCallback을 설명한 뒤에 useMemo와 useCallback을 비교**해보는 식의 포스팅을 진행할 것 같습니다.
읽어주셔서 감사합니다.



---

## useCallback 사용법

> **useCallback은 기본적으로 useMemo와 매우 유사**합니다.
> 일단 App.js와 List 컴포넌트를 다음과 같이 만들어보겠습니다.

```jsx
//App.js

import React, { useState } from "react"
import List from "./List"

function App() {
  const [number, setNumber] = useState(1)
  const [dark, setDark] = useState(false)

  const getItems = () => {
    return [number, number + 1, number + 2]
  }

  const theme = {
    backgroundColor: dark ? "#333" : "#fff",
    color: dark ? "#fff" : "#333",
  }

  return (
    <div style={theme}>
      <input
        type="number"
        value={number}
        onChange={e => setNumber(parseInt(e.target.value))}
      />
      <button onClick={() => setDark(prevDark => !prevDark)}>테마 변경</button>
      <List getItems={getItems} />
    </div>
  )
}

export default App
//List.js

import React, { useEffect, useState } from "react"

export default function List({ getItems }) {
  const [items, setItems] = useState([])
  useEffect(() => {
    setItems(getItems())
    console.log("숫자가 변동되었습니다.")
  }, [getItems])
  return items.map((item, index) => <div key={index}>{item}</div>)
}
```

![img](https://media.vlpt.us/images/kysung95/post/f217a901-638d-4937-8877-eb0ba13f38f2/Screen%20Shot%202021-04-13%20at%2010.44.52%20PM.png)

다음과 같은 화면이 보이시나요?

useMemo 때의 예제코드와 얼추 비슷합니다. input 창을 통해 숫자를 입력할 경우 페이지의 숫자 항목들이 변경되고, theme 토글 버튼을 누를 경우 css 적 요소가 변하도록 예제코드를 작성했습니다.
이제 숫자를 변경해보면 console 창에 '숫자가 변경되었습니다.' 라는 메시지를 보실 수 있을겁니다.

그러나 ✋! 테마 토글 버튼을 누를 경우에도 해당 메시지가 발생한다는 점 확인하셨나요?
우리는 테마만 바꿀 뿐인데 getItems함수가 실행되다니...

![img](https://media.vlpt.us/images/kysung95/post/bde73568-66df-42bc-8fd0-31146d8ec1d8/Screen%20Shot%202021-04-13%20at%2010.45.36%20PM.png)
...

> 이것은 제가 저번 포스팅에서도 말했던 점이 야기하는 현상입니다.
> **부모에게서 받는 getItems라는 함수 props가 부모 컴포넌트가 리렌더링 되면서 변경된 props로 인식되기에 발생하는 현상이죠.** 그렇게 되기에 부모 컴포넌트의 number값이 새로 설정되며 해당 함수가 계속 반복되어서 실행되는 것이죠.
> 우리는 App.js파일에 **useCallback**을 추가하여 이를 고칠 수 있습니다!

number에 대한 의존성을 가지는 useCallback으로 getItems 함수를 매핑시켜주면 될 것 같습니다.

```jsx
const memoizedCallback = useCallback(
  () => {
    doSomething(a, b);
  },
  [a, b],
);
```

해당코드는 **react 공홈에서 제공해주는 useCallback 예시코드**입니다!
그대로 적용시켜주어보겠습니다.

```jsx
//App.js

import React, { useState, useCallback } from "react"
import List from "./List"

function App() {
  const [number, setNumber] = useState(1)
  const [dark, setDark] = useState(false)

  const getItems = useCallback(() => {
    return [number, number + 1, number + 2]
  }, [number])

  const theme = {
    backgroundColor: dark ? "#333" : "#fff",
    color: dark ? "#fff" : "#333",
  }

  return (
    <div style={theme}>
      <input
        type="number"
        value={number}
        onChange={e => setNumber(parseInt(e.target.value))}
      />
      <button onClick={() => setDark(prevDark => !prevDark)}>테마 변경</button>
      <List getItems={getItems} />
    </div>
  )
}

export default App
```

이렇게 App.js파일을 변경 시켜준 후 한번 테스팅을 해보시기 바랍니다.
어떤가요?? 테마를 변경할 때에는 console이 찍히지 않죠?
자 그럼 여기서 여러분들에게 의문점이 생길 것입니다.

> 엥? useMemo랑 아주 똑같은데요?

네 완전 비슷하죠? 그렇지만 분명한 차이점이 존재한답니다.🤗
이제부터 **useMemo와 useCallback이 어떻게 다르고, 각각 어떤 상황에서 사용되는지** 살펴보도록 하겠습니다:)

## useCallback과 useMemo 어떻게 다를까?

App.js파일의 getItems함수에서 우리가 특정한 값을 매개변수로 받아 요소 하나하나에 더해주는 식의 코드를 짠다고 가정해보겠습니다.
그렇다면 이런식으로 변경이 가능하겠죠?

```jsx
// App.js
 const getItems = useCallback(
    increaseValue => {
      return [
        number + increaseValue,
        number + 1 + increaseValue,
        number + 2 + increaseValue,
      ]
    },
    [number]
  )
```

그 후에 List.js에서 getItems에 increaseValue를 명시해줍니다.
저는 5를 넣었습니다.

```jsx
// List.js

setItems(getItems(5))
```

자 이제 페이지를 살펴보겠습니다.

![img](https://media.vlpt.us/images/kysung95/post/2e55b597-486b-4d5a-bc4f-9d33a5dcb1bc/Screen%20Shot%202021-04-13%20at%2011.38.56%20PM.png)

어떤가요? 함수의 매개변수가 부모와 자식간에 잘 오간다는 것이 보이죠?

우리가 만약 useMemo를 사용했다면 이러한 것이 가능했을까요??
가능하긴 합니다. 이런식으로 만들어준다면요.

**useMemo를 사용**

```jsx
// App.js

 const getItems = useMemo(
    () => increaseValue => {
      return [
        number + increaseValue,
        number + 1 + increaseValue,
        number + 2 + increaseValue,
      ]
    },
    [number]
  )
  
```

사실상 **useCallback(fn, deps) 는 useMemo(() => fn, deps)**와 같습니다. 그렇기에 해당 코드와 같이 useMemo를 적용시킬 수 있죠.
굳이 이렇게 선언해야 하는 이유가 뭘까요?

> useMemo는 함수를 반환하지 않고, **함수의 값만 memoization해서 반환**하기 때문입니다!
> 그와 다르게 **useCallback은 함수 자체를 memoization 해서 반환**하죠.
> 이것이 바로 useMemo와 useCallback의 핵심적인 차이점입니다. 🤗

자식 컴포넌트에서 특정한 props 값들의 변화를 최적화시키고 싶을때는 useMemo를, 부모 컴포넌트에서 계산량이 많은 props함수를 자식 컴포넌트에게 넘겨줄 때는 useCallback을 사용하는 것이 맞다고 저는 생각합니다.

## 최적화의 딜레마

제가 저번 포스팅과 이번 포스팅에서 예제로 제시했던 코드들에서는 사실 useMemo와 useCallback을 사용하지 않아도 됩니다. 음.. 사용하지 않는게 더 낫다고 해야하나.. 애매하네요.
그 이유는 **useMemo와 useCallback은 저번 포스팅에서 언급했다시피 expensive한 연산과정에서 사용되어야 그 효과를 톡톡히 볼 수 있기 때문입니다.**

> ✋효과만 미미할 뿐 더 나은 것 아닌가요?

아닙니다. 왜냐하면 useCallback과 useMemo를 사용할 경우 해당 hook을 호출하고, 그 안에 들어갈 함수를 만들어 넘기고, 의존성 체크를 목적으로 추가적인 비용이 발생하기 때문입니다. 더불어 memoization을 해놓는 다는 것은 결국 그 값을 메모리에 할당해놓고 있다는 뜻이기에 여기서도 추가적인 비용이 발생한다고 볼 수 있습니다.
**퍼포먼스 최적화는 컴퓨터의 어떠한 부분에서도 마찬가지겠지만 절대 공짜가 아닙니다. 컴퓨팅 자원, 개발자의 자원 등 어디선가 반드시 소모되는 자원이 있을 것이고, 이에 대해 잘 저울질하여 책임감 있게 최적화를 진행해야 한다 생각합니다.** *(그리고 react 자체가 성능이 좋기에 이러한 것들이 좀 불필요하게 느껴지기도 합니다..ㅎㅎ)*

## 마무리 & 개인적인 견해

> 저는 **개인적으로 animation이 작동하는 자식컴포넌트에 대해서는 필수적으로 최적화를 시켜주어야 한다 생각**합니다. user interface 관점에서 최적화가 되어있지 않다면 animation의 끊김 현상이 발생할 수 있기 때문이죠.
> 그 외 **누가봐도 정말 한번 실행될때마다 계산 비용이 비싼 함수나 값을 넘겨줄 때에는 최적화를 하는 것이 당연**하다고 생각해요.

**물론 어디까지나 제 개인적인 견해일 뿐 이게 맞다고 제가 감히 말씀드릴 수는 없어요.**😂

여러분들도 한번 useCallback과 useMemo를 적용시켜보며 이러한 고민을 해보는 것은 어떨까요?🙄🙄

이상 김용성이었습니다. 읽어주셔서 감사합니다. ⭐️