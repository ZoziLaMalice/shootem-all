import pygame
from game import Game
import math

pygame.init()

# Init window
pygame.display.set_caption("My first Python Game!")
screen = pygame.display.set_mode((1380, 820))

# Loading background
background = pygame.image.load('assets/jungle.jpg')

# Loading Banner
banner = pygame.image.load('assets_base/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.2)

# Loading Play Button
play_button = pygame.image.load('assets/play.png')
play_button = pygame.transform.scale(play_button, (150, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(banner_rect.x + banner_rect.x * 0.5 - 35)
play_button_rect.y = math.ceil(screen.get_height() - 450)

# Loading game
game = Game()

running = True

# Infinite loop to run the game
while running:
    # Display background
    screen.blit(background, (0, 0))

    # Check if is playing
    if game.is_playing:
        game.update(screen)
    else:
        # Welcome Screen
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Update the display
    pygame.display.flip()

    # Get actions from the player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_bullet()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()