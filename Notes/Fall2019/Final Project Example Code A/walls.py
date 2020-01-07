"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.gravity = 0.5

        self.walls = []

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in hit_list:
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right

        self.change_y += self.gravity
        self.rect.y += self.change_y
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in hit_list:
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
                self.change_y = 0
            else:
                self.rect.top = wall.rect.bottom


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Test')

# Create the player object
player = Player(150, 50)

# Groups
all_sprites_list = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
player.walls = wall_sprites

wall = Wall(100, 100, 200, 20)
wall_sprites.add(wall)
all_sprites_list.add(wall)

wall = Wall(350, 150, 200, 20)
wall_sprites.add(wall)
all_sprites_list.add(wall)

all_sprites_list.add(player)

clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                # jump
                player.change_y = -10


        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)


    # --- Game logic

    # This calls update on all the sprites
    all_sprites_list.update()

    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()