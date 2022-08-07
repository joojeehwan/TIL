import React, { useCallback, useState} from 'react';
import {Form, Input, Checkbox, Button} from "antd"
import styled from "styled-components"

import AppLayout from '../components/AppLayout';
import useinput from '../hooks/useinput';
import Password from 'antd/lib/input/Password';

import { SIGN_UP_REQUEST } from '../reducers/user';

import {useSelector, useDispatch} from "react-redux"

const ErrorMessage = styled.div`
  color: red;
`

const Singup = () => {


  const dispatch = useDispatch()
  const {signUpLoading} = useSelector((state) => state.user)

  const [email, onChangeEmail] = useinput("")
  const [nickname, onChangeNickname] = useinput("")
  const [password, onChangePassword] = useinput("")
  
  const [passwordCheck, setPasswordCheck] = useState("")
  const [passwordError, setPasswordError] = useState(false)
  const onChangePasswordCheck = useCallback((e) => {
    setPasswordCheck(e.target.value)
    setPasswordError(e.target.value !== password) 
  }, [password])

  const [term, setTerm] = useState("")
  const [termError, setTermError] = useState("")
  const onChangeTerm = useCallback((e) => {
    setTerm(e.target.checked)
    setTermError(false)
  }, [])


  // const [id, setId] = useState("")
  // const onChangeId = useCallback((e) => {
  //   setId(e.target.value)
  // })
  // const [nickname, setNickname] = useState("")
  // const onChangeNickname = useCallback((e) => {
  //   setNickname(e.target.value)
  // })
  // const [password, setPassword] = useState("")
  // const onChangePassword = useCallback((e) => {
  //   setPassword(e.target.value)
  // })



  const onSubmit = useCallback(() => {
    if (password !== passwordCheck) {
      return setPasswordError(true)
    }
    if (!term) {
      return setTermError(true)
    }
    console.log(email, nickname, passwordCheck)
    dispatch({
      type: SIGN_UP_REQUEST,
      data: {email, password, nickname}
    })
  }, [email, Password, passwordCheck, term])


  return (
 <AppLayout>
   <Form onFinish={onSubmit}>
    <div>
      <label htmlFor='user-email'>이메일</label>
      <br />
      <Input name="user-email" type="email" value={email} required onChange={onChangeEmail}/>
    </div>
    <div>
      <label htmlFor='user-nick'>닉네임</label>
      <br />
      <Input name="user-nick" value={nickname} required onChange={onChangeNickname}/>
    </div>
    <div>
      <label htmlFor='user-password'>비밀번호</label>
      <br />
      <Input name="user-password" type="password" value={password} required onChange={onChangePassword}/>
    </div>
    <div>
      <label htmlFor='user-password'>비밀번호체크</label>
      <br />
      <Input 
        name="user-password-check" 
        value={passwordCheck} 
        required
        type="password"
        onChange={onChangePasswordCheck}/>
        {passwordError && <ErrorMessage>비밀번호가 일치하지 않습니다.</ErrorMessage>}
    </div>

    <div>
      <Checkbox name="user-term" checked={term} onChange={onChangeTerm}>주지환의 말을 잘 들을 것을 동의합니다.</Checkbox>
      {termError && <ErrorMessage>약관에 동의하셔야 합니다.</ErrorMessage> }
    </div>

    <div style={{marginTop:10}}>
        <Button type='primary' htmlType='submit' loading={signUpLoading}>가입하기</Button>
    </div>

   </Form>
 </AppLayout>
  )
}

export default Singup