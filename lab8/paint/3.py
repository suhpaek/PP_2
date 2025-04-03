import math
import pygame

# инициализация pygame
pygame.init()

# задаем размеры окна
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))  # заливаем экран белым цветом

# определяем цвета
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)

# список цветов и текущий цвет
colors = [colorRED, colorBLUE, colorGREEN, colorBLACK]
current_color = colorRED

# создаем объект clock для управления частотой кадров
clock = pygame.time.Clock()

# переменные для отслеживания состояния мыши и рисования
LMBpressed = False  # флаг нажатия левой кнопки мыши
THICKNESS = 5  # толщина линий
currX = currY = 0  # текущая позиция курсора
prevX = prevY = 0  # предыдущая позиция курсора

# инструмент рисования по умолчанию
# доступные инструменты: RECT, CIRCLE, ERASER, FREEHAND, SQUARE, TRIANGLE, EQ_TRIANGLE, RHOMBUS
tool = "RECT"

# функция для вычисления прямоугольника по двум диагональным точкам
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        # выход из программы
        if event.type == pygame.QUIT:
            running = False

        # обработка нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos  # запоминаем начальную точку

        # обработка отпускания кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos  # получаем конечную точку

        # обработка движения мыши (если кнопка зажата)
        if event.type == pygame.MOUSEMOTION:
            currX, currY = event.pos
            if LMBpressed:
                if tool == "FREEHAND":
                    pygame.draw.line(screen, current_color, (prevX, prevY), (currX, currY), THICKNESS)
                    prevX, prevY = currX, currY  # обновляем предыдущую позицию

                elif tool == "ERASER":
                    pygame.draw.line(screen, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS)
                    prevX, prevY = currX, currY

                elif tool == "RECT":
                    pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)

                elif tool == "CIRCLE":
                    radius = int(math.hypot(currX - prevX, currY - prevY))  # вычисляем радиус
                    pygame.draw.circle(screen, current_color, (prevX, prevY), radius, THICKNESS)

                elif tool == "SQUARE":
                    side = min(abs(currX - prevX), abs(currY - prevY))  # вычисляем сторону квадрата
                    square_rect = pygame.Rect(prevX, prevY, side, side)
                    pygame.draw.rect(screen, current_color, square_rect, THICKNESS)

                elif tool == "TRIANGLE":  # прямоугольный треугольник
                    pygame.draw.polygon(screen, current_color, [(prevX, prevY), (prevX, currY), (currX, currY)], THICKNESS)

                elif tool == "EQ_TRIANGLE":  # равносторонний треугольник
                    height = int((3**0.5 / 2) * abs(currX - prevX))  # высота по длине стороны
                    top = (prevX + (currX - prevX) // 2, prevY)
                    left = (prevX, prevY + height)
                    right = (currX, prevY + height)
                    pygame.draw.polygon(screen, current_color, [top, left, right], THICKNESS)

                elif tool == "RHOMBUS":  # ромб
                    mid_x = (prevX + currX) // 2
                    mid_y = (prevY + currY) // 2
                    dx = abs(currX - prevX) // 2
                    dy = abs(currY - prevY) // 2
                    points = [(mid_x, prevY), (currX, mid_y), (mid_x, currY), (prevX, mid_y)]
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)

        # обработка нажатий клавиш (смена инструментов и настроек)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1  # увеличиваем толщину линии
            elif event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)  # уменьшаем толщину, но не ниже 1

            # выбор инструмента
            elif event.key == pygame.K_r:
                tool = "RECT"
            elif event.key == pygame.K_c:
                tool = "CIRCLE"
            elif event.key == pygame.K_e:
                tool = "ERASER"
            elif event.key == pygame.K_f:
                tool = "FREEHAND"
            elif event.key == pygame.K_s:
                tool = "SQUARE"
            elif event.key == pygame.K_t:
                tool = "TRIANGLE"
            elif event.key == pygame.K_q:
                tool = "EQ_TRIANGLE"
            elif event.key == pygame.K_h:
                tool = "RHOMBUS"

            # выбор цвета
            elif event.key == pygame.K_1:
                current_color = colorRED
            elif event.key == pygame.K_2:
                current_color = colorBLUE
            elif event.key == pygame.K_3:
                current_color = colorGREEN
            elif event.key == pygame.K_4:
                current_color = colorBLACK

    # обновляем экран
    pygame.display.flip()
    clock.tick(60)  # ограничение частоты кадров до 60 fps

# выход из pygame после завершения цикла
pygame.quit()
