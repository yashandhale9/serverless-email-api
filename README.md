# Serverless Email API (Python + Serverless Offline)

This project is a simple REST API built using the **Serverless Framework** with **Python runtime**, which sends emails based on user input.  
It runs completely offline (no AWS account required) using the `serverless-offline` plugin.

---

## 🚀 Features
- Accepts JSON input containing:
  - `receiver_email`
  - `subject`
  - `body_text`
- Sends email via Gmail SMTP server.
- Proper error handling with HTTP status codes.
- Runs locally using **Serverless Offline**.

---

## 🧩 Project Structure

---

## ⚙️ Setup Instructions

### 1️⃣ Clone or create project folder
```
mkdir serverless-email-api
cd serverless-email-api
```

---

### 2️⃣ Create and activate virtual environment
```
python -m venv venv
.\venv\Scripts\Activate.ps1     # (For PowerShell)
```
---

### 3️⃣ Install Python dependencies
```
pip install python-dotenv
```
---

### 4️⃣ Initialize npm and install Serverless
```
npm init -y
npm install -g serverless
npm install --save-dev serverless-offline
```
---

### 5️⃣ Create .env file
```
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
```
⚠️ Generate your App Password in Google Account → Security → App Passwords.

---

### 💻 Running the API

Start the local server:
```
serverless offline
```

It will show:
```
POST | http://localhost:3000/dev/send-email
```
---

### 📬 Testing via Postman

Use **POST** request to:
```
http://localhost:3000/dev/send-email
```
**Headers:**
```
    Key	                Value
Content-Type	     application/json
```
**Body (raw JSON):**
```
{
  "receiver_email": "test@example.com",
  "subject": "Hello from Serverless API",
  "body_text": "This is a test email sent using my serverless offline setup!"
}
```

**Example Success Response:**
```
{
  "message": "Email sent successfully!"
}
```
---

### 🧠 **Error Handling**

Returns 500 for internal errors (e.g., invalid credentials)

Returns 200 when email sent successfully

Displays readable error messages in JSON format

---

### 🧾 **Requirements**

Node.js and npm

Python 3.x

Gmail account with App Password enabled

---
### **Screenshots:**
<img width="500" height="250" alt="Screenshot (231)" src="https://github.com/user-attachments/assets/c557cf0e-8a44-4062-bc2e-91710af5ff21" />
<img width="500" height="250" alt="Screenshot (232)" src="https://github.com/user-attachments/assets/a80f4a2b-1c32-4d1b-a453-0d480ac2e0bd" />


---
### 🏁 **Author**

Yash Gorakshnath Andhale

Passionate about Python, Machine Learning, and Backend Development.

---
