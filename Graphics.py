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
def draw(gridArray,gridArrayDime):
        GRID_HEIGHT_PIXEL = gridArrayDime * CELL_EDGE_SIZE_PIXEL + 3
        GRID_WIDTH_PIXEL = gridArrayDime * CELL_EDGE_SIZE_PIXEL + 3
        FRAME = Image.new(mode='RGBA', size=(GRID_HEIGHT_PIXEL, GRID_WIDTH_PIXEL), color=GRID_COLOR)
        DRAW_OBJECT = ImageDraw.Draw(FRAME)
        drawGrid(DRAW_OBJECT,gridArray,gridArrayDime)
        del DRAW_OBJECT
        FRAME.show()
