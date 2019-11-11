"""
Pygame base template
Aaron Lee - 2019
"""

import pygame
pygame.init()  # initializes pygame (need to do this before you use it)


# Global Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 150, 150)
MAROON = (100, 0, 0)
ORANGE = (255, 150, 0)
PURPLE = (100, 50, 150)


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
done = False  # Loop until the user clicks the close button.


size = (SCREEN_WIDTH, SCREEN_HEIGHT)  # Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game!")

clock = pygame.time.Clock()  # Used to manage how fast the screen updates

rect_x = 0
rect_y = 0
rect_color = RED
ellipse_x = 0
ellipse_y = 0
change_x = 0
change_y = 0

pygame.mouse.set_visible(False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop (input from user keyboard, mouse, game controller)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # MOUSE STUFF
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)  # event.button tells me which button was pressed
            print(event.pos)  # position of the mouse press
            rect_color = BLUE
        if event.type == pygame.MOUSEBUTTONUP:
            rect_color = RED
        if event.type == pygame.MOUSEMOTION:
            pass
            #print(event.rel)  # maybe use this for more advanced game
        # KEYBOARD STUFF
        if event.type == pygame.KEYDOWN:  # pressed a key
            if event.key == pygame.K_UP:
                change_y = -5
            if event.key == pygame.K_DOWN:
                change_y = 5
            if event.key == pygame.K_RIGHT:
                change_x = 5
            if event.key == pygame.K_LEFT:
                change_x = -5
        if event.type == pygame.KEYUP:  # lifted my finger
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                change_y = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                change_x = 0



    # --- Game logic should go here
    # pos = pygame.mouse.get_pos()  # returns the x and y position of cursor
    # print(pos[0])  # print the x position

    ellipse_x += change_x
    ellipse_y += change_y

    # keep the ellipse on the screen
    if ellipse_x < 0:
        ellipse_x = 0
    if ellipse_y < 0:
        ellipse_y = 0
    if ellipse_x > SCREEN_WIDTH - 30:
        ellipse_x = SCREEN_WIDTH - 30
    if ellipse_y > SCREEN_HEIGHT - 30:
        ellipse_y = SCREEN_HEIGHT - 30


    rect_x, rect_y = pygame.mouse.get_pos()  # pythonic way to do it

    if rect_x > SCREEN_WIDTH - 30:
        rect_x = SCREEN_WIDTH - 30
    if rect_y > SCREEN_HEIGHT - 30:
        rect_y = SCREEN_HEIGHT - 30

    # --- Drawing code goes here
    screen.fill(WHITE)

    pygame.draw.rect(screen, rect_color, [rect_x, rect_y, 30, 30])
    pygame.draw.ellipse(screen, GREEN, [ellipse_x, ellipse_y, 30, 30])

    # happy face
    pygame.draw.ellipse(screen, BLACK, [298, 198, 44, 44])
    pygame.draw.ellipse(screen, YELLOW, [300, 200, 40, 40])
    pygame.draw.circle(screen, BLACK, [313, 214], 3)
    pygame.draw.circle(screen, BLACK, [327, 214], 3)
    pygame.draw.line(screen, BLACK, [313, 226], [327, 226], 3)


    pygame.display.flip()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # limit to 60 frames per second


pygame.quit()  # Close the window and quit.