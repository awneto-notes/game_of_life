import pygame
import sys
import copy
import time

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 10
GRID_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (0, 0, 0)  # Black
CELL_COLOR = (0, 128, 64) 

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo da vida")

# Grid state to track cell colors
grid_state = [[BACKGROUND_COLOR for _ in range(screen_width // CELL_SIZE)] for _ in range(screen_height // CELL_SIZE)]


# Flag to track mouse button state
mouse_pressed = False


def update_grid(grid_state):
    new_grid_state = copy.deepcopy(grid_state)
    for y in range(len(grid_state)):
        for x in range(len(grid_state[0])):
            active_neighbors = 0
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    if dy==0 and dx==0:
                        continue
                    if 0 <= (y+dy) < len(grid_state) and 0 <= (x+dx) < len(grid_state[0]):
                        if grid_state[y+dy][x+dx] == CELL_COLOR:
                            active_neighbors +=1
            if grid_state[y][x] == BACKGROUND_COLOR and active_neighbors == 3:
                new_grid_state[y][x] = CELL_COLOR
            if grid_state[y][x] == CELL_COLOR and (active_neighbors < 2 or active_neighbors > 3):
                new_grid_state[y][x] = BACKGROUND_COLOR
    return(new_grid_state)

# Main loop
next_update_time = time.time() + 0.25
while True:

    current_time = time.time()
    if current_time >= next_update_time:
        grid_state = update_grid(grid_state)
        next_update_time = current_time + 0.25
        
    screen.fill(BACKGROUND_COLOR)
    
    # Draw cells based on grid state
    for y, row in enumerate(grid_state):
        for x, color in enumerate(row):
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw grid lines
    for x in range(0, screen_width, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, screen_height))
    for y in range(0, screen_height, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (screen_width, y))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
            
        if mouse_pressed:
            x, y = pygame.mouse.get_pos()
            if (0<x<screen_width) and (0<y<screen_height):
                grid_x = x // CELL_SIZE
                grid_y = y // CELL_SIZE
                grid_x = min(max(0,grid_x),screen_width // CELL_SIZE)
                grid_y = min(max(0,grid_y),screen_height // CELL_SIZE)
                grid_state[grid_y][grid_x] = CELL_COLOR

    pygame.display.flip()