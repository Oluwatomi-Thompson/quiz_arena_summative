import sqlite3

DB_name = "quiz.db"


def init_db():
    # Connect to the database
    conn = sqlite3.connect(DB_NAME)
    with open("schema.sql", "r") as f:
        script = f.read()
        conn.executescript(script)
    conn.commit()
    conn.close()
    print("Database schema created successfully.")

def load_questions():
    conn = sqlite3.connect(DB_NAME)
    with open("questions_data.sql", "r") as f:
        script = f.read()
        conn.executescript(script)
    conn.commit()
    conn.close()
    print("Quiz questions loaded successfully.")

def get_topics():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM topics")
    topics = cursor.fetchall()
    conn.close()
    return topics

def get_questions_by_topic(topic_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT question, option_a, option_b, option_c, option_d, correct_option
        FROM questions
        WHERE topic_id = ?
    """, (topic_id,))
    questions = cursor.fetchall()
    conn.close()
    return questions

# Run database setup when the script is executed directly
if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    load_questions()
    print("Database initialized successfully.")
