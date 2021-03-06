import pygame
from tiles import Tile
from setting import tile_size, screen_width
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface # screen
        self.setup_level(level_data)  #level table
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group() 
        self.player = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for col_index, cell in enumerate(row):

                x = col_index * 64
                y = row_index * 64

                if cell == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x <0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > (screen_width -(screen_width / 4)) and direction_x >0:
            self.world_shift = -8
            player.speed = 0
        else: 
            self.world_shift = 0
            player.speed = 8

    def run(self):
        # tile on screen
        self.tiles.draw(self.display_surface)
        self.tiles.update(self.world_shift)

        # player on screen
        self.player.update()
        self.player.draw(self.display_surface)

        self.scroll_x()

