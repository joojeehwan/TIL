import { useEffect, useState } from "react"
import {useParams} from "react-router-dom"
import MovieDtail from "../components/MovieDetail"

function Detail () {
  //url에서 동적으로 변하는 부분을 반환
  const {id} = useParams()
  const [movie, setMovie] = useState([])

  const getMovie = async () => {
    const json = await (
      await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
    ).json()
    console.log(json.data.movie.description_full)
    setMovie(json.data.movie)
  }
  useEffect(() => {
    getMovie()
  }, [])
  return (
  <div>
    <h1>Detail</h1>
    <MovieDtail
    rating={movie.rating}
    year={movie.year}
    description_full={movie.description_full}
    />
  </div>
  )
}

export default Detail