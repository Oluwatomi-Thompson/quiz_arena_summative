# quiz_group.py
# Multiplayer lobby + countdown + simple in-game presence check

import uuid
import time
import sqlite3

DB = "quiz.db"          # Use the same database file as the rest of the app
MIN_TO_KEEP_GOING = 1   # Minimum active players before aborting session

def can_join(name, players):
    """Check if a new player can join the lobby."""
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

def waiting_room(target=8, countdown=30):
    """
    Lobby phase: gather 'target' players then start countdown.
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

def _update_active(answers, active):
    """
    After each question, drop players who did not answer.
    Returns new active set (intersection of answered and active).
    """
    dropped = active - answers.keys()
    for p in dropped:
        print(f"{p} missed the question - disconnected")
    return active & answers.keys()

def play_round(session_id, players):
    """
    Demo round: 3 questions, 10-second answer window each.
    Replace with real question distribution as needed.
    """
    active = set(players)
    for q_num in range(1, 4):
        print(f"Question {q_num} | Active: {', '.join(sorted(active))}")
        answers = {}
        deadline = time.time() + 10
        while time.time() < deadline and len(answers) < len(active):
            try:
                raw = input("> ").strip()
                who, ans = raw.split(maxsplit=1)
                if who in active:
                    answers[who] = ans
            except ValueError:
                continue

        active = _update_active(answers, active)
        if len(active) <= MIN_TO_KEEP_GOING:
            print("Not enough players left. Aborting.")
            return
        print("Answers recorded")
    print("Session over. Survivors:", ", ".join(sorted(active)))

if __name__ == "__main__":
    sid, roster = waiting_room()
    play_round(sid, roster)
