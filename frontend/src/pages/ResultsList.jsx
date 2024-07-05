import React, { useState, useEffect } from 'react';
import axios from 'axios';
import StudentDashboard from './StudentDashboard';

// This component needs to fetch and display data.
const ResultsList = () => {
  const [results, setResults] = useState([]);

  useEffect(() => {
    axios.get('/api/results')
      .then(response => {
        setResults(response.data);
      })
      .catch(error => {
        console.error('Error fetching results', error);
      });
  }, []);

  return (
    <>
      <div>
        <StudentDashboard />
      </div>

      <div className="mx-80 m-8  text-white fixed w-10/10 h-full  bg-gray-900 py-4">
        {/* <h2 className="text-3xl mb-4">Uploaded Results</h2> */}
        <table className="table-auto  ">
          <thead>
            <tr className=''>

              <th className="px-6 w-40 " style={{ border: 'solid black' }}>Student Name</th>
              <th className="px-6 w-40 " style={{ border: 'solid black' }}>Subject</th>
              <th className="py-2 px-6 w-40 " style={{ border: 'solid black' }}>Test1</th>
              <th className="py-2 px-6 w-40 " style={{ border: 'solid black' }}>Test2</th>
              <th className="py-2 px-6 w-40 " style={{ border: 'solid black' }}>Mid</th>
              <th className="py-2 px-6 w-40 bg-gray-900 " style={{ border: 'solid black' }}>Assignment</th>
              <th className=" py-2 px-6 w-40 " style={{ border: 'solid black' }}>Exercise book</th>
              <th className=" py-2 px-6 w-40 " style={{ border: 'solid black' }}>Final</th>
              <th className=" py-2 px-6 w-40 " style={{ border: 'solid black' }}>Total Score</th>
            </tr>
          </thead>
          <tbody>
            {results.map(result => (
              <tr key={result.id}>
                <td className="border px-4 py-2">{result.studentName}</td>
                <td className="border px-4 py-2">{result.subject}</td>
                <td className="border px-4 py-2">{result.score}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
};

export default ResultsList;
