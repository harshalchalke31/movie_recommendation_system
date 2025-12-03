const API_KEY = 'a7d35fbd6d62607f63c94bbd2206420e'
const BASE_URL = 'https://api.themoviedb.org/3'

export const getPopularMovies = async() => {
    const response = await fetch(`${BASE_URL}/movie/popular?api_key=${API_KEY}`)
    const data = await response.json()
    return data.results
}

export const searchMovie = async(query) => {
    const response = await fetch(`${BASE_URL}/search/movie?api_key=${API_KEY}&query=${encodeURIComponent(query)}`)
    const data = await response.json()
    return data.results
}