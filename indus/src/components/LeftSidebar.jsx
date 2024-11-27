import React from "react";
import "./LeftSidebar.css";

const LeftSidebar = () => (
  <div className="left-sidebar">
    <div className="brand">
      <div className="brand-icon">
        <i className="fas fa-cube"></i>
      </div>
      <span className="brand-name">Indus</span>
    </div>
    <div className="nav-item active">
      <i className="fas fa-message"></i>
      Chat
    </div>
    <div className="nav-item">
      <i className="fas fa-gear"></i>
      Settings
    </div>
    <div className="nav-item">
      <i className="fas fa-circle-info"></i>
      Help
    </div>
  </div>
);

export default LeftSidebar;