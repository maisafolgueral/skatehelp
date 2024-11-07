import pygame as pg
from pygame.locals import *
from sys import exit
from config import *
from models import Car
from models.Skater import Skater
from views import Screen

pg.init()

def main():
    clock = pg.time.Clock()
    running = True

    all_sprites = pg.sprite.Group()
    car_spawn_timer = 0

    screen = Screen.Screen()

    # Adiciona a Dona Telma
    skater = Skater()
    all_sprites.add(skater)

    while running:
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
        
        car_spawn_timer += internal_clock
    
        # Movimentação da Dona Telma 
        skater.handle_keys()
        
        # Gera os carros
        if car_spawn_timer == 180:
            Car.CarSpawn(all_sprites)
            car_spawn_timer = 0
        
        screen.draw_background()
        screen.draw_score()

        all_sprites.update()
        all_sprites.draw(screen.screen)
        

        # Atualiza a tela
        pg.display.flip()
        clock.tick(60) # 60 frames por segundo

    pg.quit()
    exit()

if __name__ == "__main__":
    main()