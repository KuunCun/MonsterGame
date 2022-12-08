import pygame
from typing import Tuple, Optional


class BaseObject:
    def __init__(
        self, 
        surface: pygame.Surface,  # Image comes here.
        xpos: float = 0,  # X position
        ypos: float = 0,  # Y position
        velocity_x: float = 0,  # horizontal speed
        velocity_y: float = 0,  # vertical speed
        should_blitted: bool = True,  # Should ı blit the object?
    ) -> None:
        # Burada class değişkenlerimizin atamasını yapıyoruz.
        self.surface: pygame.Surface = surface
        self.xpos = xpos
        self.ypos = ypos
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.should_blitted = should_blitted

        # This rectangle is necessary for collisions
        # I won't draw rectangles but they need to surround the image
        self.rect = pygame.Rect(self.xpos, self.ypos, self.surface.get_width(), self.surface.get_height())

    def blit(self, main_screen: pygame.Surface):
        main_screen.blit(self.surface, (self.xpos, self.ypos))

    def update_position(self):
        
        # Update image's pozition
        self.xpos += self.velocity_x
        self.ypos += self.velocity_y

        # Update rectangle's position
        self.rect.x = self.xpos
        self.rect.y = self.ypos
