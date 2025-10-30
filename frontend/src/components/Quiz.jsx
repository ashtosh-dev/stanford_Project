import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Quiz = () => {
    const [questionData, setQuestionData] = useState(null);
    const [selectedOption, setSelectedOption] = useState(null);
    const [result, setResult] = useState(null);
    const [score, setScore] = useState(0);
    const [gameOver, setGameOver] = useState(false);

    useEffect(() => {
        fetchQuestion();
    }, []);

    const fetchQuestion = () => {
        setResult(null);
        setSelectedOption(null);
        axios.get('http://127.0.0.1:5000/api/question', { withCredentials: true })
            .then(response => {
                if (response.data.message === "No more questions") {
                    setGameOver(true);
                    setScore(response.data.score);
                } else {
                    setQuestionData(response.data);
                }
            })
            .catch(error => {
                console.error("There was an error fetching the question!", error);
            });
    };

    const handleAnswerSubmit = () => {
        axios.post('http://127.0.0.1:5000/api/answer', { answer: selectedOption }, { withCredentials: true })
            .then(response => {
                setResult(response.data);
                setScore(response.data.score);
            })
            .catch(error => {
                console.error("There was an error submitting the answer!", error);
            });
    };

    if (gameOver) {
        return (
            <div>
                <h2>Quiz Over!</h2>
                <p>Your final score is: {score}</p>
            </div>
        );
    }

    if (!questionData) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h2>{questionData.question}</h2>
            <ul>
                {questionData.options.map((option, index) => (
                    <li key={index} onClick={() => setSelectedOption(option)}>
                        {option}
                    </li>
                ))}
            </ul>
            <button onClick={handleAnswerSubmit} disabled={!selectedOption}>Submit</button>
            {result && (
                <div>
                    <h3>{result.is_correct ? "Correct!" : "Incorrect"}</h3>
                    <p>Correct Answer: {result.correct_answer}</p>
                    <button onClick={fetchQuestion}>Next Question</button>
                </div>
            )}
            <p>Score: {score}</p>
        </div>
    );
};

export default Quiz;
