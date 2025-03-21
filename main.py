# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True

    # Images
    backround_image = pygame.image.load("space.jpg").convert()
    player_image = pygame.image.load("ship.png").convert()
    player_image.set_colorkey((0,0,0))

    while running:
        running = handle_events()
        # screen.fill(config.WHITE) - Instead of a white backround!
        screen.blit(backround_image, (0, 0)) # Spaaaaaaaaaaaaceee!

        player_data = {
            'x' : pygame.mouse.get_pos()[0] - (player_image.get_width()/2),
            'y' : pygame.mouse.get_pos()[1] - (player_image.get_height()/2)
        }
        screen.blit(player_image, (player_data['x'], player_data['y']))
        pygame.display.flip()

        # Limit clock to FPS
        clock.tick(config.FPS)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()