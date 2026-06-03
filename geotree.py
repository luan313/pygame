import pygame
import math

pygame.init()

# Display size
width, length = 900, 700
screen = pygame.display.set_mode((width, length))
# Caption
pygame.display.set_caption("Geotree")

# Function that draws a branch, and recursively calls itself to draw more branches
def draw_branch(x, y, angle, length, depth, angle_opening, vento):
    # Base case: if the depth is 0, stop drawing
    if depth == 0:
        return
    
    # Calculate the end position of the branch
    x_end = x + int(math.cos(math.radians(angle)) * length)
    y_end = y - int(math.sin(math.radians(angle)) * length)

    # Color of the branch (green for younger branches, brown for older branches)
    color = (50, 180 - (depth * 15), 50) if depth < 5 else (139, 69, 19)
    
    # Draw the branch
    pygame.draw.line(screen, color, (x, y), (x_end, y_end), depth)

    # Recursive call
    draw_branch(x_end, y_end, angle - angle_opening + vento, length * 0.75, depth - 1, angle_opening, vento)
    draw_branch(x_end, y_end, angle + angle_opening + vento, length * 0.75, depth - 1, angle_opening, vento)

# Main loop
executando = True
while executando:
    # Background color
    screen.fill((240, 240, 240))
    
    # Get mouse position
    pos_mouse = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Map the mouse X position to an angle between 10 and 70 degrees
    angle_dynamic = 10 + (pos_mouse[0] / width) * 60

    # Map the Y position to the initial height of the trunk
    initial_length = 50 + ((length - pos_mouse[1]) / length) * 120

    time = pygame.time.get_ticks() / 1000 
    
    # Create a gentle wind oscillation (by senoidal wave)
    wind = math.sin(time * 2) * 0.5

    # Draw the tree from the base of the screen
    draw_branch(width // 2, length - 50, 90, initial_length, 10, angle_dynamic, wind)

    pygame.display.flip()

pygame.quit()