import pygame as pg
from pygame.locals import *
from models import Car
from models import Person
from models import Skater

class EventHandler:
    def __init__(self) -> None:
        self.running = True
        self.menu_showing = True
        self.game_over = False
        self.score = 0
        self.car_spawn_timer = 0
        self.person_spawn_timer = 0

    def start_or_stop(self, event):
        if event.type == KEYDOWN and event.key == K_SPACE:
            self.menu_showing = False if self.menu_showing else True

    def quit_game(self, event):
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            self.running = False
            exit()
        
    def on_collide(self, skater, obstacles):
        if pg.sprite.spritecollideany(skater, obstacles):
            self.running = False
            self.game_over = True
    
    def update_score_car(self):
        self.score += 20

    def update_score_person(self):
        self.score += 5

    def update_timers(self, internal_clock):
        self.car_spawn_timer += internal_clock
        self.person_spawn_timer += internal_clock

    def spawn_cars(self, all_sprites, obstacle_sprites):
        if self.car_spawn_timer >= 180:
            Car.CarSpawn(all_sprites, obstacle_sprites, self)
            self.car_spawn_timer = 0

    def spawn_people(self, all_sprites, obstacle_sprites):
        if self.person_spawn_timer >= 180:
            Person.PersonSpawn(all_sprites, obstacle_sprites, self)
            self.person_spawn_timer = 0
    
    def spawn_obstacles(self, all_sprites, obstacle_sprites):
        self.spawn_cars(all_sprites, obstacle_sprites)
        self.spawn_people(all_sprites, obstacle_sprites)