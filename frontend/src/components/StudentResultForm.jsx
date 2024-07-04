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
    <form  onSubmit={handleSubmit} className="m-20 pl-20 ">
      <div className="mb-11">
        <label className="p-2 block text-2xl text-zinc-300">Student Name:</label>
        <input className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded'
          type="text" 
          value={studentName} 
          onChange={(e) => setStudentName(e.target.value)} 
          required 
        />
      </div>
      <div className="mb-14">
        <label className="block text-white">Subject:</label>
        <input 
          type="text" 
          value={subject} 
          onChange={(e) => setSubject(e.target.value)} 
          required
           
        />
      </div>
      <div className="mb-14">
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
