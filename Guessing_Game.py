# Develop a number guessing game where the computer randomly selects a number and the player has to guess it.
import random

print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')

number = random.randint(1, 100)
attempts = 5

while attempts > 0:
    try:
        if (guess := int(input(f'Guess the number,{attempts} attempts left: '))) != number:
            print('Too low!' if guess < number else 'Too high!')
            attempts -= 1
        else:
            print(f'Congratulations!You guessed it in {5 - attempts + 1} attempts.')
            break
    except ValueError:
        print('Please enter a valid number.')
else:
    print(f'Sorry,you are out of attempts! The number was {number}.')
print('Thanks for playing!')


