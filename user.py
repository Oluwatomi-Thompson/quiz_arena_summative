def create_user():
    print("Welcome to QuizArena")

    while True:
        username = input("enter your name for the game: ").strip()

        #check if empty
        if username == "":
            print("the name can not be empty. Please try again!")
            continue
            


        