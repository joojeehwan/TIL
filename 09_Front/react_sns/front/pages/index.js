import React from 'react';
import { useSelector } from 'react-redux';

import AppLayout from "../components/AppLayout";
import PostCard from '../components/PostCard';
import PostForm from '../components/PostForm';


const Home = () => {


  const { me } = useSelector((state) => state.user)
  const { mainPosts } = useSelector((state) => state.post)

  return (
    <AppLayout>
      { me && <PostForm/>}
      {mainPosts.map((c) => (<PostCard key={c.id} post={c}/>
      ))}
    </AppLayout>
   
  )

}

export default Home;