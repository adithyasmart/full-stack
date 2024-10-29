import React from 'react';
import FileUpload from './components/FileUpload';
import DocumentList from './components/DocumentList';
import QueryInput from './components/QueryInput';
import Navbar from './components/Navbar';
import './App.css';

function App() {
    return (
        <div className="App">
            <Navbar />
            <FileUpload />
            <DocumentList />
            <QueryInput />
        </div>
    );
}

export default App;
