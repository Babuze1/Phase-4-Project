import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import logo from "../assets/images.png";
import "../styles/Navbar.css";

function Navbar() {
  const [nav, setNav] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  const changeBackground = () => {
    if (window.scrollY >= 50) {
      setNav(true);
    } else {
      setNav(false);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", changeBackground);

    return () => {
      window.removeEventListener("scroll", changeBackground);
    };
  }, []);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <nav className={nav ? "nav active" : "nav"}>
      <Link to="/home" className="logo">
        {" "}
        <img src={logo} alt="" />
      </Link>
      <input className="menu-btn" type="checkbox" id="menu-btn" />
      <label
        className={`menu-icon ${menuOpen ? "open" : ""}`}
        htmlFor="menu-btn"
        onClick={toggleMenu}>
        <span className="nav-icon"></span>
      </label>

      <li className={`menu ${menuOpen ? "open" : ""}`}>
        <ul>
          <Link to="/restaurantlist">Restaurants</Link>
        </ul>
        <ul>
          <Link to="/about">About</Link>
        </ul>
        <ul>
          <Link to="/contact">Contact</Link>
        </ul>
        <ul>
          <Link to="/">Logout</Link>
        </ul>
      </li>
    </nav>
  );
}

export default Navbar;
