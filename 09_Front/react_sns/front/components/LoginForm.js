
import React,{useCallback, useMemo} from "react"
import {Form, Input, Button} from "antd"
import Link from "next/link"
import styled from "styled-components"
import {useDispatch} from "react-redux"

import useinput from "../hooks/useinput"
import { loginRequestAction } from "../reducers/user"
import { useSelector } from "react-redux"



const ButtonWrapper = styled.div`
  margin-top: 10px;
`


const FormWrapper = styled(Form)`
  padding: 10px;
`

const LoginForm = ( ) => {

    const dispatch = useDispatch()
    const {logInLoading} = useSelector((state) => state.user)
    const [email, onChangeEmail] = useinput("")
    const [password, onChangePassword] = useinput("")

    // const [id, setId] = useState("")
    // const onChangeId = useCallback((e) => {
    //   setId(e.target.value)
    // }, [])
    
    // const [passwrod, setPassword] = useState("")
    // const onChangePasswrod = useCallback((e) => {
    //   setPassword(e.target.value)
    // }, [])

    const onSubmitForm = useCallback(() => {
          console.log(email, password)
          dispatch(loginRequestAction({email, password}))
    }, [email, password])

    const style = useMemo(() => ({marginTop: 10}), [])
    return (
      <FormWrapper onFinish={onSubmitForm}>
        <div>
          <label htmlFor="user-email">이메일</label> 
          <br />
          <Input name="user-email" type="email" value={email} onChange={onChangeEmail} required/>
        </div>
        <div>
          <label htmlFor="user-password"></label> 
            <br />
            <Input 
            name="user-password" 
            type="password"
            value={password} 
            onChange={onChangePassword} 
            required
            />
        </div>
        <ButtonWrapper style={style}>
          <Button type="primary" htmlType="submit" loading={logInLoading}>로그인</Button>
          <Link href="/signup"><a><Button>회원가입</Button></a></Link>
        </ButtonWrapper>
      </FormWrapper>
    )
}

// LoginForm.propTypes = {
//   setIsLoggedIn: PropTypes.func.isRequired,
// }


export default LoginForm