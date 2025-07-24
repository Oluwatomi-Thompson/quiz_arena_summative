import sqlite3
import random
import time

#Define variables
DB_FILE = "quiz.db"

#Fetches a random set of 8 questions from the database for the chosen topic
def generate_questions_by_topic(topic_id, num_questions=8):
    
    #Connect to SQLite database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT question, option_a, option_b, option_c, option_d, correct_option 
        FROM questions 
        WHERE topic_id = ?
    """, (topic_id,))
    
    all_questions = cursor.fetchall()
    conn.close()

    # Randomly pick up to num_questions
    return random.sample(all_questions, min(num_questions, len(all_questions)))

#Plays the quiz for a specific user and topic. Handles question display, timing, input, and scoring.
    
def play_quiz(topic_id, username):
    
    questions = generate_questions_by_topic(topic_id)
    score = 0

    print(f"\n🎮 {username}, your quiz is starting now!\n{'=' * 40}")

    for index, q in enumerate(questions, start=1):
        print(f"\nQ{index}: {q[0]}")
        print(f"A) {q[1]}")
        print(f"B) {q[2]}")
        print(f"C) {q[3]}")
        print(f"D) {q[4]}")

        start = time.time()
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        elapsed = time.time() - start

        correct = q[5].upper()
        bonus = 1 if elapsed <= 10 else 0

        if answer == correct:
            print("✅ Correct!", end=" ")
            score += 1 + bonus
            if bonus:
                print("(+1 speed bonus!)")
            else:
                print()
        else:
            print(f"❌ Incorrect. Correct answer was: {correct}")

    print(f"\n🏁 {username}, your total score is: {score}/{len(questions)*2} (includes speed bonuses)")
    return score