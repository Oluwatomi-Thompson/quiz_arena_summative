from user import create_user, show_leaderboard, add_score
from quiz_app import run_quiz
from quiz_group import waiting_room, play_round
from database import init_db, load_questions
import sqlite3

DB_NAME = "quiz.db"

def main_menu():
    print("\n" + "=" * 40)
    print("***Welcome to QuizArena***".center(40))
    print("=" * 40)
    print("1. Start Single Player Quiz")
    print("2. Join Multiplayer Quiz Group")
    print("3. View Leaderboard")
    print("4. Exit")
    print("=" * 40)

def get_user_id(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def main():
    # Run this only once to initialize database & load questions.
    # Comment out after first run to preserve data!
    #init_db()
    #load_questions()

    while True:
        main_menu()
        choice = input("Enter your choice 1-4: ").strip()
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid input. Please choose a number between 1 and 4.")
            continue

        if choice == "1":
            username = create_user()
            user_id = get_user_id(username)
            print(f"\nStarting quiz for {username}...")
            score = run_quiz()
            if score is not None:
                add_score(user_id, score)
        elif choice == "2":
            print("🌐 Multiplayer Mode: Lobby starting...")
            session_id, players = waiting_room()
            play_round(session_id, players)
        elif choice == "3":
            show_leaderboard()
        elif choice == "4":
            print("Exiting game.....")
            break
        else:
            print("Invalid input. Choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
