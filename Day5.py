# Number Guessing Game: Random number 1–50. User guesses with hints (too high/low). Count attempts.

# Import library 
import random

#The guess number
result = random.randrange(1, 51) 
print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 and 50.")

# First trial input from user
guess = int(input("Enter your guess: "))


# counts
count = 0

# The loop
if guess == result:
        print(f"✅ You did it! You guessed right in just 1 trial 👏🏽")
else:
    while guess != result:
        if guess < 0 or guess > 50:
            print(" ❌ The number is not in range! Please try between 1 and 50")
        elif guess < result:
            print("❌ Your input is LESSER than the guess!")
        else:
            print("❌ Your input is HIGHER than the guess!")
        guess = int(input("Try another guess: "))
        count += 1
    if guess == result:
        print(f"✅ You did it! You guessed right after {count+1} trials 👏🏽")


# End of program

