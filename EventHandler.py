import pygame as pg
from pygame.locals import *
from config import screen_height

class EventHandler:
    def __init__(self) -> None:
        self.score = 0

    def update_score_car(self, object):
        self.score += 20

event_handler = EventHandler()