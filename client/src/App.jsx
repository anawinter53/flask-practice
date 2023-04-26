import axios from 'axios'
import { format } from 'date-fns'
import { useEffect, useState } from 'react'
import './App.css'
import { Homepage } from './pages'

const baseUrl = 'http://localhost:4000'

function App() {
  const [description, setDescription] = useState('')
  const [movieList, setMovieList] = useState([])

  const fetchMovies = async() => {
    const data = await axios.get(`${baseUrl}/movies`)
    const { movies } = data.data
    setMovieList(movies)
    console.log("Data: ", data)
  }

  useEffect(() => {
    fetchMovies()
  }, [])

  return (
    <>
      <Homepage movies={movies}/>
    </>
  )
}

export default App
