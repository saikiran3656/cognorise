import random


def roll_dice(sides, rolls):
    results = [random.randint(1, sides) for _ in range(rolls)]
    return results


def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice (e.g., 6 for a standard dice): "))
            rolls = int(input("Enter the number of rolls: "))

            if sides <= 0 or rolls <= 0:
                print("Please enter positive integers for both the number of sides and rolls.")
                continue

            results = roll_dice(sides, rolls)
            print(f"Results of rolling a {sides}-sided dice {rolls} times: {results}")

            again = input("Do you want to roll again? (yes/no): ").strip().lower()
            if again == 'no':
                print("Thanks for using the Dice Rolling Simulator! Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter valid integers for the number of sides and rolls.")


if __name__ == "__main__":
    main()
