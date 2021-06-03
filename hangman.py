def play(word):
    lives = len(word)
    letters = ['a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters_of_word = []
    display_word = []
    for letter in word:
        letters_of_word.append(letter)
        display_word.append('_')
    display = ' '.join(display_word)
    print(display)
    while True:
        if lives == 0:
            print('Game over!')
            break
        if '_' not in display_word:
            print('Remain Lives: ' + str(lives))
            print('You win!')
            break
        guess = str(input('Guess a letter: '))
        if guess in letters:
            if guess in letters_of_word:
                for index in range(0, len(letters_of_word)):
                    if guess == letters_of_word[index]:
                        display_word[index] = guess
                        display = ' '.join(display_word)
                print(display)
            else:
                print('Nope')
                print(display)
                lives -= 1
        else:
            print('Please guess a valid character!')
                   

play()
