import pygame
from enum import Flag, auto
from typing import Optional, Tuple

from .baseobject import BaseObject


# Directions ENUM FLAG
class Direction(Flag):
    BLANK = auto()
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()


class Player(BaseObject):
    def __init__(
        self,
        xpos: float = 0, 
        ypos: float = 0, 
        velocity_x: float = 0,
        velocity_y: float = 0,
    ) -> None:
        super().__init__(
            pygame.image.load("imgs/player.png"), 
            xpos, ypos,
            velocity_x,
            velocity_y,
        )

    # Update player's position according to flags
    # This way player can move both in X and Y axis on the same frame
    def player_movement(self, flags: Direction, s_width: int, s_height: int):
        if Direction.UP in flags and self.ypos - self.velocity_y > 0:
            self.ypos -= self.velocity_y
        if Direction.DOWN in flags and self.ypos + self.velocity_y < s_height:
            self.ypos += self.velocity_y
        if Direction.RIGHT in flags and self.xpos + self.velocity_x < s_width:
            self.xpos += self.velocity_x
        if Direction.LEFT in flags and self.xpos - self.velocity_x > 0:
            self.xpos -= self.velocity_x
