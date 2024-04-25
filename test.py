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

displaySize = (1200,720)
displaySurface = pg.display.set_mode(displaySize)
displayBackgroundColour = rgb.white
displaySurface.fill(displayBackgroundColour)

imgArray = [] # contains standard coords
imgArraySize = [10,10]
for i in range(imgArraySize[0]): # x axis
    imgArray.append([])
    for j in range(imgArraySize[1]): # y axis
        imgArray[-1].append((((displaySize[0]/(imgArraySize[0]+1))*(i+1)),((displaySize[1]/(imgArraySize[1]+1))*(j+1))))

cellSize = (displaySize[0]/(imgArraySize[0]),displaySize[1]/(imgArraySize[1]))
objectArray = [] # contains object coords
lineThickness = 1
updateDisplay = True

imgArrayCursorPos = [0,0]


class chartObjects():
    colourSelection = rgb()
    colourPrimary = rgb().black
    ObjectName = 'Empty'
    ObjectId = 'empty'
    Xpos = 0 # to be defined
    Ypos = 0 # to be defined
    def __init__(self):
        anchorPos = []
    def showOrigin(self):
        pg.draw.circle(displaySurface,self.colourSelection.red,(self.Xpos,self.Ypos),2,2)
        for i in self.anchorPos:
            pg.draw.circle(displaySurface,self.colourSelection.blue,(i['Xpos'],i['Ypos']),2,2)
    def moveMe(self,newXpos,newYpos):
        self.Xpos = newXpos
        self.Ypos = newYpos

class chartRect(chartObjects):
    ObjectName = 'Rectangle-Process'
    ObjectId = 'rect'
    # rect
    XlongRect = 80
    YlongRect = 36
    def __init__(self):
        self.anchorPos = [{},{}]
    def moveMe(self,newXpos,newYpos):
        self.Xpos = newXpos
        self.Ypos = newYpos
        self.XposRect = newXpos-(self.XlongRect/2)
        self.YposRect = newYpos-(self.YlongRect/2)

        self.anchorPos[0]['Xpos'] = newXpos
        self.anchorPos[0]['Ypos'] = newYpos-(self.YlongRect/2)
        self.anchorPos[1]['Xpos'] = newXpos
        self.anchorPos[1]['Ypos'] = newYpos+(self.YlongRect/2)
        
    def showOrigin(self):
        return super().showOrigin()
    def showMe(self):
        pg.draw.rect(displaySurface,self.colourPrimary,(self.XposRect,self.YposRect,self.XlongRect,self.YlongRect),lineThickness)

class chartRound(chartObjects):
    ObjectName = 'Rounded-Terminal'
    ObjectId =  'round'
    # 2 circles 1 rect
    XlongRect = 75
    YlongRect = 42
    def __init__(self):
        self.anchorPos = [{},{}]
    def showOrigin(self):
        return super().showOrigin()
    def moveMe(self,newXpos,newYpos):
        self.Xpos = newXpos
        self.Ypos = newYpos
        self.XposRect = newXpos-(self.XlongRect/2)
        self.YposRect = newYpos-(self.YlongRect/2)

        self.anchorPos[0]['Xpos'] = newXpos
        self.anchorPos[0]['Ypos'] = newYpos-(self.YlongRect/2)
        self.anchorPos[1]['Xpos'] = newXpos
        self.anchorPos[1]['Ypos'] = newYpos+(self.YlongRect/2)
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
        self.anchorPos = [{},{}]
    def showOrigin(self):
        return super().showOrigin()
    def moveMe(self,newXpos,newYpos):
        self.Xpos = newXpos
        self.Ypos = newYpos
        self.XposPoint1 = self.Xpos-self.XlongEnd-(self.XlongMid/2)
        self.YposPoint1 = self.Ypos-(self.Ylong/2)
        self.XposPoint2 = self.Xpos+(self.XlongMid/2)
        self.YposPoint2 = self.Ypos-(self.Ylong/2)
        self.XposPoint3 = self.Xpos+(self.XlongMid/2)+self.XlongEnd
        self.YposPoint3 = self.Ypos+(self.Ylong/2)
        self.XposPoint4 = self.Xpos-(self.XlongMid/2)
        self.YposPoint4 = self.Ypos+(self.Ylong/2)

        self.anchorPos[0]['Xpos'] = newXpos
        self.anchorPos[0]['Ypos'] = newYpos-(self.Ylong/2)
        self.anchorPos[1]['Xpos'] = newXpos
        self.anchorPos[1]['Ypos'] = newYpos+(self.Ylong/2)
    def showMe(self):
        pg.draw.polygon(displaySurface,self.colourPrimary,((self.XposPoint1,self.YposPoint1),(self.XposPoint2,self.YposPoint2),(self.XposPoint3,self.YposPoint3),(self.XposPoint4,self.YposPoint4)),lineThickness)
