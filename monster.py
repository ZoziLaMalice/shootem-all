import pygame
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(1, 4)
        self.image = pygame.image.load("assets/goofy.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 575
        self.origin_image = self.image
        self.angle = 0

    def update_health_bar(self, surface):
        # Draw health bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 25, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 25, self.rect.y - 20, self.health, 5])

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            # Spawn to another monster
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 4)


    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)