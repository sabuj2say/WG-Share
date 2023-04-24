import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src="C:\Users\MdJahangirAlam\Documents\GitHub\WG-Share\wg-frontend\img\logo.png"
          width="300"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
        <hr />
        <h5>
          <i>presents</i>
        </h5>
        <h1>WG-SHARE App with React + Django</h1>
      </div>
    );
  }
}

export default Header;