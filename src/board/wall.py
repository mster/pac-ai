# import core modules and community packages
import pygame

class Wall():
    def __init__(self, pos, size, color=(33,33,222)):
        # binding
        self.pos = pos
        self.color = color

        # props
        self.dimensions = size[0] - 4, size[1] - 4

    def draw(self, surface):
        x = self.pos[0]
        y = self.pos[1]

        w = self.dimensions[0]
        h = self.dimensions[1]

        pygame.draw.rect(surface, self.color, (x + 2, y  +2, w, h), 1)
