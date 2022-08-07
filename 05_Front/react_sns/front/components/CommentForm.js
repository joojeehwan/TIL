import React,  {useCallback, useState, useEffect} from 'react';
import {Form, Button, Input } from "antd"
import PropTypes from 'prop-types';
import {useSelector, useDispatch} from "react-redux"
import { ADD_COMMENT_REQUEST } from '../reducers/post';


//post를 받아온 이유?!
// 게시글 아이디가 있으면 그 아이디 아래 댓글을 달거기 때문에! 
const CommentForm = ({post}) => {

  const dispatch = useDispatch();
  const { addCommentDone, addCommentLoading } = useSelector((state) => state.post);
  const id = useSelector((state) => state.user.me?.id);

  const [commentText, setCommentText] = useState('');
  const onChangeCommentText = useCallback((e) => {
    setCommentText(e.target.value);
  }, []);

  useEffect(() => {
    if (addCommentDone) {
      setCommentText('');
    }
  }, [addCommentDone]);
  
  const onSubmitComment = useCallback(() => {
    console.log(post.id, commentText);
    dispatch({
      type: ADD_COMMENT_REQUEST,
      data: {content: commentText, postId: post.id, userId: id}
    })
  }, [commentText, id]);


  return (

    <Form onFinish={onSubmitComment}>
    <Form.Item style={{ position: 'relative', margin: 0 }}>
      <Input.TextArea rows={4} value={commentText} onChange={onChangeCommentText} />
      <Button
        style={{ position: 'absolute', right: 0, bottom: -40, zIndex: 1 }}
        type="primary"
        htmlType="submit"
        loading={addCommentLoading}
      >삐약
      </Button>
    </Form.Item>
  </Form>
  )
}



CommentForm.propTypes = {
  post: PropTypes.object.isRequired,
};

export default CommentForm