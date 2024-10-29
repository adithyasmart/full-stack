import React, { useEffect, useState } from 'react';
import axios from 'axios';

function DocumentList() {
    const [documents, setDocuments] = useState([]);

    useEffect(() => {
        const fetchDocuments = async () => {
            const response = await axios.get('http://localhost:8000/documents');
            setDocuments(response.data);
        };
        fetchDocuments();
    }, []);

    return (
        <ul>
            {documents.map(doc => (
                <li key={doc.id}>{doc.file_name}</li>
            ))}
        </ul>
    );
}

export default DocumentList;
