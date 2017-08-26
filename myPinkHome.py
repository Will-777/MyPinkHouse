"""



 MyPinkHome


INPUT
Your list should con

 


"""


from mcpi.minecraft import Minecraft
from mcpi import block




bPink = 
bPurple = 
bWindow = block
bStone = block.STONE.id
bWater = block.WATER_STATIONARY.id

# .data
# wool = 35 
# mc.setBlock(x, y, z, wool, 1)
# 2: magenta, 3: Light Blue 4:Yellow
# 
# 6: Pink
# 10: Purple
# 




# POINTING East, West, North or South ?!
# torch can do.


mc = Minecraft.create()

mc.postToChat("Hello everyone !")
mc.postToChat("Let's try to build our Pink Home")
mc.postToChat("in a single command line ! Can we ?")


myGround = [,]

myWalls =



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


    """

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

    
    
    
