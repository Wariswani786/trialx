// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

import Home from "./pages/Home"; // ← Add this import
import Register from "./pages/Register";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import PublicTrials from "./pages/PublicTrials";
import MatchedTrials from "./pages/MatchedTrials";
import Bookmarks from "./pages/Bookmarks";
import AddTrial from "./pages/AddTrial";

function App() {
  return (
    <div className="min-h-screen bg-white text-gray-900 dark:bg-gray-900 dark:text-white transition-colors duration-300">
      <Router>
        <Navbar />
        <main className="px-4 py-8">
          <Routes>
            <Route path="/" element={<Home />} /> {/* ← Use Home here */}
            <Route path="/register" element={<Register />} />
            <Route path="/login" element={<Login />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/public-trials" element={<PublicTrials />} />
            <Route path="/matched-trials" element={<MatchedTrials />} />
            <Route path="/bookmarks" element={<Bookmarks />} />
            <Route path="/add-trial" element={<AddTrial />} />
          </Routes>
        </main>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
