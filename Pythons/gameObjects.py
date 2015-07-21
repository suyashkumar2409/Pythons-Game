import pygame
import random

"""   *********************** Colors ************************* """
black = (0, 0, 0)
green = (0, 155, 0)
red = (255, 0, 0)
white = (255, 255, 255)


## **************************** Class definitions ************************ ##
class GameWindow:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height

    def setWidth(self, width=800):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height=800):
        self.height = height

    def getHeight(self):
        return self.height

    def getDimensions(self):
        return (self.width, self.height)


class Snake:
    # The variables are
    # posx, posy
    # speed
    # width, height
    # horizontalMovement, verticalMovement
    # color
    # length
    # snakeList


    def __init__(self, posx, posy, **kwargs):
        self.properties = dict(posx=posx, posy=posy, speed=10, width=10, height=10, horizontalMovement=0,
                               verticalMovement=0, length=5, snakeList=[], increaseLength=2)
        for k, v in kwargs:
            self.properties[k] = v

    def setPosition(self, pos):
        self.properties['posx'] = pos[0]
        self.properties['posy'] = pos[1]

    def setXpos(self, val):
        self.properties['posx'] = val

    def getXpos(self):
        return self.properties['posx']

    def setYpos(self, val):
        self.properties['posy'] = val

    def getYpos(self):
        return self.properties['posy']

    def setSpeed(self, speed):
        self.properties['speed'] = speed

    def getSpeed(self):
        return self.properties['speed']

    def setSize(self, width=10, height=10):
        self.properties['width'] = width
        self.properties['height'] = height

    def getWidth(self):
        return self.properties['width']

    def getHeight(self):
        return self.properties['height']

    def setHorizontalMovement(self, val):
        self.properties['horizontalMovement'] = val

    def setVerticalMovement(self, val):
        self.properties['verticalMovement'] = val

    def getHorizontalMovement(self):
        return self.properties['horizontalMovement']

    def getVerticalMovement(self):
        return self.properties['verticalMovement']

    def getLength(self):
        return self.properties['length']

    def setLength(self, val):
        self.properties['length'] = val

    def incrementLength(self):
        self.properties['length'] += self.properties['increaseLength']

    ## The main functions
    def movementChange(self, event):
        if event.key == pygame.K_LEFT:
            if(self.getHorizontalMovement()!=1):
                self.setHorizontalMovement(-1)
                self.setVerticalMovement(0)
                return True
        elif event.key == pygame.K_RIGHT:
            if(self.getHorizontalMovement()!=-1):
                self.setHorizontalMovement(1)
                self.setVerticalMovement(0)
                return True
        elif event.key == pygame.K_UP:
            if(self.getVerticalMovement()!=1):
                self.setVerticalMovement(-1)
                self.setHorizontalMovement(0)
                return True
        elif event.key == pygame.K_DOWN:
            if(self.getVerticalMovement()!=-1):
                self.setVerticalMovement(1)
                self.setHorizontalMovement(0)
                return True

        return False

    def movementUpdate(self, window):
        temp = [0, 0]
        if self.getHorizontalMovement() == 1:
            self.setXpos(self.getXpos() + self.getSpeed())
        elif self.getHorizontalMovement() == -1:
            self.setXpos(self.getXpos() - self.getSpeed())
        elif self.getVerticalMovement() == 1:
            self.setYpos(self.getYpos() + self.getSpeed())
        elif self.getVerticalMovement() == -1:
            self.setYpos(self.getYpos() - self.getSpeed())

        self.setXpos(self.getXpos() % window.getWidth())
        self.setYpos(self.getYpos() % window.getHeight())

        temp[0] = self.getXpos()
        temp[1] = self.getYpos()

        self.properties['snakeList'].append(temp)


        if len(self.properties['snakeList']) > self.getLength():
            del self.properties['snakeList'][0]

        if(self.properties['horizontalMovement']!=0 or self.properties['verticalMovement']!=0):
            for each in self.properties['snakeList'][:-1]:
                if each[0] == self.getXpos() and each[1] == self.getYpos():
                    print ("hoolah")
                    return True

        return False


    def render(self, displayObject):
        for coordinate in self.properties['snakeList']:
            pygame.draw.rect(displayObject, green, [coordinate[0], coordinate[1], self.getWidth(), self.getHeight()])


class Food:
    def __init__(self, snake, wallwidth, window, posx=0, posy=0, width=10, height=10):
        self.properties = dict(posx=posx, posy=posy, width=width, height=height)
        self.place(snake, wallwidth, window)

    def setPosition(self, *args):
        self.properties['posx'] = args[0]
        self.properties['posy'] = args[1]

    def getPosition(self):
        return self.properties['posx'], self.properties['posy']

    def getWidth(self):
        return self.properties['width']

    def place(self, snake, wallwidth, window):
        self.properties['posx'] = round(
            random.randrange(wallwidth, window.getWidth() - snake.getWidth() - wallwidth) / 10.0) * 10
        if self.properties['posx'] >= snake.getXpos():
            self.properties['posx'] += snake.getWidth()

        self.properties['posy'] = round(
            random.randrange(wallwidth, window.getHeight() - snake.getHeight() - wallwidth) / 10.0) * 10
        if self.properties['posx'] >= snake.getYpos():
            self.properties['posx'] += snake.getHeight()

    def render(self, displayObject):
        pygame.draw.rect(displayObject, red,
                         [self.properties['posx'], self.properties['posy'], self.getWidth(), self.getWidth()])
