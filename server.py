import socket
import threading
from database import get_questions_by_topic, save_score

HOST = '0.0.0.0'
PORT = 65432

clients = []
lock = threading.Lock()

def broadcast(message):
    with lock:
        for client in clients:
            try:
                client.sendall(message.encode())
            except:
                clients.remove(client)

def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")
    conn.sendall("Waiting for other players...\n".encode())

    # Wait for minimum 2 players
    while True:
        with lock:
            if len(clients) >= 2:
                break

    conn.sendall("Game starting!\n".encode())

    # Load questions from DB (topic_id 1 for example)
    questions = get_questions_by_topic(1)
    score = 0

    for q in questions:
        question_text = f"\nQ: {q[0]}\nA) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nYour answer: "
        conn.sendall(question_text.encode())

        try:
            answer = conn.recv(1024).decode().strip().upper()
        except:
            break

        if answer == q[5]:
            conn.sendall("Correct!\n".encode())
            score += 1
        else:
            conn.sendall(f"Wrong! Correct answer was {q[5]}\n".encode())

    # For demo, use addr[1] as user_id or generate user_id properly
    user_id = addr[1]  # Simplification for example only
    save_score(user_id, score)

    conn.sendall(f"Game over. Your score: {score}\nThanks for playing!\n".encode())
    conn.close()

    with lock:
        clients.remove(conn)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        with lock:
            clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()

