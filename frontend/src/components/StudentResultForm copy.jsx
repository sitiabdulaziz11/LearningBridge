import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StudentResultForm = ({ selectedResult, onSave }) => {
  const [formData, setFormData] = useState({
    id: '',
    studentName: '',
    subject: '',
    resultType: '',
    resultValue: ''
  });

  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const subjects = ['English', 'Math', 'Science', 'History', 'Geography'];
  const resultTypes = ['Test 1', 'Test 2', 'Mid Exam', 'Assignment', 'Exercise Book', 'Final Exam'];

  useEffect(() => {
    if (selectedResult) {
      setFormData({
        id: selectedResult.id,
        studentName: selectedResult.studentName,
        subject: selectedResult.subject,
        resultType: '',
        resultValue: ''
      });
    } else {
      setFormData({
        id: '',
        studentName: '',
        subject: '',
        resultType: '',
        resultValue: ''
      });
    }
  }, [selectedResult]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const dataToSend = {
      ...formData,
      [formData.resultType.toLowerCase().replace(' ', '')]: formData.resultValue
    };

    axios.post('/api/v1/results', dataToSend)
      .then(response => {
        setSuccessMessage('Result uploaded successfully');
        onSave(response.data);
        setFormData({
          id: '',
          studentName: '',
          subject: '',
          resultType: '',
          resultValue: ''
        }); // clear form fields
      })
      .catch(error => {
        console.error('Error uploading result', error);
        setErrorMessage('Error uploading result');
      });
  };

  return (
    <>
    {successMessage && <div className="mb-4 m-10 ml-60 pl-20 text-xl text-green-500">{successMessage}</div>}
    {errorMessage && <div className="mb-4 m-10 ml-60 pl-20 text-xl text-red-500">{errorMessage}</div>}
      <form onSubmit={handleSubmit} className="m-10 bg-black ml-60 mr-80 pl-20">
        <div className="mb-8">
          <label className="p-2 block text-2xl text-zinc-300">ID Number:</label>
          <input
            className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
            type="number"
            name="id"
            value={formData.id}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-8">
          <label className="p-2 block text-2xl text-zinc-300">Student Name:</label>
          <input
            className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
            type="text"
            name="studentName"
            value={formData.studentName}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-8">
          <label className="p-2 block text-2xl text-zinc-300">Subject:</label>
          <select
            className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
            name="subject"
            value={formData.subject}
            onChange={handleChange}
            required
          >
            <option value="">Select Subject</option>
            {subjects.map((subject, index) => (
              <option key={index} value={subject}>{subject}</option>
            ))}
          </select>
        </div>
        <div className="mb-8">
          <label className="p-2 block text-2xl text-zinc-300">Result Type:</label>
          <select
            className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
            name="resultType"
            value={formData.resultType}
            onChange={handleChange}
            required
          >
            <option value="">Select Result Type</option>
            {resultTypes.map((resultType, index) => (
              <option key={index} value={resultType}>{resultType}</option>
            ))}
          </select>
        </div>
        <div className="mb-8">
          <label className="p-2 block text-2xl text-zinc-300">Value:</label>
          <input
            className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
            type="number"
            name="resultValue"
            value={formData.resultValue}
            onChange={handleChange}
            required
          />
        </div>
        <button className='text-4xl mb-11 p-2 w-40 hover:bg-green-700 bg-purple-900 rounded-2xl' type="submit">Save</button>
      </form>
    </>
  );
};

export default StudentResultForm;
