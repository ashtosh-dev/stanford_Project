import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TopicSelector = ({ onTopicSelect }) => {
    const [topics, setTopics] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/api/topics')
            .then(response => {
                setTopics(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the topics!", error);
                if (error.response) {
                  // The request was made and the server responded with a status code
                  // that falls out of the range of 2xx
                  console.error(error.response.data);
                  console.error(error.response.status);
                  console.error(error.response.headers);
                } else if (error.request) {
                  // The request was made but no response was received
                  // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                  // http.ClientRequest in node.js
                  console.error(error.request);
                } else {
                  // Something happened in setting up the request that triggered an Error
                  console.error('Error', error.message);
                }
                console.error(error.config);
            });
    }, []);

    const handleTopicClick = (topicId) => {
        axios.post('http://127.0.0.1:5000/api/quiz', { topic_id: topicId }, { withCredentials: true })
            .then(() => {
                onTopicSelect(topicId);
            })
            .catch(error => {
                console.error("There was an error starting the quiz!", error);
            });
    };

    return (
        <div>
            <h2>Choose a Topic</h2>
            <ul>
                {topics.map(topic => (
                    <li key={topic.id} onClick={() => handleTopicClick(topic.id)}>
                        {topic.name}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TopicSelector;
