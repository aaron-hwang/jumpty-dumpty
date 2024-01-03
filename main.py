import pygame

import sys

from scripts.utils import load_image
from scripts.entity import PhysicsEntity

class Game:
    def __init__(self) -> None:

        pygame.init()

        pygame.display.set_caption("Platforming game")
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 800

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # Player image
        self.assets = {
            'player' : load_image('entities/player.png')
        } 

        self.player = PhysicsEntity(self, 'player', (50, 50), (8 ,15)) 

        self.movement = [False, False]

    def run(self):
        run = True
        while run:

            # Force 60 fps maximum
            self.clock.tick(60)

            self.screen.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

            # Iterate over all inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            pygame.display.update()
    
Game().run()