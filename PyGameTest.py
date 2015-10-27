import pygame
from DropClass import Drop
import time
import random
import sys

pygame.init()

#Setting resolution
DisplayWidth=800
DisplayHeight=600
#Defining colours
Black=(0,0,0)
White=(255,255,255)
Red=(200,0,0)
BrightRed=(255,0,0)
Yellow=(255,215,0)
BrightYellow=(255,255,0)
Green=(0,200,0)
BrightGreen=(0,255,0)
Blue=(0,0,255)
#Loading character image
CharacterModel=pygame.image.load("Rec/Images/CharacterMain.png")
#Setting Character Dimensions
CharacterWidth=57
CharacterHeight=90
#Creating all instances
FGrade=Drop("Rec/Images/FGrade.png",-1000,0,85,65,5,0)
FGradeTwo=Drop("Rec/Images/FGrade.png",-1000,-1000,85,65,0,0)
AGrade=Drop("Rec/Images/AGrade.png",-1000,0,85,65,5,0)
Beer=Drop("Rec/Images/Beer.png",-1000,0,29,33,3,0)
Coffee=Drop("Rec/Images/coffee.png",-1000,0,29,40,0,0)
SpikedDrink=Drop("Rec/Images/SpikedDrink.png",-1000,0,34,30,0,0)
MenuBackground=pygame.image.load("Rec/Images/menuBackground.png")
LevelOneBackground=pygame.image.load("Rec/Images/LevelOne.png")
LevelTwoBackground=pygame.image.load("Rec/Images/LevelTwo.png")
LevelThreeBackground=pygame.image.load("Rec/Images/LevelThree.png")
#Lists
QuestionList=[]
TimeList=[]
#Attempt at sprite sheet lists
LeftList=[pygame.image.load("Rec/Images/SpriteImages/sprite_left_1.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_left_2.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_left_1.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_left_3.png")]
RightList=[pygame.image.load("Rec/Images/SpriteImages/sprite_right_1.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_right_2.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_right_1.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_right_3.png")]
UpList=[pygame.image.load("Rec/Images/SpriteImages/sprite_back_1.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_back_2.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_back_1.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_back_3.png")]
DownList=[pygame.image.load("Rec/Images/SpriteImages/sprite_front_1.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_front_2.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_front_1.png"),pygame.image.load("Rec/Images/SpriteImages/sprite_front_3.png")]
Level=1
BackgroundImage=White

#Creating the game screen
pygame.display.set_caption("Student Survival")
MainScreen=pygame.display.set_mode((DisplayWidth,DisplayHeight))
GameClock=pygame.time.Clock()

def CharacterSpeed(NewSpeed):
    CharacterSpeed=NewSpeed

#Updating functions for imported images
def Character(x,y):
    MainScreen.blit(CharacterModel,(x,y))

def PopulateList(FilePath,Remove):
    MyFile=open(FilePath,"r")   #Opens the file, read only
    MyList=[lines.split(",")for lines in MyFile] #Loops the lines in the list splitting the data elements by each comma
    for i in range(len(MyList)):     #Loops through the entire of the list
        del MyList[i][Remove]     #Removing the '\n' from each sub list in the list
    MyFile.close()
    return(MyList)

def WriteToDisk(FilePath,ListName):
    open(FilePath,"w").close()      #Clearing the file
    MyFile=open(FilePath,"w")
    FileStr='\n'.join(str(x) for x in ListName)
    MyFile.write(FileStr)
    MyFile.close()

#Text function displays text
def TextObject(Text, TextFont):
    TextSurface=TextFont.render(Text, True, Black)
    return TextSurface, TextSurface.get_rect()

def DisplayText(Text, TextSize,DisplayTime):
    TextFont=pygame.font.Font("freesansbold.ttf", TextSize)
    TextSurf, TextRect = TextObject(Text, TextFont)
    TextRect.center=((DisplayWidth/2),(DisplayHeight/2))
    MainScreen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(DisplayTime)

#Checks to see if the answer is correct
def CheckAnswer(QNum,answer):
    if answer==QuestionList[QNum][1]:
        return True
    else:
        return False

