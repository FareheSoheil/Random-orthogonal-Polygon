from Graphics import draw
from CARuleMatcher import gridCARuleMatcher
from CounterCrossMoveRuleMatcher import gridCounterCrossRuleMatcher
from CounterHoleRuleMatcher import gridCounterHoleRuleMatcher
from ProbabilisticCellAdder import probabilisticCellAdder
import random, copy

def initiatePolygon(gridArrayDime):
        randomCellX= random.randint(1,gridArrayDime)
        randomCellY= random.randint(1,gridArrayDime)
        GRID[randomCellX][randomCellY]=4
        tmp_grid[randomCellX][randomCellY]=4

if __name__ == '__main__':
    # initiate the first random cell (Starting Cell)
    gridArrayDime = 60
    GRID = [[0]*(gridArrayDime+2) for i in range(gridArrayDime+2)]
    tmp_grid = [[0]*(gridArrayDime+2) for i in range(gridArrayDime+2)]
    # print(GRID_ARRAY_DIME)
    # for value in range(1,152):
    caSteps = 20
    # random.randint(3,35)
    # int(input("Enter a number of CA steps: "))
    print("caSteps : ",caSteps)
    initiatePolygon(gridArrayDime)
    # for loop for applying :
    for value in range(caSteps):
        # 1.CA rules
        gridCARuleMatcher(GRID,tmp_grid,gridArrayDime)
        # 2.Counter Cross Move rules
        counterCrossGrid = gridCounterCrossRuleMatcher(GRID,tmp_grid,gridArrayDime)
        # 3.Counter Hole Move rules
        counterHoleGrid = gridCounterHoleRuleMatcher(GRID,counterCrossGrid,gridArrayDime)
        # 4.Randomly add cells in state 3 to polygon
        finalGrid = probabilisticCellAdder(counterHoleGrid,gridArrayDime)
        tmp_grid=copy.deepcopy(finalGrid)
        GRID=copy.deepcopy(finalGrid)
        draw(GRID,gridArrayDime)
    # GRID = [[0]*(gridArrayDime+2) for i in range(gridArrayDime+2)]
    # tmp_grid = [[0]*(gridArrayDime+2) for i in range(gridArrayDime+2)]
