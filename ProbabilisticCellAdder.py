import random

# O(GRID_DIME^2)
def probabilisticCellAdder(tmpArray,gridArrayDime):
    rowIndex=colIndex=1
    # tmpArray = copy.deepcopy(originalTmpArray)
    for row in tmpArray[1:gridArrayDime+1]:
        colIndex=1
        for col in row[1:gridArrayDime+1]:
            # only cells in condition 3 can be added to polygon
            if(col == 3):
                # produce a random number
                probability = random.randint(0,1)
                if(probability == 0):
                    tmpArray[rowIndex][colIndex] = 4
                else:
                    tmpArray[rowIndex][colIndex] = 0
            colIndex=colIndex+1
        rowIndex = rowIndex+1
    return tmpArray
