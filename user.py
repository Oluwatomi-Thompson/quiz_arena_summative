import sqlite3

from database import DB_NAME
DB_name = "quiz.db"

def create_user():
    #create new user account 
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    while True:
        username = input(f"Choose your username: ").strip()

        if not username:
            print("Username can not be empty! Try again.")
            continue

        cursor.execute("SELECT  id  FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print(f"Sorry, user {username} is taken. Try entering another name.")
        else:
            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            
            conn.commit()
            print(f"WELCOME, {username}! Acount created.")
            break
        conn.close()
        return username
    


def show_leaderboard():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    #get top 10 players

    cursor.execute("""
        SELECT users.username, SUM(scores.score) AS total_score
        FROM scores
        JOIN users ON scores.user_id = users.id
        GROUP BY users.username
        ORDER BY total_score DESC
        LIMIT 10
        """)
           
    top_players = cursor.fetchall()
    conn.close


    #display leaderboard 
    print("\n" + "=" * 40)
    print("🏆 QUIZ ARENA LEADERBOARD 🏆".center(40))
    print("=" * 40)

    if not top_players:
        print("No scores yet! Be the first to play!")
        print("=" * 40)
        return
    
    for rank, (username, score) in enumerate(top_players, 1):
        # Add medal emojis for top 3
        medal = ""
        if rank == 1: medal = "🥇 "
        elif rank == 2: medal = "🥈 "
        elif rank == 3: medal = "🥉 "
        
        # Format score with commas for readability
        formatted_score = f"{score:,}" if score >= 1000 else str(score)
        print(f"{medal}{rank}. {username}: {formatted_score} points")
    
    print("=" * 40)

def add_score(user_id, score):
    """
    Add a score to the database for a user
    Args:
        user_id (int): ID of the user
        score (int): Score to add
    """
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
    


    