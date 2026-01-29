"""
Analytics module for interview chatbot
Generates basic statistics and exports data
"""

import sqlite3
import pandas as pd
from datetime import datetime

def analyze_interviews():
    """Generate basic analytics from interview sessions"""
    try:
        conn = sqlite3.connect('interview_sessions.db')
        
        # Load all sessions
        df = pd.read_sql_query("SELECT * FROM sessions", conn)
        
        if df.empty:
            print("No interview data found. Run some interviews first!")
            conn.close()
            return
        
        print("=" * 50)
        print("INTERVIEW ANALYTICS")
        print("=" * 50)
        
        # Basic statistics
        total_sessions = df['session_id'].nunique()
        total_messages = len(df)
        avg_messages = total_messages / total_sessions
        
        print(f"\n📊 Overview:")
        print(f"   Total interview sessions: {total_sessions}")
        print(f"   Total messages: {total_messages}")
        print(f"   Average messages per session: {avg_messages:.1f}")
        
        # Message breakdown by role
        print(f"\n💬 Message Breakdown:")
        role_counts = df['role'].value_counts()
        for role, count in role_counts.items():
            print(f"   {role}: {count}")
        
        # Session details
        print(f"\n📅 Session Details:")
        for session_id in df['session_id'].unique():
            session_data = df[df['session_id'] == session_id]
            message_count = len(session_data)
            # Get first timestamp for this session
            first_timestamp = session_data.iloc[0]['timestamp']
            print(f"   {session_id}: {message_count} messages (Started: {first_timestamp})")
        
        # Export to CSV
        export_file = f'interview_data_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        df.to_csv(export_file, index=False)
        print(f"\n✅ Data exported to: {export_file}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_interviews()