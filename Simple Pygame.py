import sys, pygame, time

pygame.init()

size = width, height = 800, 800
screen = pygame.display.set_mode(size)

done = False
total_seconds = 0
while not done:
    time.sleep(1)
    total_seconds = total_seconds + 1
    pygame.display.flip()

    if total_seconds > 10:
        done = True


pygame.display.quit()
pygame.quit()
sys.exit()
