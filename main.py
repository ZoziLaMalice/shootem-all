import pygame
from game import Game

pygame.init()

# Init window
pygame.display.set_caption("My first Python Game!")
screen = pygame.display.set_mode((1380, 820))

# Loading background
background = pygame.image.load('assets/jungle.jpg')

# Loading game
game = Game()

running = True

# Infinite loop to run the game
while running:
    # Display player & background
    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)

    game.player.update_health_bar(screen)

    # Move the bullets
    for bullet in game.player.all_bullets:
        bullet.move()

    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Display the bullets
    game.player.all_bullets.draw(screen)# Draw the bullet on the background

    # Display monsters
    game.all_monsters.draw(screen)

    # Moving player
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Flip the display
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