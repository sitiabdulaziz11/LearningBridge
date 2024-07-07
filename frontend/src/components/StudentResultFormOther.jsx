import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StudentResultForm = ({ selectedResult, onSave }) => {
  const [formData, setFormData] = useState({
    id: '',
    studentName: '',
    subject: '',
    test1: '',
    test2: '',
    midExam: '',
    assignment: '',
    exerciseBook: '',
    finalExam: ''
  });

  const subjects = ['English', 'Math', 'Science', 'History', 'Geography'];
  const resultTypes = ['Test 1', 'Test 2', 'Mid Exam', 'Assignment', 'Exercise Book', 'Final Exam'];

  useEffect(() => {
    if (selectedResult) {
      setFormData({
        id: selectedResult.id,
        studentName: selectedResult.studentName,
        subject: selectedResult.subject,
        test1: selectedResult.test1,
        test2: selectedResult.test2,
        midExam: selectedResult.midExam,
        assignment: selectedResult.assignment,
        exerciseBook: selectedResult.exerciseBook,
        finalExam: selectedResult.finalExam
      });
    } else {
      setFormData({
        id: '',
        studentName: '',
        subject: '',
        test1: '',
        test2: '',
        midExam: '',
        assignment: '',
        exerciseBook: '',
        finalExam: ''
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

    axios.post('/api/results', formData)
      .then(response => {
        onSave(response.data);
        setFormData({
          id: '',
          studentName: '',
          subject: '',
          test1: '',
          test2: '',
          midExam: '',
          assignment: '',
          exerciseBook: '',
          finalExam: ''
        }); // clear form fields
      })
      .catch(error => {
        console.error('Error uploading result', error);
      });
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="m-10 bg-black ml-60 mr-80 pl-20">
        <div className="mb-8">
          <label className="p-2 block text-2xl text-zinc-300">ID Number:</label>
          <input
            className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
            type="text"
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
        {resultTypes.map((type, index) => (
          <div className="mb-8" key={index}>
            <label className="p-2 block text-2xl text-zinc-300">{type}:</label>
            <input
              className='w-1/3 p-2 text-3xl text-black bg-slate-400 border rounded-2xl'
              type="number"
              name={type.toLowerCase().replace(' ', '')}
              value={formData[type.toLowerCase().replace(' ', '')]}
              onChange={handleChange}
            />
          </div>
        ))}
        <button className='text-4xl mb-11 p-2 w-200 hover:bg-green-700 bg-purple-900 rounded-2xl' type="submit">Save</button>
      </form>
    </>
  );
};

export default StudentResultForm;
