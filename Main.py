from Graphics import draw
from CARuleMatcher import gridCARuleMatcher
from CounterCrossMoveRuleMatcher import gridCounterCrossRuleMatcher
from CounterHoleRuleMatcher import gridCounterHoleRuleMatcher
from ProbabilisticCellAdder import probabilisticCellAdder
import random, copy
import time

def initiatePolygon(gridArrayDime):
        randomCellX= random.randint(1,gridArrayDime)
        randomCellY= random.randint(1,gridArrayDime)
        GRID[randomCellX][randomCellY]=4
        tmp_grid[randomCellX][randomCellY]=4

if __name__ == '__main__':
    # initiate the first random cell (Starting Cell)
	gridArrayDime = int(input("Enter Grid's Dimention: "))
	reps =  int(input("Enter rep times: "))
	zero_grid = [[0]*(gridArrayDime+2) for i in range(gridArrayDime+2)]
	# GRID = copy.deepcopy(zero_grid) 
	# tmp_grid = copy.deepcopy(zero_grid)
	# print(GRID_ARRAY_DIME)
	caSteps = int(input("Enter Number Of CA Steps: "))
	print("caSteps : ",caSteps)
	
	for i in range(reps):
		# for loop for applying :
		GRID = copy.deepcopy(zero_grid) 
		tmp_grid = copy.deepcopy(zero_grid)
		initiatePolygon(gridArrayDime)
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
		draw(GRID,gridArrayDime,i)
        # time.sleep(.5)

