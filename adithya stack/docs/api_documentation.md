# API Documentation

## Base URL
`http://localhost:8000`

## Endpoints

### Upload Document
- **POST** `/upload`
- Request Body: 
  - Form data with file
- Response: 
  - `{ "message": "Document uploaded successfully", "url": "s3_url" }`

### Get User Documents
- **GET** `/documents`
- Response:
  - Array of document objects

### User Login
- **POST** `/login`
- Request Body:
  - `{ "username": "your_username", "password": "your_password" }`
- Response:
  - `{ "token": "generated_token" }`
