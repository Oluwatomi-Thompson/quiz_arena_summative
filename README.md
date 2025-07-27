## QuizArena - Multiplayer Educational Game

QuizArena is a terminal-based multiplayer quiz game built in Python. Designed for educational use and classroom demonstrations, it allows users to test their knowledge across various topics like Software Engineering, Healthcare, and Entrepreneurship Leadership. Players can compete solo or in groups, with scores tracked and displayed on a leaderboard.

---
## Features 

- Single-Player Mode: Choose a topic and answer quiz questions to test your knowledge.
- Multiplayer Mode: Join a quiz lobby with friends and compete in real-time.
- Leaderboard: Top scores are tracked and displayed. 
- Speed bonuses (single-player mode): Earn extra points for fast answers.
- Topic-based questions: Questions are organised by category for targeted learning.
- Persistent database: Uses SQLite to store users, scores, questions, and topics.

---
## File Structure 

QuizArena/

│
├── main.py                 # Main entry point and menu UI
├── user.py                 # Handles user creation, scoring, leaderboard
├── quiz_app.py             # Handles single-player quizzes
├── quiz_group.py           # Multiplayer session logic
├── questions.py            # Randomized question generation
├── database.py             # Database setup, schema loading, question loading
├── utils.py                # Helper functions (validation, formatting, etc.)
├── schema.sql              # Database table definitions
├── questions_data.sql      # Bulk insert SQL for topics and questions
├── quiz.db                 # SQLite database file (generated after first run)
└── README.md               # This file