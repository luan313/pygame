import pygame
import random
import math

pygame.init()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("InterGalax")
clock = pygame.time.Clock()

# Create 300 particles with random positions and colors
particles = []
for _ in range(300):
    x = random.randint(0, width)
    y = random.randint(0, height)
    color = (random.randint(100, 255), random.randint(150, 255), 255)
    particles.append({"x": x, "y": y, "vx": 0.0, "vy": 0.0, "color": color})

executing = True
while executing:
    screen.fill((5, 5, 15))
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
                for p in particles:
                    # Get vectors of the particle relative to the mouse
                    dx = p["x"] - mouse_pos[0]
                    dy = p["y"] - mouse_pos[1]
                    # Get distance between the particle and the mouse
                    distance = math.hypot(dx, dy) + 1
                    
                    # Throw the particles away from the mouse with a lot of force (25)
                    p["vx"] += (dx / distance) * 25
                    p["vy"] += (dy / distance) * 25

    for p in particles:
        # Calculate the distance to the mouse
        dx = mouse_pos[0] - p["x"]
        dy = mouse_pos[1] - p["y"]
        distance = math.hypot(dx, dy) + 1

        # Gravitational attraction effect
        if distance < 400:
            p["vx"] += (dx / distance) * 0.3
            p["vy"] += (dy / distance) * 0.3

        # Apply some friction to slow down
        p["vx"] *= 0.97
        p["vy"] *= 0.97

        # Update position
        p["x"] += p["vx"]
        p["y"] += p["vy"]

        # Bounce off the walls
        if p["x"] <= 0:
            p["x"] = 0
            p["vx"] *= -1
        elif p["x"] >= width:
            p["x"] = width
            p["vx"] *= -1

        if p["y"] <= 0:
            p["y"] = 0
            p["vy"] *= -1
        elif p["y"] >= height:
            p["y"] = height
            p["vy"] *= -1

        # Draw the particle as a small sphere
        pygame.draw.circle(screen, p["color"], (int(p["x"]), int(p["y"])), 4)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()