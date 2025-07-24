# quiz_app.py
# Terminal interface to play the quiz game

from database import get_topics, get_questions_by_topic


def run_quiz():
    print("🎮 Welcome to QuizArena!")
    print("📚 Choose a topic:\n")

    topics = get_topics()
    for i, (_, name) in enumerate(topics, start=1):
        print(f"{i}. {name}")

    try:
        choice = int(input("\nEnter topic number: "))
        topic_id = topics[choice - 1][0]
    except (ValueError, IndexError):
        print("❌ Invalid topic. Exiting.")
        return

    questions = get_questions_by_topic(topic_id)

    if not questions:
        print("⚠️ No questions available for this topic.")
        return

    score = 0

    for idx, q in enumerate(questions, start=1):
        print(f"\nQ{idx}: {q[0]}")
        print(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}")
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q[5].upper():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. Correct answer is {q[5]}")

    print(f"\n🏁 Quiz completed! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
