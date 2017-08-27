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
    I perhaps will writw the code one day...

    P.s: thanks to <(R)3

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
wDiamond_Block = block.DIAMOND_BLOCK.id #   = Block(57)

wFlower_Yellow = block.FLOWER_YELLOW.id #   = Block(37)
wFlower_Cyan = block.FLOWER_CYAN.id     #   = Block(38)
wMushroom_Red = block.MUSHROOM_RED.id   #   = Block(40)
wStone_Brick = block.STONE_BRICK.id     #   = Block(98)

# Possible colors for WOOL blocks
wWhite = 0
wOrange = 1
wMagenta = 2
wLightBlue = 3
wYellow = 4
wLime = 5
wPink = 6
wGrey = 7
wLightgrey = 8
wCyan = 9
wPurple = 10
wBlue = 11
wBrown = 12
wGreen = 13
wRed = 14
wBlack = 15

# For Brick Stones
wcrackedBrick = 2 # : Cracked stone brick

# for windows
wGlass = block.GLASS.id
wGlass_Pane = block.GLASS_PANE.id
# The door
wDoorWood = block.DOOR_WOOD.id 

bWater = block.WATER_STATIONARY.id

# POINTING East, West, North or South ?!
# torch can do.
PointingEAST = 1
PointingWEST = 2
PointingSOUTH = 3
PointingNORTHnorth = 4
Facingup = 5


#LADDERS, CHESTS, FURNACES, FENCE_GATE:
FacingNorth = 2
FacingSouth = 3
FacingWest = 4
FacingEast = 5


# My Var Might be here one day...
# myGround = [,]
# myWalls =


def ground(pos, mainColor= wPink, secondColor=wPurple):
    """
    this function will make the ground of the house .

    WOOL Default colors are as following:
    mainColor : (wPink)
    secondColor : (wPurple)

    Blocks Type:
    wool : (wool)This part will draw the ground.
    
    """
    mc.setBlocks(pos.x, pos.y-1,pos.z,pos.x+3, pos.y-1,pos.z, wool, secondColor)
    
    i = 1
    #mc.setBlock(pos.x-1, pos.y-1,pos.z+1,wool, wPink)

    while i <= 8:
        mc.setBlock(pos.x-i, pos.y-1,pos.z+i,wool, secondColor)

        mc.setBlocks(pos.x-i+1, pos.y-1, pos.z+i,
                     pos.x-i+1+2+(2*i), pos.y-1,pos.z+i,
                     wool, mainColor)

        mc.setBlock(pos.x-i+3+(2*i), pos.y-1,pos.z+i,
                    wool, secondColor)
        i += 1

    # build the larger area
    mc.setBlocks(pos.x-14, pos.y-1,pos.z+9,pos.x+17, pos.y-1,pos.z+37, wool, secondColor)
    mc.setBlocks(pos.x-13, pos.y-1,pos.z+10,pos.x+16, pos.y-1,pos.z+36, wool, mainColor)

    # remove purple line in front
    mc.setBlocks(pos.x-8, pos.y-1,pos.z+9,pos.x+11, pos.y-1,pos.z+9, wool, mainColor)

    ## End of ground fucntion ##



