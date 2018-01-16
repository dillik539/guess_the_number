import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, userRange):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, userRange)


def get_guess():
    '''get user's guess'''
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
    userRange = int(input("What range you want to generate? "))
    (low, userRange) = configure_range()
    secret = generate_secret(low, userRange)


    while True:
        guess = get_guess()

        result = check_guess(guess, secret)
        print(result)
        guess_number = +1

        if result == correct:
            break


if __name__ == '__main__':
    main()
