# the proof of concept
# 20x20 grid

# temp
# ---
# INIT GENERAL 
class rgb():
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    black = (0, 0, 0) 
    grey = (35,35,40)
    red = (255, 0, 0) 


import pygame as pg
pg.init()

displaySize = (600,400)
displaySurface = pg.display.set_mode(displaySize)
displayBackgroundColour = rgb.grey
displaySurface.fill(displayBackgroundColour)
running = True
updateDisplay = False

class chartObjects():
    colourSelection = rgb()
    colourPrimary = displayBackgroundColour
    ObjectName = 'Empty'
    ObjectId = 'empty'
    Xpos = 0 # to be defined
    Ypos = 0 # to be defined
    def showOrigin(self):
        pg.draw.circle(displaySurface,self.colourSelection.red,(self.Xpos,self.Ypos),2,2)

class chartRect(chartObjects):
    ObjectName = 'Rectangle-Process'
    ObjectId = 'rect'
    # rect
    XlongRect = 100
    YlongRect = 30
    def __init__(self) -> None:
        self.XposRect = self.Xpos-(self.XlongRect/2)
        self.YposRect = self.Ypos-(self.YlongRect/2)
    def showOrigin(self):
        return super().showOrigin()
    def showMe(self):
        pg.draw.rect(displaySurface,self.colourPrimary,(self.XposRect,self.YposRect,self.XlongRect,self.YlongRect))

class chartRound(chartObjects):
    ObjectName = 'Rounded-Terminal'
    ObjectId =  'round'
    # 2 circles 1rect
    XlongRect = 50
    YlongRect = 35
    def __init__(self) -> None:
        self.XposRect = self.Xpos-(self.XlongRect/2)
        self.YposRect = self.Ypos-(self.YlongRect/2)

        # CIRCLE LEFT
        self.XposCircle1 = self.Xpos-(self.XlongRect/2)
        self.YposCircle1 = self.Ypos

        # CIRCLE RIGHT
        self.XposCircle2 = self.Xpos+(self.XlongRect/2)
        self.YposCircle2 = self.Ypos
    
    def showOrigin(self):
        return super().showOrigin()
    def showMe(self):
        pg.draw.circle(displaySurface,self.colourPrimary,(self.XposCircle1,self.YposCircle1),(self.YlongRect/2))
        pg.draw.circle(displaySurface,self.colourPrimary,(self.XposCircle2,self.YposCircle2),(self.YlongRect/2))
        pg.draw.rect(displaySurface,self.colourPrimary,(self.XposRect,self.YposRect,self.XlongRect,self.YlongRect))



class chartPara(chartObjects):
    ObjectName = 'Parallelogram-Input/Output'
    ObjectId = 'para'
    # 2 poly, 1 rect
    XlongRect = 20
    YlongRect = 30
    XlongPoly = 30
    def __init__(self):
        self.XposRect = self.Xpos-(self.XlongRect/2)
        self.YposRect = self.Ypos-(self.YlongRect/2)

        # POLYGON LEFT
        self.XposPoly1Point1 = self.Xpos-(self.XlongRect/2)-self.XlongPoly
        self.YposPoly1Point1 = self.Ypos-(self.YlongRect/2)
        self.XposPoly1Point2 = self.Xpos-(self.XlongRect/2)
        self.YposPoly1Point2 = self.Ypos-(self.YlongRect/2)
        self.XposPoly1Point3 = self.Xpos-(self.XlongRect/2)
        self.YposPoly1Point3 = self.Ypos+(self.YlongRect/2)

        # POLYGON RIGHT
        self.XposPoly2Point1 = self.Xpos+(self.XlongRect/2)+self.XlongPoly
        self.YposPoly2Point1 = self.Ypos+(self.YlongRect/2)
        self.XposPoly2Point2 = self.Xpos+(self.XlongRect/2)
        self.YposPoly2Point2 = self.Ypos-(self.YlongRect/2)
        self.XposPoly2Point3 = self.Xpos+(self.XlongRect/2)
        self.YposPoly2Point3 = self.Ypos+(self.YlongRect/2)
    def showOrigin(self):
        return super().showOrigin()
    def showMe(self):
        pg.draw.rect(displaySurface,self.colourPrimary,(self.XposRect,self.YposRect,self.XlongRect,self.YlongRect+1))
        pg.draw.polygon(displaySurface,self.colourPrimary,((self.XposPoly1Point1,self.YposPoly1Point1),(self.XposPoly1Point2,self.YposPoly1Point2),(self.XposPoly1Point3,self.YposPoly1Point3)))
        pg.draw.polygon(displaySurface,self.colourPrimary,((self.XposPoly2Point1,self.YposPoly2Point1),(self.XposPoly2Point2,self.YposPoly2Point2),(self.XposPoly2Point3,self.YposPoly2Point3)))


def changeCellObject(Xcoord,Ycoord,type):
    print(imgArray[Xcoord][Ycoord].Xpos)
    Xpos = imgArray[Xcoord][Ycoord].Xpos
    Ypos = imgArray[Xcoord][Ycoord].Ypos
    match type:
        case 'rect':
            newObject = chartRect()
            newObject.Xpos = Xpos
            newObject.Ypos = Ypos
            newObject.colourPrimary = rgb().blue
            newObject.__init__()
            return newObject
        case 'para':
            newObject = chartPara()
            newObject.Xpos = Xpos
            newObject.Ypos = Ypos
            newObject.colourPrimary = rgb().blue
            newObject.__init__()
            return newObject
        case 'round':
            newObject = chartRound()
            newObject.Xpos = Xpos
            newObject.Ypos = Ypos
            newObject.colourPrimary = rgb().blue
            newObject.__init__()
            return newObject
        case _:
            print('Major Error: invalid type given in funct:changeCellObject')

imgArray = []
for i in range(10): # x axis
    imgArray.append([])
    for j in range(10): # y axis
        imgArray[-1].append('')
        imgArray[-1][-1] = chartObjects()
        imgArray[-1][-1].Xpos = (displaySize[0]/(10+1))*(i+1)
        imgArray[-1][-1].Ypos = (displaySize[1]/(10+1))*(j+1)
        imgArray[-1][-1].showOrigin()
    
# INIT GENERAL END
# ---
# INIT IMAGES HERE

# END INIT IMAGES
# ---
# MAIN LOOP
while running : 
      
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pg.event.get() : 

        if event.type == pg.QUIT : 
            # stops loop
            running = False
            # deactivates the pygame library 
            pg.quit() 
            # quit the program. 
            quit() 
        if event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_1:
                    updateDisplay = True
                    displayBackgroundColour = rgb.white
                    displaySurface.fill(displayBackgroundColour)
                case pg.K_2:
                    updateDisplay = True
                    imgArray[0][1] = changeCellObject(0,1,'round')
                    imgArray[0][1].showMe()
                    imgArray[0][2] = changeCellObject(0,2,'para')
                    imgArray[0][2].showMe()
                    imgArray[0][3] = changeCellObject(0,3,'rect')
                    imgArray[0][3].showMe()
  
        # Draws the surface object to the screen.  
        if updateDisplay:
            updateDisplay = False
            


            pg.display.update()  

# MAIN LOOP END