def ChangeLevel(Level):
    if(Level==1):
        DisplayText("Level 1!",70,2)
        FGrade.ResetCoordinates(random.randrange(0,(DisplayWidth-FGrade.getWidth())),-1000)
        FGradeTwo.ResetCoordinates(-1000,-1000) #Out the way
        AGrade.ResetCoordinates(random.randrange(0,(DisplayWidth-AGrade.getWidth())),-1000)
        Beer.ResetCoordinates(random.randrange(0,DisplayWidth-Beer.getWidth()),random.randrange(-5000,-2000))
        Coffee.ResetCoordinates(5,-100)  #So the player can't see it for level 1
        SpikedDrink.ResetCoordinates(5,-100) #Same as above
        FGrade.ResetSpeed(5,0)
        FGradeTwo.ResetSpeed(0,0)
        Beer.ResetSpeed(3,0)
        Coffee.ResetSpeed(0,0)
        SpikedDrink.ResetSpeed(0,0)
        LevelCounter=1
        RunLevel=0
        Score=0
        BackgroundImage=LevelOneBackground
    elif(Level==2):
        DisplayText("Level 2!",70,2)
        FGrade.ResetCoordinates(random.randrange(0,(DisplayWidth-FGrade.getWidth())),-1000)
        FGradeTwo.ResetCoordinates(-1000,-1000) #Out the way
        AGrade.ResetCoordinates(random.randrange(0,(DisplayWidth-AGrade.getWidth())),-1000)
        Beer.ResetCoordinates(random.randrange(0,DisplayWidth-Beer.getWidth()),random.randrange(-5000,-2000))
        Coffee.ResetCoordinates(random.randrange(0,DisplayWidth-Coffee.getWidth()),random.randrange(-5000,-2000))  #So the player can't see it for level 1
        SpikedDrink.ResetCoordinates(random.randrange(0,DisplayWidth-SpikedDrink.getWidth()),random.randrange(-5000,-2000)) #Same as above
        FGrade.ResetSpeed(4,10)
        FGradeTwo.ResetSpeed(0,0)
        Beer.ResetSpeed(7,3)
        Coffee.ResetSpeed(3,0)
        SpikedDrink.ResetSpeed(7,0)
        LevelCounter=2
        RunLevel=1
        Score=10
        BackgroundImage=LevelTwoBackground
    elif(Level==3):
        DisplayText("Level 3!",70,2)
        FGrade.ResetCoordinates(random.randrange(0,(DisplayWidth-FGrade.getWidth())),-1000)
        FGradeTwo.ResetCoordinates(random.randrange(0,(DisplayWidth-FGradeTwo.getWidth())),-1000)
        AGrade.ResetCoordinates(random.randrange(0,(DisplayWidth-AGrade.getWidth())),-1000)
        Beer.ResetCoordinates(random.randrange(0,DisplayWidth-Beer.getWidth()),random.randrange(-5000,-2000))
        Coffee.ResetCoordinates(random.randrange(0,DisplayWidth-Coffee.getWidth()),random.randrange(-5000,-2000))  #So the player can't see it for level 1
        SpikedDrink.ResetCoordinates(random.randrange(0,DisplayWidth-SpikedDrink.getWidth()),random.randrange(-5000,-2000)) #Same as above
        FGrade.ResetSpeed(4,10)
        FGradeTwo.ResetSpeed(4,-10)
        Beer.ResetSpeed(7,7)
        Coffee.ResetSpeed(3,-1)
        SpikedDrink.ResetSpeed(10,0)
        BackgroundImage=LevelThreeBackground

#Runs if the player has lost
def Crash():
    MainScreen.fill(White)
    DisplayText("You Lost!",70,2)
    GameLoop()
    
#Constantly keeps the score updated in the top left corner
def UpdateScore(Score, Level):
    font=pygame.font.SysFont(None,25)
    text=font.render("Score: "+str(Score)+" Level: "+str(Level),True,Black)
    MainScreen.blit(text,(0,0))

