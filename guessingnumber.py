import random

# Initialize the range of random numbers and the number of lives
ra1, ra2 = 1, 5
lives = 3
guessingnumber = random.randint(ra1, ra2)

while lives > 0:
    numb = int(input("Enter a number: "))  # Move the input inside the loop to get new input each time

    if guessingnumber == numb:
        print("You got it!")
        break  # Exit the loop if the guess is correct
    elif guessingnumber < numb:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")

    lives -= 1  # Decrement the life count on a wrong guess
    print(f"You have {lives} lives remaining.")

if lives == 0:
    print("You've run out of lives! Better luck next time.")
    print(f"The correct number was {guessingnumber}.")
