import React, { useState, useRef, useEffect } from 'react';
import './App.css';

// Chat Configuration - Easy to customize
const CHAT_CONFIG = {
  avatar: "https://ui-avatars.com/api/?name=Beata&background=0f8fff&color=fff&rounded=true&size=44",
  title: "AI Assistant Chat",
  status: "Available 24/7!"
};

function App() {
  const [messages, setMessages] = useState([
    { text: "Hello! I'm your AI assistant. How can I help you today? 😊", isUser: false }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [showEmojiPicker, setShowEmojiPicker] = useState(false);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const emojis = [
    '😊', '😂', '❤️', '👍', '🎉', '🔥', '💯', '✨',
    '😍', '🤔', '😎', '🥳', '😭', '🤣', '😅', '😇',
    '😋', '😴', '🤗', '😌', '😏', '😒', '😔', '😞',
    '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩'
  ];

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const addEmoji = (emoji) => {
    setInputValue(prev => prev + emoji);
    setShowEmojiPicker(false);
    inputRef.current?.focus();
  };

  const handleSubmit = async (e) => {
    if (e) e.preventDefault();
    if (!inputValue.trim()) return;

    const userMessage = { text: inputValue, isUser: true };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsTyping(true);

    try {
      const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: inputValue }),
      });
      const data = await response.json();
      setTimeout(() => {
        setMessages(prev => [...prev, { text: data.response, isUser: false }]);
        setIsTyping(false);
      }, 1000);
    } catch (error) {
      setTimeout(() => {
        setMessages(prev => [...prev, {
          text: "I'm here to help! (Fallback response: your backend is not running)",
          isUser: false
        }]);
        setIsTyping(false);
      }, 1000);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="chat-widget">
      <div className="chat-header">
        <img src={CHAT_CONFIG.avatar} alt="Avatar" className="avatar" />
        <div>
          <div className="chat-title">{CHAT_CONFIG.title}</div>
          <div className="chat-status">{CHAT_CONFIG.status}</div>
        </div>
      </div>
      <div className="chat-body">
        {messages.map((message, index) => (
          <div key={index} className={`message-row ${message.isUser ? 'user' : 'bot'}`}>
            {!message.isUser && (
              <div className="avatar bot-avatar">🤖</div>
            )}
            <div className={`message-bubble ${message.isUser ? 'user' : 'bot'}`}>{message.text}</div>
            {message.isUser && (
              <div className="avatar user-avatar">👤</div>
            )}
          </div>
        ))}
        {isTyping && (
          <div className="message-row bot">
            <div className="avatar bot-avatar">🤖</div>
            <div className="message-bubble bot">
              <span className="typing-indicator">Typing...</span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={handleSubmit} className="chat-input-area">
        <button
          type="button"
          className="emoji-trigger"
          onClick={() => setShowEmojiPicker(!showEmojiPicker)}
        >
          😊
        </button>
        <input
          ref={inputRef}
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          className="chat-input"
          placeholder="Enter your message..."
          maxLength={500}
        />
        {showEmojiPicker && (
          <div className="emoji-picker">
            {emojis.map((emoji, index) => (
              <button
                key={index}
                type="button"
                className="emoji-btn"
                onClick={() => addEmoji(emoji)}
              >
                {emoji}
              </button>
            ))}
          </div>
        )}
        <button
          type="submit"
          className="send-btn"
          disabled={!inputValue.trim()}
        >
          <span className="send-icon">➤</span>
        </button>
      </form>
    </div>
  );
}

export default App;
