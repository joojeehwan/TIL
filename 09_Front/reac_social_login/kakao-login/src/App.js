
import Auth from "./Auth";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Profile from "./Profile";

function App() {
  const REST_API_KEY = "024536b9d9745a03d46a16d3586e6941";
  const REDIRECT_URI = "http://localhost:3000/oauth/kakao/callback";
  const KAKAO_AUTH_URL = `https://kauth.kakao.com/oauth/authorize?client_id=${REST_API_KEY}&redirect_uri=${REDIRECT_URI}&response_type=code`;
  return (
    <Router>
    <div className="App">
      <Switch>
        <Route exact path="/">
          <h1><a href={KAKAO_AUTH_URL}>Kakao Login</a></h1>
        </Route>
        <Route path="/oauth/kakao/callback">
          <Auth />
        </Route>
        <Route path="/profile">
            <Profile />
        </Route>
      </Switch>
    </div>
    </Router>
  );
}

export default App;
