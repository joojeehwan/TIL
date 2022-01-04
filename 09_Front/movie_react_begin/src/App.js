

import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Detail from "./routes/Detail";
import Home from "./routes/Home"

function App() {
  return (
  <Router>
    <Switch>
      <Route path="/movie/:id">
        <Detail/>
      </Route>
      <Route path="/">
        <Home/>
      </Route>
    </Switch>
  </Router>
  )
}

//-----------------------------코인 트래커

// function App() {

//   const [loading, setLoading] = useState(true)
//   const [coins, setCoins] = useState([])
//   useEffect(() => {
//       fetch("https://api.coinpaprika.com/v1/tickers")
//         .then((response) => response.json())
//         .then((json) => {
//           setCoins(json)
//           setLoading(false)
//         })
//   }, [])
//   return ( 
//     <div>
//         <h1>The Coins ({coins.length})</h1>
//         {loading ? <strong>Loading...</strong> : null}
      
//         <ul>
//           {coins.map((coin) => (

//             <li>
//               {coin.name} ({coin.symbol}): ${coin.quotes.USD.price} USD
//             </li>
//           ))}
          
//         </ul>
//     </div> 
//   )
// }






//----------------todolist

// function App() {


//   const [todo, setTodo] = useState("")
//   const [toDos, setToDos] = useState([])
//   const onChange = (event) => setTodo(event.target.value)
//   const onSubmit = (event) => {
//     event.preventDefault()
//     if (todo === "") {
//       return
//     }
//     //기존의 것 + 새로운 값 배열에 추가하는 js
//     setToDos((currentArray) => [todo, ...currentArray])
//     setTodo("")
//   }
 
//   console.log(toDos)
//   return (
//     <div>
//       <h1>My To Dos ({toDos.length})</h1>
//       <form onSubmit={onSubmit}>
//         <input 
//         onChange={onChange}
//         value={todo} 
//         type="text" 
//         placeholder="Write your to do,,,"
//         />
//         <button>Add To do</button>
//       </form>
//       <hr/>

//       <ul>
//         {toDos.map((item, index) => (
//           <li key={index}>{item}</li>
//         ))}
//       </ul>
//     </div>
//   )
// }






// 1226 (2)clean up

// function Hello () {
//   // function byFn() {
//   //   console.log("bye")
//   // }

//   // function hiFn () {
//   //   console.log("created")
//   //   return byFn
//   // }
//   // useEffect(hiFn,[])
//   // useEffect(() => {
//   //   console.log("i'm created")
//   //   return () => console.log("destoryed")
//   // }, [])

//   // useEffect(() => {
//   //     console.log("hi")
//   //   return () => console.log("bye")
//   // },[])

//   useEffect(function() {
//     console.log("hi")
//     return function() {
//       console.log("bye")
//     }
//   },[])
//   return <h1>Hello</h1>
// }

// function App() {

//   const [showing, setShowing] = useState(false)
//   const onClick = () => setShowing((prev) => !prev)

//   return ( 
//   <div>
//     {showing ? <Hello /> : null}
//     <button onClick={onClick}> {showing ? "Hide" : "showing"} </button>

//   </div>
//   )



///1226 (1) useEffect

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
//}

export default App;
 