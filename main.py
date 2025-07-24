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

def prompt_for_username():
    while True:
        username = input("Enter your username (or create a new one): ").strip()
        if not username:
            print("Username cannot be empty. Please try again.")
            continue

        user_id = get_user_id(username)
        if user_id:
            print(f"Welcome back, {username}!")
            return username, user_id
        else:
            print(f"Username '{username}' not found.")
            create_new = input("Would you like to create a new account with this username? (yes/no): ").strip().lower()
            if create_new in ('yes', 'y'):
                username_created = create_user(username)
                if username_created:
                    user_id = get_user_id(username_created)
                    return username_created, user_id
            else:
                print("Let's try again.")

def main():
    # Uncomment for first run only
    # init_db()
    # load_questions()

    username, user_id = prompt_for_username()

    while True:
        main_menu()
        choice = input("Enter your choice 1-4: ").strip()
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid input. Please choose a number between 1 and 4.")
            continue

        if choice == "1":
            print(f"\nStarting single-player quiz for {username}...")
            score = run_quiz()
            if score is not None:
                add_score(user_id, score)

        elif choice == "2":
            print(f"🌐 Multiplayer Mode: Lobby starting for {username}...")
            session_id, players = waiting_room()
            # Make sure the current user is in the lobby or prompt them to join
            if username not in players:
                print(f"Note: Your username '{username}' is not in the multiplayer lobby players list.")
            play_round(session_id, players)

        elif choice == "3":
            show_leaderboard()

        elif choice == "4":
            print("Exiting game.....")
            break

if __name__ == "__main__":
    main()
