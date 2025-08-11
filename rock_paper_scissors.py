import random

# Rock, Paper, Scissors Game in Python
# ---------------------------------------

# Choices available in the game
OPTIONS = ["rock", "paper", "scissors"]

# Score tracker
player_score = 0
computer_score = 0
tie_count = 0

print("\nWelcome to Rock, Paper, Scissors!")
print("Type 'exit' anytime to quit.\n")

# Main game loop
while True:
    # Get player's choice
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    # Exit condition
    if player_choice == "exit":
        print("\nThanks for playing!")
        print(f"Final Score → You: {player_score} | Computer: {computer_score} | Ties: {tie_count}")
        break

    # Validate input
    if player_choice not in OPTIONS:
        print("Invalid choice! Please try again.\n")
        continue

    # Computer makes a random choice
    computer_choice = random.choice(OPTIONS)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie!\n")
        tie_count += 1
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!\n")
        player_score += 1
    else:
        print("Computer wins!\n")
        computer_score += 1

    # Show current score after each round
    print(f"Score → You: {player_score} | Computer: {computer_score} | Ties: {tie_count}\n")
    print("-" * 40)
