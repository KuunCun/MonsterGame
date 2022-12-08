import pygame
from typing import List, Tuple
from random import randint
from .baseobject import BaseObject
from .bullet import Bullet
from .player import Player
from .monster import Monster
from time import perf_counter


# This is for bullet delay
__last_bullet_time: float = perf_counter()


def update_objects(sc: pygame.Surface, objs: list[BaseObject]):
    for obj in objs:  # Iter over all objects
        obj.update_position()

        if obj.should_blitted:  # If object should be blitted:
            obj.blit(sc)  # Draw the object


# Spawn bullets (spawn point set to player's top left corner)
def create_bullet(bullets: List[Bullet], player: Player, bullet_speed: float, mouse_prssd: bool, delay: int):
    global __last_bullet_time
    # If mause button pressed and
    # check if delay between bullets has passed (delay is in miliseconds)
    if mouse_prssd and (perf_counter() - __last_bullet_time) * 1000 > delay:
        bullets.append(Bullet(
            player.xpos,
            player.ypos,
            bullet_speed,
            pygame.mouse.get_pos()
        ))
        __last_bullet_time = perf_counter()


# Spawns a monster at given chance
def create_monster(monsters: List[Monster], sc_size: Tuple[int, int], mon_speed: float, monster_chance: int):
    if randint(0, monster_chance) == 0:
        monsters.append(Monster(
            sc_size,
            mon_speed
        ))


# Iterate over all bullets and destroy out of screen ones
def destoy_bullets(bullets: List[Bullet], sc_size: Tuple[int, int]):
    # Use reversed range because if you delete from start of the list,
    # The indexes of all list members after the deleted member will change.
    for i in range(len(bullets)-1, -1, -1):
        if bullets[i].xpos < 0 or bullets[i].xpos > sc_size[0]:
            del bullets[i]
        elif bullets[i].ypos < 0 or bullets[i].ypos > sc_size[1]:
            del bullets[i]


# Iterate over all monsters and destroy out of screen ones
def destroy_monsters(monsters: List[Monster], sc_size: Tuple[int, int]):
    for i in range(len(monsters)-1, -1, -1):
        if monsters[i].ypos > sc_size[1]:
            del monsters[i]


# Iterate over all bullets and monsters and detect collisions
# If a collision detected, destroy colliding objects (bullet and monster)
def detect_bullet_monster_collisions(bullets: List[Bullet], monsters: List[Monster]):
    for i in range(len(bullets)-1, -1, -1):
        collided = False
        for x in range(len(monsters)-1, -1, -1):
            if bullets[i].rect.colliderect(monsters[x].rect):
                del bullets[i]
                del monsters[x]
                collided = True
                break  # Break because one bullet can collide with one monster at most, no need to iterate more
        if collided:
            continue
