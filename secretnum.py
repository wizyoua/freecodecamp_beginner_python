import random

def main(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a num between 1 and {x}: '))
        if guess < random_number:
            print('sorry guess again too low.')

        elif    guess > random_number:
            print("sorry guess again too high")
    print(f'yay you guessed the number. {random_number} correctly')

main(10)
