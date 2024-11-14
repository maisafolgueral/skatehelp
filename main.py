import pygame as pg
from pygame.locals import *
from sys import exit
from config import *
from models.Skater import Skater
from views import Screen
from EventHandler import EventHandler

pg.init()

def main():
    clock = pg.time.Clock()
    
    all_sprites = pg.sprite.Group()
    obstacle_sprites = pg.sprite.Group()

    event_handler = EventHandler()

    screen = Screen.Screen(event_handler)

    # Adiciona a Dona Telma.
    skater = Skater()
    all_sprites.add(skater)

    while event_handler.running:
        for event in pg.event.get():
            event_handler.quit_game(event)
        
        # Atualiza os timers de cada elemento gerador.
        event_handler.update_timers(internal_clock)

        # Movimentação da Dona Telma. 
        skater.handle_keys()
        
        # Gera todos os obstaculos no jogo.
        event_handler.spawn_obstacles(all_sprites, obstacle_sprites)
        
        # Gera o background e o placar do jogo.
        screen.draw_all()

        # Atualiza o jogo.
        all_sprites.update()
        all_sprites.draw(screen.screen)

        # Verificação de colisão
        event_handler.on_collide(skater, obstacle_sprites)

        # Atualiza a tela.
        pg.display.flip()
        clock.tick(60) # 60 frames por segundo.

    pg.quit()
    exit()

if __name__ == "__main__":
    main()