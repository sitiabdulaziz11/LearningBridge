import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import StudentDashboard from './StudentDashboard';

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

  // to make the result editable or Function to handle score changes
  const handleScoreChange = (studentId, subject, scoreType, newScore) => {
    setResults(prevResults => prevResults.map(result => result.id === studentId ? {
      ...result,
      results: {
        ...result.results,
        [subject]: {
          ...result.results[subject], [scoreType]: newScore
        }
      }
    }
      : result
    )
    );
  };

  const handleSaveChanges = (studentId) => {
    const updatedResult = results.find(result => result.id === studentId);
    axios.put(`/api/results/${studentId}`, updatedResult)
      .then(response => {
        console.log('Result updated successfully');
        // console.log(response.data);
      })
      .catch(error => {
        console.error('Error updating result', error);
      });
  };


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
                <th className="py-2 px-6 w-40 " style={{ border: 'solid black' }}>Mid Exam</th>
                <th className="py-2 px-6 w-40 " style={{ border: 'solid black' }}>Assignment</th>
                <th className=" py-2 px-6 w-40 " style={{ border: 'solid black' }}>Exercise book</th>
                <th className=" py-2 px-6 w-40 " style={{ border: 'solid black' }}>Final Exam</th>
                <th className=" py-2 px-6 w-40 " style={{ border: 'solid black' }}>Total Score</th>
                <th className=" py-2 px-6 w-40 " style={{ border: 'solid black' }}>Rank</th>
              </tr>
            </thead>
            <tbody>
              {results.map(result =>
                Object.keys(result.results).map(subject => (
                  <tr key={`${result.id}-${subject}`}>
                    <td className="border px-4 py-2">{result.studentName}</td>
                    <td className="border px-4 py-2">{subject}</td>
                    <td className="border px-4 py-2">
                      <input
                        type="number"
                        value={result.results[subject].test1}
                        onChange={(e) => handleScoreChange(result.id, subject, 'test1', e.target.value)}
                        className="bg-gray-800 text-white px-2 py-1"
                      />
                    </td>
                    <td className="border px-4 py-2">
                      <input
                        type="number"
                        value={result.results[subject].test2}
                        onChange={(e) => handleScoreChange(result.id, subject, 'test2', e.target.value)}
                        className="bg-gray-800 text-white px-2 py-1"
                      />
                    </td>
                    <td className="border px-4 py-2">
                      <input
                        type="number"
                        value={result.results[subject].midExam}
                        onChange={(e) => handleScoreChange(result.id, subject, 'midExam', e.target.value)}
                        className="bg-gray-800 text-white px-2 py-1"
                      />
                    </td>
                    <td className="border px-4 py-2">
                      <input
                        type="number"
                        value={result.results[subject].assignment}
                        onChange={(e) => handleScoreChange(result.id, subject, 'assignment', e.target.value)}
                        className="bg-gray-800 text-white px-2 py-1"
                      />
                    </td>
                    <td className="border px-4 py-2">
                      <input
                        type="number"
                        value={result.results[subject].exerciseBook}
                        onChange={(e) => handleScoreChange(result.id, subject, 'exerciseBook', e.target.value)}
                        className="bg-gray-800 text-white px-2 py-1"
                      />
                    </td>
                    <td className="border px-4 py-2">
                      <input
                        type="number"
                        value={result.results[subject].finalExam}
                        onChange={(e) => handleScoreChange(result.id, subject, 'finalExam', e.target.value)}
                        className="bg-gray-800 text-white px-2 py-1"
                      />
                    </td>
                    <td className="border px-4 py-2">{result.results[subject].totalScore}</td>
                    <td className="border px-4 py-2">{result.results[subject].rank}</td>

                    <td className="border px-4 py-2">
                      <button
                        onClick={() => handleSaveChanges(result.id)}
                        className="bg-blue-500 text-white px-4 py-2 rounded"
                      >
                        Save
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </>
    );
  };
  
  export default ResultsList;

  
  // Function to calculate totalScore and rank
  const calculateTotalScoreAndRank = () => {
    const updatedResults = results.map(result => {
      let totalScore = 0;
      // Sum up relevant scores
      totalScore += parseInt(result.results.test1 || 0, 10);
      totalScore += parseInt(result.results.test2 || 0, 10);
      totalScore += parseInt(result.results.midExam || 0, 10);
      totalScore += parseInt(result.results.assignment || 0, 10);
      totalScore += parseInt(result.results.exerciseBook || 0, 10);
      totalScore += parseInt(result.results.finalExam || 0, 10);
      // Add more scores as needed for your calculation

      // Calculate rank
      const clonedResults = [...results];

      // Sort clonedResults by totalScore in descending order
      clonedResults.sort((a, b) => b.results.totalScore - a.results.totalScore);

      // Initialize rank counter
      let rank = 1;
      let previousScore = null;
      let rankIncrement = 1;

      // Iterate through sorted results to assign ranks
      const updatedResults = clonedResults.map((result, index) => {
        // Compare current score with previous score
        if (previousScore !== null && result.results.totalScore !== previousScore) {
          rank += rankIncrement;
          rankIncrement = 1;
        } else {
          rankIncrement++;
        }

        previousScore = result.results.totalScore;


        return {
          ...result,
          results: {
            ...result.results,
            totalScore,
            rank
          }
        };
      });

      // Update state with the updated results including totalScore and rank
      setResults(updatedResults);
      
    });
  };