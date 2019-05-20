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
        self.gravity = 0.2


    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in hit_list:
            if self.change_x > 0:
                self.rect.right = wall.rect.left
            elif self.change_x < 0:
                self.rect.left = wall.rect.right


        self.change_y += self.gravity
        self.rect.y += self.change_y
        hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in hit_list:
            if self.change_y > 0:
                self.change_y = 0
                self.rect.bottom = wall.rect.top
            elif self.change_y < 0:
                self.rect.top = wall.rect.bottom

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Test')

# Create groups
all_sprites_list = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

# Create the objects
player = Player(50, 50)
all_sprites_list.add(player)

wall1 = Wall(100, 200, 200, 10)
wall2 = Wall(90, 200, 10, 200)
all_sprites_list.add(wall1)
all_sprites_list.add(wall2)
wall_group.add(wall1)
wall_group.add(wall2)
player.walls = wall_group


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
                player.change_y = -6

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

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