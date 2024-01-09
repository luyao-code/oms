import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from "react";

function App() {

  const [message, setMessage] = useState({})

  useEffect(() => {
    fetch('http://127.0.0.1:5000/info')
      .then(response => response.json())
      .then(data => setMessage(data))
      .catch(error => console.log(error))
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Response from Flask Server: {message.name}, {message.dev} 
        </p>
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
