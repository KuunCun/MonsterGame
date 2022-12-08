import pygame
from typing import Tuple
from math import pow, sqrt

from .baseobject import BaseObject


class Bullet(BaseObject):
    def __init__(
            self,
            xpos: float,
            ypos: float,
            base_velocity: float,
            m_pos: Tuple[int, int]
    ):
        # Calculate the triangle and vector lenghts between
        # spawn position and mouse cursor position
        dist_x = m_pos[0] - xpos
        dist_y = m_pos[1] - ypos
        hypo = sqrt(pow(dist_x, 2) + pow(dist_y, 2))

        super().__init__(
            surface=pygame.image.load("imgs/bullet.jpg"),
            xpos=xpos,
            ypos=ypos,
            velocity_x=(base_velocity * dist_x / hypo),  # basically sum of vectors * cos(a)
            velocity_y=(base_velocity * dist_y / hypo)   # basically sum of vectors * sin(a)
        )
