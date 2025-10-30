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