class chartDiam(chartObjects):
    ObjectName = 'Diamond-Decision'
    ObjectId = 'diam'
    # 1 poly
    longPoly = 60
    def __init__(self):
        self.anchorPos = [{},{}]
    def moveMe(self,newXpos,newYpos):
        self.Xpos = newXpos
        self.Ypos = newYpos
        self.XposPoint1 = self.Xpos-(self.longPoly/2)
        self.YposPoint1 = self.Ypos
        self.XposPoint2 = self.Xpos
        self.YposPoint2 = self.Ypos-(self.longPoly/2)
        self.XposPoint3 = self.Xpos+(self.longPoly/2)
        self.YposPoint3 = self.Ypos
        self.XposPoint4 = self.Xpos
        self.YposPoint4 = self.Ypos+(self.longPoly/2)

        self.anchorPos[0]['Xpos'] = newXpos
        self.anchorPos[0]['Ypos'] = newYpos-(self.longPoly/2)
        self.anchorPos[1]['Xpos'] = newXpos
        self.anchorPos[1]['Ypos'] = newYpos+(self.longPoly/2)
    def showOrigin(self):
        return super().showOrigin()
    def showMe(self):
        pg.draw.polygon(displaySurface,self.colourPrimary,((self.XposPoint1,self.YposPoint1),(self.XposPoint2,self.YposPoint2),(self.XposPoint3,self.YposPoint3),(self.XposPoint4,self.YposPoint4)),lineThickness)


def newCellObject(imgArrayContent,objectType):
    match objectType:
        case 'empty':
            cellObject = chartObjects()
        case 'rect':
            cellObject = chartRect()
        case 'round':
            cellObject = chartRound()
        case 'diam':
            cellObject = chartDiam()
        case 'para':
            cellObject = chartPara()
    cellObject.__init__()
    cellObject.moveMe(imgArrayContent[0],imgArrayContent[1])
    return cellObject
    

# INIT GENERAL END
# ---
# MAIN LOOP
running = True
updateDisplay = True
while running : 
      
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pg.event.get() : 
        # Draw the cursor
        
        if event.type == pg.QUIT : 
            # stops loop
            running = False
            # deactivates the pygame library 
            pg.quit() 
            # quit the program. 
            quit() 
        if event.type == pg.KEYDOWN:
            updateDisplay = True # TEMP TODO REMOVE
            match event.key:
                # Move cursor
                case pg.K_UP:
                    if imgArrayCursorPos[1] != 0:
                        imgArrayCursorPos[1] -= 1
                    else:
                        imgArrayCursorPos[1] = imgArraySize[1]-1
                case pg.K_DOWN:
                    if imgArrayCursorPos[1]+1 < imgArraySize[1]:
                        imgArrayCursorPos[1] += 1
                    else:
                        imgArrayCursorPos[1] = 0
                case pg.K_LEFT:
                    if imgArrayCursorPos[0] != 0:
                        imgArrayCursorPos[0] -= 1
                    else:
                        imgArrayCursorPos[0] = imgArraySize[0]-1
                case pg.K_RIGHT:
                    if imgArrayCursorPos[0]+1 < imgArraySize[1]:
                        imgArrayCursorPos[0] += 1
                    else:
                        imgArrayCursorPos[0] = 0
                # commands
                case pg.K_1:
                    updateDisplay = True
                    objectArray = [] # contains object coords 
                case pg.K_2:
                    updateDisplay = True
                    objectArray.append(newCellObject(imgArray[imgArrayCursorPos[0]][imgArrayCursorPos[1]],'round'))
                case pg.K_3:
                    updateDisplay = True
                    objectArray.append(newCellObject(imgArray[imgArrayCursorPos[0]][imgArrayCursorPos[1]],'rect'))
                case pg.K_4:
                    updateDisplay = True
                    objectArray.append(newCellObject(imgArray[imgArrayCursorPos[0]][imgArrayCursorPos[1]],'diam'))
                case pg.K_5:
                    updateDisplay = True
                    objectArray.append(newCellObject(imgArray[imgArrayCursorPos[0]][imgArrayCursorPos[1]],'para'))
                case pg.K_0:
                    updateDisplay = True
                    if len(objectArray)>0:
                        objectArray.remove(objectArray[-1])
                    else: print('nothing to undo!')
    
        # Draws the surface object to the screen.  
    if updateDisplay:
        updateDisplay = False
        # clear display
        displayBackgroundColour = rgb.white
        displaySurface.fill(displayBackgroundColour)
        # KEEP IT SIMPLE STUPID
        pg.draw.rect(displaySurface,rgb.grey,(imgArray[imgArrayCursorPos[0]][imgArrayCursorPos[1]][0]-(displaySize[0]/imgArraySize[0])/2,imgArray[imgArrayCursorPos[0]][imgArrayCursorPos[1]][1]-(displaySize[1]/imgArraySize[1]/2),cellSize[0],cellSize[1]),lineThickness)
        for target in objectArray:
            target.showMe()
            target.showOrigin()
        pg.display.update()  

# MAIN LOOP END


