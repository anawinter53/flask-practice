import React from 'react'
import MovieCard from '../MovieCard'

export default function MoviesList(movies) {
  return (
    <div>
        {movies.map(movie => {
            return (
                <MovieCard movie={movie} />
            )
        })}
    </div>
  )
}
