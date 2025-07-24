# quiz_app.py
# Terminal interface to play the quiz game

from database import get_topics, get_questions_by_topic


def run_quiz():
    while True:
        print("🎮   Welcome to QuizArena!")
        print("📚   Choose a topic:\n")

        topics = get_topics()
        for i, (_, name) in enumerate(topics, start=1):
            print(f"{i}. {name}")

        # Loop until valid topic number entered
        while True:
            try:
                choice = int(input("\nEnter topic: "))
                if 1 <= choice <= len(topics):
                    topic_id = topics[choice - 1][0]
                    break
                else:
                    print("❌   Invalid topic number. Try Again.")
            except ValueError:
                print("❌   Invalid topic. Try Again.")

        questions = get_questions_by_topic(topic_id)

        if not questions:
            print("⚠️ No questions available for this topic.")
            # Ask if want to try another topic if none available
            again = input("\n🔁  Would you like to try another topic? (yes/no): ").strip().lower()
            if again in ("yes", "y"):
                continue
            else:
                print("👋   Thanks for playing QuizArena!")
                break

        score = 0

        for idx, q in enumerate(questions, start=1):
            print(f"\nQ{idx}: {q[0]}")
            print(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}")
            ans = input("Your answer (A/B/C/D): ").strip().upper()
            if ans == q[5].upper():
                print("✅   Correct!")
                score += 1
            else:
                print(f"❌   Incorrect. Correct answer is {q[5]}")

        print(f"\n🏁   Quiz completed! Your score: {score}/{len(questions)}")

        again = input("\n🔁  Would you like to try another topic? (yes/no): ").strip().lower()
        if again in ("yes", "y"):
            # If yes, loop continues to display topics again
            continue
        else:
            print("👋   Thanks for playing QuizArena!")
            break

if __name__ == "__main__":
    run_quiz()

