import React from 'react';
import ReactDOM from 'react-dom';


function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user = {
  firstName: 'Harper',
  lastName: 'Perez'
};


const element = (
  <h1>
    Hello, {formatName(user)}!
  </h1>
);

// const name = 'Josh Perez';
// const element = <h1>Hello, {name}</h1>;


ReactDOM.render(
  element,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

