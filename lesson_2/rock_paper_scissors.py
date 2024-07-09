import random

VALID_CHOICES = ['r', 'p', 's', 'o', 'l']
WINNING_COMBOS = {
    'r': ['s', 'l'],
    'p': ['r', 'o'],
    's': ['p', 'l'],
    'l': ['p', 'o'],
    'o': ['r', 's'],
}

def prompt(message):
    print(f"==> {message}")

def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

def display_winner(player, computer):

    if winner == "player"
        prompt("You win!")
    elif winner == "computer"
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")



while True:
    prompt(f'Best of five. Choose one: {", ".join(VALID_CHOICES)}')
    prompt("(Example: r for rock or p for paper or s for scissors or o\
for spock or l for lizard)")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    if wins == 3 or computer_wins == 3:
        break