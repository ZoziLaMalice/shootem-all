import pygame
from player import Player
from monster import Monster

class Game():
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # Reset Game
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False


    def update(self, screen):
        # Display player
        screen.blit(self.player.image, self.player.rect)

        # Update life status
        self.player.update_health_bar(screen)

        # Move the bullets
        for bullet in self.player.all_bullets:
            bullet.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # Display the bullets
        self.player.all_bullets.draw(screen)# Draw the bullet on the background

        # Display monsters
        self.all_monsters.draw(screen)

        # Moving player
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)