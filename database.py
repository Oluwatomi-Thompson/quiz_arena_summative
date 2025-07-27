import os
import sqlite3
DB_NAME = "quiz.db"

# Function to get a connection to the database

def get_db_connection():
    return sqlite3.connect("quiz.db")


# Function to initialize the database schema
def init_db():
    # Create tables if not exist (no DROP statements here!)
    schema_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "schema.sql")
    with open(schema_path, "r") as f:
        schema = f.read()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()



print("Database schema created successfully.")


# Function to load quiz questions if not already loaded
def load_questions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM topics")
    count = cursor.fetchone()[0]

    if count == 0:
        questions_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "questions_data.sql")
        with open(questions_path, "r") as f:
            script = f.read()
        cursor.executescript(script)
        conn.commit()
        print("Quiz questions loaded successfully.")
    else:
        print("Questions already loaded, skipping.")

    conn.close()



# Function to get all quiz topics
def get_topics():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM topics")
    topics = cursor.fetchall()
    conn.close()
    return topics



# Function to get questions based on topic ID

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


# Main block to initialize and load data
if __name__ == "__main__":
    init_db()
    load_questions()

