import React from "react";
import { Link } from "react-router-dom";

function Welcome() {
  return (
    <div className="home container">
      <h1 className="heading">Your Opinion Matters</h1>
      <Link to="/signup" className="btn btn-primary btn-lg">
        Get Started
      </Link>
    </div>
  );
}

export default Welcome;
