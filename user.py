import sqlite3
from database import DB_NAME 
import utils 

from database import DB_NAME  # Make sure this is defined in database.py as DB_NAME = "quiz.db"

def create_user():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    while True:
        username = input("Choose your username: ").strip()

        if not username:
            print("Username cannot be empty! Try again.")
            continue

        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print(f"Sorry, user {username} is taken. Try entering another name.")
        else:
            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            conn.commit()
            print(f"WELCOME, {username}! Account created.")
            conn.close()
            return username  # Return after successful creation

def show_leaderboard():
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
        if rank == 1: medal = "🥇 "
        elif rank == 2: medal = "🥈 "
        elif rank == 3: medal = "🥉 "
        
        formatted_score = f"{score:,}" if score >= 1000 else str(score)
        print(f"{medal}{rank}. {username}: {formatted_score} points")

    print("=" * 40)

def add_score(user_id, score):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scores (user_id, score) VALUES (?, ?)",
        (user_id, score)
    )
    conn.commit()
    conn.close()
    print(f"\n⭐ Score of {score} points saved to your account!")
    
# Test function for development
def test_user_functions():
    """Test user-related functions"""
    print("Testing user creation...")
    user_id, username = create_user()
    print(f"Created user: ID={user_id}, Username={username}")
    
    print("\nTesting score addition...")
    add_score(user_id, 1500)
    
    print("\nTesting leaderboard display...")
    show_leaderboard()

if __name__ == "__main__":
    test_user_functions()
