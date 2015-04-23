import pygame
import GameHandler
import Constants

# set variable
game_running = True

# initialize pygame
pygame.init()

# set up the program window

pygame.display.set_caption("Dogger")

# initialize the screen
game_screen = pygame.display.set_mode(Constants.screen_size, Constants.screen_flags, Constants.screen_depth)
game_handler = GameHandler.GameHandler(game_screen)
back_ground = pygame.image.load("BackgroundImage.jpg").convert()

# create the game clock
game_clock = pygame.time.Clock()

# main game loop

while game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            game_handler.process_event(event)

    # Do game logic
    game_handler.game_logic()

    # Clear the screen
    game_screen.fill(Constants.black)
    game_screen.blit(back_ground, [0, 0])

    # Draw game objects
    game_handler.draw_game_objects()

    # Draw the screen
    pygame.display.flip()

    # Frame-rate
    game_clock.tick(60)