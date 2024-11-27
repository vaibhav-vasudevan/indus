import React, { useState } from "react";
import "./MainContent.css";

const MainContent = ({ chatMessages, onSendMessage, onDemoSend, onSearchClick }) => {
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (input.trim()) {
      onSendMessage(input);
      setInput("");
    }
  };


  return (
    <div className="main-content">
      <div className="main-header">
        <span className="header-title">New Chat</span>
        <div className="header-actions">
          <button className="header-button" onClick={onSearchClick}>
            <i className="fas fa-search"></i>
          </button>
          <button className="header-button">History</button>
        </div>
      </div>
      <div className="chat-area">
        {chatMessages.map((message, index) => (
          <div
            className={`message ${message.isUser ? "user-message" : "assistant-message"}`}
            key={index}
          >
            <div className="message-content">{message.content}</div>
          </div>
        ))}
      </div>
      <div className="input-area">
        <div className="input-container">
          <input
            type="text"
            className="message-input"
            placeholder="Message Indus..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                e.shiftKey ? onDemoSend("This is a demo message sent with shift+enter!") : handleSend();
                setInput("");
              }
              if (e.key === "7" && e.ctrlKey) {
                onDemoSend("This is a demo message sent with ctrl+7!");
                setInput("");
              }
              
            }}
          />
          <button className="send-button" onClick={handleSend}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default MainContent;