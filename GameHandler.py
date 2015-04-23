import pygame
import PlayerSprite
import VehicleSprite
import WaterSprite
import Game_Text


class GameHandler(object):
    # constructor
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.all_game_sprites = pygame.sprite.Group()
        self.vehicle = pygame.sprite.Group()
        self.water_sprites = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        center_width = self.game_screen.get_width() / 2
        self.game_ended = 0
        self.user_input = None
        self.game_text = []
        self.point = 0
        self.player_life = 3
        self.speed = 10
        self.speed_countdown = self.speed
        self.make_more_rafts = None
        self.game_ended = 0

        # create raft sprite
        self.raft = WaterSprite.WaterSprite(self.game_screen, 0, game_screen.get_width(),
                                            self.game_screen.get_height() - 405)
        self.water_sprites.add(self.raft)
        self.all_game_sprites.add(self.raft)
        self.more_raft = self.raft

        # create vehicle sprites
        self.vehicle_one = VehicleSprite.Vehicle(self.game_screen, 1, center_width, self.game_screen.get_height() - 108,
                                                 "car1.png", 4, 72,
                                                 64, 54)
        self.all_game_sprites.add(self.vehicle_one)
        self.vehicle.add(self.vehicle_one)

        self.vehicle_one_two = VehicleSprite.Vehicle(self.game_screen, 1, center_width + 256,
                                                     self.game_screen.get_height() - 108,
                                                     "car1.png", 4, 72, 64, 54)

        self.all_game_sprites.add(self.vehicle_one_two)
        self.vehicle.add(self.vehicle_one_two)

        self.vehicle_one_three = VehicleSprite.Vehicle(self.game_screen, 1, center_width - 256,
                                                       self.game_screen.get_height() - 108,
                                                       "car1.png", 4, 72, 64, 54)
        self.all_game_sprites.add(self.vehicle_one_three)
        self.vehicle.add(self.vehicle_one_three)

        self.vehicle_two = VehicleSprite.Vehicle(self.game_screen, 0, center_width - 320,
                                                 self.game_screen.get_height() - 162,
                                                 "car4.png", 4, 72,
                                                 64, 54)
        self.vehicle.add(self.vehicle_two)
        self.all_game_sprites.add(self.vehicle_two)

        self.vehicle_two_two = VehicleSprite.Vehicle(self.game_screen, 0, center_width,
                                                     self.game_screen.get_height() - 162,
                                                     "car4.png", 4, 72, 64, 54)
        self.vehicle.add(self.vehicle_two_two)
        self.all_game_sprites.add(self.vehicle_two_two)

        self.vehicle_two_three = VehicleSprite.Vehicle(self.game_screen, 0, center_width + 320,
                                                       self.game_screen.get_height() - 162,
                                                       "car4.png", 4, 72, 64, 54)

        self.vehicle.add(self.vehicle_two_three)
        self.all_game_sprites.add(self.vehicle_two_three)

        self.vehicle_three = VehicleSprite.Vehicle(self.game_screen, 1, center_width - 128,
                                                   self.game_screen.get_height() - 216,
                                                   "car4.png", 4, 72, 64, 54)
        self.vehicle.add(self.vehicle_three)
        self.all_game_sprites.add(self.vehicle_three)

        self.vehicle_three_two = VehicleSprite.Vehicle(self.game_screen, 1, center_width + 64,
                                                       self.game_screen.get_height() - 216,
                                                       "car4.png", 4, 72, 64, 54)

        self.vehicle.add(self.vehicle_three_two)
        self.all_game_sprites.add(self.vehicle_three_two)

        self.vehicle_three_three = VehicleSprite.Vehicle(self.game_screen, 1, center_width + 256,
                                                         self.game_screen.get_height() - 216,
                                                         "car4.png", 4, 72, 64, 54)

        self.vehicle.add(self.vehicle_three_three)
        self.all_game_sprites.add(self.vehicle_three_three)

        self.vehicle_four = VehicleSprite.Vehicle(self.game_screen, 0, center_width - 128,
                                                  self.game_screen.get_height() - 270,
                                                  "car1.png", 4, 72,
                                                  64, 54)
        self.vehicle.add(self.vehicle_four)
        self.all_game_sprites.add(self.vehicle_four)

        self.vehicle_four_two = VehicleSprite.Vehicle(self.game_screen, 0, center_width + 256,
                                                      self.game_screen.get_height() - 270,
                                                      "car1.png", 4, 72, 64, 54)

        self.vehicle.add(self.vehicle_four_two)
        self.all_game_sprites.add(self.vehicle_four_two)

        self.vehicle_five = VehicleSprite.Vehicle(self.game_screen, 1, center_width,
                                                  self.game_screen.get_height() - 324,
                                                  "car4.png", 4, 72, 64, 54)

        self.vehicle.add(self.vehicle_five)
        self.all_game_sprites.add(self.vehicle_five)

        self.vehicle_five_two = VehicleSprite.Vehicle(self.game_screen, 1, center_width + 256,
                                                      self.game_screen.get_height() - 324,
                                                      "car4.png", 4, 72, 64, 54)

        self.vehicle.add(self.vehicle_five_two)
        self.all_game_sprites.add(self.vehicle_five_two)

        self.vehicle_five_three = VehicleSprite.Vehicle(self.game_screen, 1, center_width - 256,
                                                        self.game_screen.get_height() - 324,
                                                        "car4.png", 4, 72, 64, 54)

        self.vehicle.add(self.vehicle_five_three)
        self.all_game_sprites.add(self.vehicle_five_three)

        # create player sprite
        self.dog_frog = PlayerSprite.PlayerSprite(self.game_screen, center_width - 16,
                                                  self.game_screen.get_height() - 27, 0, None, 0, 0, 0)
        self.player_group.add(self.dog_frog)
        self.all_game_sprites.add(self.dog_frog)

        # create game text
        self.game_over = Game_Text.GameText(game_screen, center_width - 230, self.game_screen.get_height()
                                            - 50, "GAME OVER: Press Space to"" Try Again!", 35)

        self.game_text.append(self.game_over)

        self.you_win = Game_Text.GameText(game_screen, center_width - 200, 27,
                                          "You Win: Press Space to"" Try Again", 35)

        self.game_text.append(self.you_win)

        # The game has ended because the snake collided, change settings to reflect this
    def end_game(self):
        # First set the game_ended flag to be true
        self.game_ended = 1

        # remove dog from game
        self.all_game_sprites.remove(self.dog_frog)
        self.player_group.remove(self.dog_frog)
        # Next clear the direction changes list

    # reset the game to early values
    def reset_game(self):
        self.game_ended = 0
        self.player_life = 3
        self.dog_frog = PlayerSprite.PlayerSprite(self.game_screen, (self.game_screen.get_width() / 2) - 16,
                                                  self.game_screen.get_height() - 27, 0, None, 0, 0, 0)
        self.all_game_sprites.add(self.dog_frog)
        self.player_group.add(self.dog_frog)

    def game_logic(self):

        # If the game has ended do not do normal processing
        if self.game_ended == 1:
            return

        # set game_ended to 0 if player life hits 0
        if self.player_life == 0:
            self.end_game()

        if self.dog_frog.win == 1:
            self.end_game()

        # process water sprites
        if len(self.water_sprites) < 114:
            new_raft = self.more_raft.more_rafts()
            self.water_sprites.add(new_raft)
            self.all_game_sprites.add(new_raft)

        self.water_sprites.update()

        # process the player sprite movement
        self.dog_frog.change_direction(self.user_input)
        if self.dog_frog.update_player == 0:
            pass
        if self.dog_frog.update_player == 1:
            self.user_input = None

        self.vehicle.update()

        # check to see if player has collided with car
        if pygame.sprite.spritecollideany(self.dog_frog, self.vehicle):
            self.dog_frog.reset()
            self.player_life -= 1

        # collision with water
        if self.dog_frog.hit == 1:
            self.player_life -= 1

        # check to see if player has collided with raft
        if pygame.sprite.spritecollideany(self.dog_frog, self.water_sprites):
            self.dog_frog.collide_with_log(1)
        else:
            self.dog_frog.collide_with_log(0)

        self.player_group.update()

    def draw_game_objects(self):
        self.all_game_sprites.draw(self.game_screen)
        if self.game_ended == 1 and self.dog_frog.win == 1:
            self.game_text[1].game_object_draw()
        if self.game_ended == 1 and self.dog_frog.win == 0:
            self.game_text[0].game_object_draw()

    def process_event(self, event):
        # Move the player
        if event.type == pygame.KEYDOWN:
            if self.dog_frog.direction is None:
                if event.key == pygame.K_UP:
                    self.user_input = 0
                    self.dog_frog.update_player = 0
                if event.key == pygame.K_DOWN:
                    self.user_input = 2
                    self.dog_frog.update_player = 0
                if event.key == pygame.K_LEFT:
                    self.user_input = 3
                    self.dog_frog.update_player = 0
                if event.key == pygame.K_RIGHT:
                    self.user_input = 1
                    self.dog_frog.update_player = 0
            if event.key == pygame.K_SPACE and self.game_ended == 1:
                self.reset_game()
