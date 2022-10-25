// import React, { useEffect } from 'react';
// import { useSelector, useDispatch } from 'react-redux';

// import AppLayout from "../components/AppLayout";
// import PostCard from '../components/PostCard';
// import PostForm from '../components/PostForm';
// import { LOAD_POSTS_REQUEST } from '../reducers/post';



// const Home = () => {

//   const dispatch = useDispatch()
//   const { me } = useSelector((state) => state.user)
//   const { mainPosts, hasMorePost} = useSelector((state) => state.post)
  
//   useEffect(() => {
//     dispatch({
//       type: LOAD_POSTS_REQUEST,
//     })
//   }, [])


//   //인피니티 스크롤 구현
//   useEffect(() => {

//     function onScroll() {
//       console.log(window.scrollY , document.documentElement.clientHeight, document.documentElement.scrollHeight )
//       if (window.scrollY + document.documentElement.clientHeight > document.documentElement.scrollHeight - 300) {
//         if(hasMorePost){

//           dispatch({
//               type: LOAD_POSTS_REQUEST
//             })
          
//         }  
//       }
//     }
//     window.addEventListener("scroll", onScroll)
//     return () => {
//       window.removeEventListener("scroll", onScroll)
//     }

//   },[hasMorePost])

//   return (
//     <AppLayout>
//       { me && <PostForm/>}
//       {mainPosts.map((c) => (<PostCard key={c.id} post={c}/>
//       ))}
//     </AppLayout>
   
//   )

// }

// export default Home;


import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';

import PostForm from '../components/PostForm';
import PostCard from '../components/PostCard';
import AppLayout from '../components/AppLayout';
import { LOAD_POSTS_REQUEST } from '../reducers/post';
import KakaomapComponent from "../components/KakaomapComponent";
import Head from 'next/head';

const Home = () => {
  <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=29214baeec4422486e3cfd0d7557aab2"></script>

  const dispatch = useDispatch();
  const { me } = useSelector((state) => state.user);
  const { mainPosts, hasMorePosts, loadPostsLoading } = useSelector((state) => state.post);

  useEffect(() => {
    dispatch({
      type: LOAD_POSTS_REQUEST,
    });
  }, []);

  useEffect(() => {
    function onScroll() {
      if (window.scrollY + document.documentElement.clientHeight > document.documentElement.scrollHeight - 300) {
        if (hasMorePosts && !loadPostsLoading) {
          dispatch({
            type: LOAD_POSTS_REQUEST,
            data: mainPosts[mainPosts.length - 1].id,
          });
        }
      }
    }
    window.addEventListener('scroll', onScroll);
    return () => {
      window.removeEventListener('scroll', onScroll);
    };
  }, [mainPosts, hasMorePosts, loadPostsLoading]);

  const kakaoMap = React.useRef(null);
  useEffect(() => {
      if (kakaoMap && kakaoMap.current) {
          const x = 126.570667;
          const y = 33.450701;
          const coords = new window.kakao.maps.LatLng(y, x); // 지도의 중심좌표
          const options = {
              center: coords,
              level: 2,
          };
          const map = new window.kakao.maps.Map(kakaoMap.current, options);
          const marker = new window.kakao.maps.Marker({
              position: coords,
              map,
          });
          // 맵의 중앙으로 이동
          map.relayout();
          map.setCenter(coords);
          // 마커를 중앙으로 이동
          marker.setPosition(coords);
          // 일반 지도와 스카이뷰로 지도 타입을 전환할 수 있는 지도타입 컨트롤을 생성합니다
          const mapTypeControl = new window.kakao.maps.MapTypeControl();
          // 지도에 컨트롤을 추가해야 지도위에 표시됩니다
          // kakao.maps.ControlPosition은 컨트롤이 표시될 위치를 정의하는데 TOPRIGHT는 오른쪽 위를 의미합니다
          map.addControl(mapTypeControl, window.kakao.maps.ControlPosition.TOPRIGHT);
          // 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
          const zoomControl = new window.kakao.maps.ZoomControl();
          map.addControl(zoomControl, window.kakao.maps.ControlPosition.RIGHT);
      }
  }, [kakaoMap]);


  return (

    <>
    <Head>
    <script 
    type="text/javascript" 
    src="//dapi.kakao.com/v2/maps/sdk.js?appkey=29214baeec4422486e3cfd0d7557aab2">
    </script>
        
    </Head>
    {React.createElement(KakaomapComponent, { ref: kakaoMap })}

    <AppLayout>
      {me && <PostForm />}
      {mainPosts.map((c) => (
        <PostCard key={c.id} post={c} />
        ))}
    </AppLayout>
    </>
  );

  
};

export default Home;