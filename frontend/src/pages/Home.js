import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import PDFUpload from '../components/PDFUpload';
import './Home.css';

function Home() {
  const navigate = useNavigate();

  const handleUploadSuccess = (data) => {
    // Navigate to chat page with the uploaded document
    navigate(`/chat/${data.document_id}`);
  };

  return (
    <div className="home">
      <div className="hero">
        <h1>📚 Smart PDF Tutor</h1>
        <p>Learn smarter with AI-powered PDF analysis</p>
        <p className="subtitle">Upload a PDF and ask questions, get summaries, generate quizzes, and create flashcards.</p>
      </div>

      <PDFUpload onUploadSuccess={handleUploadSuccess} />

      <div className="features">
        <div className="feature-card">
          <h3>💬 Ask Questions</h3>
          <p>Get answers to your questions based on the PDF content</p>
        </div>
        <div className="feature-card">
          <h3>📝 Summarize</h3>
          <p>Generate automatic summaries of chapters or entire documents</p>
        </div>
        <div className="feature-card">
          <h3>❓ Quiz</h3>
          <p>Test your knowledge with AI-generated quiz questions</p>
        </div>
        <div className="feature-card">
          <h3>🎯 Flashcards</h3>
          <p>Create flashcards for efficient learning and memorization</p>
        </div>
      </div>
    </div>
  );
}

export default Home;
