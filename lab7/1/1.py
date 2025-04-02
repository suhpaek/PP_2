import pygame
import os
import datetime

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image


pygame.init()

screen = pygame.display.set_mode((800, 600))
done = False
clock = pygame.time.Clock()


BLACK = (0, 0, 0) 
font = pygame.font.Font(None, 36)



while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('1\clock.png'), (0, 0))

        now=datetime.datetime.now()
        seconds = now.second
        minutes = now.minute
        dt_text=now.strftime("%H:%M:%S")
        text_surface = font.render(dt_text, True, BLACK)

        min_hand = get_image('1\min_hand.png')
        min_hand=pygame.transform.scale_by(min_hand, 0.7)
        rotated_min_hand = pygame.transform.rotate(min_hand, -6 * minutes)
        min_rect = rotated_min_hand.get_rect(center=(400, 300))
        screen.blit(rotated_min_hand, min_rect.topleft)


        sec_hand = get_image('1\sec_hand.png')
        sec_hand=pygame.transform.scale_by(sec_hand, 0.7)
        rotated_sec_hand = pygame.transform.rotate(sec_hand, -6 * seconds)
        sec_rect = rotated_sec_hand.get_rect(center=(400, 300))
        screen.blit(rotated_sec_hand, sec_rect.topleft)


        screen.blit(text_surface, (350, 550))
        
        
        pygame.display.flip()
        clock.tick(60)