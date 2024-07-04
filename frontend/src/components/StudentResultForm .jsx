import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StudentResultForm = ({ selectedResult, onSave }) => {
  const [studentName, setStudentName] = useState('');
  const [subject, setSubject] = useState('');
  const [score, setScore] = useState('');

  useEffect(() => {
    if (selectedResult) {
      setStudentName(selectedResult.studentName);
      setSubject(selectedResult.subject);
      setScore(selectedResult.score);
    } else {
      setStudentName('');
      setSubject('');
      setScore('');
    }
  }, [selectedResult]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const result = { studentName, subject, score };
    
    axios.post('/api/results', result)
      .then(response => {
        onSave(response.data);
        setStudentName(''); // this part clears the form fields after saving it.
        setSubject('');
        setScore('');
      })
      .catch(error => {
        console.error('Error uploading result', error);
      });
  };

  return (
    <>
    <form  onSubmit={handleSubmit} className="bg-green-500 py-7 p-4 rounded-lg">
      <div className="mb-4">
        <label className="block text-black">Student Name:</label>
        <input
          type="text" 
          value={studentName} 
          onChange={(e) => setStudentName(e.target.value)} 
          required 
        />
      </div>
      <div className="mb-4">
        <label className="block text-white">Subject:</label>
        <input 
          type="text" 
          value={subject} 
          onChange={(e) => setSubject(e.target.value)} 
          required
           
        />
      </div>
      <div className="mb-4">
        <label className="block text-white">Score:</label>
        <input 
          type="number" 
          value={score} 
          onChange={(e) => setScore(e.target.value)} 
          required
          
        />
      </div>
      <button type="submit">Save</button>
    </form>
    </>
  );
};

export default StudentResultForm;
