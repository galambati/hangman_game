import random


def play():
    word = get_a_word(select_type())
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
                   

def get_a_word(type):
    animals_easy = ['Tiger', 'Hippo', 'Horse', 'Hyena', 'Camel']
    animals_hard = ['Chinchilla', 'Wildebeest', 'Chimpanzee', 'Cottontail']
    car_brands_easy = ['Subaru', 'Suzuki', 'Jaguar', 'Nissan', 'Toyota']
    car_brands_hard = ['Mitsubishi', 'Volkswagen', 'Chevrolet']

    if type == 'animals_easy':
        return(random.choice(animals_easy))
    elif type == 'animals_hard':
        return(random.choice(animals_hard))
    elif type == 'car_brands_easy':
        return(random.choice(car_brands_easy))
    else:
        return(random.choice(car_brands_hard))


def select_type():
    print('Welcome to this Hangman Game!')
    print('No typos allowed!')
    type = str(input('Type in, what kind of word you wanna guess (-animals- or -car_brands-): '))
    type_2 = str(input('Type in your level (-easy- or -hard-): '))
    return(type + '_' + type_2)


play()
