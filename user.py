import sqlite3
from database import get_db_connection 
import utils 


DB_NAME = "quiz.db"

def create_user(preferred_username=None):
    """
    Create a new user account.
    If preferred_username is given, tries to create with that username first.
    Returns the created username.
    """
    conn = sqlite3.connect(DB_NAME)

from database import get_db_connection
import utils

def create_user():
    conn = get_db_connection()  # Use the function imported from database.py
    cursor = conn.cursor()

    while True:
        if preferred_username:
            username = preferred_username
            preferred_username = None  # use only once
        else:
            username = input("Choose your username: ").strip()

        if not username:
            print("Username cannot be empty! Try again.")
            continue

        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print(f"Sorry, user '{username}' is taken. Try another name.")
            continue
        else:
            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            conn.commit()
            print(f"WELCOME, {username}! Account created.")
            conn.close()
            return username

def show_leaderboard():
    """
    Display the top 10 players by total score.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT users.username, SUM(scores.score) AS total_score
        FROM scores
        JOIN users ON scores.user_id = users.id
        GROUP BY users.username
        ORDER BY total_score DESC
        LIMIT 10
    """)

    top_players = cursor.fetchall()
    conn.close()

    print("\n" + "=" * 40)
    print("🏆 QUIZ ARENA LEADERBOARD 🏆".center(40))
    print("=" * 40)

    if not top_players:
        print("No scores yet! Be the first to play!")
        print("=" * 40)
        return

    for rank, (username, score) in enumerate(top_players, 1):
        medal = ""
        if rank == 1:
            medal = "🥇 "
        elif rank == 2:
            medal = "🥈 "
        elif rank == 3:
            medal = "🥉 "
        formatted_score = f"{score:,}" if score >= 1000 else str(score)
        print(f"{medal}{rank}. {username}: {formatted_score} points")

    print("=" * 40)

def add_score(user_id, score):
    """
    Add a score to the database for a user.
    Args:
        user_id (int): ID of the user.
        score (int): Score to add.
    """
    if score is None:
        print("No score to add.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scores (user_id, score) VALUES (?, ?)",
        (user_id, score)
    )
    conn.commit()
    conn.close()
    print(f"\n⭐ Score of {score} points saved to your account!")

# Optional test function for development
if __name__ == "__main__":
    print("Testing user creation...")
    username = create_user()
    print(f"Created user: {username}")

    print("\nTesting leaderboard display...")
    show_leaderboard()
