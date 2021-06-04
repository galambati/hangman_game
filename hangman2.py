import random


def get_word(file, level):
   with open(file, "r") as f:
        lines=f.readlines()
        random_line = random.choice(lines)
        splitted_line = random_line.split(' | ')
        splitted_line[1]=splitted_line[1].removesuffix("\n")
        if level > 3:
            chosen_word = random.choice(splitted_line)
        else:
            chosen_word = splitted_line[0]
   return chosen_word 


def play(word, lives):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = [] #korábban tippelt betűk, mindig nagy
    guessed_words = [] #korábban tippelt szavak
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ")
        if len(guess) == 1 and guess.isalpha(): #egy betűt tippelt
            if guess.upper() in guessed_letters: #tippelt betű már volt, nagy betűt nagy betűvel összehasonlít
                print("You already guessed the letter", guess) #tippelt betű kiírása
                print("Tried letters: ", end =" ") #korábban tippelt betűk kiírása
                print(', '.join(guessed_letters)) #korábban tippelt betűk kiírása
            elif guess.upper() not in word.upper(): #tippelt betű nincs a keresett szóban, nagy betűt nagy betűvel összehasonlít
                print(guess, "is not in the word.") #tippelt betű kiírása
                print("Tried letters: ", end =" ") #korábban tippelt betűk kiírása
                print(', '.join(guessed_letters)) #korábban tippelt betűk kiírása
                lives -= 1 #élet csökkentése
                guessed_letters.append(guess.upper()) #tippelt betű hozzáadása a korábban tippeltekhez
            else:
                print("Good job,", guess, "is in the word!") #tippelt betű benne van a szóban
                guessed_letters.append(guess.upper()) #tippelt betű hozzáadása a korábban tippeltekhez
                word_as_list = list(word_completion) #string szétszedése elemekre
                indices = [i for i, letter in enumerate(word.upper()) if letter == guess.upper()] #tippelt betű helyeinek megkeresése a szóban
                for index in indices: #tippelt betű kitöltése
                    word_as_list[index] = (list(word))[index]
                word_completion = "".join(word_as_list) #betűelemek összefűzése stringgé
                if "_" not in word_completion: #nincs több _, nyert
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha(): #szót tippelt
            if guess.upper() in guessed_words: #tippelt szó már volt, nagy betűt nagy betűvel összehasonlít
                print("You already guessed the word", guess) #tippelt szó kiírása
            elif guess.upper() != word.upper(): #tippelt szó nem talált
                print(guess, "is not the word.")
                lives -= 1 #élet csökkentése
                guessed_words.append(guess.upper()) #tippelt szó hozzáadása a korábbi tippekhez
            else: #tippelt szó talált, nyert
                guessed = True 
                word_completion = word
        elif guess.upper() == "QUIT": #kilépett
            print("Goodbye")
            quit()
        else: #érvénytelen tippelés
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
    level = int(input("Please choose level (1-5): "))

    word = get_word("countries-and-capitals.txt", level)
    
    lives = 8-level

    play(word, lives)
    while input("Play Again? (Y/N) ").upper() == "Y":
        level = input("Please choose level (1-5): ")
        word = get_word("countries-and-capitals.txt")
        lives = 8-int(level)
        play(word, lives)


if __name__ == "__main__":
    main()
