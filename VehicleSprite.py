import pygame
import SpriteSheet


class Vehicle(pygame.sprite.Sprite):

    # constructor
    def __init__(self, game_screen, direction, x_position, y_position, car_type, car_x_pos, car_y_pos,
                 car_x_size, car_y_size):
        self.driving_frames_l = []
        self.driving_frames_r = []
        self.game_screen = game_screen
        self.direction = direction
        self.speed_init = 10
        self.speed = self.speed_init
        self.pos = 0
        self.x_position = x_position
        self.y_position = y_position
        self.car_type = car_type
        self.car_x_pos = car_x_pos
        self.car_y_pos = car_y_pos
        self.car_x_size = car_x_size
        self.car_y_size = car_y_size
        self.change_x = 0
        self.change_y = 0

        # call the parent constructor
        super().__init__()
        sprite_sheet = SpriteSheet.SpriteSheet(self.car_type)
        # load all images facing left and add to left list
        image = sprite_sheet.get_image(self.car_x_pos, self.car_y_pos, self.car_x_size, self.car_y_size,
                                       (255, 255, 255))
        self.driving_frames_l.append(image)
        image = sprite_sheet.get_image(self.car_x_pos + 64, self.car_y_pos, self.car_x_size, self.car_y_size,
                                       (255, 255, 255))
        self.driving_frames_l.append(image)
        image = sprite_sheet.get_image(self.car_x_pos + 128, self.car_y_pos, self.car_x_size, self.car_y_size,
                                       (255, 255, 255))
        self.driving_frames_l.append(image)
        image = sprite_sheet.get_image(self.car_x_pos + 192, self.car_y_pos, self.car_x_size, self.car_y_size,
                                       (255, 255, 255))
        self.driving_frames_l.append(image)

        # flip all images facing left and add to right list
        image = sprite_sheet.get_image(self.car_x_pos, self.car_y_pos, self.car_x_size, self.car_y_size,
                                       (255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.driving_frames_r.append(image)
        image = sprite_sheet.get_image(self.car_x_pos + 64, self.car_y_pos, self.car_x_size, self.car_y_size,
                                       (255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.driving_frames_r.append(image)
        image = sprite_sheet.get_image(self.car_x_pos + 128, self.car_y_pos, self.car_x_size, self.car_y_size,
                                       (255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.driving_frames_r.append(image)
        image = sprite_sheet.get_image(self.car_x_pos + 192, self.car_y_pos, self.car_x_size, self.car_y_size,
                                       (255, 255, 255))
        image = pygame.transform.flip(image, True, False)
        self.driving_frames_r.append(image)

        # set a reference to the image rect
        self.image = self.driving_frames_l[self.pos]
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position

    # update vehicle class
    def update(self, *args):
        # check to see if car is going left and update
        if self.direction == 1:
            self.image = self.driving_frames_l[self.pos]
            self.speed -= .5
            self.change_x = 1
            self.rect.x -= self.change_x
            if self.speed == 0:
                self.pos += 1
                self.image = self.driving_frames_l[self.pos]

            if self.pos >= 3:
                self.pos = 0
                self.image = self.driving_frames_l[self.pos]
            # check to see if car has collided with left of screen
            if self.rect.x <= 0:
                self.rect.x = self.game_screen.get_width() + 256

        # check to see if car is going right and update
        if self.direction == 0:
            self.image = self.driving_frames_r[self.pos]
            self.speed -= .5
            self.change_x = - 1
            self.rect.x -= self.change_x
            if self.speed == 0:
                self.pos += 1
                self.image = self.driving_frames_r[self.pos]

            if self.pos >= 3:
                self.pos = 0
                self.image = self.driving_frames_r[self.pos]

            # check to see if car has collided with right of screen
            if self.rect.x >= self.game_screen.get_width():
                self.rect.x = - 256
