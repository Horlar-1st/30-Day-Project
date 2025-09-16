# Number Guess Redux: Improve your guessing game with error handling and a play-again option

# import neccesary libraries
import random

# the winning number
result = random.randrange(1,51)

# Action to start play
play = input("Do you want to play the guessing game: ")
play = play.lower().strip()[:1]                             # for the first letter "y"


# the loop
while play == "y":
    # try and except
    try:
        # First trial input
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

    except Exception as e:
        print(f"An error occurred: {e}")
    
    play = input("\nDo you want to play the guessing game again: ")    

# final remark
print("Thanks for your time with us!")
