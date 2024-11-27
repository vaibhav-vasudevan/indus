import React, { useState } from "react";
import "./SearchModal.css";

const SearchModal = ({ onClose, chatMessages }) => {
  const [searchQuery, setSearchQuery] = useState("");
  const filteredMessages = chatMessages.filter((message) =>
    message.content.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="search-modal">
      <div className="search-modal-content">
        <span className="close-button" onClick={onClose}>
          &times;
        </span>
        <input
          type="text"
          className="search-input"
          placeholder="Search..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <div className="search-results">
          {filteredMessages.length > 0 ? (
            filteredMessages.map((message, index) => (
              <div className="search-result-item" key={index}>
                {message.content}
              </div>
            ))
          ) : (
            <p>No results found.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default SearchModal;