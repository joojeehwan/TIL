
import { useEffect, useState } from "react"



function Hello () {
  // function byFn() {
  //   console.log("bye")
  // }

  // function hiFn () {
  //   console.log("created")
  //   return byFn
  // }
  // useEffect(hiFn,[])
  // useEffect(() => {
  //   console.log("i'm created")
  //   return () => console.log("destoryed")
  // }, [])

  // useEffect(() => {
  //     console.log("hi")
  //   return () => console.log("bye")
  // },[])

  useEffect(function() {
    console.log("hi")
    return function() {
      console.log("bye")
    }
  },[])
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



///-------------------------------------------

  // const [counter, setValue] = useState(0)
  // const [keyword, setKeyword] = useState("")
  // const onClick = () => setValue((prev) => prev + 1)
  // const onChange = (event) => setKeyword(event.target.value)
  // // console.log("i run all the time")
  // // const iRunOnlyOnce = () => {
  // //   console.log("i run only once. ")
  // // }
  // // useEffect(() => {
  // //   console.log("call the api,,,")
  // // }, [])
  // useEffect(() => {
  //   console.log("나는 한번만 실행")
  // }, [])
  // useEffect(() => {
  //   console.log("나는 키워드가 변할때만")
  // }, [keyword])
  // useEffect(() => {
  //   console.log("나는 카운터가 변할떄만")
  // }, [counter])
  // useEffect(() => {
  //   console.log("나는 카운터랑 키워드가 변할떄만")
  // }, [counter, keyword])
  // // useEffect(() => {
  // //   if (keyword !== "" && keyword.length > 5) {
  // //     console.log("검색 : ", keyword)
  // //   }
  // // }, [keyword])
  // return (
  //   <div>
  //     <input value={keyword} onChange={onChange} type="text" placeholder="Search here..."/>
  //     <h1> {counter}</h1>
  //     <button onClick={onClick}>click me</button>  
  //   </div>
  // )
}

export default App;
 