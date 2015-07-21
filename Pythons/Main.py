import pygame
import time
import random

pygame.init()

"""   *********************** Colors ************************* """
black = (0, 0, 0)
green = (0,155,0)
red = (255, 0, 0)
white = (255, 255, 255)

""" ************************** Set window ******************** """
width = 800
height = 600
displayObject = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python")


""" ************************** Functions ******************** """

##################### MESSAGE FUNCTION #####################################
font = pygame.font.SysFont(None, 25)  ## The sysfont font object


def message_on_screen(message, color, pos):
    text_message = font.render(message, True, color)
    # pos_x=width*0.42
    # pos_y=height/2
    displayObject.blit(text_message, [pos[0], pos[1]])
    pygame.display.update()


##################### LOOP FUNCTION ########################################

clock = pygame.time.Clock()


def gameLoop():

################### Main Variables #######################
    ################################# Snake Variables ############################
    snake_width = 10
    snake_height = 10

    snake_pos_x = width / 2
    snake_pos_y = height / 2

    snake_speed = 10

    horizontal_movement = 0
    vertical_movement = 0


    ################################ Boundary Variables #######################
    wallwidth = 10

    leftwall = 0
    rightwall = width - wallwidth
    topwall = 0
    bottomwall = height - wallwidth


    ################################  Apple Variables  ############################
    apple_width = snake_width
    apple_height = apple_width

    apple_pos_x= round(random.randrange(wallwidth,width-snake_width-wallwidth)/10.0)*10
    if apple_pos_x>= snake_pos_x:
            apple_pos_x+=snake_width

    apple_pos_y= round(random.randrange(wallwidth,height-snake_height-wallwidth)/10.0)*10
    if apple_pos_y>= snake_pos_y:
            apple_pos_y+=snake_height

    ############################### GAME FPS ######################
    fps = 50

    ############################### Boolean Loop ###################
    MainLoop = True
    GameOver = False
    while MainLoop:
        onlyOnce = True
        while GameOver:
            displayObject.fill(white)
            if onlyOnce:
                message_on_screen("Press y to play again, n to exit",red,[width*0.34, height*0.7])
                message_on_screen("GAME OVER",red,[width*0.42,height*0.5])
                pygame.display.update()
                onlyOnce = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        snake_pos_x = width / 2
                        snake_pos_y = height / 2

                        horizontal_movement = 0
                        vertical_movement = 0
                        apple_pos_x= round(random.randrange(wallwidth,width-snake_width-wallwidth)/10.0)*10
                        if apple_pos_x>= snake_pos_x:
                            apple_pos_x+=snake_width

                        apple_pos_y= round(random.randrange(wallwidth,height-snake_height-wallwidth)/10.0)*10
                        if apple_pos_y>= snake_pos_y:
                            apple_pos_y+=snake_height

                        GameOver = False

                    elif event.key == pygame.K_n:
                        MainLoop = False
                        GameOver = False
                        break

        if MainLoop == False:
            break
        #################### EVENT HANDLING #############################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    horizontal_movement = -1
                    vertical_movement = 0
                if event.key == pygame.K_RIGHT:
                    horizontal_movement = 1
                    vertical_movement = 0
                if event.key == pygame.K_UP:
                    vertical_movement = -1
                    horizontal_movement = 0
                if event.key == pygame.K_DOWN:
                    vertical_movement = 1
                    horizontal_movement = 0

        ###############  Snake Direction Changing  ##########################################


        if horizontal_movement == 1:
            snake_pos_x += snake_speed
        elif horizontal_movement == -1:
            snake_pos_x -= snake_speed
        elif vertical_movement == 1:
            snake_pos_y += snake_speed
        elif vertical_movement == -1:
            snake_pos_y -= snake_speed

        snake_pos_x %= width
        snake_pos_y %= width

        #################  Snake collision with boundary  #######################################
        leftboundary = leftwall + wallwidth
        rightboundary = rightwall - snake_width
        topboundary = topwall + wallwidth
        bottomboundary = bottomwall - snake_height

        if snake_pos_x < leftboundary or snake_pos_x > rightboundary or snake_pos_y < topboundary or snake_pos_y > bottomboundary:
            GameOver = True
        ###############  Snake eating apple  ###################
        if snake_pos_x>=apple_pos_x and snake_pos_x<apple_pos_x+apple_width and snake_pos_y>=apple_pos_y and snake_pos_y<apple_pos_y+apple_height:
            apple_pos_x= round(random.randrange(wallwidth,width-snake_width-wallwidth)/10.0)*10
            if apple_pos_x>= snake_pos_x:
                    apple_pos_x+=snake_width

            apple_pos_y= round(random.randrange(wallwidth,height-snake_height-wallwidth)/10.0)*10
            if apple_pos_y>= snake_pos_y:
                    apple_pos_y+=snake_height

  #################  Graphics #################################################
        displayObject.fill(white)

        #################  Boundary #################################################
        pygame.draw.rect(displayObject, black, [leftwall, 0, wallwidth, height])  ##left wall
        pygame.draw.rect(displayObject, black, [rightwall, 0, wallwidth, height])  ##right wall
        pygame.draw.rect(displayObject, black, [0, topwall, width, wallwidth])  ##left wall
        pygame.draw.rect(displayObject, black, [0, bottomwall, width, wallwidth])  ##left wall
        #################### Snake  #############################################

        pygame.draw.rect(displayObject, green, [snake_pos_x, snake_pos_y, snake_width, snake_height])

        ####################  Apple  ############################################
        pygame.draw.rect(displayObject, red, [apple_pos_x, apple_pos_y, apple_width, apple_height])
        pygame.display.update()

        clock.tick(fps)

    #message_on_screen("GAME OVER", red, [width * 0.42, height / 2])
    time.sleep(2)
    pygame.quit()


""" ****************************  MAIN BODY ****************************************** """

gameLoop()
