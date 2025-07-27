# Multiplayer lobby + countdown + simple in-game presence check
import uuid
import time
import sqlite3
from database import get_questions_by_topic, get_topics
from user import add_score, get_user_id

DB = "quiz.db"  # Use the correct DB filename used by your app
# MIN_TO_KEEP_GOING = 1  # Minimum active players before aborting session


def can_join(name, players):
    """
    Check if a new player can join the lobby
    Requirements: non-empty alphanumeric, exists in users table, not already present
    """
    if len(name) < 3 or not name.isalnum():
        print("Invalid username.")
        return False
    with sqlite3.connect(DB) as conn:
        cur = conn.execute("SELECT 1 FROM users WHERE username = ?", (name,))
        if not cur.fetchone():
            print("Username not registered. Create it in main menu first.")
            return False
    if name in players:
        print("Already in lobby.")
        return False
    return True
# Lobby phase: gather exactly 'target' players then start countdown
# Returns (session_id, list_of_players) once countdown finishes


def waiting_room(target=5, countdown=30):
    """
    Lobby phase: gather exactly 'target' players then start countdown.
    Returns (session_id, list_of_players) once countdown finishes.
    """
    players = set()
    print("Quiz Arena Lobby")
    print(f"Waiting for {target} players...")

    while len(players) < target:
        name = input("Enter username: ").strip()
        if can_join(name, players):
            players.add(name)
            print(f"{len(players)} / {target} joined: {', '.join(sorted(players))}")

    print("All players ready. Countdown begins...")

    for sec in range(countdown, 0, -1):
        print(f"{sec}s remaining")
        time.sleep(1)
    print("Lobby locked. Game starts")
    session_id = str(uuid.uuid4())[:8]
    return session_id, list(players)


def update_active(answers, active):
    """
    After each question, drop players who did not answer.
    Returns new active set (intersection of answered and active).
    """
    dropped = active - answers.keys()
    for p in dropped:
        print(f"{p} missed the question - disconnected")
    return active & answers.keys()

# this is without the timer for class demo purposes


def play_round(session_id, players):
    print(f"\n🎮 Starting Multiplayer Quiz | Session ID: {session_id}")

    # Choose Topic
    print("\n📚 Available Topics:")
    topics = get_topics()
    for idx, (_, name) in enumerate(topics, 1):
        print(f"{idx}. {name}")

    while True:
        try:
            choice = int(input("\nEnter topic number for this session: "))
            if 1 <= choice <= len(topics):
                topic_id = topics[choice - 1][0]
                break
            else:
                print("❌ Invalid number. Try again.")
        except ValueError:
            print("❌ Enter a number.")

    questions = get_questions_by_topic(topic_id)
    if not questions:
        print("⚠️ No questions found for this topic.")
        return

    print(
        f"\n🧠 Quiz begins! {len(players)} players, {min(5, len(questions))} questions total.")

    # nitialize player scores
    scores = {player: 0 for player in players}

    # Loop over questions
    for q_index, q in enumerate(questions[:5], start=1):
        print("\n" + "=" * 40)
        print(f"Q{q_index}: {q[0]}")
        print(f"A) {q[1]}")
        print(f"B) {q[2]}")
        print(f"C) {q[3]}")
        print(f"D) {q[4]}")
        correct = q[5].upper()

        # Collect all player answers first
        answers = {}
        for player in players:
            while True:
                answer = input(
                    f"{player}'s answer (A/B/C/D): ").strip().upper()
                if answer in {"A", "B", "C", "D"}:
                    answers[player] = answer
                    break
                print("❌ Invalid input. Please enter A, B, C, or D.")

        # After all players have answered, show results
        print(f"\n✅ Correct answer: {correct}")
        for player, answer in answers.items():
            if answer == correct:
                scores[player] += 1
                print(f"✅ {player} was correct!")
            else:
                print(f"❌ {player} chose {answer} — incorrect.")

    # Final Leaderboard
    print("\n🏁 Quiz Over! Final Scores:")
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for rank, (player, score) in enumerate(ranked, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else ""
        print(f"{medal} {rank}. {player} — {score} points")

        # Save score to database
        user_id = get_user_id(player)
        if user_id:
            add_score(user_id, score)
        else:
            print(f"[WARN] Could not find user ID for {player}")

    print("=" * 40)
    print("🎉 Thanks for playing the multiplayer round!")

# this is including the timer
# def play_round(session_id, players):
#     print(f"\n🎮 Starting Multiplayer Quiz | Session: {session_id}")

#     # Choose topic for group
#     print("\n📚 Available Topics:")
#     topics = get_topics()
#     for idx, (_, name) in enumerate(topics, 1):
#         print(f"{idx}. {name}")

#     while True:
#         try:
#             topic_choice = int(input("\nEnter topic number for the quiz: "))
#             if 1 <= topic_choice <= len(topics):
#                 topic_id = topics[topic_choice - 1][0]
#                 break
#             else:
#                 print("❌ Invalid topic number.")
#         except ValueError:
#             print("❌ Please enter a valid number.")

#     questions = get_questions_by_topic(topic_id)
#     if not questions:
#         print("⚠️ No questions for this topic.")
#         return

#     num_questions = min(5, len(questions))
#     print(f"\n🧠 Quiz will include {num_questions} questions. Answer format: username answer")

#     active = set(players)
#     scores = {player: 0 for player in players}

#     for q_index in range(num_questions):
#         q = questions[q_index]
#         print(f"\nQ{q_index+1}: {q[0]}")
#         print(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}")
#         correct = q[5].upper()

#         answers = {}
#         deadline = time.time() + 15
#         print("⏳ You have 15 seconds. Answer format: username answer (e.g., alice B)")

#         while time.time() < deadline and len(answers) < len(active):
#             try:
#                 raw = input("> ").strip()
#                 who, ans = raw.split(maxsplit=1)
#                 if who in active and ans.upper() in {"A", "B", "C", "D"}:
#                     answers[who] = ans.upper()
#             except ValueError:
#                 continue

#         # Eliminate players who didn't answer
#         missed = active - answers.keys()
#         for p in missed:
#             print(f"❌ {p} missed the question and has been removed.")
#         active = active & answers.keys()

#         for player, answer in answers.items():
#             if answer == correct:
#                 scores[player] += 1
#                 print(f"✅ {player}: Correct!")
#             else:
#                 print(f"❌ {player}: Wrong. Correct answer: {correct}")


#         if len(active) <= 1:
#             print("⚠️ Not enough players left. Ending session.")
#             break

#     # Final Results
#     print("\n🏁 Session Complete! Final Scores:")
#     ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
#     for rank, (player, score) in enumerate(ranked, 1):
#         medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else ""
#         print(f"{medal} {rank}. {player} — {score} points")

#         # Save score to DB
#         user_id = get_user_id(player)
#         if user_id:
#             add_score(user_id, score)
#         else:
#             print(f"[WARN] Could not find DB ID for {player}")

# Run lobby + demo round when file is executed directly
if __name__ == "__main__":
    try:
        sid, roster = waiting_room()
        play_round(sid, roster)
    except KeyboardInterrupt:
        print("\nExiting gracefully.")