def makeTheHouse(pos, blockTypeMain = wool, blockTypeSecond = wool, mainColor=wMagenta , secondColor =wWhite):
    """
    thie function will make the main house building.

    WOOL Default colors are as following:
    mainColor : (wMagenta)
    secondColor : (wWhite)

    Blocks Type:
    wool : (wool)
    wGass_Pane : (Glass_ Pane can be changed by anything you want as well.
    
    """

    ### FRONT (& BACK )###
    for Front in range(0,22,21): #This is the trick for the back copy...
        
        mc.setBlocks(pos.x-4, pos.y,pos.z+6+Front,
                     pos.x+7, pos.y+9, pos.z+6+Front, blockTypeMain, mainColor)
        mc.setBlocks(pos.x-3, pos.y+1,pos.z+6+Front,
                     pos.x+6, pos.y+8, pos.z+6+Front, blockTypeSecond, secondColor)
        # FRONT - Remove blocks
        # Small trick to remove the 6 empty space by a loop
        #[[x,y],[x,y],[x,y],...]
        for i in [[-1,+1],[5,+1],[+2,0],[-1,+5],[2,+5],[5,+5]]:
            mc.setBlocks(pos.x+i[0], pos.y+i[1],pos.z+6+Front,
                     pos.x+i[0]-1, pos.y+i[1]+2, pos.z+6+Front, air)
        #let's put the Glasses (that's almost the same than remove actually...)
        for i in [[-1,+1],[5,+1],[-1,+5],[2,+5],[5,+5]]:
            mc.setBlocks(pos.x+i[0], pos.y+i[1],pos.z+6+Front,
                     pos.x+i[0]-1, pos.y+i[1]+2, pos.z+6+Front, wGlass_Pane)
        # The door at Entrance
        mc.setBlock(pos.x+1,   pos.y,   pos.z+6+Front, wDoorWood,4)
        mc.setBlock(pos.x+1,   pos.y+1, pos.z+6+Front, wDoorWood,8)
        mc.setBlock(pos.x+2,   pos.y,   pos.z+6+Front, wDoorWood,1)
        mc.setBlock(pos.x+2,   pos.y+1, pos.z+6+Front, wDoorWood,8)
        
        # ************
        
        # FRONT -  Small top
        mc.setBlocks(pos.x-3, pos.y+10,pos.z+6+Front,
                     pos.x+6, pos.y+14, pos.z+6+Front, blockTypeSecond, secondColor)
        mc.setBlocks(pos.x-1, pos.y+10,pos.z+6+Front,
                     pos.x+4, pos.y+13, pos.z+6+Front, blockTypeMain, mainColor)
        mc.setBlocks(pos.x, pos.y+10,pos.z+6+Front,
                     pos.x+3, pos.y+12, pos.z+6+Front, blockTypeSecond, secondColor)
        # FRONT-Small top Remove Blocks
        mc.setBlocks(pos.x+1, pos.y+11,pos.z+6+Front,
                     pos.x+2, pos.y+12, pos.z+6+Front, air)
        # small trick to remove as "stairs" - funny ? no ?
        for i in range(0,10,1):
            iy = i
            if i > 5:
                iy=9-i
            #print i, iy
            mc.setBlocks(pos.x-3+i, pos.y+11+iy,pos.z+6+Front,
                         pos.x-3+i, pos.y+15, pos.z+6+Front, air)
        # FRONT-Small Top put Glass
        mc.setBlocks(pos.x+1, pos.y+11,pos.z+6+Front,
                     pos.x+2, pos.y+12, pos.z+6+Front, wGlass_Pane)


        # FRONT-Right & Left side 
        for i in range(0,19,18):
            #print i
            mc.setBlocks(pos.x-4+i, pos.y,pos.z+7+Front,
                         pos.x-11+i, pos.y+8, pos.z+7+Front, blockTypeMain, mainColor)
            mc.setBlocks(pos.x-5+i, pos.y+1,pos.z+7+Front,
                         pos.x-10+i, pos.y+7, pos.z+7+Front, blockTypeSecond, secondColor)
            # blocks removal
            mc.setBlocks(pos.x-6+i, pos.y+1,pos.z+7+Front,
                         pos.x-9+i, pos.y+7, pos.z+7+Front, wGlass_Pane)
            # the line
            mc.setBlocks(pos.x-5+i, pos.y+4,pos.z+7+Front,
                         pos.x-11+i, pos.y+4, pos.z+7+Front, blockTypeMain, mainColor)
        
    #remove 2 extra columns
    mc.setBlocks(pos.x-4, pos.y, pos.z+7,
                 pos.x-4, pos.y+8, pos.z+7, air)
    mc.setBlocks(pos.x-4+11, pos.y, pos.z+7,
                 pos.x-4+11, pos.y+8, pos.z+7, air)


    ### MAIN WALLS RIGHT & LEFT SIDE ###
    for wall in range(0,26,25):
        mc.setBlocks(pos.x-11+wall, pos.y, pos.z+8,
                     pos.x-11+wall, pos.y+8, pos.z+28, blockTypeMain, mainColor)

        mc.setBlocks(pos.x-11+wall, pos.y+1, pos.z+8,
                     pos.x-11+wall, pos.y+7, pos.z+27, blockTypeSecond, secondColor)

        for i in range(0,15,7):
            mc.setBlocks(pos.x-11+wall, pos.y+1,pos.z+9+i,
                     pos.x-11+wall, pos.y+7, pos.z+12+i, wGlass_Pane)
    
        # the 3 lines
        mc.setBlocks(pos.x-11+wall, pos.y, pos.z+14,
                     pos.x-11+wall, pos.y+8, pos.z+14, blockTypeMain, mainColor)
        mc.setBlocks(pos.x-11+wall, pos.y, pos.z+21,
                     pos.x-11+wall, pos.y+8, pos.z+21, blockTypeMain, mainColor)
        mc.setBlocks(pos.x-11+wall, pos.y+4, pos.z+8,
                     pos.x-11+wall, pos.y+4, pos.z+28, blockTypeMain, mainColor)


    

    #same 
    #removeBlocks(pos.x-1, pos.y+2, pos.z+6, 2, 
    pass

