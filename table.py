# fstring playground
from random import randint as rnd

tableSize = 100
tablePartition = '|'+tableSize*'_'+'|'
tableStart = '|'+tableSize*'*'+'|'
randNames = ('Ethan',
'Maya',
'Oliver',
'Ava',
'Liam',
'Isabella',
'Noah',
'Sophia',
'William',
'Mia',
'James',
'Charlotte',
'Benjamin',
'Amelia',
'Lucas',
'Harper',
'Elijah',
'Evelyn',
'Alexander',
'Abigail',
'Michael',
'Emily',
'Daniel',
'Elizabeth',
'Henry',
'Victoria',
'Samuel',
'Madison',
'David',
'Grace',
'Christopher',
'Lily',
'Matthew',
'Zoey',
'Andrew',
'Chloe',
'Joshua',
'Sofia',
'Gabriel',
'Riley',
'Aiden',
'Scarlett',
'Jack',
'Natalie',
'Logan',
'Hannah',
'Jackson',
'Avery',
'Ryan',
'Addison',
)
randSurnames = ('Reynolds','Patel','Fernandez','Gallagher','Chen','Singh','Rodriguez','Kim','Nguyen','Sullivan','Gupta','Martinez','Khan','Li','Lim','Wong',
'Taylor',
'Kumar',
'Ali',
'Smith',
'Johnson',
'Brown',
'Rivera',
'Park',
'Campbell',
'Shah',
'Lee',
'Gonzales',
'Wu',
'Mitchell',
'Chen',
'Baker',
'Kumar',
'Patel',
'Carter',
'Nguyen',
'Rodriguez',
'Garcia',
'Lopez',
'Smith',
'Martin',
'Ramirez',
'Thompson',
'Clark',
'Khan',
'Davis',
'Wilson',
'Hall',
'Brown',
'Torres')

class rowFactory():
    colType = 0  # default
    def loadData(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def randData(self):
        self.name = f'{randNames[rnd(0,len(randNames))]} {randNames[rnd(0,len(randSurnames))]}'
        self.age = rnd(4,20)+rnd(4,20)+2
        self.height = (rnd(2,14)+rnd(2,14)-2)/10
        self.weight = rnd(10,60)+rnd(10,60)+5

        
rowLOOKUP = [tableStart,rowFactory(),tablePartition]
rowLOOKUP[1].name = 'Name'
rowLOOKUP[1].age = 'Age'
rowLOOKUP[1].height = 'Height'
rowLOOKUP[1].weight = 'Weight'

# CREATE LOAD
for i in range(3):
    rowLOOKUP.append(rowFactory())
    rowLOOKUP[-1].randData()
rowLOOKUP.append(tableStart)

# RENDER LOAD
for here in rowLOOKUP:

    if type(here) == type('a'):
        print(here)
    elif here.colType == 0:
        print(f"| {here.name:<28} | {here.age:^5} | {here.height:<8} | {here.weight:<8} |")