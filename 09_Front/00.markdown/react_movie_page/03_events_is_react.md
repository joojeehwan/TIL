

react vs vanila js

````js
<button id="btn"> click me </button> 

const button = document.getElementById("btn")
const span = document.querySelector("span")
    
button.addEventListener("click", handleClick)


위의 4줄의 코드를
  const btn = React.createElement("button", {
        onclick: () => console.log("클릭했음")
      }, "click me")

  하나로 대체함! => REACT의 효율


````



----



````js
      const root = document.getElementById("root")


      const Title =  () => (
        <h3 id="title" onMouseEnter={() => console.log("mouser enter")}>
            Hello 나는 타이틀
          </h3>
      )


      // const h3 = React.createElement("h3", {
      //   onMouseEnter: () => console.log("mouser enter")
      // }, "Hello i m a span")


      const Button = () => (
        <button
        style={{
          backgroundColor: "tomato",
        }}
        onClick={() => console.log("나는 클랙당했다")}
        >
        Click me
        </button>
      )


      // const btn = React.createElement("button", {
      //   onClick: () => console.log("클릭했음"),
      //   style: {
      //     backgroundColor: "tomato",
      //   }
      // }, "click me")

      // const container = React.createElement("div", null, [Title, Button])
      const Container = 
      <div>
        <Title/> 
        <Button/>
      </div>
      ReactDOM.render(container, root)
      // react 엘리먼트들을 root div안에서 보여주라는 뜻 

#주의! componet의 이름은 항상 대문자일것! 소문자면 html 태그로 인식해버릴 수도,,! 
````





---



변수의 함수화



````js
     const Button = () => (
        <button
        style={{
          backgroundColor: "tomato",
        }}
        onClick={() => console.log("나는 클랙당했다")}
        >
        Click me
        </button>
      )
````





----



state를 할 수 있는 2가지 방법





1. 최고의 방법

`````js

      const root = document.getElementById("root")
      function App() {
        const [counter, setCounter] = React.useState(0)
        const onClick = () => {
          //setCounter(counter + 1)
          // 현재의 값을 기준으로! counter라는 값은 다른곳에서 변할 수도 있으니! 
          // 함수 전달방법으로 하는게 맞음
          setCounter((current) => current + 1)
        }
      
        return (
          <div>
            <h3>Total clicks: {counter}</h3>
            <button onClick={onClick}>Clike me</button>
          </div>
        )
      }

      ReactDOM.render(<App/>, root)
`````



2. 안좋은 방법

````js
      const root = document.getElementById("root")
      let counter = 0
      function countUp() {
        counter = counter + 1
        render()

      }

      function render() {
        ReactDOM.render(<Container/>, root)

      }
      const Container = () => (

        <div>
          <h3>Total clicks: {counter}</h3>
          <button onClick={countUp}>Clike me</button>
        </div>
    
      )

      render()
````

state가 바귀면 reacr가 리렌더링을 해줌! 그 부분만!! 





---







