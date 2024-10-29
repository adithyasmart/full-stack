import React, { useState } from 'react';
import axios from 'axios';

function QueryInput() {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState('');

    const handleQuery = async () => {
        const res = await axios.post('http://localhost:8000/query', { query });
        setResponse(res.data);
    };

    return (
        <div>
            <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
            <button onClick={handleQuery}>Ask</button>
            <div>{response}</div>
        </div>
    );
}

export default QueryInput;
