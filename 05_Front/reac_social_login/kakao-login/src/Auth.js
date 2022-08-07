import React from "react"
import { useEffect } from "react";
import { useHistory } from "react-router-dom";
import axios from "axios";
import qs from "qs";



const Auth  = () => {
    const REST_API_KEY = "024536b9d9745a03d46a16d3586e6941";
    const REDIRECT_URI = "http://localhost:3000/oauth/kakao/callback";
    const CLIENT_SECRET = "qfsksK3EHyGjIDwEoaIXrk0SOXVSa9mP";

    const code = new URL(window.location.href).searchParams.get("code");
    const history = useHistory();
    const getToken = async () => {
      const payload = qs.stringify({
        grant_type: "authorization_code",
        client_id: REST_API_KEY,
        redirect_uri: REDIRECT_URI,
        code: code,
        client_secret: CLIENT_SECRET,
      });
      try {
        // access token 가져오기
        const res = await axios.post(
          "https://kauth.kakao.com/oauth/token",
          payload
        );
        
        // Kakao Javascript SDK 초기화
        window.Kakao.init(REST_API_KEY);
        // access token 설정
        window.Kakao.Auth.setAccessToken(res.data.access_token);
        history.replace("/profile");
      } catch (err) {
        console.log(err);
      }
    };
    useEffect(() => {
      getToken();
    }, []);
    return null;
    // 코드 내용은 Redirect 주소로 전달받은 code 값을 추출하여 보여주는 코드입니다.
}


export default Auth