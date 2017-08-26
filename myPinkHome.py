"""

    MyPinkHome super programm !

Requirement
    Plateform : Raspberry Pi
    Game : Minecraft Pi
    OS : Raspbian
    Python : 2.7.9

    INPUT
        Your list should con

Date : 2017/8/26 


How to
1) first get your current position . even if you move,
    we're going to use that to localize where to construct
    >>> pos = mc.player.getPos()
    
2) maybe you need some clean-up ? Use the bulldozer first !
    >>> bulldozer(pos)

3) make the ground of the house first
    >>> ground(pos)

4) The rest of the house, the roof, the internal decoration and the garden.
    I am writting the code now so be patient :p

"""
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

mc.postToChat("Hello everyone !")
mc.postToChat("Let's try to build our Pink Home")
mc.postToChat("in a single command line ! Can we ?")

# !!! remember to DO the following command MANUALLY !!! (1)
# pos = mc.player.getPos()


# Define the block we are going to use.
air = 0
grass = block.GRASS.id
wool = block.WOOL.id

#color for wool blocks
wPink = 6
wPurple = 10

# for windows
wGlass = block.GLASS.id
wGlass_Pane = block.GLASS_PANE.id
# 

bWater = block.WATER_STATIONARY.id

# POINTING East, West, North or South ?!
# torch can do.

# My Var Might be here one day...
# myGround = [,]
# myWalls =


def ground(pos):
    """

    """
    mc.setBlocks(pos.x, pos.y-1,pos.z,pos.x+3, pos.y-1,pos.z, wool, wPurple)
    
    i = 1
    #mc.setBlock(pos.x-1, pos.y-1,pos.z+1,wool, wPink)

    while i <= 8:
        mc.setBlock(pos.x-i, pos.y-1,pos.z+i,wool, wPurple)

        mc.setBlocks(pos.x-i+1, pos.y-1, pos.z+i,
                     pos.x-i+1+2+(2*i), pos.y-1,pos.z+i,
                     wool, wPink)

        mc.setBlock(pos.x-i+3+(2*i), pos.y-1,pos.z+i,
                    wool, wPurple)
        i += 1

    # build the larger area
    mc.setBlocks(pos.x-14, pos.y-1,pos.z+9,pos.x+17, pos.y-1,pos.z+27, wool, wPurple)
    mc.setBlocks(pos.x-13, pos.y-1,pos.z+10,pos.x+16, pos.y-1,pos.z+26, wool, wPink)

    # remove purple line in front
    mc.setBlocks(pos.x-8, pos.y-1,pos.z+9,pos.x+11, pos.y-1,pos.z+9, wool, wPink)

"""
    ii = 1    
    while ii <= 10:

"""

def makeTheHouse(pos):
    pass

def theRoof(pos):
    pass

def makeTheGarden(pos):
    pass

def makeTheDecoration(pos):
    pass


def bulldozer(pos):
    # Make it empty
    mc.setBlocks(pos.x-30, pos.y-1, pos.z-10,
                 pos.x+40, pos.y+20, pos.z+40, air)

    # put grass on the ground
    mc.setBlocks(pos.x-30, pos.y-1, pos.z-10,
                 pos.x+40, pos.y-1, pos.z+40, grass)
    



def MCPI_Builder(myList):
    """
    This command build what you will ask
    INPUT :
    ** myList**
    should contain subList with following argument
        subList:
        material ID
        x,y,z(start)
        x,y,z(weight/High)


    ##### Code from here?
    pass

    # player position pos.x, pos.y & pos.z
    pos = mc.player.getPos()

    # building Start Point
    bSP = 

    for tinyPart in myList:
        if len(tinyPart) == 7:
            xa = tinyPart[0]
            ya = tinyPart[1]
            za = tinyPart[2]
            xb = tinyPart[3]
            yb = tinyPart[4]
            zb = tinyPart[5]
            material = tinyPart[6]
            
            mc.setBlocks(xa,ya,za,xb,yb,zb,material)
            
    return mc.postToChat("Work done !")
    """
    pass


def MCPI_Build_The_Ground(myListForTheGround):
    """
    list should be the first line
    then for 7 more lines (the area at entrance )
    then the next one will be rectangular area (easier to do)

    myListForTheGround
    argument = x,y,z to start
    pink stone id
    purple stone id
    let's put flower later

    example
    myListForTheGround = [x,y,z,
    """

    pass    
    
    
