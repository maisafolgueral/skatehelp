import pygame as pg
from pygame.locals import *
import random
from config import screen_height

# Array com as imagens dos carros
car_image_array = []
for i in range(13):
    car_image = pg.image.load(f"assets/icons/cars/car#{i}.png")
    car_image.set_colorkey((255, 255, 255))
    car_image_width = car_image.get_width()
    car_image_height = car_image.get_height()
    proportional_width = 185
    proportional_height = proportional_width * (car_image_height / car_image_width)
    car_image = pg.transform.scale(car_image, (proportional_width, proportional_height))
    car_image_array.append(car_image)

# Classe do Carro
class Car(pg.sprite.Sprite):
    def __init__(self, event_handler):
        super(Car,self).__init__()
        self.event_handler = event_handler
        self.alive = True
        self.image = random.choice(car_image_array)
        self.allowed_x_positions = [480, 800]
        self.position = pg.math.Vector2(random.choice(self.allowed_x_positions), -170)
        self.speed = 4
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        if self.alive == False or self.position.y >= screen_height + 180:
            print(self)
            self.event_handler.update_score_car()
            self.kill()

        self.position.y += self.speed
        self.rect.center = self.position
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

def CarSpawn(all_sprites, obstacle_sprites, event_handler):
    car = Car(event_handler)
    all_sprites.add(car)
    obstacle_sprites.add(car)