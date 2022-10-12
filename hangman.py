import random
from tkinter import Y
from words import word_list
from tabulate import tabulate

def print_title():
    print("\n")
    print("\n")
    print("                              ~~ HANGMAN OR BE HANGED ~~ ")

def score_board(wins, losses):
    mydata = [[wins, losses]]
    head = ["Wins", "Losses"]
    print(tabulate(mydata, headers= head, tablefmt="grid"))
    print("\n")

def get_word():
    print("\n")
    command = input("Would you like to choose your own word (Y) or have a word generated for you (N) : ")
    print("\n")

    if (command == "Y" or command == "y"):
        word = input("Please enter a word: ")
        print("Scroll down so your fellow player doesn't see the word you typed in!")
        print("\n")
        print("\n")
        print("\n")
        return word.upper()

    elif(command == "N" or command == "n"):
        print("A word is being selected for you...")
        print("\n")        
        word = random.choice(word_list)
        return word.upper()

def play(word, wins, losses):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome! Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        wins += 1 
        print("Nice job, you guessed the word! You win!")
    else:
        losses += 1
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
    return wins, losses




def display_hangman(tries):
    stages = [   """
                    --------
                    |       |                    
                    |       O
                    |      \\|/
                    |       |
                    |      / \\
                    -
                """,
                """
                     --------
                    |       |                    
                    |       O
                    |      \\|/
                    |       |
                    |      / 
                    -
                """,
                """
                     --------
                    |       |                    
                    |       O
                    |      \\|/
                    |       |
                    |       
                    -
                """,
                """
                     --------
                    |       |                    
                    |       O
                    |       |/
                    |       |
                    |       
                    -
                """,
                """
                     --------
                    |       |                    
                    |       O
                    |       |
                    |       |
                    |       
                    -
                """,
                """
                     --------
                    |       |                    
                    |       O
                    |       
                    |       
                    |       
                    -
                """,
                """
                     --------
                    |       |                    
                    |       
                    |       
                    |       
                    |       
                    -
                """
    ]
    return stages[tries]


def main():
    print_title()
    word = get_word()
    wins = 0
    losses = 0
    score_board(wins, losses)
    wins, losses = play(word, wins, losses)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_word()
        score_board(wins, losses)
        wins, losses = play(word, wins, losses)
    print("\n")
    print("Your final win and loss streak is")
    score_board(wins, losses)
    print("Good game! Hope to see you soon player!")
    print("\n")

if __name__ == "__main__":
    main()
