import pygame

class Drop:
    def __init__(self,ImagePath,y,x,ImageHeight,ImageWidth,YSpeed,XSpeed):
        self.Image=pygame.image.load(ImagePath)
        self.y=y
        self.x=x
        self.Height=ImageHeight
        self.Width=ImageWidth
        self.YSpeed=YSpeed
        self.XSpeed=XSpeed

    def Update(self,Display):
        self.y+=self.YSpeed
        self.x+=self.XSpeed
        Display.blit(self.Image,(self.x,self.y))

    def ResetSpeed(self,ySpeed,xSpeed):
        self.YSpeed=ySpeed
        self.XSpeed=xSpeed

    def ResetCoordinates(self,x,y):
        self.x=x
        self.y=y

    def setYSpeed(self,Speed):
        self.YSpeed=Speed

    def setXSpeed(self,Speed):
        self.XSpeed=Speed

    def getYSpeed(self):
        return self.YSpeed

    def getXSpeed(self):
        return self.XSpeed

    def getHeight(self):
        return self.Height
    def getWidth(self):
        return self.Width
