import pygame
import sys
import random

pygame.init()

score = 0
score_font = pygame.font.SysFont('comicsansms', 35)

rect_position = [400, 700]

object_pos = [random.randint(0, 700), 0] 

screen = pygame.display.set_mode((800, 800))
background_image = pygame.image.load("trees.jpeg").convert()
lives = 3 

game_over = False


clock = pygame.time.Clock()

def catch(rect_position, object_pos, score):
    # if lives > 0:
    if object_pos[0] >= (rect_position[0] - 30) and object_pos[0] < (rect_position[0] + 40):
        if object_pos[1] >= rect_position[1] and object_pos[1] < (rect_position[1] + 60):
            score += 1
        else:
            lives - 1
    return score 

    

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = rect_position[0]
            y = rect_position[1]
            if event.key == pygame.K_LEFT:
                x -= 50
            elif event.key == pygame.K_RIGHT:
                x += 50
            rect_position = [x, y]

    screen.blit(background_image, [0, 0])

    if object_pos[1] >= 0 and object_pos[1] < 700:
        object_pos[1] += 10
        # speed for the falling objects 
    else:
        object_pos[0] = random.randint(30, 670)
        object_pos[1] = 0


    score = catch(rect_position, object_pos, score)
    player_score = "Score: " + str(score)
    show_score = score_font.render(player_score, 1, (155,100,50))
    screen.blit(show_score, (340, 10))
    if lives == 0:
        game_over = True
  

    pygame.draw.rect(screen, (0,0,255), (object_pos[0], object_pos[1], 50, 50))
    pygame.draw.rect(screen, (0,255,0), (rect_position[0], rect_position[1], 80, 60))

    red_apple = pygame.image.load("red_apple.jpeg").convert()
    apples = pygame.Rect(object_pos[0], object_pos[1], 50, 50)
    apple = pygame.transform.scale(red_apple, (50, 50))
    screen.blit(apple, apples)

    basket_img = pygame.image.load("emp-basket1.jpeg").convert()
    rect = pygame.Rect(rect_position[0], rect_position[1], 80, 60)
    basket = pygame.transform.scale(basket_img, (80, 60))
    screen.blit(basket, rect)
    
    
    
  

    clock.tick(30)
    pygame.display.update()

