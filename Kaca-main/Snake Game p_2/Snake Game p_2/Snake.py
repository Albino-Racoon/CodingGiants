import pygame
import copy
from Direction import Direction
from Segment import Segment


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        # head's original image
        self.original_image = pygame.image.load("images/head.png")
        # auxiliary image that will change when the direction changes
        self.image = pygame.transform.rotate(self.original_image, 0)
        # head coordinates
        self.rect = self.image.get_rect(center=(12*32+16, 9*32+16))
        # variables responsible for direction and those connected to it
        self.direction = Direction.UP
        self.new_direction = Direction.UP

        self.last_position=self.rect
        self.add_segment=False
        self.segments=[]

    def change_direction(self, direction):
        possible_change = True
        if direction == Direction.UP and self.direction == Direction.DOWN:
            possible_change = False
        if direction == Direction.DOWN and self.direction == Direction.UP:
            possible_change = False
        if direction == Direction.LEFT and self.direction == Direction.RIGHT:
            possible_change = False
        if direction == Direction.RIGHT and self.direction == Direction.LEFT:
            possible_change = False
        if possible_change:
            self.new_direction = direction

    def update(self):
        self.direction = self.new_direction
        self.image = pygame.transform.rotate(
            self.original_image, (self.direction.value*-90))

        self.last_position=copy.deepcopy(self.rect)
        if self.direction == Direction.UP:
            self.rect.move_ip(0, -32)
        if self.direction == Direction.RIGHT:
            self.rect.move_ip(32, 0)
        if self.direction == Direction.LEFT:
            self.rect.move_ip(-32, 0)
        if self.direction == Direction.DOWN:
            self.rect.move_ip(0, 32)
        for i in range(len(self.segments)):
            if i==0:
                self.segments[i].shift(self.last_position)
            else:
                self.segments[i].shift(self.segments[i-1].last_position)

        if self.add_segment:
            new_segment=Segment()

            new_position=None
            if len(self.segments)>0:
                new_position=copy.deepcopy(self.segments[-1].position)
            else:
                new_position=copy.deepcopy(self.last_position)
            new_segment.position=new_position
            self.segments.append(new_segment)
            self.add_segment=False
            
    def draw_segments(self, ekran):
        for segment in self.segments:
            ekran.blit(segment.image, segment.position)

    def eat_apple(self):
        self.add_segment=True
    def collision_check(self):
        for segment in self.segments:
            if self.rect.topleft==segment.position.topleft:
                return True
            
        if self.rect.top<0 or self.rect.top>=608:
            return True
        if self.rect.left<0 or self.rect.left>=608:
            return True
        return False