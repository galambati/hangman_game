import random


def get_word(file):
   with open(file, "r") as f:
      lines=f.readlines()
      random_line = random.choice(lines)
      splitted_line = random_line.split(' | ')
      imported_country = splitted_line[0]
      # imported_city = splitted_line[1]
   return imported_country # , imported_city


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 7
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ")
        if len(guess) == 1 and guess.isalpha():
            if guess.upper() in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess.upper() not in word.upper():
                print(guess, "is not in the word.")
                lives -= 1
                guessed_letters.append(guess.upper())
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess.upper())
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess.upper() in guessed_words:
                print("You already guessed the word", guess)
            elif guess.upper() != word.upper():
                print(guess, "is not the word.")
                lives -= 1
                guessed_words.append(guess.upper())
            else:
                guessed = True
                word_completion = word
        elif guess.upper() == "QUIT":
            print("Goodbye")
            quit()
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of lives. The word was " + word + ". Maybe next time!")


def display_hangman(lives):
    stages = [  # 7
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # 6
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # 3
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # 2
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # 1
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # 0
                 """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]


def main():
    word = get_word("countries-and-capitals.txt")
    print(word)
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
