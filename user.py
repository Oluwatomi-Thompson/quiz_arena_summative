def create_user():
    print("Welcome to QuizArena")

    while True:
        username = input("enter your name for the game: ").strip()

        #check if empty
        if username == "":
            print("the name can not be empty. Please try again!")
            continue

        #check if username is already taken
        cursor = conn.execute("SELECT * FROM users WHERE username = ?", (username,))

        if cursor.fetchone() is not None:
            print(f"Sorry, {username} is taken. choose another name")
            else 
            #save to the database
            conn.execute("INSERT INTO users (username) values (?)", (username,))
            conn.commit()
            print(f"account created! Welcome {username}")
            break

    conn.close()
    

        