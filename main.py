import pygame
import src

from typing import List


# FPS
FPS = 60
clock = pygame.time.Clock()


PLAYER_SPEED    = 7     # pixel per frame
BULLET_SPEED    = 10      # pixel per frame
BULLET_DELAY    = 300    # miliseconds
MONSTER_SPEED   = 4      # pixel per frame
MONSTER_CHANCE  = 300    # 1 / x per frame (lower is more chance)

FULL_SCREEN     = False  # True if you want to play in fullscreen
PREFERRED_SIZE  = (900, 600)
SCREEN_SIZE     = (0, 0) if FULL_SCREEN else PREFERRED_SIZE


def mainloop():
    pygame.init()
    pygame.display.set_caption("Monsters")
    pygame.key.set_repeat(1, 15)  # Keyboard btn repeat 1 ms, 15 ms

    screen = pygame.display.set_mode(
        SCREEN_SIZE,
        pygame.FULLSCREEN if FULL_SCREEN else 0,
        vsync=1
    )
    player = src.Player(
        xpos        = (SCREEN_SIZE[0] / 2),  # Spawns in the middle of the screen
        ypos        = (SCREEN_SIZE[1] / 2),
        velocity_x  = PLAYER_SPEED,
        velocity_y  = PLAYER_SPEED
    )

    # For checking collisions and screen boundaries
    bullets:    List[src.Bullet]    = []  # Empty bullets list
    monsters:   List[src.Monster]   = []  # Empty monsters list

    is_mouse_pressed = False
    running          = True

    while running:
        pm_flags = src.Direction.BLANK  # empty player movements flag
        screen.fill((0, 0, 0))          # Fill screen with black (delete everything on screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            # For the multikey player movement
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                # Assing flags with bitwise or
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    pm_flags |= src.Direction.LEFT
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    pm_flags |= src.Direction.DOWN
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    pm_flags |= src.Direction.RIGHT
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    pm_flags |= src.Direction.UP

            # For shooting while holding mouse buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                is_mouse_pressed = False

        # Move the player and draw/blit to screen
        player.player_movement(pm_flags, SCREEN_SIZE[0], SCREEN_SIZE[1])
        screen.blit(player.surface, (player.xpos, player.ypos))

        # Create a bullet, update all bullets' positions and destroy all out-of-screen bullets
        src.create_bullet(bullets, player, BULLET_SPEED, is_mouse_pressed, BULLET_DELAY)
        src.update_objects(screen, bullets)
        src.destoy_bullets(bullets, SCREEN_SIZE)

        # Create a monster, update all mosters' positions and destroy all out-of-screen monsters
        src.create_monster(monsters, SCREEN_SIZE, MONSTER_SPEED, MONSTER_CHANCE)
        src.update_objects(screen, monsters)
        src.destroy_monsters(monsters, SCREEN_SIZE)

        # Very simple rectangle collision detection
        # Collided bullets and monsters are deleted
        src.detect_bullet_monster_collisions(bullets, monsters)

        # Update the display
        pygame.display.flip()
        # Fixed FPS
        clock.tick(FPS)


if __name__ == "__main__":
    mainloop()
