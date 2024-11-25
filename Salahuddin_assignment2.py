import random

# Initialize counters
player_wins = 0
computer_wins = 0
draws = 0

print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'quit' to stop the game.\n")

while True:
    #  player's choice
    player_choice = input("Your choice: ").lower()

    if player_choice == "quit":
        break  # Exit the game
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a draw!")
        draws += 1
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        player_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

# Display final results
print("\nGame Over!")
print(f"You won: {player_wins} time(s)")
print(f"Computer won: {computer_wins} time(s)")
print(f"Draws: {draws} time(s)")
print("Thanks for playing!")