#Creates a button
def Button(btnText,x,y,Width,Height,TextSize,InactiveColour,ActiveColour,Event=None):
    Mouse=pygame.mouse.get_pos()
    Click=pygame.mouse.get_pressed()

    if((x+Width>Mouse[0]>x)and(y+Height>Mouse[1]>y)):
        pygame.draw.rect(MainScreen, ActiveColour,(x, y, Width, Height))
        if((Click[0]==1)and(Event!=None)):
            Event()
    else:
        pygame.draw.rect(MainScreen, InactiveColour,(x, y, Width, Height))

    SmallText=pygame.font.Font("freesansbold.ttf", TextSize)
    textSurf, textRect=TextObject(btnText, SmallText)
    textRect.center=((x+(Width/2)),(y+(Height/2)))
    MainScreen.blit(textSurf, textRect)

def QuestionButton(btnText,x,y,Width,Height,TextSize,InactiveColour,ActiveColour,Level,QuestionNum,answer):
    Mouse=pygame.mouse.get_pos()
    Click=pygame.mouse.get_pressed()

    if((x+Width>Mouse[0]>x)and(y+Height>Mouse[1]>y)):
        pygame.draw.rect(MainScreen, ActiveColour,(x, y, Width, Height))
        if(Click[0]==1):
            if(CheckAnswer(QuestionNum,answer)==True):
                NewLevel=Level+1
                return(NewLevel)
            else:
                return(Level)
    else:
        pygame.draw.rect(MainScreen, InactiveColour,(x, y, Width, Height))

    SmallText=pygame.font.Font("freesansbold.ttf", TextSize)
    textSurf, textRect=TextObject(btnText, SmallText)
    textRect.center=((x+(Width/2)),(y+(Height/2)))
    MainScreen.blit(textSurf, textRect)

def QuitGame():
    pygame.quit()
    quit()

def Question(QuestionList,QuestionNum,Level):
    Question=True

    while Question:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                QuitGame()
        MainScreen.fill(White)
        DisplayText(QuestionList[QuestionNum][0],20,0)
        Option1=QuestionButton(QuestionList[QuestionNum][1],100,400,200,100,20,Green,BrightGreen,Level,QuestionNum,QuestionList[QuestionNum][1])    #creates answer buttons
        Option2=QuestionButton(QuestionList[QuestionNum][2],500,400,200,100,20,Green,BrightGreen,Level,QuestionNum,QuestionList[QuestionNum][2])
        pygame.display.update()
        GameClock.tick(15)
        if((Option1!=None)or(Option2!=None)):
            break
    if(Option1!=None):      #returns new level value depending on answer
        MainScreen.fill(White)
        DisplayText("Correct!",50,2)
        return(Option1)
    if(Option2!=None):
        MainScreen.fill(White)
        DisplayText("Wrong!",50,2)
        return(Option2)

def ShowTimes():
    Menu=True
    while Menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                QuitGame()
        MainScreen.blit(MenuBackground,(0,0))
        with open("Rec/Data/Times.txt","r") as MyFile:
            TimeList=MyFile.read().splitlines()
        MyFile.close()          
        Button("Quit",550,500,200,100,40,Red,BrightRed,GameMenu)
        YSize=500
        for i in range(len(TimeList)):
            YSize-=100
            Text=str(TimeList[2-i])
            TextFont=pygame.font.Font("freesansbold.ttf", 30)
            TextSurf, TextRect = TextObject(Text, TextFont)
            TextRect.center=((DisplayWidth/2),(YSize))
            MainScreen.blit(TextSurf, TextRect)
            pygame.display.update()

def GameMenu():
    Menu=True

    while Menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                QuitGame()
        MainScreen.blit(MenuBackground,(0,0))
        DisplayText("Student Survival",70,0)

        Button("Start",50,400,200,100,40,Green,BrightGreen,GameLoop)
        Button("Best Times",300,400,200,100,35,Yellow,BrightYellow,ShowTimes)
        Button("Quit",550,400,200,100,40,Red,BrightRed,QuitGame)
        
        pygame.display.update()
        GameClock.tick(15)

