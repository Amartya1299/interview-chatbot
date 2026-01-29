# AI Interview Chatbot for Research Data Collection

A conversational AI prototype for conducting structured interviews and collecting user data using Google's Gemini API with persistent database logging.

## 🎯 Project Overview

This chatbot demonstrates:
- LLM-powered conversational interview workflows
- SQLite database integration for session logging
- Prompt engineering for structured data collection
- Error handling and graceful API failure recovery
- Basic analytics and data export capabilities

## 🛠️ Tech Stack

- **Python 3.x**
- **Google gemini-2.0-flash API**
- **SQLite3** for data persistence
- **Pandas** for data analysis
- **python-dotenv** for environment management

## 📋 Prerequisites

- Python 3.8 or higher
- GOOGLE API key ([Get one here](https://aistudio.google.com/api-keys))
- pip package manager

## 🚀 Installation

1. **Clone the repository**
```bash
   git clone https://github.com/Amartya1299/interview-chatbot.git
   cd interview-chatbot
```

2. **Create virtual environment (recommended)**
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
```
   GOOGLE_API_KEY=your_google_api_key_here
```

## 💻 Usage

### Running Interviews
```bash
python Chatbot.py
```

The chatbot will:
1. Present an opening question about technology usage
2. Engage in a 3-5 question conversational interview
3. Log all messages to SQLite database with timestamps
4. Generate an automatic summary when you type `exit`

### Analyzing Data
```bash
python analytics.py
```

This will:
- Display session statistics
- Show message breakdowns by role
- Export all data to CSV for further analysis

## 📊 Database Schema

**Table: `sessions`**

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Auto-incrementing primary key |
| session_id | TEXT | Unique identifier for each interview |
| timestamp | TEXT | ISO format timestamp |
| role | TEXT | Message role (system/user/assistant/summary) |
| message | TEXT | Content of the message |

## 🎨 Features

- ✅ Conversational AI using Google gemini-2.0-flash
- ✅ Session-based logging with unique identifiers
- ✅ Timestamp tracking for temporal analysis
- ✅ Automated interview summarization
- ✅ Error handling for API failures
- ✅ Data export to CSV
- ✅ Basic analytics dashboard

## 🔒 Security Notes

- API keys are stored in `.env` file (not tracked in git)
- Uses parameterized SQL queries to prevent injection
- `.gitignore` configured to exclude sensitive data

## 🚧 Future Enhancements

- [ ] Add FastAPI wrapper for web access
- [ ] Implement consent flow before data collection
- [ ] Add data validation schemas
- [ ] Integrate vector database for semantic search
- [ ] Build visualization dashboard (Plotly/Streamlit)
- [ ] Add unit tests with pytest
- [ ] Support multiple LLM providers (Anthropic, Cohere)
- [ ] Implement conversation branching logic

## 📝 Project Structure
```
interview-chatbot/
├── Chatbot.py    # Main chatbot application
├── analytics.py     # Analytics module
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in git)
├── .gitignore             # Git ignore rules
├── README.md              # This file
└── interview_sessions.db  # SQLite database (created on first run)
```

## 🤝 Contributing

This is a learning project, but suggestions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests with improvements
- Share feedback on the implementation

## 📄 License

MIT License - feel free to use this project for learning or research purposes.

## 👤 Author

**Amartya Mishra**
- GitHub: [@yourusername](https://github.com/Amartya1299)
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/amartya-mishra-b7a447230/)
- Email: mishra.amartya5@gmail.com

## 🙏 Acknowledgments

- Built as part of Master's program at Purdue University Northwest
- Inspired by research assistant position in AI-assisted interviewing
- Uses Google's gemini-2.0-flash for conversational intelligence

---

**Note:** This project is for educational and research purposes. When conducting real interviews, always obtain proper consent and follow ethical guidelines for data collection.
```

---

### **Step 11: Create .env.example**

Create `.env.example`:
```
GOOGLE_API_KEY=your_google_api_key_here