# Import library 
import random

#The guess number
result = random.randrange(1, 51) 
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")

# First trial input from user
guess = int(input("Enter your guess: "))

# counts the number of trials
count = 1

# The loop to check the guess
while guess != result:
    if guess < 0 or guess > 50:
        print(" ❌ The number is not in range! Please try between 1 and 50 only.")
    elif guess < result:
        print("❌ Your input is LESSER than the guess!")
    else:
        print("❌ Your input is HIGHER than the guess!")
    guess = int(input("Try another guess: "))
    count += 1
    if guess == result:
        print(f"✅ Yes, you did it! You guessed right after {count} trials 👏🏽")