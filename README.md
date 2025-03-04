# ChatGPT-like Flask Web Application

## 📌 Overview
This is a ChatGPT-like web application built using the Flask framework. It allows users to interact with multiple AI models (ChatGPT, DeepSeek, Gemini) through a user-friendly interface. The app features a **dark mode theme**, supports **Enter key for sending messages**, includes a **chat history panel**, and allows users to **select AI models dynamically**.

## 🚀 Features
- **User Interface** similar to ChatGPT
- **Dark Mode** theme for a modern look
- **Text Input Box** with Enter key support
- **New Chat Button** to reset the conversation
- **Chat History Panel** to view past conversations
- **Model Selector Panel** for choosing AI models (ChatGPT, DeepSeek, Gemini)
- **Responsive Design** for desktop and mobile

---

## 🏗️ Project Structure
```
chatgpt-flask-app/
├── app.py                  # Main application file
├── config.py               # Configuration settings (loads .env variables)
├── .env                    # API keys and environment variables (ignored in Git)
├── requirements.txt        # Python dependencies
│
├── templates/              # HTML templates
│   ├── index.html          # Main chat UI
│
├── static/                 # CSS, JavaScript, and assets
│   ├── css/style.css       # Custom styling
│   ├── js/script.js        # Frontend logic
│
├── chat/                   # Modular chat handling
│   ├── routes.py           # Chat routes
│   ├── models.py           # AI models integration
│   ├── handlers.py         # API communication logic
│
└── .gitignore              # Ignore sensitive files like .env
```

---

## 🔧 Setup Instructions

### 1️⃣ Prerequisites
Make sure you have **Python 3.8+** and **pip** installed.

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/chatgpt-flask-app.git
cd chatgpt-flask-app
```

### 3️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 5️⃣ Set Up the `.env` File
Create a `.env` file in the project root and add:
```
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_openai_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 6️⃣ Run the Flask App
```sh
python app.py
```

The server will start at: **http://127.0.0.1:5000**

---

## 🛠️ API Integration
- **OpenAI API** for ChatGPT
- **DeepSeek API** for advanced AI responses
- **Gemini API** for Google’s AI capabilities

Modify `handlers.py` to configure API requests.

---

## 🎨 Frontend
- HTML (Jinja2 templates)
- CSS (Custom styling)
- JavaScript (AJAX for API calls)

---

## 🔥 Future Enhancements
- **User Authentication** (Sign-in & Sign-out)
- **Database Storage** for chat history
- **Improved UI Design** with animations
- **Real-time WebSockets** for smoother conversations

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 🤝 Contributing
Feel free to fork the repo, create a new branch, and submit a pull request!

Happy Coding! 🚀

