import pygame as pg
from pygame.locals import *
import random
from config import screen_height
from EventHandler import event_handler

# Array com as imagens das pessoas
person_image_array = []
for i in range(3):
    person_image = pg.image.load(f"./assets/icons/people/person_{i}.png")
    person_image.set_colorkey((255, 255, 255))
    person_image_width = person_image.get_width()
    person_image_height = person_image.get_height()
    proportional_width = 70
    proportional_height = proportional_width * (person_image_height / person_image_width)
    person_image = pg.transform.scale(person_image, (proportional_width, proportional_height)) 
    person_image_array.append(person_image)

# Classe das pessoas
class Person(pg.sprite.Sprite):
    def __init__(self):
        super(Person,self).__init__()
        self.alive = True
        self.image = random.choice(person_image_array)
        self.allowed_x_positions = [285, 990]
        self.position = pg.math.Vector2(random.choice(self.allowed_x_positions), -170)
        self.speed = 1.5
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        if self.alive == False or self.position.y >= screen_height + 170:
            print(self)
            self.kill()
        
        self.position.y += self.speed
        self.rect.center = self.position
   
    def draw(self, screen):
        screen.blit(self.image, self.rect)

def PersonSpawn(all_sprites):
    person = Person()
    all_sprites.add(person)