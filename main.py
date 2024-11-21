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
    timer = 0
    internal_clock = 1
    
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
            event_handler.start_or_stop(event)
            
            while event_handler.menu_showing:
                pg.time.delay(100) # delay para impedir o jogo de crashar
                for event in pg.event.get():
                    event_handler.quit_game(event)
                    event_handler.start_or_stop(event)
                screen.show_menu()

        timer+=1 # 60 incrementos a cada segundo (60 fps)
        if timer >= 300: # A cada x segundos aumenta a velocidade do jogo - 300=5s ou 3600=1min
            internal_clock += 1
            timer = 0

        # Atualiza os timers de cada elemento gerador.
        event_handler.update_timers(internal_clock)

        # Movimentação da Dona Telma. 
        skater.handle_keys()
        
        # Gera todos os obstaculos no jogo.
        event_handler.spawn_obstacles(all_sprites, obstacle_sprites)
        
        # Gera o background e o placar do jogo.
        screen.draw_all(internal_clock)

        # Atualiza o jogo.
        all_sprites.update(internal_clock)
        all_sprites.draw(screen.screen)

        # Verificação de colisão
        event_handler.on_collide(skater, obstacle_sprites)

        # Atualiza a tela.
        pg.display.flip()
        clock.tick(60) # 60 frames por segundo.

    while event_handler.game_over:
        pg.time.delay(100) # delay para impedir o jogo de crashar
        screen.show_game_over_screen()
        for event in pg.event.get():
            if event.type == KEYDOWN and event.key == K_r:
                main()
            event_handler.quit_game(event)

    pg.quit()
    exit()

if __name__ == "__main__":
    main()