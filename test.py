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
        pg.draw.rect(displaySurface,self.colourPrimary,(self.XposRect,self.YposRect,self.XlongRect,self.YlongRect),lineThickness)

class chartRound(chartObjects):
    ObjectName = 'Rounded-Terminal'
    ObjectId =  'round'
    # 2 circles 1rect
    XlongRect = 75
    YlongRect = 42
    def __init__(self) -> None:
        self.XposRect = self.Xpos-(self.XlongRect/2)
        self.YposRect = self.Ypos-(self.YlongRect/2)
    def showOrigin(self):
        return super().showOrigin()
    def showMe(self):
        pg.draw.rect(displaySurface,self.colourPrimary,(self.XposRect,self.YposRect,self.XlongRect,self.YlongRect),lineThickness,border_bottom_left_radius=int(self.YlongRect/2),border_bottom_right_radius=int(self.YlongRect/2),border_top_left_radius=int(self.YlongRect/2),border_top_right_radius=int(self.YlongRect/2))



class chartPara(chartObjects):
    ObjectName = 'Parallelogram-Input/Output'
    ObjectId = 'para'
    # 1 poly
    Ylong = 32
    XlongEnd = 30
    XlongMid = 30
    def __init__(self):
        self.XposPoint1 = self.Xpos-self.XlongEnd-(self.XlongMid/2)
        self.YposPoint1 = self.Ypos-(self.Ylong/2)
        self.XposPoint2 = self.Xpos+(self.XlongMid/2)
        self.YposPoint2 = self.Ypos-(self.Ylong/2)
        self.XposPoint3 = self.Xpos+(self.XlongMid/2)+self.XlongEnd
        self.YposPoint3 = self.Ypos+(self.Ylong/2)
        self.XposPoint4 = self.Xpos-(self.XlongMid/2)
        self.YposPoint4 = self.Ypos+(self.Ylong/2)
        
        
    def showOrigin(self):
        return super().showOrigin()
    def showMe(self):
        pg.draw.polygon(displaySurface,self.colourPrimary,((self.XposPoint1,self.YposPoint1),(self.XposPoint2,self.YposPoint2),(self.XposPoint3,self.YposPoint3),(self.XposPoint4,self.YposPoint4)),lineThickness)
class chartDiam(chartObjects):
    ObjectName = 'Diamond-Decision'
    ObjectId = 'diam'
    # 1 poly
    longPoly = 60
    def __init__(self):
        self.XposPolyPoint1 = self.Xpos-(self.longPoly/2)
        self.YposPolyPoint1 = self.Ypos
        self.XposPolyPoint2 = self.Xpos
        self.YposPolyPoint2 = self.Ypos-(self.longPoly/2)
        self.XposPolyPoint3 = self.Xpos+(self.longPoly/2)
        self.YposPolyPoint3 = self.Ypos
        self.XposPolyPoint4 = self.Xpos
        self.YposPolyPoint4 = self.Ypos+(self.longPoly/2)
    def showOrigin(self):
        return super().showOrigin()
    def showMe(self):
        pg.draw.polygon(displaySurface,self.colourPrimary,((self.XposPolyPoint1,self.YposPolyPoint1),(self.XposPolyPoint2,self.YposPolyPoint2),(self.XposPolyPoint3,self.YposPolyPoint3),(self.XposPolyPoint4,self.YposPolyPoint4)),lineThickness)

def changeCellObject(Xcoord,Ycoord,type):
    print(imgArray[Xcoord][Ycoord].Xpos)
    Xpos = imgArray[Xcoord][Ycoord].Xpos
    Ypos = imgArray[Xcoord][Ycoord].Ypos
    match type:
        case 'rect':
            newObject = chartRect()
            newObject.Xpos = Xpos
            newObject.Ypos = Ypos
            newObject.colourPrimary = rgb().black
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
            newObject.colourPrimary = rgb().black
            newObject.__init__()
            return newObject
        case 'diam':
            newObject = chartDiam()
            newObject.Xpos = Xpos
            newObject.Ypos = Ypos
            newObject.colourPrimary = rgb().black
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
lineThickness = 1
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
                    # imgArray[0][3] = changeCellObject(0,3,'diam')
                    # imgArray[0][3].showMe()
  
        # Draws the surface object to the screen.  
        if updateDisplay:
            updateDisplay = False
            


            pg.display.update()  

# MAIN LOOP END