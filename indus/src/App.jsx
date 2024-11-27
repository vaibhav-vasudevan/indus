import React, { useState } from "react";
import LeftSidebar from "./components/LeftSidebar";
import MainContent from "./components/MainContent";
import RightSidebar from "./components/RightSidebar";
import SearchModal from "./components/SearchModal";
import "./App.css";

const App = () => {
  const [showSearchModal, setShowSearchModal] = useState(false);
  const [chatMessages, setChatMessages] = useState([
    { content: "Hello! How can I help you today?", isUser: false },
  ]);
  const demoSend = (msg) => {
    setChatMessages([...chatMessages, { content: msg, isUser: false }]);
  };
  const handleSendMessage = async (message) => {
    if (!message.trim()) return;

    // Add user message
    const newMessages = [...chatMessages, { content: message, isUser: true }];
    setChatMessages(newMessages);
    
    // Simulate API call
    try {
      const response = await fetch(`http://127.0.0.1:8000/${encodeURIComponent(message)}`);
      const data = await response.json();

      // Add tool plan and store final answer
      const toolPlanMessage = { content: data.tool_plan, isUser: false };
      setChatMessages((prev) => [...prev, toolPlanMessage]);
      
      // Attach final answer
      window.finalAnswer = data.final_answer;
    } catch (error) {
      console.error("Error:", error);
      setChatMessages((prev) => [
        ...prev,
        { content: "Sorry, there was an error processing your request.", isUser: false },
      ]);
    }
  };

  return (
    <div className="app-container">
      <LeftSidebar />
      <MainContent
        chatMessages={chatMessages}
        onSendMessage={handleSendMessage}
        onDemoSend={demoSend}
        onSearchClick={() => setShowSearchModal(true)}
      />
      
      {showSearchModal && (
        <SearchModal onClose={() => setShowSearchModal(false)} chatMessages={chatMessages} />
      )}
    </div>
  );
};

export default App;