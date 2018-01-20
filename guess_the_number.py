import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range(low, high):
    '''Set the high and low values for the random number'''
    return low, high


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess and handles exceptions.'''
    while True:
        try:
            userInput = int(input('Guess the secret number? '))
        except ValueError:
            print("Not an integer. Try again.")
        else:
            return userInput


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    print("Enter two different numbers to generate the range of secret number.")
    #lower limit of the range.
    lowerLimit = int(input("Enter the lower limit number: "))
    #upper limit of the range.
    upperLimit = int(input("Enter the upper limit number: "))
    #initializes the counter.
    guess_count = 0
    configure_range(lowerLimit, upperLimit)
    secret = generate_secret(lowerLimit, upperLimit)

    while True:
        guess = get_guess()
        if (guess<lowerLimit or guess>upperLimit):
            print("The number is out of range. Enter the number again.")
            guess_count+=1
        else:
            result = check_guess(guess, secret)
            print(result)
            guess_count+=1

            if result == correct:
                print('You had ', guess_count ,' tries!')
        play_again = input("Play again! Please type y for yes: ")
        if play_again != "y":
            break



if __name__ == '__main__':
    main()
