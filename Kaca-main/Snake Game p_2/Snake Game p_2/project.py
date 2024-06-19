import pygame
import random
import time
from Direction import Direction
from Snake import Snake
from Apple import Apple

# width and height of the display
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 608
Points=0
# background creation
background = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
for i in range(25):
    for j in range(19):
        image = pygame.image.load("images/background.png")
        mask = (random.randrange(0, 20), random.randrange(
            0, 20), random.randrange(0, 20))

        image.fill(mask, special_flags=pygame.BLEND_ADD)
        background.blit(image, (i*32, j*32))

# settings
pygame.init()
# display object and game clock
display = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
clock = pygame.time.Clock()
my_font=pygame.font.SysFont("Comic Sans MS", 24)
# Snake
snake = Snake()
MOVE_SNAKE = pygame.USEREVENT + 1
event_timer = 200
pygame.time.set_timer(MOVE_SNAKE, event_timer)

# apples
apple = Apple()
apples = pygame.sprite.Group()
apples.add(apple)

game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
            if event.key == pygame.K_w:
                snake.change_direction(Direction.UP)
            if event.key == pygame.K_s:
                snake.change_direction(Direction.DOWN)
            if event.key == pygame.K_a:
                snake.change_direction(Direction.LEFT)
            if event.key == pygame.K_d:
                snake.change_direction(Direction.RIGHT)
            if event.key == pygame.K_o:
                event_timer += 10
                pygame.time.set_timer(MOVE_SNAKE, event_timer)
            if event.key == pygame.K_p:
                event_timer -= 10
                pygame.time.set_timer(MOVE_SNAKE, event_timer)

        elif event.type == MOVE_SNAKE:
            snake.update()
        elif event.type == pygame.QUIT:
            game_on = False

    collision_with_apple=pygame.sprite.spritecollideany(snake,apples)
    if collision_with_apple !=None:
        collision_with_apple.kill()
        snake.eat_apple()
        apple=Apple()
        apples.add(apple)
        Points+=1

    # drawing background
    display.blit(background, (0, 0))
    snake.draw_segments(display)
    # drawing snake's head
    display.blit(snake.image, snake.rect)
    # drawing apples
    for apple in apples:
        display.blit(apple.image, apple.rect)

    result_text=my_font.render(
        f"Points:{Points}",False, (0,0,0))
    
    display.blit(result_text, (16,16))
    if snake.collision_check():
        loose_text=my_font.render(
            "You lost", False, (200,0,0))
    display.blit(loose_text, (DISPLAY_WIDTH/2-50,DISPLAY_HEIGHT/2))
    game_on=False
    pygame.display.flip()
    clock.tick(30)

time.sleep(3)
pygame.quit()
