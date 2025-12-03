import { Link } from "react-router-dom"
import '../css/Navbar.css'


function NavBar() {
    return <nav className="navbar">
        <div className="nav-brand">
            <Link to="/">AI Movie Recommender</Link>
        </div>
        <div className="nav-links">
            <Link to="/" className="nav-link">Home</Link>
            <Link to="/favorites" className="nav-link">Favorites</Link>
        </div>
        </nav>
}

export default NavBar