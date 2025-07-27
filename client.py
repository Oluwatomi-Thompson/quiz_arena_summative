import socket

SERVER_HOST = '127.0.0.1'  # Change to your server's IP address if running remotely
SERVER_PORT = 65432

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_HOST, SERVER_PORT))
    except ConnectionRefusedError:
        print("Unable to connect to the server. Make sure the server is running.")
        return

    try:
        while True:
            message = client.recv(4096).decode()
            if not message:
                print("\nConnection closed by server.")
                break

            print(message, end="")  # Print server message without extra newline

            # When server asks for an answer, read input and send back
            if "Your answer:" in message:
                answer = input()
                client.sendall(answer.strip().encode())

    except KeyboardInterrupt:
        print("\nDisconnected from server.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
