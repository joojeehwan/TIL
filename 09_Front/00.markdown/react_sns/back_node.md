```js
const http = require("http")
const server = http.createServer((req, res) => {
  console.log(req.url, req.method)
  res.end("hello node")
})

server.listen(3065, () =>{
  console.log("서버 실행 중")
})
```



요청에 대한 정보 확인은 req에서 

응답에 대한 정보는 res에 담아서!

소스를 껏다가 끼면 다시 껏다가 켜야 함



---

rest api ,, 어느정도 타협,,! 



애매하면 ,, post로 하자! 



스웨거?! 





---

**require 가 import라고 보면 된다.** 

**module.exports** 는 그대로 exports 라고 보면 된다





mysql에서 막히네,,재설치 고고