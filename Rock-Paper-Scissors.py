while True:
    print("1. play")
    print("2. quit")

    user_choice = input("enter your choice: ")

    if user_choice == '2':
        print("Okay, let's play again!")
        break

    if user_choice == '1':
        user_move = input("rock, paper, scissors? ").lower()

        import random
        computer_move = random.choice(["rock", "paper", "scissors"])

        if user_move == computer_move:
            print("It's a tie!")
        elif (user_move == 'rock' and computer_move == 'scissors') or \
            (user_move == 'scissors' and computer_move == 'paper') or \
            (user_move == 'paper' and computer_move == 'rock'):
            print("you win!")
        else:
            print("you lose!")
