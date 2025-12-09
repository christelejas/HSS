import pygame
import sys
import csv
import os
import math
from datetime import datetime
import random


# PARAMETERS ----------------------------------------------------

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

REF_BASE_LENGTH = 260                 # base bar length (px)
LENGTH_DIFFS = [-40, -20, 0, 20, 40]  # top_length - bottom_length
TRIALS_PER_DIFF = 10                  # number of trials per difference

TOP_Y = SCREEN_HEIGHT // 2 - 80
BOTTOM_Y = SCREEN_HEIGHT // 2 + 80

FIXATION_TIME = 500                   # fixation cross duration (ms)


# DISPLAY FUNCTIONS ---------------------------------------------

def draw_ponzo_frame(screen):
    """Draws two converging lines (Ponzo frame)."""
    color = (200, 200, 200)
    # converging lines like a road in perspective
    pygame.draw.line(screen, color,
                     (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT),
                     (SCREEN_WIDTH // 2 - 40, 150), 3)
    pygame.draw.line(screen, color,
                     (SCREEN_WIDTH // 2 + 250, SCREEN_HEIGHT),
                     (SCREEN_WIDTH // 2 + 40, 150), 3)

def draw_bar(screen, length, y, color=(255, 255, 255), thickness=4):
    """Draws a centered horizontal bar."""
    x1 = SCREEN_WIDTH // 2 - length // 2
    x2 = SCREEN_WIDTH // 2 + length // 2
    pygame.draw.line(screen, color, (x1, y), (x2, y), thickness)

def show_text_center(screen, text, size=32):
    """Displays centered multi-line text."""
    font = pygame.font.Font(None, size)
    lines = text.split("\n")
    total_height = len(lines) * size * 1.4
    start_y = SCREEN_HEIGHT // 2 - total_height // 2

    for i, line in enumerate(lines):
        surf = font.render(line, True, (255, 255, 255))
        rect = surf.get_rect(center=(SCREEN_WIDTH // 2,
                                     start_y + i * size * 1.4))
        screen.blit(surf, rect)


# MAIN EXPERIMENT -----------------------------------------------

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ponzo Illusion")
    clock = pygame.time.Clock()

    # Ask for a file name to create
    subject_id = input("Enter file name to store the experiment results: ")

    # CSV file preparation
    if not os.path.exists("data"):
        os.makedirs("data")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/{subject_id}_ponzo_{timestamp}.csv"

    fieldnames = [
        "subject_id", "trial_index",
        "length_diff", "top_length", "bottom_length",
        "correct_answer", "response", "is_correct", "rt"
    ]

    csvfile = open(filename, "w", newline="", encoding="utf-8")
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Instructions screen
    screen.fill((0, 0, 0))
    show_text_center(
        screen,
        "Ponzo Illusion\n\n"
        "Two horizontal lines are shown between converging lines.\n"
        "Which line APPEARS longer?\n\n"
        "UP ARROW   = top line appears longer\n"
        "DOWN ARROW = bottom line appears longer\n\n"
        "Press SPACE to begin.",
        size=28
    )
    pygame.display.flip()

    # Wait for SPACE to start
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                csvfile.close()
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

    # Trial generation
    trials = []
    for diff in LENGTH_DIFFS:
        for _ in range(TRIALS_PER_DIFF):
            trials.append(diff)
    random.shuffle(trials)

    trial_index = 0

    # Experimental loop -----------------------------------------
    for length_diff in trials:
        trial_index += 1

        # Define actual bar lengths
        bottom_length = REF_BASE_LENGTH
        top_length = REF_BASE_LENGTH + length_diff

        # Determine correct answer
        if top_length > bottom_length:
            correct_answer = "top"
        elif top_length < bottom_length:
            correct_answer = "bottom"
        else:
            correct_answer = "equal"

        # Fixation cross
        screen.fill((0, 0, 0))
        show_text_center(screen, "+", size=80)
        pygame.display.flip()
        pygame.time.wait(FIXATION_TIME)

        # Trial start
        rt_start = pygame.time.get_ticks()
        response = None
        is_correct = None

        running_trial = True
        while running_trial:
            screen.fill((0, 0, 0))

            # Ponzo frame
            draw_ponzo_frame(screen)

            # Top bar
            draw_bar(screen, top_length, TOP_Y)

            # Bottom bar
            draw_bar(screen, bottom_length, BOTTOM_Y)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    csvfile.close()
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        csvfile.close()
                        pygame.quit()
                        sys.exit(0)
                    # Responses
                    if event.key == pygame.K_UP:
                        response = "top"
                        running_trial = False
                    if event.key == pygame.K_DOWN:
                        response = "bottom"
                        running_trial = False

            clock.tick(60)

        rt = (pygame.time.get_ticks() - rt_start) / 1000.0

        # Determine accuracy
        if correct_answer == "equal":
            is_correct = ""
        else:
            is_correct = (response == correct_answer)

        # Save trial data
        writer.writerow({
            "subject_id": subject_id,
            "trial_index": trial_index,
            "length_diff": length_diff,
            "top_length": top_length,
            "bottom_length": bottom_length,
            "correct_answer": correct_answer,
            "response": response,
            "is_correct": is_correct,
            "rt": rt
        })
        csvfile.flush()

    # End screen
    screen.fill((0, 0, 0))
    show_text_center(screen, "Thank you for your participation!", size=40)
    pygame.display.flip()
    pygame.time.wait(2000)

    csvfile.close()
    pygame.quit()
    print(f"Data saved in: {filename}")


if __name__ == "__main__":
    main()


