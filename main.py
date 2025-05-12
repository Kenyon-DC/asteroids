import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # Instantiate Player at screen center
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        # Update player state
        updatable.update(dt)
        # Draw Player
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = Clock.tick(60)/1000



if __name__ == "__main__":
    main()