def main():
    print("*** Welcome to QuizArena! ***")

    while True:

        #Login/Register for the game
        #Login/Register

        

        print(f"\nWelcome 'User's name, Get ready to play. ")

        #Starting Quiz
        

        #Show leaderboard
        print("\n *** Leaderboard ***")
        #Shows leaderboard

        #Replay the game/exit
        print("\nDo you want to play again(y/n)")
        replay_game = input("").strip().lower()

        if replay_game != "y":
            print("\nThanks for playing the game. See you later")
            break
        else:
            print("\nRestarting game...\n")


#Running the game
if __name__ == "__main__":
    main()
