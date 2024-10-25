import pygame as pg
from pygame.locals import *
import random
from sys import exit

pg.init()

# Configuração da tela
screen_width = 1280
screen_height = 720
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Skatehelp')

# Array com as imagens dos carros
car_image_array = []
for i in range(13):
    car_image = pg.image.load(f"./assets/icons/cars/car#{i}.png").convert()
    car_image = pg.transform.scale(car_image, (108.4, 159.7))
    car_image_array.append(car_image)

# Classe do Carro
class Car():
    def __init__(self):
        self.position = pg.math.Vector2(480, -170)
        self.speed = 2
        self.image = car_image_array[12]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        if self.position.y >= screen_height + 170:
            self.position.y = -170
        self.position.y += self.speed
        self.rect.center = self.position
    
    def draw(self):
        screen.blit(self.image, self.rect)

def main():
    clock = pg.time.Clock()
    running = True

    car = Car()

    # Carregar a imagem de fundo
    background = pg.image.load("./assets/bgs/bg#0.jpg").convert()
    background = pg.transform.scale(background, (screen_width, screen_height))

    # Variáveis para o movimento do fundo
    background_y = 0
    background_speed = 2

    while running:
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
        
        # Atualiza a posição do fundo
        background_y += background_speed
        if background_y >= screen_height:
            background_y -= screen_height

        # Desenha o fundo
        screen.blit(background, (0, background_y))
        screen.blit(background, (0, background_y - screen_height))

        car.update()
        car.draw()
        
        # Atualiza a tela
        pg.display.flip()
        clock.tick(60) # 60 frames por segundo

    pg.quit()
    exit()

if __name__ == "__main__":
    main()
