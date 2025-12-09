import pygame
import sys
import csv
import os
import math
from datetime import datetime
import random

# PARAMETERS


REF_LENGTH = 300        # pixels
INITIAL_TEST_LENGTH = 300
STEP_SIZE = 10          # pixels per left/right press
ANGLES = [40, 70, 110, 140]
TRIALS_PER_ANGLE = 10

FIXATION_TIME = 500     # ms
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

TEST_Y = SCREEN_HEIGHT // 2 + 80
REF_Y = SCREEN_HEIGHT // 2 - 80


# FUNCTIONS


def draw_line_with_wings(screen, length, y, angle_deg, color=(255,255,255)):
    """ Draw a horizontal line centered + Müller-Lyer wings """
    
    x1 = SCREEN_WIDTH//2 - length//2
    x2 = SCREEN_WIDTH//2 + length//2
    
    # Draw main line
    pygame.draw.line(screen, color, (x1, y), (x2, y), 3)
    
    # Wing length
    wing = 40
    ang = math.radians(angle_deg)
    
    # Left wings
    pygame.draw.line(screen, color, (x1, y),
                     (x1 - wing*math.cos(ang), y - wing*math.sin(ang)), 2)
    pygame.draw.line(screen, color, (x1, y),
                     (x1 - wing*math.cos(ang), y + wing*math.sin(ang)), 2)
    
    # Right wings
    pygame.draw.line(screen, color, (x2, y),
                     (x2 + wing*math.cos(ang), y - wing*math.sin(ang)), 2)
    pygame.draw.line(screen, color, (x2, y),
                     (x2 + wing*math.cos(ang), y + wing*math.sin(ang)), 2)

def show_text_center(screen, text, size=36):
    font = pygame.font.Font(None, size)
    surf = font.render(text, True, (255,255,255))
    rect = surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.blit(surf, rect)


# MAIN EXPERIMENT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Ask for a file name 
    subject_id = input("Enter File name containing results of the experiment")


    # Prepare output CSV
    if not os.path.exists("data"):
        os.makedirs("data")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/{subject_id}_muller_lyer_{timestamp}.csv"

    fieldnames = [
        "subject_id", "trial_index", "angle",
        "ref_length", "initial_test_length",
        "final_test_length", "adjustment_steps", "rt"
    ]

    csvfile = open(filename, "w", newline="", encoding="utf-8")
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Show instructions
    screen.fill((0,0,0))
    show_text_center(screen,
        "Adjust the bottom line using LEFT/RIGHT arrows.\nPress SPACE to confirm.\nPress ESC to exit.",
        size=32
    )
    pygame.display.flip()

    # Wait for SPACE
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

    # Generate trials
    trials = []
    for angle in ANGLES:
        for _ in range(TRIALS_PER_ANGLE):
            trials.append(angle)
    random.shuffle(trials)

    # Trial loop
    trial_index = 0

    for angle in trials:
        trial_index += 1
        current_length = INITIAL_TEST_LENGTH
        adjustment_steps = 0

        # Fixation
        screen.fill((0,0,0))
        show_text_center(screen, "+", size=80)
        pygame.display.flip()
        pygame.time.wait(FIXATION_TIME)

        # Start RT timer
        rt_start = pygame.time.get_ticks()

        # Adjustment loop
        adjusting = True
        while adjusting:
            screen.fill((0,0,0))

            # Draw reference line
            draw_line_with_wings(screen, REF_LENGTH, REF_Y, angle, color=(120,120,120))

            # Draw test line
            draw_line_with_wings(screen, current_length, TEST_Y, angle)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    csvfile.close()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        csvfile.close()
                        sys.exit(0)
                    if event.key == pygame.K_LEFT:
                        current_length -= STEP_SIZE
                        adjustment_steps += 1
                    if event.key == pygame.K_RIGHT:
                        current_length += STEP_SIZE
                        adjustment_steps += 1
                    if event.key == pygame.K_SPACE:
                        rt = (pygame.time.get_ticks() - rt_start) / 1000
                        adjusting = False

            clock.tick(60)

        # Save trial
        writer.writerow({
            "subject_id": subject_id,
            "trial_index": trial_index,
            "angle": angle,
            "ref_length": REF_LENGTH,
            "initial_test_length": INITIAL_TEST_LENGTH,
            "final_test_length": current_length,
            "adjustment_steps": adjustment_steps,
            "rt": rt
        })
        csvfile.flush()

    # End screen
    screen.fill((0,0,0))
    show_text_center(screen, "Thank you for participating!", size=40)
    pygame.display.flip()
    pygame.time.wait(2000)

    csvfile.close()
    pygame.quit()

if __name__ == "__main__":
    main() 
