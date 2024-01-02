import pygame

import sys

class Game:
    def __init__(self) -> None:

        pygame.init()

        pygame.display.set_caption("Platforming game")
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 800

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load('jumpty-dumpty/data/images/clouds/cloud_1.png')
        self.image_pos = [100, 200]

    def run(self):

        player = pygame.Rect((300, 250, 50, 50))
        run = True
        while run:

            self.screen.blit(self.image, self.image_pos)

            pygame.display.update()
            # Force 60 fps maximum
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            pygame.draw.rect(self.screen, (255, 0, 0), player)

            # Key handling
            key = pygame.key.get_pressed()
            if key[pygame.K_a] == True:
                player.move_ip(-1, 0)
            elif key[pygame.K_d] == True:
                player.move_ip(1, 0)
            elif key[pygame.K_w] == True:
                player.move_ip(0, -1)
            elif key[pygame.K_s] == True:
                player.move_ip(0, 1)

            # Iterate over all inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
    
Game().run()