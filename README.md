# Fluentian Task One Backend

**Base URL:** `https://fluentian-task-one-backend.onrender.com/`

A **FastAPI backend** for managing user authentication, account management, and verification workflows for the Fluentian platform.

---

## Features

- User Registration & Login
- Password hashing using **bcrypt** (truncated to 72 bytes)
- Email-based code verification
- JWT-based authentication
- User account retrieval (`/me`)
- Account deletion (`/delete-account`)

---

## Endpoints

### 1. Login

**POST** `/login`

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "YourPassword123"
}

Response:

{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
2. Send Verification Code

POST /send-code

Request Body:

{
  "email": "user@example.com"
}

Response:

{
  "message": "Verification code sent"
}
3. Verify Code

POST /verify

Request Body:

{
  "email": "user@example.com",
  "code": "123456"
}

Response:

{
  "message": "User verified successfully"
}
4. Get Current User

GET /me

Headers:

Authorization: Bearer <jwt_token>

Response:

{
  "id": 1,
  "email": "user@example.com",
  "is_active": true
}
5. Delete Account

DELETE /delete-account

Headers:

Authorization: Bearer <jwt_token>

Response:

{
  "message": "Account deleted successfully"
}
Installation & Setup
Clone the repo:
git clone https://github.com/your-username/fluentian-task-one-backend.git
cd fluentian-task-one-backend
Create virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run the server locally:
uvicorn app.main:app --reload
Technologies
Python 3.12
FastAPI
Passlib + bcrypt for secure password hashing
Pydantic for request/response validation
Uvicorn ASGI server
Hosted on Render: https://fluentian-task-one-backend.onrender.com/
Notes
Passwords are truncated to 72 bytes before hashing due to bcrypt limitations.
JWT authentication is required for /me and /delete-account.
Use /send-code and /verify for email verification workflows.
```
