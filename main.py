from game_data import data
import random
from art import logo, vs


# Clear Console
def clear():
    print('\033c', end=None)


# Compare Choices
def check_answer(account_one, account_two):
    if account_one['follower_count'] > account_two['follower_count']:
        return 'a'
    else:
        return 'b'


# Get Next Choice
def next_choice(account_one, account_two):
    account_one = account_two
    account_two = random.choice(data)
    return account_one, account_two


# Formatting account information to display
def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


# Starting the game structure
def game():
    # Base Data
    account_one = random.choice(data)
    account_two = random.choice(data)
    score = 0
    print(logo)

    play = True
    while play:
        print(f'Compare A: {format_data(account_one)}')
        print(vs)
        print(f'Against B: {format_data(account_two)}')

        guess = input('Who has more followers "A" or "B"? ').lower()
        correct_answer = check_answer(account_one, account_two)

        # Check if Guess is correct
        if correct_answer == guess:
            clear()
            score += 1
            print(logo)
            print(f"You're Right. Current Score: {score}")
            account_one, account_two = next_choice(account_one, account_two)
        else:
            print(f"You're Wrong. Final Score: {score}")
            if input('Play again? ') == 'no':
                play = False
            else:
                clear()
                game()

game()
