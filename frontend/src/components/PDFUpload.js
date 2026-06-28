import React, { useState } from 'react';
import axios from 'axios';
import './PDFUpload.css';

function PDFUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile);
      setError(null);
    } else {
      setError('Please select a valid PDF file');
      setFile(null);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file first');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      onUploadSuccess(response.data);
      setFile(null);
    } catch (err) {
      setError(err.response?.data?.detail || 'Upload failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="pdf-upload">
      <h2>Upload PDF</h2>
      <div className="upload-area">
        <input
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          className="file-input"
          id="pdf-input"
        />
        <label htmlFor="pdf-input" className="upload-label">
          {file ? file.name : 'Click to select PDF or drag and drop'}
        </label>
      </div>
      
      {error && <p className="error-message">{error}</p>}
      
      <button
        onClick={handleUpload}
        disabled={!file || loading}
        className="upload-button"
      >
        {loading ? 'Uploading...' : 'Upload PDF'}
      </button>
    </div>
  );
}

export default PDFUpload;
