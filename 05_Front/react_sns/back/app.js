
//기본 노드로 
// const http = require("http")
// const server = http.createServer((req, res) => {
//   console.log(req.url, req.method)
//   res.end("hello node")
// })
// server.listen(3065, () =>{
//   console.log("서버 실행 중")
// })


//express 설치 후
const express = require("express")
const postRouter = require("./routes/post")


const app = express()

app.get("/", (req, res) => {
  res.send("hello express")
})


app.user('/post', postRouter)


app.listen(3065, () => {
  console.log("서버 실행 중")
})
