import pygame
import time
import random

pygame.init()

"""   *********************** Colors ************************* """
black = (0, 0, 0)
green = (0,155,0)
red = (255, 0, 0)
white = (255, 255, 255)
## **************************** Class definitions ************************ ##
class GameWindow:
    def __init__(self,width=800,height=600):
        self.width=width
        self.height=height

    def setWidth(self,width=800):
        self.width=width

    def getWidth(self):
        return self.width

    def setHeight(self,height=800):
        self.height=window.height

    def getHeight(self):
        return self.height

    def getDimensions(self):
        return (self.width,self.height)

class Snake:
    # The variables are
    #posx, posy
    #speed
    #width, height
    #horizontalMovement, verticalMovement
    #color


    def __init__(self,posx,posy,**kwargs):
        self.properties=dict(posx=posx,posy=posy,speed=10,width=10,height=10,horizontalMovement=0,verticalMovement=0)
        for k,v in kwargs:
            self.properties[k]=v

    def setPosition(self,pos):
        self.properties['posx']=pos[0]
        self.properties['posy']=pos[1]

    def setXpos(self,val):
        self.properties['posx']=val

    def getXpos(self):
        return self.properties['posx']

    def setYpos(self,val):
        self.properties['posy']=val

    def getYpos(self):
        return self.properties['posy']

    def setSpeed(self,speed):
        self.properties['speed']=speed

    def getSpeed(self):
        return self.properties['speed']

    def setSize(self,width=10,height=10):
        self.properties['width']=width
        self.properties['height']=height

    def getWidth(self):
        return self.properties['width']

    def getHeight(self):
        return self.properties['height']

    def setHorizontalMovement(self,val):
        self.properties['horizontalMovement']=val
    
    def setVerticalMovement(self,val):
        self.properties['verticalMovement']=val
    
    def getHorizontalMovement(self):
        return self.properties['horizontalMovement']
    
    def getVerticalMovement(self):
        return self.properties['verticalMovement']

    ## The main functions
    def movementChange(self,event):
        if event.key == pygame.K_LEFT:
            self.setHorizontalMovement(-1)
            self.setVerticalMovement(0)
        if event.key == pygame.K_RIGHT:
            self.setHorizontalMovement(1)
            self.setVerticalMovement(0)
        if event.key == pygame.K_UP:
            self.setVerticalMovement(-1)
            self.setHorizontalMovement(0)
        if event.key == pygame.K_DOWN:
            self.setVerticalMovement(1)
            self.setHorizontalMovement(0)

    def movementUpdate(self,window):
        if self.getHorizontalMovement() == 1:
            self.setXpos(self.getXpos()+self.getSpeed())
        elif self.getHorizontalMovement() == -1:
            self.setXpos(self.getXpos()-self.getSpeed())
        elif self.getVerticalMovement() == 1:
            self.setYpos(self.getYpos()+self.getSpeed())
        elif self.getVerticalMovement() == -1:
            self.setYpos(self.getYpos()-self.getSpeed())

        self.setXpos(self.getXpos() % window.getWidth())
        self.setYpos(self.getYpos() % window.getHeight())

    def render(self,displayObject):
        pygame.draw.rect(displayObject, green, [self.getXpos(), self.getYpos(), self.getWidth(), self.getHeight()])

class Food:
    def __init__(self,snake,wallwidth,posx=0,posy=0,width=10,height=width):
        self.properties = dict(posx=posx,posy=posy,width=width,height=height)
        self.place(snake,wallwidth)

    def setPosition(self,*args):
        self.properties['posx']=args[0]
        self.properties['posy']=args[1]

    def getPosition(self):
        return self.properties['posx'],self.properties['posy']

    def getWidth(self):
        return self.properties['width']

    def place(self,snake,wallwidth):
        self.properties['posx']= round(random.randrange(wallwidth,window.getWidth()-snake.getWidth()-wallwidth)/10.0)*10
        if self.properties['posx']>= snake.getXpos():
            self.properties['posx']+=snake.getWidth()

        self.properties['posy']= round(random.randrange(wallwidth,window.getHeight()-snake.getHeight()-wallwidth)/10.0)*10
        if self.properties['posx']>= snake.getYpos():
            self.properties['posx']+=snake.getHeight()

    def render(self,displayObject):
        pygame.draw.rect(displayObject, red, [self.properties['posx'], self.properties['posy'],self.getWidth(), self.getWidth()])



""" ************************** Set window ******************** """

window=GameWindow(800,600)
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


##################### LOOP FUNCTION ########################################

clock = pygame.time.Clock()


def gameLoop():

################### Main Variables #######################
    ################################# Snake Variables ############################
    snake=Snake(window.getWidth()/2,window.getHeight()/2)

 ################################ Boundary Variables #######################
    wallwidth = 10

    leftwall = 0
    rightwall = window.getWidth() - wallwidth
    topwall = 0
    bottomwall = window.getHeight() - wallwidth


    ################################  Apple Variables  ############################
    apple = Food(snake,wallwidth)
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
                message_on_screen("Press y to play again, n to exit",red,[window.getWidth()*0.34, window.getHeight()*0.7])
                message_on_screen("GAME OVER",red,[window.getWidth()*0.42,window.getHeight()*0.5])
                pygame.display.update()
                onlyOnce = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        snake=Snake(window.getWidth() / 2,window.getHeight() / 2)
                        apple.place(snake,wallwidth)
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
                snake.movementChange(event)

        ###############  Snake Direction Changing  ##########################################

        snake.movementUpdate(window)
 #################  Snake collision with boundary  #######################################
        leftboundary = leftwall + wallwidth
        rightboundary = rightwall - snake.getWidth()
        topboundary = topwall + wallwidth
        bottomboundary = bottomwall - snake.getHeight()

        if snake.getXpos() < leftboundary or snake.getXpos() > rightboundary or snake.getYpos() < topboundary or snake.getYpos() > bottomboundary:
            GameOver = True
        ###############  Snake eating apple  ###################
        if snake.getXpos()>=apple.getPosition()[0] and snake.getXpos()<apple.getPosition()[0]+apple.getWidth() and snake.getYpos()>=apple.getPosition()[1] and snake.getYpos()<apple.getPosition()[1]+apple.getWidth():
            apple.place(snake,wallwidth)

  #################  Graphics #################################################
        displayObject.fill(white)

              #################  Boundary #################################################
        pygame.draw.rect(displayObject, black, [leftwall, 0, wallwidth, window.getHeight()])  ##left wall
        pygame.draw.rect(displayObject, black, [rightwall, 0, wallwidth, window.getHeight()])  ##right wall
        pygame.draw.rect(displayObject, black, [0, topwall, window.getWidth(), wallwidth])  ##left wall
        pygame.draw.rect(displayObject, black, [0, bottomwall, window.getWidth(), wallwidth])  ##left wall
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
