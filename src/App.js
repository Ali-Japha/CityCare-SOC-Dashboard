import React from 'react';
import logData from './logs.json';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>CityCare Hospital - SOC Log Viewer</h1>
      <table border="1" cellPadding="10" style={{ margin: '0 auto', width: '80%', textAlign: 'left' }}>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Level</th>
            <th>Message</th>
          </tr>
        </thead>
        <tbody>
          {logData.map((log, index) => (
            <tr key={index}>
              <td>{log.Timestamp}</td>
              <td>{log.Level}</td>
              <td>{log.Message}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
