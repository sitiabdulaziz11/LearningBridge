import React, { useState, useEffect } from 'react';
import axios from 'axios';
import StudentDashboard from './StudentDashboard';

const ResultsList = () => {
  const [results, setResults] = useState([]);

  useEffect(() => {
    axios.get('/api/results')
      .then(response => {
        console.log('Fetched results:', response.data); // Debugging log
        if (response.data.length > 0) {
          const updatedResults = calculateTotalScoreAndRank(response.data);
          setResults(updatedResults);
        } else {
          console.log('No results found');
        }
      })
      .catch(error => {
        console.error('Error fetching results', error);
      });
  }, []);

  const handleScoreChange = (studentId, subject, scoreType, newScore) => {
    setResults(prevResults => {
      const updatedResults = prevResults.map(result => result.id === studentId ? {
        ...result,
        results: {
          ...result.results,
          [subject]: {
            ...result.results[subject], [scoreType]: newScore
          }
        }
      } : result);

      return calculateTotalScoreAndRank(updatedResults);
    });
  };

  const handleSaveChanges = (studentId) => {
    const updatedResult = results.find(result => result.id === studentId);
    axios.put(`/api/results/${studentId}`, updatedResult)
      .then(response => {
        console.log('Result updated successfully');
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

      <div className="mx-80 mt-2 text-white fixed w-1/2 h-full bg-gray-900 py-4">
        {results.length === 0 ? (
          <p className="text-center text-white">No results available</p>
        ) : (
          <table className="table-auto w-full">
            <thead>
              <tr>
                <th className="px-6 w-40" style={{ border: 'solid black' }}>Student Name</th>
                <th className="px-6 w-40" style={{ border: 'solid black' }}>Subject</th>
                <th className="py-2 px-6 w-40" style={{ border: 'solid black' }}>Test1</th>
                <th className="py-2 px-6 w-40" style={{ border: 'solid black' }}>Test2</th>
                <th className="py-2 px-6 w-40" style={{ border: 'solid black' }}>Mid Exam</th>
                <th className="py-2 px-6 w-40" style={{ border: 'solid black' }}>Assignment</th>
                <th className="py-2 px-6 w-40" style={{ border: 'solid black' }}>Exercise book</th>
                <th className="py-2 px-6 w-40" style={{ border: 'solid black' }}>Final Exam</th>
                <th className="py-2 px-6 w-40" style={{ border: 'solid black' }}>Total Score</th>
                <th className="py-2 px-6 w-40" style={{ border: 'solid black' }}>Rank</th>
                <th className="py-2 px-6 w-40" style={{ border: 'solid black' }}>Action</th>
              </tr>
            </thead>
            <tbody>
              {results.map(result => (
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
              ))}
            </tbody>
          </table>
        )}
      </div>
    </>
  );
};

const calculateTotalScoreAndRank = (results) => {
  // Calculate total scores
  const updatedResults = results.map(result => {
    let totalScore = 0;

    // Function to check if a value is a valid number
    const addScore = (score) => {
      if (!isNaN(score) && Number.isInteger(Number(score))) {
        totalScore += Number(score);
      } else {
        console.warn(`Invalid score: ${score} for student ${result.studentName}`);
      }
    };

    // Sum up relevant scores
    addScore(result.results.test1);
    addScore(result.results.test2);
    addScore(result.results.midExam);
    addScore(result.results.assignment);
    addScore(result.results.exerciseBook);
    addScore(result.results.finalExam);

    return {
      ...result,
      results: {
        ...result.results,
        totalScore: totalScore,
      },
    };
  });

  // Sort by totalScore in descending order
  const clonedResults = [...updatedResults];
  clonedResults.sort((a, b) => b.results.totalScore - a.results.totalScore);

  // Assign ranks
  let currentRank = 1;
  let lastScore = null;
  let lastRank = 1;

  clonedResults.forEach((result, index) => {
    if (lastScore === result.results.totalScore) {
      result.results.rank = lastRank;
    } else {
      result.results.rank = currentRank;
      lastRank = currentRank;
    }
    lastScore = result.results.totalScore;
    currentRank++;
  });

  // Update the original results with ranks
  return updatedResults.map(result => {
    const clonedResult = clonedResults.find(r => r.id === result.id);
    return {
      ...result,
      results: {
        ...result.results,
        rank: clonedResult.results.rank,
      },
    };
  });
};

export default ResultsList;
