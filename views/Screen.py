import pygame as pg
from pygame.locals import *
from config import screen_height, screen_width
from EventHandler import event_handler

class Screen():
    def __init__(self):
        # Configuração da tela
        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption('Skatehelp')
        
        # Variáveis para movimento do background
        self.background_y = 0
        self.background_speed = 2
        
        # Carregar a imagem de fundo
        self.background = pg.image.load("./assets/bgs/bg#0.jpg")
        self.background = pg.transform.scale(self.background, (screen_width, screen_height))

    # Desenha o fundo
    def draw_background(self):
        self.move_background()
        self.screen.blit(self.background, (0, self.background_y))
        self.screen.blit(self.background, (0, self.background_y - screen_height))

    # Atualiza a posição do fundo
    def move_background(self):
        self.background_y += self.background_speed
        if self.background_y >= screen_height:
            self.background_y -= screen_height

    # Mostra o placar do jogo
    def draw_score(self):
        score = event_handler.score

        font = pg.font.SysFont('Consolas', 36)
        text_surface = font.render(f'SCORE: {score}', True, (255,255,255))
        self.screen.blit(text_surface, (10, screen_height - 40))

