import pygame
import time
import gameObjects

pygame.init()


""" ************************** Set window ******************** """

window=gameObjects.GameWindow(800,600)
displayObject = pygame.display.set_mode(window.getDimensions())
pygame.display.set_caption("Python")


""" ************************** Functions ******************** """

##################### MESSAGE FUNCTION #####################################
font = pygame.font.SysFont(None, 25)  ## The sysfont font object


def message_on_screen(message, color, pos):
    text_message = font.render(message, True, color)
    # pos_x=window.getWidth()*0.42
    # pos_y=window.getHeight()/2
    displayObject.blit(text_message, [pos[0], pos[1]])
    pygame.display.update()

######################## Eating function ##################################

def eat(snake,apple,wallwidth):
    if snake.getXpos()>=apple.getPosition()[0] and snake.getXpos()<apple.getPosition()[0]+apple.getWidth() and snake.getYpos()>=apple.getPosition()[1] and snake.getYpos()<apple.getPosition()[1]+apple.getWidth():
        apple.place(snake,wallwidth,window)
        snake.incrementLength()

##################### LOOP FUNCTION ########################################

clock = pygame.time.Clock()


def gameLoop():

################### Main Variables #######################
    ################################# Snake Variables ############################
    snake=gameObjects.Snake(window.getWidth()/2,window.getHeight()/2)

 ################################ Boundary Variables #######################
    wallwidth = 10

    leftwall = 0
    rightwall = window.getWidth() - wallwidth
    topwall = 0
    bottomwall = window.getHeight() - wallwidth


    ################################  Apple Variables  ############################
    apple = gameObjects.Food(snake,wallwidth,window)
    ############################### GAME FPS ######################
    fps = 25
    ############################### Boolean Loop ###################
    MainLoop = True
    GameOver = False
    while MainLoop:
        onlyOnce = True
        while GameOver:
            displayObject.fill(gameObjects.white)
            if onlyOnce:
                message_on_screen("Press y to play again, n to exit",gameObjects.red,[window.getWidth()*0.34, window.getHeight()*0.7])
                message_on_screen("GAME OVER",gameObjects.red,[window.getWidth()*0.42,window.getHeight()*0.5])
                pygame.display.update()
                onlyOnce = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        snake=gameObjects.Snake(window.getWidth() / 2,window.getHeight() / 2)
                        apple.place(snake,wallwidth,window)
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
                if snake.movementChange(event):
                    break

        ###############  Snake eating apple  ###################
        eat(snake,apple,wallwidth)

##############  Snake Direction Changing  ##########################################

        GameOver = snake.movementUpdate(window)

 #################  Snake collision with boundary  #######################################
        leftboundary = leftwall + wallwidth
        rightboundary = rightwall - snake.getWidth()
        topboundary = topwall + wallwidth
        bottomboundary = bottomwall - snake.getHeight()

        if snake.getXpos() < leftboundary or snake.getXpos() > rightboundary or snake.getYpos() < topboundary or snake.getYpos() > bottomboundary:
            GameOver = True

  #################  Graphics #################################################
        displayObject.fill(gameObjects.white)

              #################  Boundary #################################################
        pygame.draw.rect(displayObject, gameObjects.black, [leftwall, 0, wallwidth, window.getHeight()])  ##left wall
        pygame.draw.rect(displayObject, gameObjects.black, [rightwall, 0, wallwidth, window.getHeight()])  ##right wall
        pygame.draw.rect(displayObject, gameObjects.black, [0, topwall, window.getWidth(), wallwidth])  ##left wall
        pygame.draw.rect(displayObject, gameObjects.black, [0, bottomwall, window.getWidth(), wallwidth])  ##left wall
            #################### Snake  #############################################

        snake.render(displayObject)

        ####################  Apple  ############################################
        apple.render(displayObject)
        pygame.display.update()

        clock.tick(fps)

    #message_on_screen("GAME OVER", red, [window.getWidth() * 0.42, window.getHeight() / 2])
    time.sleep(2)
    pygame.quit()


""" ****************************  MAIN BODY ****************************************** """

gameLoop()
