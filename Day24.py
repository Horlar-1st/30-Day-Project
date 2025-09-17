# Hangman Lite: Build a simple hangman game with one hardcoded word. Track user guesses

# import random
import random

class Hangman:
    def __init__(self):
        # Answers and hint in a dictionary
        self.answers = {"SUN": "That star in our solar system",
                        "SNAKE": "A type of reptile.",
                        "LAKE": "It's bigger than a pond but smaller than an ocean.",
                       "HOUSE": "Built on a foundation",
                       "BALL": "Used in many sports",
                        "BOOK": "Something you can read"}
        # list of words of answers
        self.answer_words = list(self.answers.keys())


    def the_game(self):
        self.answer = random.choice(self.answer_words)         # Random selction of words
        self.answer_len = len(self.answer)                     # Length of the words
        self.guess_lst = ["_"]*self.answer_len                 # Blank spaces for predictions and guesses
        self.hint = self.answers[self.answer]                  # Hints

        
        # trials and numbers of trials
        count = 0
        n_trials = int(self.answer_len * 1.5)

        
        print(f"Hint: {self.hint}")
        while count < n_trials and "_" in self.guess_lst:
            # comments
            self.comment_of_guess = []
            
            print("The word is: " + " ".join(self.guess_lst))
            self.guess = input("Guess a letter: ")
            self.guess = self.guess.upper()
                
            if self.guess in self.answer:
                positions = [i for i, char in enumerate( self.answer) if char == self.guess] #self.answer.index(self.guess)
                for position in positions:   
                    self.guess_lst[position] = self.guess
                self.comment_of_guess.append(f"Correct! {self.guess} is in position {position+1} in the word. You have {n_trials-count-1} trials left!!")
            else:
                self.comment_of_guess.append(f"Wrong imput! {self.guess} is not in the word.  You have {n_trials-count-1} trials left!!")
            
            print("\n".join(self.comment_of_guess) + "\n")
            count +=1
                
        return "Success!! \"" + " ".join(self.guess_lst) + "\" is the answer" if "_" not in self.guess_lst else "Please retry!"
    

# initilizing
demo = Hangman()


# running
demo.the_game()

# Answers are either BALL, BOOK, HOUSE, LAKE, SNAKE, OR SUN

# End of code 
