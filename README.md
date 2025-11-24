# 📘 Flask Trivia Quiz Web App

A simple, interactive **Flask-based trivia quiz application** that lets users:

- View trivia questions  
- Add new questions  
- Remove existing questions  
- Use REST API endpoints  
- Navigate a multi-page UI built with Flask templates  

---

## 🚀 Features

### ✅ Web Application
- Home page showing all questions  
- View an individual question  
- Add new quiz questions  
- Delete existing questions  
- JSON-based lightweight storage  
- Jinja2-powered templates  

### 🔌 REST API Endpoints
| Endpoint | Description |
|---------|-------------|
| `/api/questions` | Returns all questions as JSON |
| `/api/questions/<index>` | Returns a specific question |

---

## 🧩 Project Structure

```text
Flask-Trivia-Quiz-web-app/
│
├── static/
│   ├── quiz.png
│   ├── bird.png
│   ├── welcome.css
│
├── templates/
│   ├── home.html
│   ├── quiz.html
│   ├── add_question.html
│   ├── remove_question.html
│
├── model.py
├── questions.json
├── quiz.py                # Main Flask application
└── venv/                  # Virtual environment
```

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/anjpraj/Flask-Trivia-Quiz-web-app.git
cd Flask-Trivia-Quiz-web-app
```
### 2️⃣ Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```
### 3️⃣ Install dependencies
```bash
pip install flask
```

### ▶️ Running the Application
```bash
python quiz.py
```

### Then open your browser and go to:
```bash
http://127.0.0.1:5000/
```
