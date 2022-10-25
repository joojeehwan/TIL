## Prop Drilling?

`Prop Drilling` 은 props를 오로지 하위 컴포넌트로 전달하는 용도로만 쓰이는 컴포넌트들을 거치면서 React Component 트리의 한 부분에서 다른 부분으로 데이터를 전달하는 과정입니다.

### 예시

[(참고자료)](https://javascript.plainenglish.io/how-to-avoid-prop-drilling-in-react-using-component-composition-c42adfcdde1b)

```js
import React from "react";
import "./styles.css";

export default function App() {
  return (
    <div className="App">
      <FirstComponent content="Who needs me?" />
    </div>
  );
}

function FirstComponent({ content }) {
  return (
    <div>
      <h3>I am the first component</h3>;
      <SecondComponent content={content} />|
    </div>
  );
}

function SecondComponent({ content }) {
  return (
    <div>
      <h3>I am the second component</h3>;
      <ThirdComponent content={content} />
    </div>
  );
}

function ThirdComponent({ content }) {
  return (
    <div>
      <h3>I am the third component</h3>;
      <ComponentNeedingProps content={content} />
    </div>
  );
}

function ComponentNeedingProps({ content }) {
  return <h3>{content}</h3>;
}
```

`content` 를 `App > First > Second > Third > ComponentNeedingProps` 순으로 전달합니다.

`ComponentNeedingProps` 컴포넌트에서 해당 props를 사용하기 위해 전달하는 과정을 거치게 됩니다.

## 뭐가 문제인가?

우선 `Prop Drilling` 는 문제가 되지 않습니다. prop 전달이 3~5개 정도의 컴포넌트라면 말이죠.

하지만 prop 전달이 10개, 15개 같이 더 많은 과정을 거치게 된다면 어떻게 될까요? 코드를 읽을 때 해당 prop을 추적하기 힘들어집니다.

그렇기 때문에 유지보수도 더욱 어려워집니다.

## 그럼 어떻게 해야 할까?

과도한 Prop Drilling를 피하기 위해서는 여러 방법이 있습니다.

첫 번째로 `전역 상태관리 라이브러리 사용`

`redux`, `MobX`, `recoil` 등을 사용하여 해당 값이 필요한 컴포넌트에서 직접 불러서 사용할 수 있습니다.

여기서 궁금해하시는 분들이 계실겁니다.

> Store와 연결되어 있는 부분을 따로 빼고 싶은데요?

해당 질문에 대한 답은 두 번째 방법에 있습니다.

두 번째로는 `children` 을 적극적으로 사용하는 것입니다.

### 예시

```js
import React from "react";
import "./styles.css";

export default function App() {
  const content = "Who needs me?";
 return (
    <div className="App">
      <FirstComponent>
        <SecondComponent>
          <ThirdComponent>
            <ComponentNeedingProps content={content}  />
          </ThirdComponent>
        </SecondComponent>
      </FirstComponent>
    </div>
  );
}

function FirstComponent({ children }) {
  return (
    <div>
      <h3>I am the first component</h3>;
     { children }
    </div>
  );
}

function SecondComponent({ children }) {
  return (
    <div>
      <h3>I am the second component</h3>;
     {children}
    </div>
  );
}

function ThirdComponent({ children }) {
  return (
    <div>
      <h3>I am the third component</h3>
        {children}
    </div>
  );
}

function ComponentNeedingProps({ content }) {
  return <h3>{content}</h3>
}
```

이렇게 리팩토링을 진행한다면 하나의 컴포넌트에서 값을 관리하고, 그 값을 하위요소로 전달할 때 전혀 코드의 추적이 어려워지지 않습니다.

## 마치며

프론트엔드 면접 준비를 진행하던 도중 `Prop Drilling` 이라는 흥미로운 요소를 발견하게 되어 이렇게 글을 적어 보았습니다.

프론트엔드 공부를 할 때 이 글이 도움이 되셨으면 합니다.



# 참고

1. https://slog.website/post/13
2. 즐겨찾기, 프론트 A better ~ 이 부분 참고

