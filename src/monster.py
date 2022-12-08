import pygame
from typing import Tuple
from random import randint
from .baseobject import BaseObject


class Monster(BaseObject):
    def __init__(
            self,
            screen_size: Tuple[int, int],
            base_speed: float
    ):
        super().__init__(
            surface=pygame.image.load("imgs/monster.png"),
            xpos=randint(0, screen_size[0]),  # Randomize spawn position on the x-axis
            ypos=-60,
            velocity_y=base_speed
        )
