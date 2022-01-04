import { EllipsisOutlined, HeartOutlined, MessageOutlined, RetweetOutlined, HeartTwoTone } from "@ant-design/icons"
import PropTypes from 'prop-types';
import { Card, Popover, Button, Avatar, List, Comment } from "antd"
import React, {useCallback, useState}from "react"
import Link from 'next/link';
import { useSelector, useDispatch } from 'react-redux';

import PostImages from "./PostImages";
import CommentForm from "./CommentForm";
import PostCardContent from "./PostCardContent";

import styled from 'styled-components';
import { REMOVE_POST_REQUEST } from "../reducers/post";

const CardWrapper = styled.div`
  margin-bottom: 20px;
`;


const PostCard = ({ post }) => {

  const dispatch = useDispatch()
  const {removePostLoding} = useSelector((state) => state.post)
  const [commentFormOpened, setCommentFormOpened] = useState(false)
  const [liked, setLiked] = useState(false);

  const onToggleLike = useCallback(() => {
    setLiked((prev) => !prev)
  }, [])

  const onToggleComment = useCallback(() => {
    setCommentFormOpened((prev) => !prev);
  }, []);

  const onRemovePost = useCallback(() => {
    dispatch({
      type: REMOVE_POST_REQUEST,
      data: post.id
    })
  }, [])

  const id = useSelector((state) => state.user.me?.id)
  return (

    <CardWrapper key={post.id}>
      <Card
        cover={post.Images[0] && <PostImages images={post.Images} />}
        actions={[
          <RetweetOutlined key="retweet"/>,
          liked
            ? <HeartTwoTone twoToneColor="#eb2f96" key="heart" onClick={onToggleLike} />
            : <HeartOutlined key="heart" onClick={onToggleLike} />,
          <MessageOutlined key="message" onClick={onToggleComment}/>,
          <Popover
          key="ellipsis"
          content={(
            <Button.Group>
              {id && post.User.id === id
                ? (
                  <>
                    <Button>수정</Button>
                    <Button type="danger" onClick={onRemovePost} loading={removePostLoding}>삭제</Button>
                  </>
                )
                : <Button>신고</Button>}
            </Button.Group>
          )}
            
            
            >
              <EllipsisOutlined/>
          </Popover>
        ]}
      >
      <Card.Meta
          avatar={<Avatar>{post.User.nickname[0]}</Avatar>}
          title={post.User.nickname}
          description={<PostCardContent postData={post.content} />}
      />
      </Card>

      {commentFormOpened && (
      <div>
        <CommentForm post={post}/>
        <List
          header={`${post.Comments.length} 댓글`}
          itemLayout="horizontal"
          dataSource={post.Comments}
          renderItem={(item) => (
            <li>
              <Comment
                author={item.User.nickname}
                avatar={(
                  <Link href={{ pathname: '/user', query: { id: item.User.id } }} as={`/user/${item.User.id}`}>
                    <a><Avatar>{item.User.nickname[0]}</Avatar></a>
                  </Link>
                )}
                content={item.content}
              />
            </li>
          )}
        
        />
      </div>)}

    </CardWrapper>

  )

}

PostCard.propTypes = {
  post: PropTypes.shape({
    id: PropTypes.number,
    User: PropTypes.object,
    content: PropTypes.string,
    createdAt: PropTypes.object,
    Comments: PropTypes.arrayOf(PropTypes.any),
    Images: PropTypes.arrayOf(PropTypes.any),
  }),
}


export default PostCard