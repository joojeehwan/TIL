import React, {useRef, useCallback, useState, useEffect} from "react"
import {Form, Input, Button} from "antd"
import { useSelector, useDispatch } from 'react-redux';

import { addPost } from "../reducers/post";


const PostForm = () => {

    const dispatch = useDispatch()
    const [text, setText] = useState("")
    const { imagePaths, addPostLoading, addPostDone } = useSelector((state) => state.post);

    const imageInput = useRef()
    
    const onClickImageUpload = useCallback(() => {
      imageInput.current.click();
    }, [imageInput.current]);
    
    
    useEffect(() => {
      if (addPostDone) {
        setText('');
      }
    }, [addPostDone]);
    
    const onChangeText = useCallback((e) => {
      setText(e.target.value);
    }, []);

    const onSubmit = useCallback(() => {
      console.log("서브밋")
      dispatch(addPost(text));
    }, [text])
    

    return (
        <Form style={{ margin: '10px 0 20px' }} encType="multipart/form-data" onFinish={onSubmit}>
           <Input.TextArea value={text} onChange={onChangeText} maxLength={140} placeholder="어떤 신기한 일이 있었나요?" />
          <div>
            <input type="file" multiple hidden ref={imageInput}  />
            <Button onClick={onClickImageUpload}>이미지 업로드</Button>
            <Button type="primary" style={{ float: 'right' }} htmlType="submit">짹짹</Button>
          </div>
          <div>
          {imagePaths.map((v) => {
          return (
            <div key={v} style={{ display: 'inline-block' }}>
              <img src={v} style={{ width: '200px' }} alt={v} />
              <div>
                <Button>제거</Button>
              </div>
            </div>
          )
        })}
          </div>
        </Form>
    )

}

export default PostForm