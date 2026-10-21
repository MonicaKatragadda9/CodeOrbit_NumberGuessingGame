
# CodeOrbit Tech - Number Guessing Game
# The computer chooses a random number, and the user tries to guess it.

import random

# Function to play one round of the game
def play_game():

    # Choose a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Count the number of guesses
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess the number!")

    # Repeat until the user guesses correctly
    while True:
        try:
            # Get the user's guess
            guess = int(input("\nEnter your guess: "))

            # Count this attempt
            attempts += 1

            # Check whether the guess is valid
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")

            # Tell the user if the guess is too low
            elif guess < secret_number:
                print("Too low! Try again.")

            # Tell the user if the guess is too high
            elif guess > secret_number:
                print("Too high! Try again.")

            # The guess is correct
            else:
                print("Congratulations! You guessed the number!")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            # Handle input that is not a whole number
            print("Invalid input! Please enter a whole number.")

# Allow the user to play multiple rounds
while True:
    play_game()

    # Ask whether the user wants another round
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for playing!")
        break
