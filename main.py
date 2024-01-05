import pygame

import sys

from scripts.utils import load_image
from scripts.utils import load_images
from scripts.tilemap import TileMap
from scripts.entity import PhysicsEntity

class Game:
    def __init__(self) -> None:

        pygame.init()

        pygame.display.set_caption("Platforming game")
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 800

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((400, 400))

        # Player image
        self.assets = {
            'decor' : load_images('tiles/decor'),
            'grass' : load_images('tiles/grass'),
            'large_decor' : load_images('tiles/large_decor'),
            'stone' : load_images('tiles/stone'),
            'player' : load_image('entities/player.png')
        } 

        print(self.assets)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8 ,15)) 

        self.movement = [False, False]

        self.tilemap = TileMap(self, tile_size=16)

    def run(self):
        run = True
        while run:

            # Force 60 fps maximum
            self.clock.tick(60)

            # Render background
            self.display.fill((14, 219, 248))
            
            # Render the tilemap
            self.tilemap.render(self.display)

            # Render and move the player
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            

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
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()

Game().run()