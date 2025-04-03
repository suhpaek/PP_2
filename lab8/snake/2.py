# импортируем необходимые библиотеки
import random
import time

import pygame


# инициализация pygame
pygame.init()

# настройки экрана
WIDTH = 600
HEIGHT = 600
CELL = 30  # размер каждой клетки на сетке

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

# создание окна игры
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# шрифты и текст для экрана "game over"
font1 = pygame.font.SysFont("Verdana", 60)
image_game_over = font1.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))


# функция для рисования сетки в стиле шахмат
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(
                screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL)
            )


# класс для представления точки на сетке
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"


# класс для змейки
class Snake:
    def __init__(self):
        # инициализация тела змейки, направления, счета и уровня
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # горизонтальное направление движения
        self.dy = 0  # вертикальное направление движения
        self.score = 0
        self.level = 1

    # функция для перемещения змейки, обновляя положение ее тела
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    # функция для рисования змейки на экране
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(
                screen, colorBLUE, (segment.x * CELL, segment.y * CELL, CELL, CELL)
            )

    # функция для проверки столкновения с едой
    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")  # получена еда
            self.body.append(Point(head.x, head.y))  # змейка растет
            self.score += food.value  # добавляем стоимость еды к счету

            # повышение уровня каждые 3 очка
            if self.score % 3 == 0:
                self.level += 1
                return "LEVEL_UP"
            return "ATE"
        return None


# класс для представления еды
class Food:
    def __init__(self):
        self.generate_new()

    # функция для генерации новой еды с позицией и значением
    def generate_new(self):
        self.pos = Point(
            random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1)
        )
        self.value = random.randint(1, 5)
        self.timer_start = time.time()  # старт таймера на исчезновение еды

    # функция для рисования еды и ее значения
    def draw(self):
        pygame.draw.rect(
            screen, colorYELLOW, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)
        )
        font = pygame.font.SysFont("Verdana", 15)
        value_text = font.render(str(self.value), True, colorBLACK)
        screen.blit(value_text, (self.pos.x * CELL + 5, self.pos.y * CELL + 5))

    # функция для генерации новой еды, избегая тела змейки
    def generate_rand(self, snake_body):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            conflict = any(segment.x == x and segment.y == y for segment in snake_body)
            if not conflict:
                self.pos = Point(x, y)
                self.value = random.randint(1, 5)
                self.timer_start = time.time()
                break

    # функция для проверки, не истек ли таймер еды (5 секунд)
    def is_expired(self):
        return time.time() - self.timer_start > 5


# настройки игры
FPS = 5  # количество кадров в секунду
clock = pygame.time.Clock()

# инициализация объектов игры
food = Food()
snake = Snake()

# главный игровой цикл
running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    # рисование сетки шахматного поля
    draw_grid_chess()

    # перемещение змейки и проверка столкновений
    snake.move()
    result = snake.check_collision(food)

    # обработка столкновения с едой
    if result == "ATE" or result == "LEVEL_UP":
        food.generate_rand(snake.body)
        if result == "LEVEL_UP":
            FPS += 2  # увеличение скорости игры

    # обработка истечения времени еды
    if food.is_expired():
        print("Food expired and disappeared!")  # еда исчезла
        food.generate_rand(snake.body)

    # проверка на столкновение змейки со стеной
    head = snake.body[0]
    if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
        print("Snake hit the wall!")  # змейка столкнулась со стеной
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)
        running = False

    # рисование змейки и еды
    snake.draw()
    food.draw()

    # отображение счета и уровня
    font_info = pygame.font.SysFont("Verdana", 20)
    score_text = font_info.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font_info.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # обновление экрана и управление кадровой частотой
    pygame.display.flip()
    clock.tick(FPS)

# выход из игры
pygame.quit()
