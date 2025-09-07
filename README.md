# 🌐 EzzyText – AI-Powered Text Evaluation Dashboard

EzzyText is a **professional web application** built with **Flask (Python)** and **modern frontend design** to evaluate text using AI.  
The system helps detect **fake names, fake news, and spam text**, providing users with **accuracy scores**, clear explanations, and an **interactive dashboard UI** similar to enterprise-grade software.

---

## ✨ Key Features

- 📝 **Smart Text Evaluation**  
  Analyze any text using AI and get structured results in seconds.

- 🕵️ **Fake News Detection**  
  Identify misinformation, rumors, or unverified content.

- 🚫 **Spam Likelihood Scoring**  
  Evaluate whether the text is spam or suspicious.

- 📊 **Accuracy & Reliability Scores**  
  Display evaluation results as percentages and interactive progress bars.

- 🎨 **Professional UI/UX**  
  Clean, modern dashboard with hover effects, animations, and responsive design.

- ⚡ **Lightweight & Fast**  
  Powered by Flask on the backend, and a single-page dashboard frontend.

---

## 📂 Project Structure

EzzyText/
│── index.html # Frontend (Dashboard UI)
│── evaluate_text.py # Backend Flask server (API + OpenAI integration)
│── .env # Environment variables (API key) – not uploaded
│── .env.example # Example environment file (shared in repo)
│── requirements.txt # Python dependencies
│── README.md # Documentation
│── .gitignore # Ignore sensitive files (e.g., .env, pycache)

yaml
Copy code

---

## 🛠️ Installation & Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/EzzyText.git
cd EzzyText
2. Create Environment Variables
Copy the .env.example file and rename it to .env:

bash
Copy code
cp .env.example .env
Edit .env and add your OpenAI API key:

ini
Copy code
OPENAI_API_KEY=your_api_key_here
⚠️ Important: Never share or upload your real .env file to GitHub.

3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Flask Application
bash
Copy code
python evaluate_text.py
The app will run locally at:

cpp
Copy code
http://127.0.0.1:5000/
📊 Example Workflow
Input:
pgsql
Copy code
Breaking news: Scientists found a way to live on Mars without oxygen!
Output (AI-generated JSON):
json
Copy code
{
  "fakeNews": 4,
  "SpamWord": 2,
  "explanation": "The text is exaggerated and not based on verified scientific facts. Spam indicators are low but fake news likelihood is high."
}
Dashboard View:
✅ Fake News Score: 80% risk

✅ Spam Score: 40% risk

✅ Explanation: Clear, short reasoning provided to the user.

🔒 Security & Privacy
API keys are stored in a .env file and never uploaded to GitHub.

.gitignore ensures sensitive files are excluded from commits.

The system is designed for local usage but can be deployed to cloud platforms like Heroku, Render, or AWS.

🌍 Deployment Options
Local Development: Run with Flask as shown above.

Production (Recommended): Use gunicorn or uvicorn with Nginx.

Cloud Deployment:

Heroku

Render

AWS EC2

Azure App Service

🤝 Contributing
Contributions are welcome!

Fork the project

Create a new feature branch

Submit a Pull Request

Please ensure your code follows best practices and is well-documented.

📸 Screenshots (Optional)
(You can add real screenshots here once you run the app)

Dashboard	Result View

📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it as long as proper credit is given.

🙌 Acknowledgments
Flask – lightweight backend framework

OpenAI API – powering the AI evaluation

TailwindCSS – modern CSS utility framework

Font Awesome – icons for UI polish

🚀 Future Improvements
Add user authentication & role management

Store evaluation history in a database (PostgreSQL or SQLite)

Export results as PDF/CSV reports

Add multi-language support (English, Arabic, etc.)

Deploy a public demo version online