import pygame
import time
import random

# speed of snake will eventually be 10
snake_speed = 20

# size of box
axis_x = 500
axis_y = 500

# establishing color with pygame
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

red = pygame.Color(244, 113, 116)
blue = pygame.Color(147, 202, 237)
green = pygame.Color(172, 209, 175)

# pygame GO
pygame.init()

# game window
pygame.display.set_caption("Hungry Snakes")
game_window = pygame.display.set_mode((axis_x, axis_y))

# frames per second with pygame and also time
fps = pygame.time.Clock()

# snake position!
snake_position = [50, 100]
direction = "RIGHT"
change_to = direction

# size of the snake
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# fruit with random
fruit_position = [random.randrange(1, (axis_x//10)) * 10, random.randrange(1, (axis_y//10)) * 10]
fruit_spawn = True

# scoring

score = 0

# scoring function
def show_score(choice, color, font, size):
    # font for scoring
    score_font = pygame.font.SysFont(font, size)
    # show the score
    score_surface = score_font.render("Score: " + str(score), True, color)
    # create object for the text surface
    score_rect = score_surface.get_rect()
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over
def game_over():
    # creating font object
    my_font = pygame.font.SysFont("times new roman", 50)
    # creating a text surface for the text
    game_over_surface = my_font.render("Your score is: " +  str(score), True, red)
    # object for the text
    game_over_rect = game_over_surface.get_rect()
    # setting position of text
    game_over_rect.midtop = (axis_x/2, axis_y/4)
    # draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    # will quit after 2 seconds
    time.sleep(2)
    pygame.quit()
    quit()

while True:
   
    # handling key events
    for event in pygame.event.get():
        # taking key inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores will be
    # incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (axis_x//10)) * 10,
                          random.randrange(1, (axis_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(game_window, white, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > axis_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > axis_y-10:
        game_over()
     
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
     
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)
     
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)

"""

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to == "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[1] -= 10
    if direction == "RIGHT":
        snake_position[1] += 10
        

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (axis_x//10)) * 10, random.randrange(1, (axis_y//10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > axis_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > axis_y-10:
        game_over()

    for block in snake_position[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, "times new roman", 20)

    pygame.display.update()
    fps.tick(snake_speed)
    
"""
