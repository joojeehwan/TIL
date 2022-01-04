

useState를 통해 state를 변경하는 방법 2가지



1. setTodo에 함수를 전달
2. 직접 값을 넣음

```js
const [todo, setTodo] = useState("")
  const [toDos, setToDos] = useState([])
  const onChange = (event) => setTodo(event.target.value)
  const onSubmit = (event) => {
    event.preventDefault()
    if (todo === "") {
      return
    }
    //기존의 것 + 새로운 값 배열에 추가하는 js
    setToDos((currentArray) => [todo, ...currentArray])
    setTodo("")
  }

  console.log(toDos)
  return (
    <div>
      <h1>My To Dos ({toDos.length})</h1>
      <form onSubmit={onSubmit}>
        <input 
        onChange={onChange}
        value={todo} 
        type="text" 
        placeholder="Write your to do,,,"
        />
        <button>Add To do</button>
      </form>
    </div>
  )
```

