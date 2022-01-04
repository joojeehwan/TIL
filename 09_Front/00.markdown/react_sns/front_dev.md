

# _app.js => 공통적인것 넣으면 좋다! 



intro 이어서 학습



````js
//_app.js
const NodeBird= ({Component}) => {

    return (
      <Component/>
    )
}
````

`component`에

인덱스 js, 프로필 js. 사인업 js 의 return 부분이 위의 component의 매개변수로 들어가서 return 으로 출력되는 것!

_app.js가 인덱스,프로필, 사입업 js의 부모가 된다





>  **AppLayOut은 일부분이 공통이 부분**
>
> **_app.js는 완전 다 같은 부분**



----



* Next에선 `head`태그에 대해서 따로 import해서 쓰는 것이 있음 

* Introduced in React v16.2.0, the empty tag (`<>`...`</>`) in react is merely a shorter syntax for explicitly declaring fragments with [`참고`](https://reactjs.org/docs/fragments.html)

```js
render() {
  return (
    <React.Fragment>
      <ChildA />
      <ChildB />
      <ChildC />
    </React.Fragment>
  );
}

//단축문법

class Columns extends React.Component {
  render() {
    return (
      <>
        <td>Hello</td>
        <td>World</td>
      </>
    );
  }
}


```



---



반응형

가로 먼저 하고 세로 자른다! 



1. 모바일 -> 테블링 -> 데스크탑 순서로 디자인을 해야 함

브레이크 포인트 설정이 골떄려짐! 



xs : 모바일

sm : 테블릿

md : 작은 데스크 탑



24개의 컬럼을 나눔! => n / 24라고 생각! 

gutter = > 컬럼 사이의 간격

---



* 컴포넌트의 프롭스로 넘겨주는 함수는 usercallback를 꼭 쓰자 그래야 최적화가 됨! 



---



성능상에 문제가 없으면 굳이 아래와 같은 인라인 스타일을 적어도 되지만! 알아두면 좋을 것

```js
 <div style={{marginTop: 10}}>
          <Button type="primary" htmlType="submit" loading={false}>로그인</Button>
          <Link href="/signup"><a><Button>회원가입</Button></a></Link>

</div>
```



> 이렇게 적으면 계속 리렌더링이 된다. 
>
> 버츄얼 돔으로 검사하면서 객체가 다르다라고 생각한다! 저런식으로 적으면 
>
> why?
>
> js에선 {} === {} 는 항상 false 객체는 항상 다르니깐 



````js
const ButtonWrapper = styled.div`
  margin-top: 10px;
`
 
// div 컴포넌트이면서 위와 같은 css가 적용된 컴포넌트가 생성됨
````

혹은 `useMemo`를 사용해서 불필요한 리렌더링이 되는 것을 막아서 성능을 높일 수 있음. 

리엑트 돔이 착각하고 바뀐게 아닌데 다시 리렌더링하는 실수를 줄이도록 

```js
const style = useMemo(() => ({marginTop: 10}), [])


   <ButtonWrapper style={style}>
          <Button type="primary" htmlType="submit" loading={false}>로그인</Button>
          <Link href="/signup"><a><Button>회원가입</Button></a></Link>
   </ButtonWrapper>


// 이런식으로 리렌더링이 되는것을 막아줄 수 있음.

const SearchInput = styled(Input.Search)`
  vertical-align: middle;
`

<Menu.Item>
          <SearchInput enterButton />
</Menu.Item>
```



----



`<Form>`태그에서 submit을 하면 제출이 가능해짐! 

그것을 받는 메서드가 `onFinish` => 여기엔(ant design) 자동으로 preventDefault가 적용되어 있음.

보통아래에 있는 걸 적어서 새로고침이 되는 것을 막지만 온피니시에선 할필요가 없다.

```js
const onSubmitForm = (e) => {
	e.preventDefault();
}
```



----



**react  개발 TIP**

```js
import React from 'react';
import Head from "react"
import AppLayout from '../components/AppLayout';

const Profile = () => {
  return (
  <>
    <Head>
        <title>내 프로필 | NodeBird </title>?
    </Head>

    <AppLayout>
      <NicknameEditForm />
      <FollowingList header="팔로잉 목록"/>
      <FollowingList header="팔로워 목록"/>
    </AppLayout>
    
  
  </>
  )
}

export default Profile
```



가상의 컴포넌트들을 미리 그냥 어떻게 배치할지 정해놓고 시작

데이터는 더미데이터 만들고





----



Form 같은 경우는 react form 라이브러리를 쓰는게 훨씬 나음! => 왜냐면 일일이 다하면 비효율적임





---

props의 개수가 여러개 일수도 있어! 

----



공식문서에 있는 것은 외우지 말자! antd 같은 것! 



----



## 커스텀 훅



Form을 다루다 보면 공통적으로 아래와 같은 작업을 반복해야 한다. 이럴떄 사용 하는게 커스컴 훅



````js
  const [id, setId] = useState("")
  const onChangeId = useCallback((e) => {
    setId(e.target.value)
  })
  const [nickname, setNickname] = useState("")
  const onChangeNickname = useCallback((e) => {
    setNickname(e.target.value)
  })
  const [password, setPassword] = useState("")
  const onChangePassword = useCallback((e) => {
    setPassword(e.target.value)
  })
````



````js
import { useState, useCallback } from "react";



export default (initalValue = null) => {

  const [value, setValue] = useState(initalValue)
  const handler = useCallback((e) => {
    setValue(e.target.value)
  }, [])

  return [value, handler]

}


```
로그인 폼에서 
```
import useinput from "../hooks/useinput"
	//이렇게 대체가 가능
const [id, onChangeId] = useinput("")

// const [id, setId] = useState("")
// const onChangeId = useCallback((e) => {
//   setId(e.target.value)
// }, [])
````





----





### 논리 && 연산자가 있는 인라인 조건

중괄호로 감싸면 [JSX에 어떤 표현식이던 넣을 수](https://reactjs-kr.firebaseapp.com/docs/introducing-jsx.html#embedding-expressions-in-jsx) 있습니다. 여기에는 자바스크립트 논리 `&&` 연산자도 포함됩니다. 이를 사용하면 요소의 조건부 포함을 더 편리하게 할 수 있습니다.

```js
function Mailbox(props) {
  const unreadMessages = props.unreadMessages;
  return (
    <div>
      <h1>Hello!</h1>
      {unreadMessages.length > 0 &&
        <h2>
          You have {unreadMessages.length} unread messages.
        </h2>
      }
    </div>
  );
}

const messages = ['React', 'Re: React', 'Re:Re: React'];
ReactDOM.render(
  <Mailbox unreadMessages={messages} />,
  document.getElementById('root')
);
```

[Try it on CodePen.](https://codepen.io/gaearon/pen/ozJddz?editors=0010)

자바스크립트에서 `true && expression` 은 항상 `expression` 으로 평가되고, `false && expression` 은 항상 `false` 로 평가되기 때문에 이 코드는 동작합니다.

따라서 조건이 `true` 라면 `&&` 다음에 오는 요소가 노출됩니다. 만약 조건이 `false` 라면, React는 이를 무시하고 건너뜁니다.
