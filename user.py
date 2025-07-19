from splite3 import error 
from utils import validate_username 

def create_user(conn):
    cursor = conn.cursor()
    while True:
        username = input("Enter your nickname for the game:").strip()
        if not validate_username(username):
            continue
        