# Chatbot Project

A modern, full-stack chatbot application featuring:
- **Flask backend** for conversational logic
- **Node.js bridge** for seamless API communication
- **React frontend** with a floating, stylish chat widget UI

## Features

- Friendly, customizable AI chat with memory and fun responses
- Modern floating chat widget with gradient header, avatar, and online status
- Real-time communication between frontend and backend via a Node.js bridge

---

## Project Structure

```
chatbot/
│
├── backend/      # Flask backend (Python)
│   └── app.py
│
├── bridge/       # Node.js bridge server
│   └── index.js
│
├── frontend/     # React frontend (chat widget UI)
│   └── src/
│
├── start_all.ps1         # PowerShell script to start all services
├── start_backend.ps1     # PowerShell script to start backend
├── start_frontend.ps1    # PowerShell script to start frontend
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.x (for backend)
- Node.js & npm (for bridge and frontend)
- PowerShell (for provided startup scripts, or use terminal equivalents)

---

### 1. Backend (Flask)

**Setup:**
```sh
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install flask flask-cors
```

**Run:**
```sh
python app.py
```
The backend will start on `http://localhost:5000`.

---

### 2. Bridge (Node.js)

**Setup:**
```sh
cd bridge
npm install
```

**Run:**
```sh
node index.js
```
The bridge will start on `http://localhost:3001` and forward chat messages to the Flask backend.

---

### 3. Frontend (React)

**Setup:**
```sh
cd frontend
npm install
```

**Run:**
```sh
npm start
```
The frontend will start on `http://localhost:3000` and connect to the bridge.

---

### 4. All-in-One Startup

You can use the provided PowerShell script from the project root to start all services:
```sh
./start_all.ps1
```

---

## Output

Below is a screenshot of the modern floating chat widget UI in action:

![Chatbot UI Screenshot](screenshot.png)

- The chat widget features a gradient header, avatar, chat title, online status, and a stylish input area.
- The UI is centered, rectangular with slightly rounded corners, and fully responsive.
- Example conversation is shown in the screenshot above.

---

## Customization

- **Chat header, avatar, and status** can be easily customized in the React frontend (`App.js`).
- Backend logic and responses are in `backend/app.py`.

---

## Deployment

- Deploy backend and bridge to your preferred server (ensure CORS and ports are configured).
- Build the React frontend for production with `npm run build` and serve with any static server.

---
