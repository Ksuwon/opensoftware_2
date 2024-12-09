import math
import random
import time

import config

import pygame
from pygame.locals import Rect, K_LEFT, K_RIGHT

class Basic:
    def __init__(self, color: tuple, speed: int = 0, pos: tuple = (0, 0), size: tuple = (0, 0)):
        self.color = color
        self.rect = Rect(pos[0], pos[1], size[0], size[1])
        self.center = (self.rect.centerx, self.rect.centery)
        self.speed = speed
        self.start_time = time.time()
        self.dir = 270

    def move(self):
        dx = math.cos(math.radians(self.dir)) * self.speed
        dy = -math.sin(math.radians(self.dir)) * self.speed
        self.rect.move_ip(dx, dy)
        self.center = (self.rect.centerx, self.rect.centery)


class Block(Basic):
    def __init__(self, color: tuple, pos: tuple = (0,0), alive = True):
        super().__init__(color, 0, pos, config.block_size)
        self.pos = pos
        self.alive = alive

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)
    
    def collide(self, items_list):
        # ============================================
        # TODO: Implement an event when block collides with a ball
        self.alive =False
        self.rect.size = (0,0)
        if random.random() < 0.2:  # 20% 확률
            item_color = (0, 0, 255) if random.random() < 0.5 else (255, 0, 0)  # 파란 공 또는 빨간 공
            item = Basic(color=item_color, pos=self.pos, size=config.item_size)
            items_list.append(item)  # 매개변수로 전달된 리스트에 추가
        return self.alive


class Paddle(Basic):
    def __init__(self):
        super().__init__(config.paddle_color, 0, config.paddle_pos, config.paddle_size)
        self.start_pos = config.paddle_pos
        self.speed = config.paddle_speed
        self.cur_size = config.paddle_size

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move_paddle(self, event: pygame.event.Event):
        if event.key == K_LEFT and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        elif event.key == K_RIGHT and self.rect.right < config.display_dimension[0]:
            self.rect.move_ip(self.speed, 0)


class Ball(Basic):
    def __init__(self, pos: tuple = config.ball_pos):
        super().__init__(config.ball_color, config.ball_speed, pos, config.ball_size)
        self.power = 1
        self.dir = 90 + random.randint(-45, 45)

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)

    def collide_block(self, blocks: list, items_list):
        for block in blocks[:]:
            if self.rect.colliderect(block.rect):
                block.collide(items_list)
                blocks.remove(block)
                self.dir = 360 - self.dir + random.randint(-5,5)

    def collide_paddle(self, paddle: Paddle) -> None:
        if self.rect.colliderect(paddle.rect):
            self.dir = 360 - self.dir + random.randint(-5, 5)

    def hit_wall(self):
        # ============================================
        # TODO: Implement a service that bounces off when the ball hits the wall
        # 좌우 벽 충돌
        if self.rect.left <=0:
            self.rect.left = 0
            self.dir = 180 - self.dir + random.randint(-10,10)

        elif self.rect.right >= config.display_dimension[0]:
            self.rect.right = config.display_dimension[0]
            self.dir = 180 - self.dir + random.randint(-10,10)
        
        # 상단 벽 충돌
        if self.rect.top <=0:
            self.rect.top = 0
            self.dir = 360 - self.dir + random.randint(-5,5)
    
    def alive(self):
        # ============================================
        # TODO: Implement a service that returns whether the ball is alive or not
        if self.rect.top >= config.display_dimension[1]:
            return False
        return True
     
