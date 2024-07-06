import React from 'react';

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
export default calculateTotalScoreAndRank;