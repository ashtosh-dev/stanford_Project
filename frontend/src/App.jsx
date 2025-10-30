import React, { useState } from 'react';
import './App.css';
import TopicSelector from './components/TopicSelector';
import Quiz from './components/Quiz';

function App() {
    const [selectedTopic, setSelectedTopic] = useState(null);

    return (
        <div className="App">
            <header className="App-header">
                <h1>Quiz App</h1>
            </header>
            <main>
                {selectedTopic ? (
                    <Quiz topicId={selectedTopic} />
                ) : (
                    <TopicSelector onTopicSelect={setSelectedTopic} />
                )}
            </main>
        </div>
    );
}

export default App;
