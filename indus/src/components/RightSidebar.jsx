import React from "react";
import "./RightSidebar.css";

const tasks = [
  {
    title: "Automate Repetitive Order Processing",
    description: "Entering customer codes, finding parts, and setting pickup sites",
  },
  {
    title: "Customer Feedback Mechanism",
    description: "Gather insights on customer satisfaction",
  },
  {
    title: "Fill Monthly Order",
    description: "Approve routine queries and orders...",
  },
  {
    title: "Inventory and Alternative Parts Finder",
    description: "Locate parts and suggest alternatives when specific items are unavailable",
  },
];

const RightSidebar = () => (
  <div className="right-sidebar">
    <div className="section-title">SUGGESTED TASKS</div>
    <div className="task-list">
      {tasks.map((task, index) => (
        <div className="task-item" key={index}>
          <div className="task-title">{task.title}</div>
          <div className="task-description">{task.description}</div>
        </div>
      ))}
    </div>
  </div>
);

export default RightSidebar;