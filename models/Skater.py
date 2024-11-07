import pygame as pg
from pygame.locals import *
from config import screen_width, screen_height

# Classe do Skater
class Skater(pg.sprite.Sprite):
    def __init__(self):
        super(Skater,self).__init__()
        self.image = pg.image.load("./assets/icons/skater/skater_0.png").convert()
        self.image.set_colorkey((255, 255, 255)) # Faz o png ficar transparente
        self.image = pg.transform.scale_by(self.image, 0.12) # Faz o scale proporcional da imagem
        self.position = pg.math.Vector2(screen_width // 2, screen_height - 100)
        self.speed = 5
        self.rect = self.image.get_rect(center=self.position)

    def handle_keys(self):
        keys = pg.key.get_pressed()
        if keys[K_LEFT]:
            self.position.x -= self.speed
        if keys[K_RIGHT]:
            self.position.x += self.speed
        if keys[K_UP]:
            self.position.y -= self.speed
        if keys[K_DOWN]:
            self.position.y += self.speed

        # Limita o movimento do jogador dentro da tela
        self.position.x = max(0, min(screen_width - self.rect.width, self.position.x))
        self.position.y = max(0, min(screen_height - self.rect.height, self.position.y))
        
        self.rect.center = self.position

    def draw(self):
        screen.blit(self.image, self.rect)
