import React from 'react'
import { MoviesList } from '../../components'

export default function Homepage(movies) {
  return (
    <div>
        <MoviesList movies={movies} />
    </div>
  )
}
