from random import randint

i = 0

while True:
    number = randint(1,101)
    guess_count = 0
    while True:
        try:
            guess = int(input('Guess a number between 1 & 100 inclusive:    '))
            guess_count += 1
            if guess > 100 or guess < 1:
                print('You must input a number in between 1 and 100 inclusive.    ')
                continue
            elif guess == number:
                play_again = input('Congratulations!! You guessed the right number: {}. It only took {} tries. Do you want to play again?    '.format(number, guess_count))
                while True:
                    if play_again == 'yes':
                        break
                    elif play_again == 'no':
                        i = 1
                        break
                    else:
                        play_again = input('You must answer yes or no (lowercase)    ')
                break
            elif -10 <= guess - number <= 10:
                print('Warm! You are within 10.')
            else:
                print('Cold, you are further than 10 away!')
            if guess_count > 1:
                if abs(guess - number) <= abs(prev_guess - number):
                    print('Getting warmer!!')
                else:
                    print('Getting colder!')
            prev_guess = guess
        except:
            print('You must input a whole number between 1 & 100.')
    if i == 1:
        break
    
