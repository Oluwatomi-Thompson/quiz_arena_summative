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

```bash
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
├── .gitignore              # Specifies files and directories that Git should ignore
└── README.md               # This is a documentation file
```


---
## set up instructions 
follow these steps to get QuizArena running on your machine:


## install requirements 
1.python 3.8+ installed on your system
 
2. sqlite3

## installation
1. clone this repository  using  git clone https://github.com/Oluwatomi-Thompson/quiz_arena_summative.git

2. change the directory to QuizArena using cd quiz_arena_summative

3. initialize the database using python3 database.py

4. run the game using python3 main.py

5. follow the instructions on the screen to play the game.
  - you will be asked to enter a username and if it is new, a new account will be created.
  - from the main menu, you can chooe to play in single-player mode or in multiplayer mode.

  - to view the leaderboard choose option 3 in the main menu  3.view leaderboard. to see top players



