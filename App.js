import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [type, setType] = useState('');
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const handleRequest = (numberType) => {
    setError(null);
    axios.get(http://localhost:9876/numbers/${numberType})
      .then(res => {
        setResponse(res.data);
      })
      .catch(err => {
        setError('Failed to fetch numbers. Please try again.');
        console.error(err);
      });
  };

  return (
    <div className="App">
      <h1>Average Calculator</h1>
      
      <div className="buttons">
        <button onClick={() => handleRequest('p')}>Prime Numbers</button>
        <button onClick={() => handleRequest('fibo')}>Fibonacci Numbers</button>
        <button onClick={() => handleRequest('e')}>Even Numbers</button>
        <button onClick={() => handleRequest('r')}>Random Numbers</button>
      </div>

      {error && <p className="error">{error}</p>}

      {response && (
        <div className="response">
          <h3>Previous Window State:</h3>
          <p>{response.windowPrevState.join(', ')}</p>

          <h3>Numbers Fetched:</h3>
          <p>{response.numbers.join(', ')}</p>

          <h3>Current Window State:</h3>
          <p>{response.windowCurrState.join(', ')}</p>

          <h3>Average:</h3>
          <p>{response.avg}</p>
        </div>
      )}
    </div>
  );
}

export default App;