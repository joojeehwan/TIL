react , vue이런건 사용자와의 빠른 인터렉션을 위해서 쓰는 것!

react와 vue를 쓰면,,, 검색엔진 문제,, 

그 해결방법 => 서버사이드 렌더링(첫방문만 ssr, 그 다음부터의 사용자와의 인터렉션은 csr로!) / 코드 스플릿팅(방문한 페이지만 보여주는,,! )



Next를 쓰고 안쓰고를 구분해야해,,! ssr이랑 코드 스플릿도 필요 없는 사이트?! => 어드민 페이지! 복잡하게 굳이.!

그냥 리엑트로만! 



아 리엑트로도 ssr이 가능해,, 신기하다,,, 





----





# next 맛보기



next는 `pages` 라는 폴더를 인식한다. 여기 안에 있는 파일들을 개인적인 페이지로 만들어 준다.

> 이름 꼭 pages로 해야한다. 그래야 인식 할 수 있음

=> 컴포넌트랑 1대1 매칭해줌,,! 그래서 바로 그냥 url 주소 적으면 된다,,! 이건 장고보다 편한듯?! 

라우팅 되게 편하다,, 리엑트 뷰보다 진짜로!

> 폴더 생기면 `/폴더이름/컴포넌트 이름` 이런식으로 주소가 된다,, 

next를 하면서 겪은 첫 오류,,,!



> Profile(...): Nothing was returned from render. This usually means a return statement is missing. Or, to render nothing, return null. 



보통,, 내가 return에서 실수 한것,, render링이 되는 부분에서 문법적오류가 없는지 잘 확인해보자!



```js
render() {
    return 
    (
        <div>Here comes JSX !</div>
    );
}
```



````js
render() {
    return (
        <div>Here comes JSX !</div>
    );
}
````



----

**components**

컴포넌트 재사용되거나 불필요하게 리 랜더링 되는것 막기위해서 쪼갬 !





----







모든 컴포넌트의 props 객체는 children이라고 이름된 property를 가진다. 

 

this.props.children은 컴포넌트의 오프닝과 JSX태그들 클로징 사이에서 모든것을 리턴할 것이다. 

 

지금까지, <MyComponentClass />같이 당신이 봐온 모든 컴포넌트들은 self-closing tag들이었다. 

그들은 그럴필요는 없다!

당신은 <MyComponentClass></MyComponentClass> 라고 적을수도 있고, 이것은 여전히 동작할 것이다. 

 

this.props.children은 <MyComponentClass></MyComponentClass>사이에서 모든것들을 리턴할것이다.





````js
import PropTypes from "prop-types"

const AppLayout = ({children}) => {
  return (
    <div>
      <div>공통메뉴</div>
      {children}
    </div>
  )
}



AppLayout.propTypes = {
  children: PropTypes.node.isRequired,

}

export default AppLayout
````







```js
import AppLayout from "../components/AppLayout";

const Home = () => {

  return (
    <AppLayout>
      <div>Hello, Next!</div>
    </AppLayout>
   
  )

}

export default Home;
```





**children으로 안하면 렌더링안된다! 특정 keyword가 존재 하는 것!** 



----



React.js에서 props는 Immutable Data 즉, 변하지 않는 데이터입니다. 상위(부모) 컴포넌트에서 하위(자식) 컴포넌트로 데이터를 넘겨줄 때 사용합니다.

이번 글에선 React.js에서 props를 사용하는 방법과 default props를 지정하는 방법 및 props type을 검증하는 방법에 대해 알아보겠습니다.

먼저 props 사용방법은 <컴포넌트이름 props이름 = “값”> 이렇게 상위 컴포넌트에서 HTML의 attribute를 정의하듯이 하위 컴포넌트의 속성처럼 사용하면 되는데요. props를 정의하면 하위 컴포넌트에서 {this.props.props이름}으로 사용할 수 있습니다(함수형 컴포넌트라면 {props파라미터.props이름} 이렇게 사용할 수 있습니다).

this.props.children이란 것도 있는데요. this.props.children은 <하위Component>*여기 값이 들어값니다.*</하위Component> 이렇게 하위 컴포넌트로 감싸여진 값이 props.children의 값으로 들어가게 됩니다.

[여기 참고](https://medium.com/@su_bak/react-js-react-js%EC%9D%98-props-%EC%82%AC%EC%9A%A9%EB%B0%A9%EB%B2%95-bc59a5c257a)





````js
// React.js 예제 코드
class Children extends React.Component { // 하위(자식) 컴포넌트
  render() {
    return (
      <div>
        // 상위 컴포넌트가 넘겨준 props인 name사용
        <h1>Hello {this.props.name}</h1>
        // 상위 컴포넌트가 넘겨준 props.children 사용
        <div>{this.props.children}</div>
      </div>
    );
  }
}
class App extends React.Component { // 상위(부모) 컴포넌트
  render() {
    return (
      // props이름 : name
      // name이란 props의 값 : 이름
      // this.props.children의 값 : 이 사이에 있는거는 children
      <Children name="이름">이 사이에 있는거는 children</Children>
    );
  }
}
ReactDOM.render(<App/>, document.getElementById("root"));
````



---

페이지를 맨 처음 초기화해주는 아주 중요한 녀석이다. 이녀석이 없으면 앱이 실행되지 않는다.

React.js나 Vue.js에 꼭 필요한 app.js라고 보면 된다.

 

이 페이지는 처음 초기화를 해줄 뿐더러 페이지를 탐색할 때 상태 유지를 해주고 페이지들의 공통된 레이아웃을 담당해준다. 또 초기 데이터를 페이지에 주입(pageProps)해주고 Global CSS를 추가할 수 있다.

 

보통 Header, Side, Footer를 공통된 Component로 두고 싶을 때 여기서 먼저 Component를 주입시켜주면 된다.



출처: https://soft91.tistory.com/92 [너와 나의 프로그래밍]

