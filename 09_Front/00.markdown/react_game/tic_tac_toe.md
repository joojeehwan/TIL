**주의**

타이핑 횟수를 줄이고 [`this`의 혼란스러운 동작](https://yehudakatz.com/2011/08/11/understanding-javascript-function-invocation-and-this/)을 피하기 위해 아래부터는 이벤트 핸들러에 [화살표 함수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)를 사용하겠습니다.

```js
class Square extends React.Component {
 render() {
   return (
     <button className="square" onClick={() => console.log('click')}>       {this.props.value}
     </button>
   );
 }
}
```

`onClick={() => console.log('click')}`이 어떻게 동작하는지 살펴보면 `onClick` prop으로 *함수*를 전달하고 있습니다. React는 클릭했을 때에만 이 함수를 호출할 것입니다. `() =>`을 잊어버리고 `onClick={console.log('click')}`이라고 작성하는 것은 자주 발생하는 실수이며 컴포넌트가 다시 렌더링할 때마다 경고 창을 띄울 것입니다.



----

 **tip**

**여러개의 자식으로부터 데이터를 모으거나 두 개의 자식 컴포넌트들이 서로 통신하게 하려면 부모 컴포넌트에 공유 state를 정의해야 합니다. 부모 컴포넌트는 props를 사용하여 자식 컴포넌트에 state를 다시 전달할 수 있습니다. 이것은 자식 컴포넌트들이 서로 또는 부모 컴포넌트와 동기화 하도록 만듭니다.**



----

**state 끌어올리기**

````js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Square extends React.Component {


  render() {
    return (
      <button 
      className="square" 
      onClick={() => this.props.onClick()} 
      >
        {this.props.value}
      </button>
    );
  }
}

class Board extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      squares: Array(9).fill(null)
    }
  }
  renderSquare(i) {
    return(
    <Square 
    value={this.state.squares[i]} 
    onClick={() => this.handleClick(i)}
    />
    );
  }
````



1. 내장된 DOM `<button>` 컴포넌트에 있는 `onClick` prop은 React에게 클릭 이벤트 리스너를 설정하라고 알려줍니다.
2. 버튼을 클릭하면 React는 Square의 `render()` 함수에 정의된 `onClick` 이벤트 핸들러를 호출합니다.
3. 이벤트 핸들러는 `this.props.onClick()`를 호출합니다. Square의 `onClick` prop은 Board에서 정의되었습니다.
4. Board에서 Square로 `onClick={() => this.handleClick(i)}`를 전달했기 때문에 Square를 클릭하면 Board의 `handleClick(i)`를 호출합니다.
5. 아직 `handleClick()`를 정의하지 않았기 때문에 코드가 깨질 것입니다. 지금은 사각형을 클릭하면 “this.handleClick is not a function”과 같은 내용을 표시하는 붉은 에러 화면을 보게됩니다.



----





````js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Square extends React.Component {


  render() {
    return (
      <button 
      className="square" 
      onClick={() => this.props.onClick()} 
      >
        {this.props.value}
      </button>
    );
  }
}

