from models import Car
from models import Person
from pygame.locals import *
from config import screen_height

class EventHandler:
    def __init__(self) -> None:
        self.running = True
        self.score = 0
        self.car_spawn_timer = 0
        self.person_spawn_timer = 0

    def quit_game(self, event):
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            self.running = False
    
    def update_score_car(self):
        self.score += 20

    def update_score_person(self):
        self.score += 5

    def update_timers(self, internal_clock):
        self.car_spawn_timer += internal_clock
        self.person_spawn_timer += internal_clock

    def spawn_cars(self, all_sprites):
        if self.car_spawn_timer == 180:
            Car.CarSpawn(all_sprites, self)
            self.car_spawn_timer = 0

    def spawn_people(self, all_sprites):
        if self.person_spawn_timer == 180:
            Person.PersonSpawn(all_sprites, self)
            self.person_spawn_timer = 0
    
    def spawn_obstacles(self, all_sprites):
        self.spawn_cars(all_sprites)
        self.spawn_people(all_sprites)