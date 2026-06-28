import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './Chat.css';

function Chat() {
  const { documentId } = useParams();
  const [question, setQuestion] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Load PDF info and set initial message
    setMessages([
      {
        type: 'system',
        text: `Loaded document: ${documentId}. How can I help you learn today?`,
      },
    ]);
  }, [documentId]);

  const handleSendQuestion = async () => {
    if (!question.trim()) return;

    // Add user message
    setMessages([...messages, { type: 'user', text: question }]);
    setQuestion('');
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:8000/question', {
        question: question,
        document_id: documentId,
      });

      // Add AI response
      setMessages((prev) => [
        ...prev,
        { type: 'ai', text: response.data.answer },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { type: 'error', text: 'Failed to get answer. Please try again.' },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat">
      <div className="chat-container">
        <div className="chat-header">
          <h2>Chat about: {documentId}</h2>
          <p>Ask me anything about this document</p>
        </div>

        <div className="messages">
          {messages.map((msg, idx) => (
            <div key={idx} className={`message message-${msg.type}`}>
              <div className="message-content">{msg.text}</div>
            </div>
          ))}
          {loading && (
            <div className="message message-system">
              <div className="message-content">Thinking...</div>
            </div>
          )}
        </div>

        <div className="input-area">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendQuestion()}
            placeholder="Ask a question about the document..."
            disabled={loading}
            className="input-field"
          />
          <button
            onClick={handleSendQuestion}
            disabled={loading || !question.trim()}
            className="send-button"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default Chat;
