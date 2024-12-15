import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Input number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

# Initialize scores
max_score = 50
players_score = [0 for _ in range(players)]

# Game loop
while max(players_score) < max_score:
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn has just started!\n")
        print(f"Your total score is: {players_score[player_index]}\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0  # Reset current score for this turn
                break
            else:
                current_score += value
                print(f"You rolled a {value}.")
                print(f"Your current turn score is: {current_score}")
        
        # Update the player's total score
        players_score[player_index] += current_score
        print(f"Player {player_index + 1}'s total score is now: {players_score[player_index]}")
        
        # Check if this player has reached or exceeded the max score
        if players_score[player_index] >= max_score:
            break

    # Stop the game if someone has won
    if max(players_score) >= max_score:
        break

# Determine the winner
max_score = max(players_score)
winning_idx = players_score.index(max_score)
print(f"\nPlayer {winning_idx + 1} is the winner with a score of {max_score}!")
