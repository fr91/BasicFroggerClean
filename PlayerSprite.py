import pygame
import SpriteSheet


class PlayerSprite(pygame.sprite.Sprite):

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    walking_frames_d = []

    # constructor
    def __init__(self, game_screen, x_position, y_position, update_player, direction, hit, collide, win):
        self.game_screen = game_screen
        self.speed_init = 10
        self.speed = self.speed_init
        self.pos = 2
        self.x_position = x_position
        self.y_position = y_position
        self.change_x = 0
        self.change_y = 0
        self.direction = direction
        self.update_player = update_player
        self.collide = collide
        self.hit = hit
        self.win = win

        # call parent constructor
        super().__init__()
        sprite_sheet = SpriteSheet.SpriteSheet("Animal.png")
        # load all images facing right
        image = sprite_sheet.get_image(0, 72, 32, 27, (120, 195, 128))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(64, 72, 32, 27, (120, 195, 128))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(32, 72, 32, 27, (120, 195, 128))
        self.walking_frames_r.append(image)

        # load all images facing left
        image = sprite_sheet.get_image(0, 40, 32, 27, (120, 195, 128))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(64, 40, 32, 27, (120, 195, 128))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(32, 40, 32, 27, (120, 195, 128))
        self.walking_frames_l.append(image)

        # load all images facing up
        image = sprite_sheet.get_image(0, 101, 32, 27, (120, 195, 128))
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(64, 101, 32, 27, (120, 195, 128))
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(32, 101, 32, 27, (120, 195, 128))
        self.walking_frames_u.append(image)

        # load all images facing down
        image = sprite_sheet.get_image(0, 5, 32, 27, (120, 195, 128))
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(64, 5, 32, 27, (120, 195, 128))
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(32, 5, 32, 27, (120, 195, 128))
        self.walking_frames_d.append(image)

        # set the image the player starts with
        self.image = self.walking_frames_u[self.pos]
        # set a reference to the image rect
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position

    # Update the player object
    def update(self, *args):
        if self.update_player == 0:
            if self.direction == 0:
                self.speed -= 1
                if self.speed == 0:
                    self.pos -= 1
                    self.image = self.walking_frames_u[self.pos]
                    self.move()
                    self.rect.y -= self.change_y
                    self.speed = self.speed_init
                    if self.pos < 0:
                        self.pos = 2
                        self.image = self.walking_frames_u[self.pos]
                        self.change_y = 0
                        self.update_player = 1

            if self.direction == 1:
                self.speed -= 1
                self.image = self.walking_frames_r[self.pos]
                if self.speed == 0:
                    self.pos -= 1
                    self.image = self.walking_frames_r[self.pos]
                    self.move()
                    self.rect.x += self.change_x
                    self.speed = self.speed_init
                    if self.pos < 0:
                        self.pos = 2
                        self.image = self.walking_frames_r[self.pos]
                        self.change_x = 0
                        self.update_player = 1

            if self.direction == 2:
                self.speed -= 1
                self.image = self.walking_frames_d[self.pos]
                if self.speed == 0:
                    self.pos -= 1
                    self.image = self.walking_frames_d[self.pos]
                    self.move()
                    self.rect.y += self.change_y
                    self.speed = self.speed_init
                    if self.pos < 0:
                        self.pos = 2
                        self.image = self.walking_frames_d[self.pos]
                        self.change_y = 0
                        self.update_player = 1

            if self.direction == 3:
                self.speed -= 1
                self.image = self.walking_frames_l[self.pos]
                if self.speed == 0:
                    self.pos -= 1
                    self.image = self.walking_frames_l[self.pos]
                    self.move()
                    self.rect.x -= self.change_x
                    self.speed = self.speed_init
                    if self.pos < 0:
                        self.pos = 2
                        self.image = self.walking_frames_l[self.pos]
                        self.change_x = 0
                        self.update_player = 1

        # check to see if sprite has collided with left side of screen
        if self.rect.x <= 0:
            self.rect.x = 0

        # check to see if sprite has collided with right side of screen
        if self.rect.x + 32 >= self.game_screen.get_width():
            self.rect.x = self.game_screen.get_width() - 32

        # check to see if sprite has collided with bottom of screen
        if self.rect.y + 27 >= self.game_screen.get_height():
            self.rect.y = self.game_screen.get_height() - 27

        # check to see if sprite has collided with top of screen
        if self.rect.y <= 0:
            self.reset()
            self.speed = self.speed_init
            self.win = 1

        # check to see if sprite has collided with water or log

        if self.collide != 0:
            if 297 > self.rect.y >= 243:
                self.rect.x -= 1

            if 243 > self.rect.y >= 189:
                self.rect.x += 1

            if 189 > self.rect.y >= 135:
                self.rect.x -= 1

            if 135 > self.rect.y >= 81:
                self.rect.x += 1

            if 81 > self.rect.y >= 54:
                self.rect.x -= 1

            if 54 > self.rect.y >= 27:
                self.rect.x += 1

        if 27 <= self.rect.y <= self.game_screen.get_height() - 405:
            if self.collide == 0:
                self.hit = 1
                if self.hit == 1:
                    self.reset()

    # defines how the player will move
    def move(self):
        self.change_y = (27/3)
        self.change_x = (32/3)

    # Stops the players movements
    def stop_moving(self):
        self.change_x = 0
        self.change_y = 0

    # updates changes in direction
    def change_direction(self, direction):
        self.direction = direction

    # resets position of player
    def reset(self):
        self.rect.x = self.x_position
        self.rect.y = self.y_position
        self.speed = self.speed_init
        self.update_player = 1
        self.pos = 2
        self.image = self.walking_frames_u[self.pos]
        self.hit = 0

    # sets collide flag
    def collide_with_log(self, collide):
        self.collide = collide
