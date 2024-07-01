import random


def play_game():
    print("0 - ROCK")
    print("1 - PAPER")
    print("2 - SCISSORS")
    choices = ["ROCK", "PAPER", "SCISSORS"]

    while True:
        user_input = input("Enter your choice 0/1/2 or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            break

        user = int(user_input)
        if user in [0, 1, 2]:
            print(f"You chose {choices[user]}")
            computer = random.randint(0, 2)
            print(f"Computer chose {choices[computer]}")

            if user == computer:
                print("It's a draw!")
            elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
                print("You win!")
            else:
                print("You lose!")
        else:
            print("Invalid choice. Please choose 0, 1, or 2.")


play_game()