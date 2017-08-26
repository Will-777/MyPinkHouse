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
wGold = block.GOLD_ORE.id

#color for wool blocks
wWhite = 0
wPink = 6
wMagenta = 2
wPurple = 10

# for windows
wGlass = block.GLASS.id
wGlass_Pane = block.GLASS_PANE.id
# The door
wDoor = block.DOOR_WOOD.id

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
    mc.setBlocks(pos.x-14, pos.y-1,pos.z+9,pos.x+17, pos.y-1,pos.z+37, wool, wPurple)
    mc.setBlocks(pos.x-13, pos.y-1,pos.z+10,pos.x+16, pos.y-1,pos.z+36, wool, wPink)

    # remove purple line in front
    mc.setBlocks(pos.x-8, pos.y-1,pos.z+9,pos.x+11, pos.y-1,pos.z+9, wool, wPink)

"""
    ii = 1    
    while ii <= 10:

"""

def makeTheHouse(pos):


    ### FRONT (& BACK )###
    for Front in range(0,24,23): #This is the trick for the back copy...
        
        mc.setBlocks(pos.x-4+Front, pos.y,pos.z+6,
                     pos.x+7, pos.y+9, pos.z+6, wool, wMagenta)
        mc.setBlocks(pos.x-3, pos.y+1,pos.z+6,
                     pos.x+6, pos.y+8, pos.z+6, wool, wWhite)
        # FRONT - Remove blocks
        # Small trick to remove the 6 empty space by a loop
        #[[x,y],[x,y],[x,y],...]
        for i in [[-1,+1],[5,+1],[+2,0],[-1,+5],[2,+5],[5,+5]]:
            mc.setBlocks(pos.x+i[0], pos.y+i[1],pos.z+6,
                     pos.x+i[0]-1, pos.y+i[1]+2, pos.z+6, air)
        #let's put the Glasses (that's almost the same than remove actually...)
        for i in [[-1,+1],[5,+1],[-1,+5],[2,+5],[5,+5]]:
            mc.setBlocks(pos.x+i[0], pos.y+i[1],pos.z+6,
                     pos.x+i[0]-1, pos.y+i[1]+2, pos.z+6, wGlass_Pane)
        # The door at Entrance
        mc.setBlocks(pos.x+2, pos.y+0,pos.z+6,
                     pos.x+1, pos.y+0, pos.z+6, wDoor)
        
        # FRONT -  Small top
        mc.setBlocks(pos.x-3, pos.y+10,pos.z+6,
                     pos.x+6, pos.y+14, pos.z+6, wool, wWhite)
        mc.setBlocks(pos.x-1, pos.y+10,pos.z+6,
                     pos.x+4, pos.y+13, pos.z+6, wool, wMagenta)
        mc.setBlocks(pos.x, pos.y+10,pos.z+6,
                     pos.x+3, pos.y+12, pos.z+6, wool, wWhite)
        # FRONT-Small top Remove Blocks
        mc.setBlocks(pos.x+1, pos.y+11,pos.z+6,
                     pos.x+2, pos.y+12, pos.z+6, air)
        # small trick to remove as "stairs" - funny ? no ?
        for i in range(0,10,1):
            iy = i
            if i > 5:
                iy=9-i
            #print i, iy
            mc.setBlocks(pos.x-3+i, pos.y+11+iy,pos.z+6,
                         pos.x-3+i, pos.y+15, pos.z+6, air)
        # FRONT-Small Top put Glass
        mc.setBlocks(pos.x+1, pos.y+11,pos.z+6,
                     pos.x+2, pos.y+12, pos.z+6, wGlass_Pane)


        # FRONT-Right & Left side 
        for i in range(0,19,18):
            #print i
            mc.setBlocks(pos.x-4+i, pos.y,pos.z+7,
                         pos.x-11+i, pos.y+8, pos.z+7, wool, wMagenta)
            mc.setBlocks(pos.x-5+i, pos.y+1,pos.z+7,
                         pos.x-10+i, pos.y+7, pos.z+7, wool, wWhite)
            # blocks removal
            mc.setBlocks(pos.x-6+i, pos.y+1,pos.z+7,
                         pos.x-9+i, pos.y+7, pos.z+7, wGlass_Pane)
            # the line
            mc.setBlocks(pos.x-5+i, pos.y+4,pos.z+7,
                         pos.x-11+i, pos.y+4, pos.z+7, wool, wMagenta)
        
    #remove 2 extra columns
    mc.setBlocks(pos.x-4, pos.y, pos.z+7,
                 pos.x-4, pos.y+8, pos.z+7, air)
    mc.setBlocks(pos.x-4+11, pos.y, pos.z+7,
                 pos.x-4+11, pos.y+8, pos.z+7, air)


    ### MAIN WALLS RIGHT & LEFT SIDE ###
    for wall in range(0,26,25):
        mc.setBlocks(pos.x-11+wall, pos.y, pos.z+8,
                     pos.x-11+wall, pos.y+8, pos.z+28, wool, wMagenta)

        mc.setBlocks(pos.x-11+wall, pos.y+1, pos.z+8,
                     pos.x-11+wall, pos.y+7, pos.z+27, wool, wWhite)

        for i in range(0,15,7):
            mc.setBlocks(pos.x-11+wall, pos.y+1,pos.z+9+i,
                     pos.x-11+wall, pos.y+7, pos.z+12+i, wGlass_Pane)
    
        # the 3 lines
        mc.setBlocks(pos.x-11+wall, pos.y, pos.z+14,
                     pos.x-11+wall, pos.y+8, pos.z+14, wool, wMagenta)
        mc.setBlocks(pos.x-11+wall, pos.y, pos.z+21,
                     pos.x-11+wall, pos.y+8, pos.z+21, wool, wMagenta)
        mc.setBlocks(pos.x-11+wall, pos.y+4, pos.z+8,
                     pos.x-11+wall, pos.y+4, pos.z+28, wool, wMagenta)


    

    #same 
    #removeBlocks(pos.x-1, pos.y+2, pos.z+6, 2, 
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
    

def removeBlocks(posx1, posy1, posz1, xnum, ynum, znum, air=air):
    mc.setBlocks(pos.x-1, pos.y+2,pos.z+6,
                 pos.x-2, pos.y+4, pos.z+6, air)
    


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
    

def yesBuild(pos):
    ground(pos)
    pos.z += 5
    makeTheHouse(pos)
    return mc.postToChat("Work done !")
