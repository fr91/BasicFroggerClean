import pygame
import SpriteSheet


class WaterSprite(pygame.sprite.Sprite):

    # constructor
    def __init__(self, game_screen, direction, x_position, y_position):
        self.game_screen = game_screen
        self.direction = direction
        self.speed_init = 10
        self.speed = self.speed_init
        self.x_position = x_position
        self.y_position = y_position
        self.change_x = 0
        self.raft_list = []
        self.multi_y = 0
        self.x_dist = 0
        self.raft_direction = 0
        self.list_length = 6
        self.add_list = 5

        # load sprite sheet

        super().__init__()
        sprite_sheet = SpriteSheet.SpriteSheet("raft.png")

        # set the image the player starts with
        self.image = sprite_sheet.get_image(0, 0, 32, 27, (0, 0, 0))

        # set a reference to the image rect
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position
        self.x_position = self.rect.x
        self.y_position = self.rect.y
        self.raft_list.append(self.rect)

    def update(self, *args):
            if self.direction == 0:
                self.change_x = 1
                self.rect.x -= self.change_x
                if self.rect.x <= 0:
                    self.rect.x = self.game_screen.get_width() + 256

            if self.direction == 1:
                self.change_x = 1
                self.rect.x += self.change_x
                if self.rect.x >= self.game_screen.get_width():
                    self.rect.x = -256

    # create all rafts
    def more_rafts(self):

            for rafts in range(self.game_screen.get_width()):
                rafts = self.__class__(self.game_screen, self.direction + self.raft_direction, self.x_position +
                                       + ((32 * len(self.raft_list))-self.x_dist),
                                       self.y_position - (27 * self.multi_y))
                self.raft_list.append(rafts)

                if len(self.raft_list) >= self.list_length:
                        rafts = self.__class__(self.game_screen, self.direction + self.raft_direction, self.x_position +
                                               ((32 * len(self.raft_list))-self.x_dist) + 96,
                                               self.y_position - (27 * self.multi_y))
                if len(self.raft_list) >= self.list_length + self.add_list:
                        rafts = self.__class__(self.game_screen, self.direction + self.raft_direction, self.x_position +
                                               ((32 * len(self.raft_list))-self.x_dist) + 192,
                                               self.y_position - (27 * self.multi_y))

                if len(self.raft_list) >= self.list_length + (self.add_list * 2) and self.multi_y >= 8:
                    rafts = self.__class__(self.game_screen, self.direction + self.raft_direction, self.x_position +
                                           ((32 * len(self.raft_list))-self.x_dist) + 288,
                                           self.y_position - (27 * self.multi_y))

                if len(self.raft_list) >= self.list_length + (self.add_list * 2) - 1 and self.multi_y == 0:
                    del self.raft_list[:]
                    self.multi_y += 1
                    self.x_dist = 14

                if len(self.raft_list) >= self.list_length + (self.add_list * 2) - 1 and self.multi_y == 1:
                    del self.raft_list[:]
                    self.multi_y += 1
                    self.raft_direction += 1
                    self.x_position = - self.x_position
                    self.x_dist = 32
                    self.list_length -= 1
                    self.add_list -= 1

                if len(self.raft_list) >= self.list_length + (self.add_list * 2) - 1 and self.multi_y == 2:
                    del self.raft_list[:]
                    self.multi_y += 1
                    self.x_dist = 20

                if len(self.raft_list) >= self.list_length + (self.add_list * 2) - 1 and self.multi_y == 3:
                    del self.raft_list[:]
                    self.multi_y += 1
                    self.raft_direction += -1
                    self.x_position = self.game_screen.get_width()
                    self.x_dist = - 92
                    self.list_length -= 1
                    self.add_list -= 1

                if len(self.raft_list) >= self.list_length + (self.add_list * 2) - 1 and self.multi_y == 4:
                    del self.raft_list[:]
                    self.multi_y += 1
                    self.x_dist = - 83

                if len(self.raft_list) >= self.list_length + (self.add_list * 2) - 1 and self.multi_y == 5:
                    del self.raft_list[:]
                    self.multi_y += 1
                    self.raft_direction += 1
                    self.x_position = - self.x_position
                    self.x_dist = 32

                if len(self.raft_list) >= self.list_length + (self.add_list * 2) - 1 and self.multi_y == 6:
                    del self.raft_list[:]
                    self.multi_y += 1
                    self.x_dist = 23

                if len(self.raft_list) >= self.list_length + (self.add_list * 2) - 1 and self.multi_y == 7:
                    del self.raft_list[:]
                    self.multi_y += 1
                    self.raft_direction += -1
                    self.x_position = self.game_screen.get_width()
                    self.x_dist = 32

                if len(self.raft_list) >= self.list_length + (self.add_list * 3) - 1 and self.multi_y == 8:
                    del self.raft_list[:]
                    self.multi_y += 1
                    self.raft_direction += 1
                    self.x_position = - self.x_position
                    self.x_dist = 0

                return rafts