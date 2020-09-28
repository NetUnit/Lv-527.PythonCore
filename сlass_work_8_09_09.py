import pygame                                       # pygame module import

#class_work 8 'py_game'- SoftServe8 - Lesson8

# 1.1 We need a plane to fly, but not multiply

# block 1 - setup display and colour constants

WHITE = (255, 255, 255)                             # cortege of data, default white colour according to the RGB format scale, https://prnt.sc/unbjtj                                                 
BLACK = (0, 0, 0)                                   # RGB format scale is an open source info like (w3schools).

WIDTH_DISPLAY = 800                                 # better way to represent constants as variables, in this case the code is more understandable
HEIGHT_DISPLAY = 600                                # in such a way we can change the constants single time in our code in order to make it simple

COORD_X=50
COORD_Y=50
WIDTH_IMAGE=50
HEIGHT_IMAGE=50
DELTA_STEP=5                                        # step of the single aircraft movement

# Call this function so the Pygame library can initialize itself
pygame.init()


# Create an 800x600 sized screen
screen = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption('Fly')       # it defines our display caption

clock = pygame.time.Clock()                         # used to manage how fast the screen would update. correspons to a frame draw and depiction at the display
                                                    # # we use the 'time' module to define time within game, this mostly used for FPS 'frames  per second'. The fact is utmost visble benchmark for a human eye is 30 FPS.

                                                    # block set up constants

                                                    # colour constants

pygame.display.update()


# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
player_image = pygame.image.load("/media/netunit/SSD.LI/SoftServe/SoftServe#8_09.09/py_game/cartoon_plane_41.gif").convert()
background_image = pygame.image.load("/media/netunit/SSD.LI/SoftServe/SoftServe#8_09.09/py_game/clouds.gif").convert()



#when a picture does not possess a transparent layer we should equal picture background and layer background (in our case not necessary)
#set_colorkey() method to implement this## "Surface class":

player_image.set_colorkey(BLACK)

done = False                                        # create condition of closing the main frmae∕display # loop until the user close clicks the close button


#block2 - action loop or exit - drawing curves
# ------------------------------ Main Program Loop ---------------------------

while not done:                                     # while done != True (not done) or done == False or ('while done')
    # ---- Main event loop 
    
    for event in pygame.event.get():                # user did something
                                                    # event - module that corresponds to the action that user is doing in the loop (pushing buttons, clicking, drawing, moving items or etc.)
        if event.type == pygame.QUIT:               # method get() - read all events that user is doing in the loop
                                                    
            
            done = True                            
            #print ('User asked to quit')
                                                    # pygame.Quit() = exit (quit should be lovercase)
                                                    # flag that we are done - that would exit a loop (cycle) # dissatisfy condition
                                                    # when condition satisfies each other - it will continue the loop. 'done = True'
                                                    # when condition contradicts each other, it will end the loop. 'done = False' AS IN THE HEADING CONDITION


    ### SETUP EDGES ### DOES NOT WORK
    keys=pygame.key.get_pressed()                   # за допомогою цього блоку ми зчитуємо які саме клавіші юзер натискає (вправо, вліво, вниз, вгору)
                                                    # змінна keys (яка є одночасно і функцією, зчитає те що наклікав юзер)
    
    if keys[pygame.K_LEFT] and COORD_X>DELTA_STEP:   # блок коду який відповідає за зміну координат, а саме аналіз де є яка координата
        COORD_X=COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X<WIDTH_DISPLAY - DELTA_STEP - WIDTH_IMAGE: # координата X має бути меншою за ширину нашого дисплею + крок (якщо ми не хочемо максимально наблизити блок до рамки)
        COORD_X=COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y>DELTA_STEP:
        COORD_Y=COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y<HEIGHT_DISPLAY - DELTA_STEP - HEIGHT_IMAGE:
        COORD_Y=COORD_Y+DELTA_STEP                  # COORD_Y - Задана координата, COORD_Y + DELTA STEP - КООРДИНАТА Y + КРОК РУХУ, ТАКИМ ЧИНОМ ЗДІЙСНЮЄТЬСЯ ЗЧИТУВАННЯ РУХУ    
    ### БЛОК АНАЛІЗУ КООРДИНАТ КАРТИНКИ (НЕ ПРАЦЮЄ) 


    #-block3 - reading the movement that user is pressing -

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    # return a position of mouse at the screen 
    
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    screen.fill((0, 0, 0))                          # filling before the update (BLACK COLOUR)

    # Copy image to screen:
    screen.blit(player_image, [x, y])


    # update the screen
    pygame.display.flip()
    
    
    clock.tick(60)


pygame.quit()





