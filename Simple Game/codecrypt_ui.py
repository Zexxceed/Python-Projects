import pygame
import sys

# Initialize Pygame
pygame.init()

# Game window settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CodeCrypt: Python Mastery")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.SysFont("Arial", 36)

# Puzzle dictionary (placeholder for actual puzzles)
puzzles = {
    "easy": "Solve this: x + 5 = 10. What is x?",
    "medium": "Solve this: 2x + 3 = 7. What is x?",
    "hard": "Write a Python function to find the sum of a list."
}

# Game variables
current_puzzle = ""
difficulty = ""
is_puzzle_solved = False

# Function to display text
def draw_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

# Function to display buttons
def draw_button(text, x, y, w, h, color, action=None):
    pygame.draw.rect(screen, color, (x, y, w, h))
    draw_text(text, font, WHITE, x + 10, y + 10)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Check if button is clicked
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action:
            action()

# Functions to set the difficulty and puzzle
def select_easy():
    global current_puzzle, difficulty
    difficulty = "easy"
    current_puzzle = puzzles[difficulty]

def select_medium():
    global current_puzzle, difficulty
    difficulty = "medium"
    current_puzzle = puzzles[difficulty]

def select_hard():
    global current_puzzle, difficulty
    difficulty = "hard"
    current_puzzle = puzzles[difficulty]

# Main game loop
def game_loop():
    global current_puzzle, is_puzzle_solved

    running = True
    while running:
        screen.fill(WHITE)

        # Display title
        draw_text("CodeCrypt: Python Mastery", font, BLACK, 200, 50)

        # Display difficulty selection buttons
        draw_button("Easy", 100, 150, 150, 50, BLUE, select_easy)
        draw_button("Medium", 300, 150, 150, 50, GREEN, select_medium)
        draw_button("Hard", 500, 150, 150, 50, RED, select_hard)

        # Display current puzzle if a difficulty is selected
        if current_puzzle:
            draw_text(f"Puzzle ({difficulty.capitalize()}):", font, BLACK, 100, 250)
            draw_text(current_puzzle, font, BLACK, 100, 300)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update display
        pygame.display.update()

# Start the game
if __name__ == "__main__":
    game_loop()
