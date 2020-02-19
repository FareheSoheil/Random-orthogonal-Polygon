from PIL import Image, ImageDraw
from Constants import STARTING_X,STARTING_Y,CELL_EDGE_SIZE_PIXEL,GRID_COLOR,CELL_DEFAULT_COLOR



def drawCell(pen,x,y,colorCode):
    color = CELL_DEFAULT_COLOR
    if colorCode == 4 :
        color = (26, 83, 255)
    pen.rectangle([(x,y),(x+CELL_EDGE_SIZE_PIXEL,y+CELL_EDGE_SIZE_PIXEL)], fill=color, outline=0)

def drawGrid(pen, gridArray,gridArrayDime):
        x=STARTING_X
        y=STARTING_Y
        for row in gridArray[1:gridArrayDime+1]:
            x=STARTING_X
            for col in row[1:gridArrayDime+1]:
                drawCell(pen,x,y,col)
                x=x+CELL_EDGE_SIZE_PIXEL
            y=y+CELL_EDGE_SIZE_PIXEL


#             im=Image.new("rgb",(200,10),"#ddd") #Frame = im
#             draw=Image.draw.draw(im) #draw = draw-object
# draw.text((10,10),"run away",fill="red")
# im.save("g.jpeg")


def draw(gridArray,gridArrayDime,i):
        GRID_HEIGHT_PIXEL = gridArrayDime * CELL_EDGE_SIZE_PIXEL + 3
        GRID_WIDTH_PIXEL = gridArrayDime * CELL_EDGE_SIZE_PIXEL + 3
        FRAME = Image.new("RGB", size=(GRID_HEIGHT_PIXEL, GRID_WIDTH_PIXEL), color=GRID_COLOR)
        DRAW_OBJECT = ImageDraw.Draw(FRAME)
        drawGrid(DRAW_OBJECT,gridArray,gridArrayDime)
        name = "g_"+str(i)+".jpeg"
        FRAME.save(name)
        del DRAW_OBJECT
        # FRAME.show()
