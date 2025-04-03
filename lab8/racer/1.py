import random
import time

import pygame

# инициализация всех модулей pygame
pygame.init()

# размеры окна
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# загрузка изображений
image_background = pygame.image.load("AnimatedStreet.png")
image_player = pygame.image.load("Player.png")
image_enemy = pygame.image.load("Enemy.png")
image_coin = pygame.image.load("coin.png")
pygame.transform.scale_by(image_coin, 0.5)  # изменение размера изображения монеты

# загрузка фоновой музыки и воспроизведение в цикле
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)  # -1 означает бесконечный цикл

# загрузка звука столкновения
sound_crash = pygame.mixer.Sound("crash.wav")

# настройка экрана "игра окончена"
font1 = pygame.font.SysFont("Verdana", 60)
image_game_over = font1.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# шрифт для отображения счета
font2 = pygame.font.SysFont("Verdana", 50)


# класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5
        self.score = 0  # счет игрока (собранные монеты)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        # предотвращение выхода игрока за границы экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


# класс машины-противника
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10

    def generate_random_rect(self):
        # случайное расположение противника в верхней части экрана
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        # сброс положения противника, если он уходит за экран
        if self.rect.top > HEIGHT:
            self.generate_random_rect()


# класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.value = random.randint(1, 10)  # случайное значение монеты
        self.speed = 10

    def generate_random_rect(self):
        # случайное расположение монеты в верхней части экрана
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        # респаун монеты, если она уходит за экран
        if self.rect.top > HEIGHT:
            self.generate_random_rect()


# управление основным игровым циклом
running = True
clock = pygame.time.Clock()
FPS = 60

# создание экземпляров классов
player = Player()
enemy = Enemy()
coin = Coin()

# группы спрайтов для обновления и проверки столкновений
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

# добавление спрайтов в соответствующие группы
all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

# основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # обновление отображения счета
    image_coin_score = font2.render(f"{player.score}", True, "black")
    image_coin_score_rect = image_coin_score.get_rect()

    # движение игрока
    player.move()

    # отрисовка фона
    screen.blit(image_background, (0, 0))

    # движение и отрисовка всех игровых объектов
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # проверка столкновения с противником
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        running = False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)

    # проверка столкновения с монетой
    if pygame.sprite.spritecollide(player, coin_sprites, False):
        player.score += coin.value  # увеличение счета на значение монеты
        enemy.speed += coin.value / 24  # небольшое увеличение скорости противника
        pygame.display.flip()
        coin.kill()  # удаление старой монеты

        # создание новой монеты
        new_coin = Coin()
        new_coin.generate_random_rect()
        coin = new_coin
        coin_sprites.add(coin)
        all_sprites.add(coin)

    # отображение текущего счета
    screen.blit(image_coin_score, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)

# выход из игры
pygame.quit()
