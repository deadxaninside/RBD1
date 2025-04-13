import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100, 100), (90, 100), (80, 100)]
direction = "RIGHT"
food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
        random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)


def move():
    global snake  # direction здесь не нужен, т.к. он не изменяется
    head_x, head_y = snake[0]

    if direction == "UP":
        head_y -= CELL_SIZE
    elif direction == "DOWN":
        head_y += CELL_SIZE
    elif direction == "LEFT":
        head_x -= CELL_SIZE
    elif direction == "RIGHT":
        head_x += CELL_SIZE

    snake.insert(0, (head_x, head_y))

    if snake[0] == food:
        spawn_food()
    else:
        snake.pop()


def spawn_food():
    global food
    food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
            random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    move()

    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, (255, 0, 0), (*food, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()