"""
AI Interview Chatbot for Research Data Collection
Developed by Amartya Mishra
January 2026

A conversational AI system for conducting structured interviews
with database logging and session management.
"""

import os
import sqlite3
from datetime import datetime
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()  # auto-reads GOOGLE_API_KEY
#client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
#assert os.getenv("GOOGLE_API_KEY"), "GOOGLE_API_KEY not loaded"


# Initialize database for session logging
def init_database():
    conn = sqlite3.connect('interview_sessions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sessions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  session_id TEXT,
                  timestamp TEXT,
                  role TEXT,
                  message TEXT)''')
    conn.commit()
    return conn

def log_message(conn, session_id, role, message):
    """Log conversation to database for analysis"""
    c = conn.cursor()
    c.execute("INSERT INTO sessions (session_id, timestamp, role, message) VALUES (?, ?, ?, ?)",
              (session_id, datetime.now().isoformat(), role, message))
    conn.commit()

def chat(messages):
    try:
        # Build a single prompt from message history
        prompt = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]

            if role == "system":
                prompt += f"Instructions:\n{content}\n\n"
            elif role == "user":
                prompt += f"User: {content}\n"
            elif role == "assistant":
                prompt += f"Interviewer: {content}\n"

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=300,
            )
        )

        return response.text

    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "I'm having trouble connecting. Please try again."



def conduct_interview():
    """Main interview flow with structured data collection"""
    conn = init_database()
    session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Interview prompt designed for data collection
    SYSTEM = """You are an AI research interviewer collecting data about user experiences 
    with technology. Ask 3-5 focused questions about their daily tech usage, challenges, 
    and preferences. Be conversational but ensure you gather specific, actionable data."""
    
    history = [{"role": "system", "content": SYSTEM}]
    log_message(conn, session_id, "system", SYSTEM)
    
    print("=== AI Interview Chatbot ===")
    print("Type 'exit' to end the interview\n")
    
    # Start with an opening question
    opening = "Hi! I'd like to learn about your technology usage. What devices do you use most often in your daily life?"
    history.append({"role": "assistant", "content": opening})
    log_message(conn, session_id, "assistant", opening)
    print(f"Interviewer: {opening}\n")
    
    try:
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ("exit", "quit"):
                # Closing summary
                summary_prompt = "Based on this conversation, provide a brief 2-sentence summary of key findings."
                history.append({"role": "user", "content": summary_prompt})
                summary = chat(history)
                print(f"\n=== Interview Summary ===\n{summary}")
                log_message(conn, session_id, "summary", summary)
                break
            
            if not user_input:
                continue
                
            history.append({"role": "user", "content": user_input})
            log_message(conn, session_id, "user", user_input)
            
            reply = chat(history)
            history.append({"role": "assistant", "content": reply})
            log_message(conn, session_id, "assistant", reply)
            
            print(f"Interviewer: {reply}\n")
            
    except KeyboardInterrupt:
        print("\n\nInterview ended.")
    finally:
        conn.close()
        print(f"\nSession {session_id} saved to database.")

if __name__ == "__main__":
    conduct_interview()