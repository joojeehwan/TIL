````
<script crossorigin src="https://unpkg.com/react@17/umd/react.development.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"></script>

리엑트 돔 => 모든 리엑트 엘리멘트들이  HTML 바이데 둘 수 있도록 해줌
````







````js

const root = document.getElementById("root")


  const span = React.createElement(
        "span",
        {id: "sexy-span", style: {color : "red"}},
        "Hello i m a span"
      )
  
  
  createElement 안의 span은 우리가 진짜로 쓰이는 element이름이어야 함! => react를 통해서 element를 만드는 것
  
  
  ReactDOM.render(span, root)
=> span을 어디다 둘건데?! 바로 root 안에 다가! 
````

