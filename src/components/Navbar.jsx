// src/components/Navbar.jsx
import { Link } from "react-router-dom";
import ThemeToggle from "./ThemeToggle";

function Navbar() {
  return (
    <nav className="bg-white dark:bg-gray-950 shadow-md px-6 py-4 flex justify-between items-center transition-colors duration-300">
      {/* Logo */}
      <Link to="/" className="text-2xl font-bold text-primary dark:text-white">
        ClinicalTrials
      </Link>

      {/* Nav Links */}
      <div className="hidden md:flex gap-6 items-center text-sm font-medium">
        <Link to="/" className="hover:text-primary dark:hover:text-secondary">
          Home
        </Link>
        <Link to="/register" className="hover:text-primary dark:hover:text-secondary">
          Register
        </Link>
        <Link to="/login" className="hover:text-primary dark:hover:text-secondary">
          Login
        </Link>
        <Link to="/profile" className="hover:text-primary dark:hover:text-secondary">
          Profile
        </Link>
        <Link to="/public-trials" className="hover:text-primary dark:hover:text-secondary">
          Public Trials
        </Link>
        <Link to="/matched-trials" className="hover:text-primary dark:hover:text-secondary">
          Matched Trials
        </Link>
        <Link to="/bookmarks" className="hover:text-primary dark:hover:text-secondary">
          Bookmarks
        </Link>
        <Link to="/add-trial" className="hover:text-primary dark:hover:text-secondary">
          Add Trial
        </Link>
      </div>

      {/* Dark Mode Toggle */}
      <div className="ml-4">
        <ThemeToggle />
      </div>
    </nav>
  );
}

export default Navbar;

