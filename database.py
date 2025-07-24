import sqlite3
import os

DB_NAME = "quiz.db"

def get_db_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    # Create tables if not exist (no DROP statements here))
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schema.sql")
    with open(schema_path, "r") as f:
        schema = f.read()

    conn = get_db_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print("Database schema created or already exists.")

def load_questions():
    # Load questions only if topics table is empty (to avoid duplicate loading)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM topics")
    count = cursor.fetchone()[0]
    if count == 0:
        questions_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions_data.sql")
        with open(questions_path, "r") as f:
            script = f.read()
        conn.executescript(script)
        conn.commit()
        print("Quiz questions loaded successfully.")
    else:
        print("Questions already loaded, skipping.")

    conn.close()

def get_topics():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM topics")
    topics = cursor.fetchall()
    conn.close()
    return topics

def get_questions_by_topic(topic_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT question, option_a, option_b, option_c, option_d, correct_option
        FROM questions
        WHERE topic_id = ?
    """, (topic_id,))
    questions = cursor.fetchall()
    conn.close()
    return questions

if __name__ == "__main__":
    init_db()
    load_questions()
