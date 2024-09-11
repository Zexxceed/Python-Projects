import time
import random

# Basic game setup variables
player_xp = 0
current_level = 1

# Dictionary to store XP for each difficulty level
xp_rewards = {"easy": 50, "medium": 100, "hard": 200}

# Placeholder for level puzzles
puzzles = {
    1: {"easy": "Easy puzzle code here", "medium": "Medium puzzle code here", "hard": "Hard puzzle code here"},
    2: {"easy": "Easy puzzle code here", "medium": "Medium puzzle code here", "hard": "Hard puzzle code here"},
    # Add puzzles for more levels as needed
}

# Function to display the tutorial
def show_tutorial():
    print("Welcome to CodeCrypt: Python Mastery!")
    print("In this game, you'll solve puzzles by writing Python code.")
    print("Each level has three difficulties: Easy, Medium, and Hard.")
    print("Solve all Hard puzzles to move to the next level!")
    print("\nHint: If you're stuck for 3 minutes, a hint will appear.\n")

# Function to show the hint after inactivity (no input)
def show_hint(puzzle_type):
    print(f"\nHint for {puzzle_type} puzzle: Remember to use correct Python syntax for solving this type of problem!")

# Function to simulate solving puzzles (replace with actual puzzle-solving logic)
def solve_puzzle(level, difficulty):
    print(f"\nSolving {difficulty} puzzle at level {level}...")
    time.sleep(1)  # Simulate solving time

    # Simulate user input timeout for hint (real game would use user input)
    start_time = time.time()
    input_attempt = input(f"Try solving the {difficulty} puzzle (Type your solution): ")

    # Simulate hint system - if no input for 3 minutes
    while True:
        current_time = time.time()
        if input_attempt or current_time - start_time > 180:  # 3 minutes (180 seconds) timeout
            break
        time.sleep(10)

    # For simplicity, assume the player solves the puzzle correctly
    print(f"Correct! You've solved the {difficulty} puzzle.")
    return True

# Function to handle progression and leveling
def level_progression():
    global player_xp, current_level

    # Loop through each level
    while current_level <= 5:  # Max level 5
        print(f"\nLevel {current_level}: Choose your difficulty (easy/medium/hard):")
        difficulty = input().lower()

        if difficulty in ["easy", "medium", "hard"]:
            puzzle_solved = solve_puzzle(current_level, difficulty)
            if puzzle_solved:
                player_xp += xp_rewards[difficulty]
                print(f"You've earned {xp_rewards[difficulty]} XP! Total XP: {player_xp}")

            # Only advance to the next level if hard puzzle is completed
            if difficulty == "hard":
                current_level += 1
                print(f"Congratulations! You've unlocked Level {current_level}.\n")
        else:
            print("Invalid choice, please select easy, medium, or hard.")

        # Add a condition to break out when max level is reached
        if current_level > 5:
            print("You've completed all levels! Well done!")
            break

# Main game loop
def start_game():
    show_tutorial()  # Display the tutorial at the start
    level_progression()  # Begin level progression

# Start the game
if __name__ == "__main__":
    start_game()
