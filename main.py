# Import modules
import pygame,sys

# Initalize pygame
pygame.init()

# Window Parameters
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Game')

# Define colors
white = (255,255,255)
black = (0,0,0)
blue = (0,200,50)

# Define and create sprites
player = pygame.Rect((10,700),(50,100))

# Create a set fps rate
clock = pygame.time.Clock()
# Game Loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close the window if user clicks close
            pygame.quit()
            running == False
            sys.exit()
    # Screen fill
    screen.fill(white)
    
    # Draw sprites onto screen
    pygame.draw.rect(screen, blue, player)
    
    pygame.display.flip() # Update the screen

    clock.tick(60) # Set framerate of 60 fps
    

