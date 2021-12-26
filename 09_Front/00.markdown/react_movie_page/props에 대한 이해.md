

```js
    function SaveBtn() {
      return (
        <button
        style ={{
          backgroundColor: "tomato",
          color: "white",
          padding: "10px 20px",
          border: 0,
          borderRadius: 10,
          }}
        >
          Save Changes
        </button>
      )
    }

    function ConfirmBtn() {
      return <button
      style ={{
          backgroundColor: "tomato",
          color: "white",
          padding: "10px 20px",
          border: 0,
          borderRadius: 10,
          }}
          >Confirm
          </button>
    }

    function App() {
        return ( 
        <div>
          <SaveBtn />
          <ConfirmBtn/>  
        </div>
        )
    }

    const root = document.getElementById("root")
    ReactDOM.render(<App/>, root)

```





이렇게 하는 건 뭐랄까 반복이야! 

하나의 컴포넌트에서 텍스트만 바꾸면 되자나!





----





```js
  function Btn({text, onClick}) {
      return (
        <button
        #이렇게 내가 직접 손수 사용해야해! 
        onClick={onClick},
        style ={{
          backgroundColor: "tomato",
          color: "white",
          padding: "10px 20px",
          border: 0,
          borderRadius: 10,
          }}
        >
          {text}
        </button>
      )
    }
    function App() {
      const [value, setValue] = React.useState("Save Changes")
      const changeValue = () => setValue("Revert changes")
        return ( 
        <div>
          <Btn text={value} onClick={changeValue} />
            #이곳에 무엇을 넣든간에 그것들은 단지 prop이 될뿐!
    	    #이것들을 결코 실제HTML 태그안에 들어가지 않음
          <Btn text="Continue" />  
        </div>
        )
    }
    
   
```



> prop를 한다고 해서 자동적으로 prop을 전달하는 곳으로 return이 전달되지는 않음!
>
> 내가 직접 return 에다가 값을 넣어야 해! 









---



메모(Memo)





````js
  function Btn({text, onClick}) {
      return (
        <button
        onClick={onClick}
        style ={{
          backgroundColor: "tomato",
          color: "white",
          padding: "10px 20px",
          border: 0,
          borderRadius: 10,
          }}
        >
          {text}
        </button>
      )
    }
    function App() {
      const [value, setValue] = React.useState("Save Changes")
      const changeValue = () => setValue("Revert changes")
        return ( 
        <div>
            #이 아래에 있는 부분은 클릭에 의해서 value가 props되고
            #값이 변화한다! 부모컴포넌트의 값을 자식의 행동으로 인해 바뀌네,, !
          <Btn text={value} onClick={changeValue} />
            # 이 아래에 있는 부분은 바뀌면 안돼지! 왜냐면 setValue에 의해서 
        	#props의 값이 변화하는게 아니자나! 이 아래에 있는 props는 변화
            #하지 않으니! 
          <Btn text="Continue" />  
        </div>
        )
    }

    const root = document.getElementById("root")
    ReactDOM.render(<App/>, root)

````





그러기 위해서 사용하는게 memo





```JS
 function Btn({text, onClick}) {
      return (
        <button
        onClick={onClick}
        style ={{
          backgroundColor: "tomato",
          color: "white",
          padding: "10px 20px",
          border: 0,
          borderRadius: 10,
          }}
        >
          {text}
        </button>
      )
    }
    const MemorizedBtn = React.memo(Btn)
    function App() {
      const [value, setValue] = React.useState("Save Changes")
      const changeValue = () => setValue("Revert changes")
        return ( 
        <div>
          <MemorizedBtn text={value} onClick={changeValue} />
          <MemorizedBtn text="Continue" />  
        </div>
        )
    }

    const root = document.getElementById("root")
    ReactDOM.render(<App/>, root)
```

**부모의 state의 변화로 인해서 변경이 생겨서 자식들이 모두 다시 리렌더링 된다면 속도에 문제가 생길 수 있음**

이게 천개면,, 어우,,,

> props가 변경되지 않는다면 다시 그릴 필요가 없다! 고 위에서 말한것 !







----



PropTypes



````js
   function Btn({text, fontSize}) {
      return (
        <button
        style ={{
          backgroundColor: "tomato",
          color: "white",
          padding: "10px 20px",
          border: 0,
          borderRadius: 10,
          fontSize,
          }}
        >
          {text}
        </button>
      )
    }
    //이런식으로 리엑트에게 알려준다! 
    // 정확히 무엇이 props되어야 한느지! 
    Btn.propTypes = {
      text: PropTypes.string,
      fontSize: PropTypes.number.isRequried,
    }


    function App() {
      const [value, setValue] = React.useState("Save Changes")
        return ( 
        <div>
          <Btn text="안녕친구들" fontSize={16}/>
          <Btn text="text"/>
        </div>
        )
    }

    const root = document.getElementById("root")
    ReactDOM.render(<App/>, root)

````



