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

# Array com as posições dos obstáculos da rua
items_positions = [480, 800]

# Array com as imagens dos carros
car_image_array = []
for i in range(13):
    car_image = pg.image.load(f"./assets/icons/cars/car#{i}.png").convert()
    car_image.set_colorkey((255, 255, 255))
    car_image = pg.transform.scale(car_image, (108.4, 159.7))
    car_image_array.append(car_image)

# Classe do Carro
class Car():
    def __init__(self):
        self.image = random.choice(car_image_array)
        self.position = pg.math.Vector2(random.choice(items_positions), -170)
        self.speed = 2
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        if self.position.y >= screen_height + 170:
            self.position.y = -170
            self.position.x = random.choice(items_positions)
            self.image = random.choice(car_image_array)
        self.position.y += self.speed
        self.rect.center = self.position
    
    def draw(self):
        screen.blit(self.image, self.rect)

# Classe do Player
class Player():
    def __init__(self):
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

def main():
    clock = pg.time.Clock()
    running = True

    car = Car()
    player = Player()

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

        # Atualiza e desenha o carro
        car.update()
        car.draw()
        
        # Atualiza e desenha o jogador
        player.handle_keys()
        player.draw()
        
        # Atualiza a tela
        pg.display.flip()
        clock.tick(60) # 60 frames por segundo

    pg.quit()
    exit()

if __name__ == "__main__":
    main()
