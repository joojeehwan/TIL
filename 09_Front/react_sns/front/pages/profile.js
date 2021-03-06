import React, {useEffect} from 'react';
import AppLayout from '../components/AppLayout';
import NicknameEditForm from '../components/NicknameEditForm';
import FollowList from '../components/FollowList';
import {useSelector} from "react-redux"
import Router from 'next/router';

const Profile = () => {

  // const followerList = [{nickname:"jeehwab"}, {nickname:"바보"}, {nickname:"hello"}]
  // const followingList = [{nickname:"jeehwab"}, {nickname:"바보"}, {nickname:"hello"}]
  // 더 이상 이 친구들이 필요가 없음! 

  const {me} = useSelector((state) => state.user)


  useEffect(() => {
    if (!(me && me.id)) {
      Router.push('/');
    }
  }, [me && me.id]);
  if (!me) {
    return null;
  }

  return (
  <>
    <AppLayout>
      <NicknameEditForm />
      <FollowList header="팔로잉 목록" data={me.Followings}/>
      <FollowList header="팔로워 목록" data={me.Followers}/>
    </AppLayout>
    
  
  </>
  )
}

export default Profile