def theRoof(pos, mainColor=wPurple, replaceGlass = wGlass):
    """
    thie function will make the roof of the house.

    WOOL Default colors are as following:
    mainColor : (wPurple)
    secondColor : None

    Blocks Type:
    wool : (wool)
    wGass_Pane : (Glass_ Pane can be changed by anything you want as well.
    
    """
    
    # try again the same trick to add the roof
    # Middle part
    for i in range(0,12,1):
        iy = i
        if i >= 6:
           iy=11-i
        #print i, iy
        mc.setBlocks(pos.x-4+i, pos.y+10+iy, pos.z+4,
                     pos.x-4+i, pos.y+10+iy, pos.z+29, wool, mainColor)

    # RIGHT SIDE of the house
    for ii in range(0,3,1):
        mc.setBlocks(pos.x-5+ii, pos.y+9+ii, pos.z+5+ii,
                     pos.x-13+ii, pos.y+9+ii, pos.z+29-ii, wool, mainColor)
        #Remove the blocks

        material = air
        if ii >=2 :
            material = wGlass
        mc.setBlocks(pos.x-5+ii, pos.y+9+ii, pos.z+8,
                     pos.x-11+ii, pos.y+9+ii, pos.z+26-ii, material)
        
    # and LEFT side of the house
    xAdjust = 21
    for ii in range(0,3,1):
        mc.setBlocks(pos.x-5-ii+xAdjust, pos.y+9+ii, pos.z+5+ii,
                     pos.x-13-ii+xAdjust, pos.y+9+ii, pos.z+29-ii, wool, mainColor)
        #Remove the blocks

        material = air
        if ii >=2 :
            material = replaceGlass
        mc.setBlocks(pos.x-7-ii+xAdjust, pos.y+9+ii, pos.z+8,
                     pos.x-13-ii+xAdjust, pos.y+9+ii, pos.z+26-ii, material)
    
  

def makeTheGarden(pos):
    pass


def theDamnedDoor(pos, whereX=0, whereY=0, whereZ=0, theDoor = wDoorWood):
    """
    Blabla...
    tell me more about the door...
    """
    mc.setBlock(pos.x+1+whereX, pos.y+whereY,   pos.z+whereZ, theDoor,4)
    mc.setBlock(pos.x+1+whereX, pos.y+1+whereY, pos.z+whereZ, theDoor,8)
    mc.setBlock(pos.x+2+whereX, pos.y+whereY,   pos.z+whereZ, theDoor,1)
    mc.setBlock(pos.x+2+whereX, pos.y+1+whereY, pos.z+whereZ, theDoor,8)
    pass
    

def makeTheDeco(pos, flowers= wFlower_Cyan):
    """
    Decoration
    Let me think about that !
    
    """
    mc.setBlock(pos.x, pos.y,pos.z-5, flowers)
    mc.setBlock(pos.x+3, pos.y,pos.z-5, flowers)
    ## makeTheDeco Function END ##


def bulldozer(pos, sizeX=20 , sizeY=20, sizeZ=40, putGrass="yes"):
    """
    Thie function will make flat the ground to clean around.
    
    for a large bulldozer :
    bulldozer(pos, sizeX=40 , sizeY=20, sizeZ=40, putGrass="yes")
    """
    # Make the place empty
    #mc.setBlocks(pos.x-30, pos.y-1, pos.z-10,
    #             pos.x+40, pos.y+20, pos.z+40, air)
    
    mc.setBlocks(pos.x-sizeX, pos.y-1, pos.z-10,
                 pos.x+sizeX, pos.y+sizeY, pos.z+sizeZ, air)
    
    if putGrass == "yes":
        # put grass on the ground
        mc.setBlocks(pos.x-30, pos.y-1, pos.z-10,
                     pos.x+sizeX, pos.y-1, pos.z+sizeZ, grass)
    elif putGrass == "no":
        pass
        

def removeBlocks(posx1, posy1, posz1, xnum, ynum, znum, air=air):
    mc.setBlocks(pos.x-1, pos.y+2,pos.z+6,
                 pos.x-2, pos.y+4, pos.z+6, air)
    

# !!! remember to DO the following command MANUALLY !!! (1)
# pos = mc.player.getPos()    

def myBarbieHome(pos):
    """
    All the command to build your Barbie's Home
    """
    bulldozer(pos)
    ground(pos)
    print mc.postToChat("Ground done !")

    pos.z += 5
    makeTheHouse(pos)
    print mc.postToChat("House done !")
    theRoof(pos)
    print mc.postToChat("Roof done !")

    makeTheDeco(pos, flowers = wFlower_Cyan)
    print mc.postToChat("ALL Work done !")


def addamsFamily(pos):
    """
    To paint Pink "Barbie's" home as the AddamsFamily
    it is just an example about color you can change.
    
    """
    bulldozer(pos)
    print mc.postToChat("We made some free place. done !")
    
    ground(pos, mainColor= wLightgrey, secondColor=wBlack)
    mc.setBlock(pos.x, pos.y, pos.z, 40)
    mc.setBlock(pos.x-1, pos.y, pos.z, 40)
    print mc.postToChat("Ground done !")

    pos.z += 5
    makeTheHouse(pos, blockTypeMain = wool, blockTypeSecond = wStone_Brick, mainColor=wBlack , secondColor =wcrackedBrick)
    print mc.postToChat("House done !")
    
    theRoof(pos, mainColor=wBlack)
    print mc.postToChat("The roof is done !")

    makeTheDeco(pos, flowers= wMushroom_Red)
    print mc.postToChat("ALL Work done !")
    
