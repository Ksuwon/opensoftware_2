import sys
from implements import Basic, Block, Paddle, Ball
import config

import pygame
from pygame.locals import QUIT, Rect, K_ESCAPE, K_SPACE


pygame.init()
pygame.key.set_repeat(3, 3)
surface = pygame.display.set_mode(config.display_dimension)

fps_clock = pygame.time.Clock()

paddle = Paddle()
ball1 = Ball()
BLOCKS = []
ITEMS = []
BALLS = [ball1]
life = config.life
start = False


def create_blocks():

    cols, rows = config.num_blocks  # 행(row)과 열(col)을 가져옴
    for i in range(cols):
        for j in range(rows):
            x = config.margin[0] + i * (config.block_size[0] + config.spacing[0])
            y = (
                config.margin[1]
                + config.scoreboard_height
                + j * (config.block_size[1] + config.spacing[1])
            )
            if j == rows - 1:  # 맨 아래 행은 깨지지 않는 벽 블럭
                if i == 2:
                    color_index = j % len(config.colors) # 한칸은 깨지는 벽으로 둠
                    block = Block(color=config.colors[color_index], pos=(x, y), alive=True, is_wall=False)
                else: block = Block(color=(128, 128, 128), pos=(x, y), alive=True, is_wall=True)
            else:  # 나머지는 깨지는 블럭
                color_index = j % len(config.colors)
                block = Block(color=config.colors[color_index], pos=(x, y), alive=True, is_wall=False)
            BLOCKS.append(block)

def tick():
    global life
    global BLOCKS
    global ITEMS
    global BALLS
    global paddle
    global ball1
    global start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:  # ESC 키가 눌렸을 때
                pygame.quit()
                sys.exit()
            if event.key == K_SPACE:  # space키가 눌려지만 start 변수가 True로 바뀌며 게임 시작
                start = True
            paddle.move_paddle(event)

    for ball in BALLS:
        if start:
            ball.move()
        else:
            ball.rect.centerx = paddle.rect.centerx
            ball.rect.bottom = paddle.rect.top

        ball.collide_block(BLOCKS, ITEMS)
        ball.collide_paddle(paddle)
        ball.hit_wall()
        if ball.alive() == False:
            BALLS.remove(ball)

    # 아이템 움직임
    for item in ITEMS[:]:
        item.rect.move_ip(0, 5)  # 아래로 떨어짐
        if item.rect.top > config.display_dimension[1]:  # 화면 밖으로 나가면 제거
            ITEMS.remove(item)
        elif item.rect.colliderect(paddle.rect):  # 패들과 충돌
            ITEMS.remove(item)
            if item.color == (0, 0, 255):  # 파란 공 효과
                pass
            elif item.color == (255, 0, 0):  # 빨간 공 효과
                pass


def main():
    global life
    global BLOCKS
    global ITEMS
    global BALLS
    global paddle
    global ball1
    global start
    my_font = pygame.font.SysFont(None, 50)
    mess_clear = my_font.render("Cleared!", True, config.colors[2])
    mess_over = my_font.render("Game Over!", True, config.colors[2])
    create_blocks()

    while True:
        tick()
        surface.fill((0, 0, 0))
        paddle.draw(surface)

        for block in BLOCKS:
            block.draw(surface)

        cur_score = config.num_blocks[0] * config.num_blocks[1] - len(BLOCKS)

        score_txt = my_font.render(f"Score : {cur_score * 10}", True, config.colors[2])
        life_font = my_font.render(f"Life: {life}", True, config.colors[0])

        surface.blit(score_txt, config.score_pos)
        surface.blit(life_font, config.life_pos)

        for item in ITEMS:
            pygame.draw.ellipse(surface, item.color, item.rect)

        if len(BALLS) == 0:
            if life > 1:
                life -= 1
                ball1 = Ball()
                BALLS = [ball1]
                start = False
            else:
                surface.blit(mess_over, (200, 300))
        elif all(block.alive == False for block in BLOCKS):
            surface.blit(mess_clear, (200, 400))
        else:
            for ball in BALLS:
                if start == True:
                    ball.move()
                ball.draw(surface)
            for block in BLOCKS:
                block.draw(surface)

        pygame.display.update()
        fps_clock.tick(config.fps)


if __name__ == "__main__":
    main()