def GameLoop():
    #Coordinates and moving varibles
    x=350
    y=500
    x_Change=0
    y_Change=0
    LevelCounter=1
    CharacterSpeed=5
    LeftPress=False
    RightPress=False
    UpPress=False
    DownPress=False
    Score=0
    Level=1
    GameTimer=0
    BeerStart=0
    CoffeeStart=0
    SpikedStart=0
    BeerAffected=False
    CoffeeAffected=False
    SpikedAffected=False
    RunLevel=0
    Counter=0
    
    #Setting Coordinates of drop objects
    FGrade.ResetCoordinates(random.randrange(0,(DisplayWidth-FGrade.getWidth())),-1000)
    AGrade.ResetCoordinates(random.randrange(0,(DisplayWidth-AGrade.getWidth())),-1000)
    Beer.ResetCoordinates(random.randrange(0,DisplayWidth-Beer.getWidth()),random.randrange(-5000,-2000))
    Coffee.ResetCoordinates(5,-100)  #So the player can't see it for level 1
    SpikedDrink.ResetCoordinates(5,-100) #Same as above
    
    #Init of main loop variable
    GameExit=False
    MainScreen.fill(White)
    BackgroundImage=LevelOneBackground
    ChangeLevel(1)
    #Main game loop
    while not GameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                QuitGame()
            MainScreen.blit(BackgroundImage,(0,0))
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    CharacterModel=(LeftList[Counter])
                    Counter=(Counter+1)%len(LeftList)
                    LeftPress=True
                if event.key==pygame.K_RIGHT:
                    CharacterModel=(RightList[Counter])
                    Counter=(Counter+1)%len(RightList)
                    RightPress=True
                if event.key==pygame.K_UP:
                    CharacterModel=(UpList[Counter])
                    Counter=(Counter+1)%len(UpList)
                    UpPress=True
                if event.key==pygame.K_DOWN:
                    CharacterModel=(DownList[Counter])
                    Counter=(Counter+1)%len(DownList)
                    DownPress=True
            if event.type==pygame.KEYUP:
                if LeftPress and event.key==pygame.K_LEFT:
                    LeftPress=False
                if RightPress and event.key==pygame.K_RIGHT:
                    RightPress=False
                if UpPress and event.key==pygame.K_UP:
                    UpPress=False
                if DownPress and event.key==pygame.K_DOWN:
                    DownPress=False

        #Changing coordinates to move image for x axis
        if LeftPress and RightPress:
            x_Change*=1    #Stays the same
        elif LeftPress:
            x_Change=-CharacterSpeed
        elif RightPress:
            x_Change=CharacterSpeed
        else:
            x_Change=0
        x+=x_Change

        #Changing coordinates to move image for y axis
        if UpPress and DownPress:
            y_Change*=1    #Stays the same
        elif UpPress:
            y_Change=-CharacterSpeed
        elif DownPress:
            y_Change=CharacterSpeed
        else:
            y_Change=0
        y+=y_Change

        #Creating background and updating all objects
        MainScreen.fill(White)
        #MainScreen.blit(BackgroundImage,(0,0))
        #PC lags with this images loading
        FGrade.Update(MainScreen)
        FGradeTwo.Update(MainScreen)
        AGrade.Update(MainScreen)
        Beer.Update(MainScreen)
        Coffee.Update(MainScreen)
        SpikedDrink.Update(MainScreen)
        Character(x,y)
        UpdateScore(Score, LevelCounter)
        #Level 2
        if(LevelCounter==2)and(RunLevel==0):
            LevelVal=Question(QuestionList,0,1)
            MainScreen.fill(White)
            pygame.display.update()
            ChangeLevel(LevelVal)
            pygame.display.update()
            RunLevel=1
            #Resetting the values so character doesn't keep moving
            LeftPress=False
            RightPress=False
            UpPress=False
            DownPress=False
            if LevelVal==1:
                Score=0
                LevelCounter=1
                RunLevel=0
            elif LevelVal==2:
                Score=10
                LevelCounter=2
        #Level 3
        if(LevelCounter==3)and(RunLevel==1):
            LevelVal=Question(QuestionList,1,2)
            MainScreen.fill(White)
            pygame.display.update()
            ChangeLevel(LevelVal)
            pygame.display.update()
            RunLevel=2
            #Resetting the values so character doesn't keep moving
            LeftPress=False
            RightPress=False
            UpPress=False
            DownPress=False
            if LevelVal==2:
                Score=10
                LevelCounter=2
                RunLevel=1
            elif LevelVal==3:
                Score=20
                LevelCounter=3

        #Creating boundaries
        if x<0:
            x=0
        if x>DisplayWidth-CharacterWidth:
            x=(DisplayWidth-CharacterWidth)
        if y<0:
            y=0
        if y>DisplayHeight-CharacterHeight:
            y=(DisplayHeight-CharacterHeight)
        #Creating Boundaries for F grade
        if FGrade.x<0:
            FGrade.setXSpeed(FGrade.getXSpeed()*-1)
        if FGrade.x>(DisplayWidth-FGrade.Width):
            FGrade.setXSpeed(FGrade.getXSpeed()*-1)
        #Creating Boundaries for F grade
        if FGradeTwo.x<0:
            FGradeTwo.setXSpeed(FGradeTwo.getXSpeed()*-1)
        if FGradeTwo.x>(DisplayWidth-FGradeTwo.Width):
            FGradeTwo.setXSpeed(FGradeTwo.getXSpeed()*-1)
        #Creating Boundaries for beer
        if Beer.x<0:
            Beer.setXSpeed(Beer.getXSpeed()*-1)
        if Beer.x>(DisplayWidth-Beer.Width):
            Beer.setXSpeed(Beer.getXSpeed()*-1)
        #Resetting A Grade after going off screen
        if(AGrade.y>DisplayHeight):
            AGrade.y=0-AGrade.Height
            AGrade.x=random.randrange(0,(DisplayWidth-AGrade.Width))
        #Resetting F Grade after going off screen
        if(FGrade.y>DisplayHeight):
            FGrade.y=(0-FGrade.Height)
            FGrade.x=random.randrange(0,(DisplayWidth-FGrade.Width))
        #Resetting second F Grade after going off screen
        if(FGradeTwo.y>DisplayHeight):
            FGradeTwo.y=(0-FGradeTwo.Height)
            FGradeTwo.x=random.randrange(0,(DisplayWidth-FGradeTwo.Width))
        #Resetting Beer after going off screen
        if(Beer.y>DisplayHeight):
            Beer.ResetCoordinates(random.randrange(-5000,-2000),random.randrange(0,DisplayWidth-Beer.Width))
        #Resetting Coffee after going off screen
        if(Coffee.y>DisplayHeight):
            Coffee.ResetCoordinates(random.randrange(-3000,-1000),random.randrange(0,(DisplayWidth-Coffee.Width)))
        #Resetting Spiked Drink after going off screen
        if(SpikedDrink.y>DisplayHeight):
            SpikedDrink.ResetCoordinates(random.randrange(-3000,-1000),random.randrange(0,(DisplayWidth-Coffee.Width)))
            
        #Collision Logic for bad grade
        if (y>FGrade.y)and(y<FGrade.y+FGrade.Height)or(y+CharacterHeight>FGrade.y)and(y+CharacterHeight<FGrade.y+FGrade.Height):
            if (x>FGrade.x)and(x<FGrade.x+FGrade.Width)or(x+CharacterWidth>FGrade.x)and(x+CharacterWidth<FGrade.x+FGrade.Width):
                Crash()
        #Collision Logic for second bad grade
        if (y>FGradeTwo.y)and(y<FGradeTwo.y+FGradeTwo.Height)or(y+CharacterHeight>FGradeTwo.y)and(y+CharacterHeight<FGradeTwo.y+FGradeTwo.Height):
            if (x>FGradeTwo.x)and(x<FGradeTwo.x+FGradeTwo.Width)or(x+CharacterWidth>FGradeTwo.x)and(x+CharacterWidth<FGradeTwo.x+FGradeTwo.Width):
                Crash()
        #Collision Logic for good grade
        if (y>AGrade.y)and(y<AGrade.y+AGrade.Height)or(y+CharacterHeight>AGrade.y)and(y+CharacterHeight<AGrade.y+AGrade.Height):
            if (x>AGrade.x)and(x<AGrade.x+AGrade.Width)or(x+CharacterWidth>AGrade.x)and(x+CharacterWidth<AGrade.x+AGrade.Width):
                Score+=5
                AGrade.ResetCoordinates(random.randrange(0,(DisplayWidth-AGrade.Width)),0-AGrade.Height)
        #Collision for beer
        if (y>Beer.y)and(y<Beer.y+Beer.Height)or(y+CharacterHeight>Beer.y)and(y+CharacterHeight<Beer.y+Beer.Height):
            if (x>Beer.x)and(x<Beer.x+Beer.Width)or(x+CharacterWidth>Beer.x)and(x+CharacterWidth<Beer.x+Beer.Width):
                CharacterSpeed=2
                Beer.ResetCoordinates(random.randrange(0,DisplayWidth-Beer.Width),random.randrange(-5000,-2000))
        #Collision for Coffee
        if (y>Coffee.y)and(y<Coffee.y+Coffee.Height)or(y+CharacterHeight>Coffee.y)and(y+CharacterHeight<Coffee.y+Coffee.Height):
            if (x>Coffee.x)and(x<Coffee.x+Coffee.Width)or(x+CharacterWidth>Coffee.x)and(x+CharacterWidth<Coffee.x+Coffee.Width):
                CharacterSpeed=10
                Coffee.ResetCoordinates(random.randrange(0,(DisplayWidth-Coffee.Width)),random.randrange(-3000,-1000))
        #Collision for spiked drink
        if (y>SpikedDrink.y)and(y<SpikedDrink.y+SpikedDrink.Height)or(y+CharacterHeight>SpikedDrink.y)and(y+CharacterHeight<SpikedDrink.y+SpikedDrink.Height):
            if (x>SpikedDrink.x)and(x<SpikedDrink.x+SpikedDrink.Width)or(x+CharacterWidth>SpikedDrink.x)and(x+CharacterWidth<SpikedDrink.x+SpikedDrink.Width):
                CharacterSpeed=-5
                SpikedDrink.ResetCoordinates(random.randrange(0,(DisplayWidth-Coffee.Width)),random.randrange(-3000,-1000))
    
        #Updates the display through every iteration of the loop
        GameTimer+=1
        #Beer affect Logic
        if (CharacterSpeed==2)and(BeerAffected==False):
            BeerAffected=True
            BeerStart=GameTimer
        if GameTimer==(BeerStart+300):
            BeerAffected=False
            CharacterSpeed=5
        #Coffee Affect Logic
        if (CharacterSpeed==10)and(CoffeeAffected==False):
            CoffeeAffected=True
            CoffeeStart=GameTimer
        if GameTimer==(CoffeeStart+300):
            CoffeeAffected=False
            CharacterSpeed=5
        #Spiked Drink Affect logic
        if (CharacterSpeed==-5)and(SpikedAffected==False):
            SpikedAffected=True
            SpikedStart=GameTimer
        if GameTimer==SpikedStart+300:
            SpikedAffected=False
            CharacterSpeed=5
        #Leveling
        if Score==10:
            LevelCounter=2
        if Score==20:
            LevelCounter=3
        if Score==30:
            LevelVal=Question(QuestionList,2,3)
            if(LevelVal==4):
                MainScreen.fill(White)
                with open("Rec/Data/Times.txt","r") as MyFile:
                    TimeList=MyFile.read().splitlines()
                MyFile.close()    
                print(TimeList)
                DisplayText("You Win!",70,2)
                print(TimeList)
                for i in range(len(TimeList)):
                    if(GameTimer<=int(TimeList[i])):
                        TimeList.insert(i,GameTimer)
                        del TimeList[3]
                        break
                print(TimeList)
                WriteToDisk("Rec/Data/Times.txt",TimeList)
                GameExit=True
            else:
                Crash()
        print(GameTimer)
        pygame.display.update()
        GameClock.tick(60)

QuestionList=PopulateList("Rec/Data/Questions.txt",3)
GameMenu()
GameLoop()
pygame.quit()
quit()