class Board extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      squares: Array(9).fill(null)
    }
  }


  handleClick(i) {
    const squares = this.state.squares.slice()
    squares[i] = "X"
    this.setState({squares: squares})
  }
  renderSquare(i) {
    return(
    <Square 
    value={this.state.squares[i]} 
    onClick={() => this.handleClick(i)}
    />
    );
  }

  render() {
    const status = 'Next player: X';

    return (
      <div>
        <div className="status">{status}</div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  <Game />,
  document.getElementById('root')
);

````





**[지금까지의 전체 코드 확인하기](https://codepen.io/gaearon/pen/ybbQJX?editors=0010)**

이제 이전과 마찬가지로 Square를 클릭하여 사각형을 채울 수 있습니다. 그러나 이제는 state가 각 Square 컴포넌트 대신에 Board 컴포넌트에 저장됩니다. Board의 상태가 변화할 때 Square 컴포넌트는 자동으로 다시 렌더링합니다. Board 컴포넌트의 모든 사각형의 상태를 유지하는 것으로 이후에 승자를 결정하는 것이 가능합니다.

Square 컴포넌트가 더 이상 state를 유지하지 않기 때문에 Square 컴포넌트는 Board 컴포넌트에서 값을 받아 클릭될 때 Board 컴포넌트로 정보를 전달합니다. React 용어로 Square 컴포넌트는 이제 **제어되는 컴포넌트**입니다. Board는 이들을 완전히 제어합니다.









----



### 불변성이 왜 중요할까요?

이전 코드 예시에서 기존 배열을 수정하는 것이 아니라 `.slice()` 연산자를 사용하여 `squares` 배열의 사본 만들기를 추천했습니다. 지금부터 불변성이 무엇인지와 왜 불변성이 중요한지 알아보겠습니다.

일반적으로 데이터 변경에는 두 가지 방법이 있습니다. 첫 번째는 데이터의 값을 직접 *변경*하는 것입니다. 두 번째는 원하는 변경 값을 가진 새로운 사본으로 데이터를 교체하는 것입니다.

#### 객체 변경을 통해 데이터 수정하기

```
var player = {score: 1, name: 'Jeff'};
player.score = 2;
// 이제 player는 {score: 2, name: 'Jeff'}입니다.
```

#### 객체 변경 없이 데이터 수정하기

```
var player = {score: 1, name: 'Jeff'};

var newPlayer = Object.assign({}, player, {score: 2});
// 이제 player는 변하지 않았지만 newPlayer는 {score: 2, name: 'Jeff'}입니다.

// 객체 spread 구문을 사용한다면 이렇게 쓸 수 있습니다.
// var newPlayer = {...player, score: 2};
```

최종 결과는 동일하지만 직접적인 객체 변경이나 기본 데이터의 변경을 하지 않는다면 아래에 기술된 몇 가지 이점을 얻을 수 있습니다.

#### 복잡한 특징들을 단순하게 만듦

불변성은 복잡한 특징들을 구현하기 쉽게 만듭니다. 자습서에서는 “시간 여행” 기능을 구현하여 틱택토 게임의 이력을 확인하고 이전 동작으로 “되돌아갈 수 있습니다”. 이 기능은 게임에만 국한되지 않습니다. 특정 행동을 취소하고 다시 실행하는 기능은 애플리케이션에서 일반적인 요구사항 입니다. 직접적인 데이터 변이를 피하는 것은 이전 버전의 게임 이력을 유지하고 나중에 재사용할 수 있게 만듭니다.

#### 변화를 감지함

객체가 직접적으로 수정되기 때문에 복제가 가능한 객체에서 변화를 감지하는 것은 어렵습니다. 감지는 복제가 가능한 객체를 이전 사본과 비교하고 전체 객체 트리를 돌아야 합니다.

불변 객체에서 변화를 감지하는 것은 상당히 쉽습니다. 참조하고 있는 불변 객체가 이전 객체와 다르다면 객체는 변한 것입니다.

#### React에서 다시 렌더링하는 시기를 결정함

불변성의 가장 큰 장점은 React에서 *순수 컴포넌트*를 만드는 데 도움을 준다는 것입니다. 변하지 않는 데이터는 변경이 이루어졌는지 쉽게 판단할 수 있으며 이를 바탕으로 컴포넌트가 다시 렌더링할지를 결정할 수 있습니다.

`shouldComponentUpdate()`와 *순수 컴포넌트*를 작성하는 법에 대해 더 알아보고 싶다면 [성능 최적화하기](https://ko.reactjs.org/docs/optimizing-performance.html#examples)를 보세요.

### 





----



### 함수 컴포넌트

이제 Square를 **함수 컴포넌트**로 바꿔보겠습니다.

React에서 **함수 컴포넌트**는 더 간단하게 컴포넌트를 작성하는 방법이며 state 없이 `render` 함수만을 가집니다. `React.Component`를 확장하는 클래스를 정의하는 대신 `props`를 입력받아서 렌더링할 대상을 반환하는 함수를 작성할 수 있습니다. 함수 컴포넌트는 클래스로 작성하는 것보다 빠르게 작성할 수 있으며 많은 컴포넌트를 함수 컴포넌트로 표현할 수 있습니다.

Square 클래스를 아래의 함수로 바꿔보세요.

```
function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}
```

모든 `this.props`를 `props`로 변경하였습니다.

**[지금까지의 전체 코드 확인하기](https://codepen.io/gaearon/pen/QvvJOv?editors=0010)**

> 주의
>
> Square를 함수 컴포넌트로 수정했을 때 `onClick={() => this.props.onClick()}`을 `onClick={props.onClick}`로 간결하게 작성했습니다. *양쪽* 모두 괄호가 사라진 것에 주목해주세요.







----







### 순서 만들기

우리의 틱택토 게임이 가진 큰 문제점을 고칠 시간입니다. 게임판에서 “O”가 표시되지 않는 점이죠.

첫 번째 차례를 “X”로 시작하겠습니다. Board 생성자의 초기 state를 수정하는 것으로 기본값을 설정할 수 있습니다.

```
class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
      xIsNext: true,    };
  }
```

플레이어가 수를 둘 때마다 `xIsNext` (boolean 값)이 뒤집혀 다음 플레이어가 누군지 결정하고 게임의 state가 저장될 것입니다. Board의 `handleClick` 함수를 수정하여 `xIsNext` 값을 뒤집겠습니다.

```
  handleClick(i) {
    const squares = this.state.squares.slice();
    squares[i] = this.state.xIsNext ? 'X' : 'O';    this.setState({
      squares: squares,
      xIsNext: !this.state.xIsNext,    });
  }
```

이제 “X”와 “O”는 번갈아 나타납니다. 한 번 시도해보세요!

Board의 `render` 안에 있는 “status” 텍스트도 바꿔서 어느 플레이어가 다음 차례인지 알려주겠습니다.

```
  render() {
    const status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    return (
      // 나머지는 그대로입니다.
```

변경사항을 적용하면 Board 컴포넌트는 다음과 같습니다.

```
class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
      xIsNext: true,    };
  }

  handleClick(i) {
    const squares = this.state.squares.slice();    squares[i] = this.state.xIsNext ? 'X' : 'O';    this.setState({      squares: squares,      xIsNext: !this.state.xIsNext,    });  }

  renderSquare(i) {
    return (
      <Square
        value={this.state.squares[i]}
        onClick={() => this.handleClick(i)}
      />
    );
  }

  render() {
    const status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    return (
      <div>
        <div className="status">{status}</div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}
```

**[지금까지의 전체 코드 확인하기](https://codepen.io/gaearon/pen/KmmrBy?editors=0010)**

### 





---





### 승자 결정하기

이제 어떤 선수가 다음 차례인지 알려주었으니 승부가 나는 때와 더 이상 둘 곳이 없을 때를 알려주어야 합니다. 다음의 도우미 함수를 복사하여 파일 최하단에 붙여넣으세요.

```
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
```

9개의 사각형의 배열을 가지고 함수는 승자를 확인하여 적절한 값으로 `'X'`, `'O'`, 또는 `null`을 반환합니다.

어떤 플레이어가 우승했는지 확인하기 위해 Board의 `render` 함수에서 `calculateWinner(squares)`를 호출할 것입니다. 한 플레이어가 이긴다면 “Winner: X” 또는 “Winner: O” 같은 문구를 표시할 수 있습니다. Board의 `render` 함수에서 선언한 `status`를 아래 코드로 바꿔주세요.

```
  render() {
    const winner = calculateWinner(this.state.squares);    let status;    if (winner) {      status = 'Winner: ' + winner;    } else {      status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');    }
    return (
      // 나머지는 그대로입니다.
```

누군가가 승리하거나 Square가 이미 채워졌다면 Board의 `handleClick` 함수가 클릭을 무시하도록 변경하겠습니다.

```
  handleClick(i) {
    const squares = this.state.squares.slice();
    if (calculateWinner(squares) || squares[i]) {      return;    }    squares[i] = this.state.xIsNext ? 'X' : 'O';
    this.setState({
      squares: squares,
      xIsNext: !this.state.xIsNext,
    });
  }
```

**[지금까지의 전체 코드 확인하기](https://codepen.io/gaearon/pen/LyyXgK?editors=0010)**

축하합니다! 이제 제대로 동작하는 틱택토 게임을 만들었습니다. 그리고 React의 기본도 배웠습니다. 여기서 진정한 승자는 *여러분*인 것 같네요.