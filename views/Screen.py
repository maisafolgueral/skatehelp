import pygame as pg
from pygame.locals import *
from config import screen_height, screen_width

class Screen():
    def __init__(self, event_handler):
        self.event_handler = event_handler

        # Configuração da tela
        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption('Skatehelp')
        
        # Variáveis para movimento do background
        self.background_y = 0
        self.background_speed = 1
        
        # Carregar a imagem de fundo
        self.background = pg.image.load("./assets/bgs/bg#0.jpg")
        self.background = pg.transform.scale(self.background, (screen_width, screen_height))

        self.font = pg.font.SysFont('Consolas', 36)

    # Desenha o fundo
    def draw_background(self, internal_clock):
        self.move_background(internal_clock)
        self.screen.blit(self.background, (0, self.background_y))
        self.screen.blit(self.background, (0, self.background_y - screen_height))

    # Atualiza a posição do fundo
    def move_background(self, internal_clock):
        self.background_y += (self.background_speed * internal_clock)
        if self.background_y >= screen_height:
            self.background_y -= screen_height

    # Mostra o placar do jogo
    def draw_score(self):
        score = self.event_handler.score
        text_surface = self.font.render(f'SCORE: {score}', True, (255,255,255))
        self.screen.blit(text_surface, (10, screen_height - 40))

    # Mostrar o menu.
    def show_menu(self):
        text_surface = self.font.render('PRESS SPACE TO PLAY', True, (255,255,255))
        self.screen.fill((0,0,0))
        self.screen.blit(text_surface, (screen_width / 2.85, screen_height / 2.10))
        pg.display.flip()

    # Mostrar o menu.
    def show_game_over_screen(self):
        text_surface = self.font.render('GAME OVER', True, (255,255,255))
        self.screen.fill((0,0,0))
        self.screen.blit(text_surface, (screen_width / 2.35, screen_height / 2))
        pg.display.flip()

    # Mostra todos os objetos
    def draw_all(self, internal_clock):
        self.draw_background(internal_clock)
        self.draw_score()
