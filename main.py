import pygame

import sys

from scripts.utils import load_image
from scripts.utils import load_images
from scripts.tilemap import TileMap
from scripts.entity import PhysicsEntity, Player
from scripts.utils import Animation
from scripts.clouds import Cloud
from scripts.clouds import Clouds

class Game:
    def __init__(self) -> None:

        pygame.init()

        pygame.display.set_caption("Platforming game")
        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 480

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((320, 240))

        # Player image
        self.assets = {
            'decor' : load_images('tiles/decor'),
            'grass' : load_images('tiles/grass'),
            'large_decor' : load_images('tiles/large_decor'),
            'stone' : load_images('tiles/stone'),
            'player' : load_image('entities/player.png'),
            'background' : load_image('background.png'),
            'clouds' : load_images('clouds'),
            'player/idle' : Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run' : Animation(load_images('entities/player/run'), img_dur=4),
            'player/jump' : Animation(load_images('entities/player/jump')),
            'player/slide' : Animation(load_images('entities/player/slide')),
            'player/wall_slide' : Animation(load_images('entities/player/wall_slide')),
        }

        self.clouds = Clouds(self.assets['clouds'], 16) 

        print(self.assets)

        self.player = Player(self, (50, 50), (8 ,15)) 

        self.movement = [False, False]

        self.tilemap = TileMap(self, tile_size=16)

        self.scroll = [0, 0]

    def run(self):
        run = True
        while run:

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_width() / 2 - self.scroll[1]) / 30

            render_scroll = (int(self.scroll[0]) , int(self.scroll[1]))

            # Force 60 fps maximum
            self.clock.tick(60)

            # Render background
            self.display.blit(self.assets['background'], (0, 0))

            # Render Clouds
            self.clouds.update()
            self.clouds.render(surface=self.display, offset=render_scroll)
            
            # Render the tilemap
            self.tilemap.render(self.display, offset=render_scroll)

            # Render and move the player
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            

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