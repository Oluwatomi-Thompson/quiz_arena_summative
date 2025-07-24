# quiz_group.py
# Multiplayer lobby + countdown + simple in-game presence check
# Author: Becky – Day 4-5 task
# Purpose: Collect 8 players, run 30-second countdown, launch quiz rounds
# Dependencies: uuid, time, sqlite3 (built-in), utils.validate_username (teammate helper)

import uuid
import time
import sqlite3

DB = "quizarena.db"          # SQLite database file shared by whole team
MIN_TO_KEEP_GOING = 1        # Minimum active players before aborting session

# Check if a new player can join the lobby
# Requirements: non-empty alphanumeric, exists in users table, not already present


def can_join(name, players):
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


def waiting_room(target=8, countdown=30):
    players = set()
    print("Quiz Arena Lobby")
    print(f"Waiting for {target} players...")

    while len(players) < target:git 
     name = input("Enter username: ").strip()
        if can_join(name, players):
            players.add(name)
<<<<<<< HEAD

    print(f"{len(players)} / {target} joined: {', '.join(sorted(players))}")

    print("All players ready. Countdown begins...")
=======
            print(f"{len(players)} / {target} joined: {', '.join(sorted(players))}")
 print("All players ready. Countdown begins...")
>>>>>>> 1b4d717e56f1bbbad8c9e2249a0cd6224a2f3cf5

    for sec in range(countdown, 0, -1):
        print(f"{sec}s remaining")
        time.sleep(1)
    print("Lobby locked. Game starts")
    session_id = str(uuid.uuid4())[:8]
    return session_id, list(players)

# After each question, drop players who did not answer
# Returns new active set (intersection of answered and active)


def _update_active(answers, active):
    dropped = active - answers.keys()
    for p in dropped:
        print(f"{p} missed the question - disconnected")
    return active & answers.keys()

# Demo round: 3 questions, 10-second answer window each
# Replace this with real question distribution later


def play_round(session_id, players):
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


# Run lobby + demo round when file is executed directly
if __name__ == "__main__":
    sid, roster = waiting_room()
    play_round(sid, roster)
