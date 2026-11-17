import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Starter Code")

# Colors (R, G, B)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
RED = (220, 20, 60)        # Enemy 1 color
PURPLE = (148, 0, 211)     # Enemy 2 color
ORANGE = (255, 140, 0)     # Enemy 3 color
GREEN = (34, 139, 34)      # Food color
DARK_GRAY = (50, 50, 50)   # Bullet color

# Clock, Frame Counter, and Fonts
clock = pygame.time.Clock()
FPS = 60
frame_count = 0
text_font = pygame.font.SysFont(None, 36)

# Player position and properties
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_radius = 10
player_speed = 5
vel_x = 0
vel_y = 0

# Bullet
bullet_radius = 5
bullet_speed = player_speed * 2 
bullets_x = []
bullets_y = []
bullets_vel_x = []
bullets_vel_y = []

# Food
food_radius = 12
food_x = random.randint(food_radius, SCREEN_WIDTH - food_radius)
food_y = random.randint(food_radius, SCREEN_HEIGHT - food_radius)

# Enemy 1
enemy1_x = 100.0
enemy1_y = 100.0
enemy1_radius = 25
enemy1_speed = player_speed / 2

# Enemy 2
enemy2_x = 0.0
enemy2_y = float(SCREEN_HEIGHT // 2)
enemy2_radius = 22
enemy2_vel_x = 4.0
enemy2_vel_y = 0.0

# Enemy 3s
enemy3_radius = 20
enemy3_orbit_radius = (SCREEN_HEIGHT // 2) - 30
enemy3_orbit_speed = 0.01

enemy3_x = float((SCREEN_WIDTH // 2) + enemy3_orbit_radius)
enemy3_y = float(SCREEN_HEIGHT // 2)
enemy3_vel_x = 0.0
enemy3_vel_y = 0.0

# Game state variables
score = 0
lives = 3
game_state = "PLAYING"  # "PLAYING", "WIN", or "LOSE"

# Main game loop
running = True
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == "PLAYING":
                # Direction changes
                if event.key == pygame.K_LEFT:
                    vel_x = -player_speed
                    vel_y = 0
                elif event.key == pygame.K_RIGHT:
                    vel_x = player_speed
                    vel_y = 0
                elif event.key == pygame.K_UP:
                    vel_x = 0
                    vel_y = -player_speed
                elif event.key == pygame.K_DOWN:
                    vel_x = 0
                    vel_y = player_speed
                # Fire bullet in current direction of travel
                elif event.key == pygame.K_SPACE:
                    if vel_x != 0 or vel_y != 0:
                        dir_x = vel_x / player_speed
                        dir_y = vel_y / player_speed
                        
                        bullets_x.append(player_x)
                        bullets_y.append(player_y)
                        bullets_vel_x.append(dir_x * bullet_speed)
                        bullets_vel_y.append(dir_y * bullet_speed)

    # Update Positions
    if game_state == "PLAYING":
        frame_count += 1

        # Update player position
        player_x += vel_x
        player_y += vel_y

        # Boundary Checking
        if player_x - player_radius < 0:
            player_x = player_radius
        elif player_x + player_radius > SCREEN_WIDTH:
            player_x = SCREEN_WIDTH - player_radius

        if player_y - player_radius < 0:
            player_y = player_radius
        elif player_y + player_radius > SCREEN_HEIGHT:
            player_y = SCREEN_HEIGHT - player_radius

        # Enemy 1
        dx1 = player_x - enemy1_x
        dy1 = player_y - enemy1_y
        dist1 = math.hypot(dx1, dy1)
        if dist1 > 0:
            enemy1_x += (dx1 / dist1) * enemy1_speed
            enemy1_y += (dy1 / dist1) * enemy1_speed

        # Enemy 2
        enemy2_vel_y = math.cos(frame_count * 0.05) * 3.0
        enemy2_x += enemy2_vel_x
        enemy2_y += enemy2_vel_y

        if enemy2_x > SCREEN_WIDTH - enemy2_radius:
            enemy2_x = SCREEN_WIDTH - enemy2_radius
            enemy2_vel_x = -abs(enemy2_vel_x)
        elif enemy2_x < enemy2_radius:
            enemy2_x = enemy2_radius
            enemy2_vel_x = abs(enemy2_vel_x)

        # Enemy 3
        enemy3_vel_x = -enemy3_orbit_radius * enemy3_orbit_speed * math.sin(frame_count * enemy3_orbit_speed)
        enemy3_vel_y = enemy3_orbit_radius * enemy3_orbit_speed * math.cos(frame_count * enemy3_orbit_speed)
        enemy3_x += enemy3_vel_x
        enemy3_y += enemy3_vel_y

        #Bullets
        for i in range(len(bullets_x) - 1, -1, -1):
            bullets_x[i] += bullets_vel_x[i]
            bullets_y[i] += bullets_vel_y[i]

            # Check off screen
            off_screen = (
                bullets_x[i] < 0 or bullets_x[i] > SCREEN_WIDTH or
                bullets_y[i] < 0 or bullets_y[i] > SCREEN_HEIGHT
            )

            # Bullet collision with Enemy 1
            hit_enemy1 = math.hypot(bullets_x[i] - enemy1_x, bullets_y[i] - enemy1_y) < (bullet_radius + enemy1_radius)
            if hit_enemy1:
                enemy1_x = random.choice([50, SCREEN_WIDTH - 50])
                enemy1_y = random.choice([50, SCREEN_HEIGHT - 50])

            # Bullet collision with Enemy 2
            hit_enemy2 = math.hypot(bullets_x[i] - enemy2_x, bullets_y[i] - enemy2_y) < (bullet_radius + enemy2_radius)
            if hit_enemy2:
                enemy2_x = 0.0 if enemy2_vel_x < 0 else float(SCREEN_WIDTH)
                enemy2_y = float(random.randint(100, SCREEN_HEIGHT - 100))
                enemy2_vel_x = -enemy2_vel_x

            # Bullet collision with Enemy 3
            hit_enemy3 = math.hypot(bullets_x[i] - enemy3_x, bullets_y[i] - enemy3_y) < (bullet_radius + enemy3_radius)
            if hit_enemy3:
                frame_count += 300

            if off_screen or hit_enemy1 or hit_enemy2 or hit_enemy3:
                bullets_x.pop(i)
                bullets_y.pop(i)
                bullets_vel_x.pop(i)
                bullets_vel_y.pop(i)

        # Collision: Player and Food
        dist_to_food = math.hypot(player_x - food_x, player_y - food_y)
        if dist_to_food < player_radius + food_radius:
            score += 1
            if score >= 10:
                game_state = "WIN"
            else:
                food_x = random.randint(food_radius, SCREEN_WIDTH - food_radius)
                food_y = random.randint(food_radius, SCREEN_HEIGHT - food_radius)

        # Collision: Player and Enemies
        dist_to_enemy1 = math.hypot(player_x - enemy1_x, player_y - enemy1_y)
        dist_to_enemy2 = math.hypot(player_x - enemy2_x, player_y - enemy2_y)
        dist_to_enemy3 = math.hypot(player_x - enemy3_x, player_y - enemy3_y)

        if (dist_to_enemy1 < player_radius + enemy1_radius or
            dist_to_enemy2 < player_radius + enemy2_radius or
            dist_to_enemy3 < player_radius + enemy3_radius):
            lives -= 1
            player_x = random.randint(player_radius, SCREEN_WIDTH - player_radius)
            player_y = random.randint(player_radius, SCREEN_HEIGHT - player_radius)
        if lives < 1:
            game_state = "LOSE"

    # Drawing / Rendering
    screen.fill(LIGHT_BLUE)

    # Draw Game Elements
    pygame.draw.circle(screen, GREEN, (food_x, food_y), food_radius)
    pygame.draw.circle(screen, RED, (int(enemy1_x), int(enemy1_y)), enemy1_radius)
    pygame.draw.circle(screen, PURPLE, (int(enemy2_x), int(enemy2_y)), enemy2_radius)
    pygame.draw.circle(screen, ORANGE, (int(enemy3_x), int(enemy3_y)), enemy3_radius)
    
    # Draw Bullets
    for i in range(len(bullets_x)):
        pygame.draw.circle(screen, DARK_GRAY, (int(bullets_x[i]), int(bullets_y[i])), bullet_radius)

    # Draw Player
    pygame.draw.circle(screen, BLACK, (int(player_x), int(player_y)), player_radius)

    # Scoreboard
    score_surface = text_font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_surface, (10, 10))

    # Lives
    lives_surface = text_font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(lives_surface, (10, 40))

    # Win/Lose
    if game_state == "WIN":
        win_text = text_font.render("YOU WIN!", True, GREEN)
        text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(win_text, text_rect)
    elif game_state == "LOSE":
        lose_text = text_font.render("GAME OVER", True, RED)
        text_rect = lose_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(lose_text, text_rect)

    pygame.display.flip()

    # Cap frame rate
    clock.tick(FPS)

# Clean up and exit
pygame.quit()
sys.exit()