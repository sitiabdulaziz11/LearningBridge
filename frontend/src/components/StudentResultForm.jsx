import React, { useState, useEffect } from 'react';
import axios from 'axios';

// This function is used to handle the form submission.
//  It makes POST request to the backend API to save the result.
const StudentResultForm = ({ selectedResult, onSave }) => {
  const [studentName, setStudentName] = useState('');
  const [subject, setSubject] = useState('');
  const [score, setScore] = useState('');
  // const [message, setMessage] = useState('Result uploaded successfully');

  useEffect(() => {
    if (selectedResult) {
      setStudentName(selectedResult.studentName); // this maybe stud id
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
        // setMessage('Result uploaded successfully');
        setStudentName(''); // this part clears the form fields after saving it.
        setSubject('');
        setScore('');
      })
      .catch(error => {
        console.error('Error uploading result', error);
        setMessage('Error uploading result');
      });
  };

  return (
    <>
     {/* {message && <div className="mb-4 m-10 ml-60 pl-20 text-xl text-red-500">{message}</div>} */}
    <form  onSubmit={handleSubmit} className="m-10 ml-60 pl-20 ">
      <div className="mb-9">
        <label className="p-2 block text-2xl text-zinc-300">Student Name:</label>
        <input className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
          type="text" 
          value={studentName} 
          onChange={(e) => setStudentName(e.target.value)} 
          required 
        />
      </div>
      <div className="mb-9">
        <label className="p-2 block text-2xl text-zinc-300">Subject:</label>
        <input className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
          type="text" 
          value={subject} 
          onChange={(e) => setSubject(e.target.value)} 
          required
           
        />
      </div>
      <div className="mb-9">
        <label className="p-2 block text-2xl text-zinc-300">Score:</label>
        <input className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
          type="number" 
          value={score} 
          onChange={(e) => setScore(e.target.value)} 
          required
          
        />
      </div>
      <button className='text-3xl p-4 m-3 ml-10 w-100 hover:bg-pink-800 bg-green-800 rounded-2xl' type="submit">Save</button>
    </form>
    </>
  );
};

export default StudentResultForm;
