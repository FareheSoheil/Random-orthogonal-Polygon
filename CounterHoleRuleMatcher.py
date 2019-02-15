import copy

# O(GRID_DIME^2)
def gridCounterHoleRuleMatcher(gridArray,originalTmpArray,gridArrayDime):
    rowIndex=colIndex=1
    tmpArray = copy.deepcopy(originalTmpArray)
    for row in originalTmpArray[1:gridArrayDime+1]:
        colIndex=1
        for col in row[1:gridArrayDime+1]:
            # only cells in condition 2 can be matched with counter hole rules
            if(col == 2):
                tmpArray[rowIndex][colIndex] = cellRuleMatcher(rowIndex,colIndex,gridArray,originalTmpArray)
            colIndex=colIndex+1
        rowIndex = rowIndex+1
    return tmpArray

# O(1)
def cellRuleMatcher(i,j,gridArray,originalTmpArray):
    res=3
        # both N and S are in polygon
    if(((gridArray[i-1][j] == 4 and gridArray[i+1][j] == 4 ) or
        # one is in polygon and the other one in state 2
       (originalTmpArray[i-1][j] == 2 and gridArray[i+1][j] == 4 ) or
       (gridArray[i-1][j] == 4 and originalTmpArray[i+1][j] == 2 )) and
       # none of E and W are no in polygon
       (gridArray[i][j-1] == 0 and gridArray[i][j+1] == 0 )
      ):
        res = 0
        # both E and W are in polygon
    if(((gridArray[i][j-1] == 4 and gridArray[i][j+1] == 4 ) or
        # one is in polygon and the other one in state 2
       (originalTmpArray[i][j-1] == 2 and gridArray[i][j+1] == 4 ) or
       (gridArray[i][j-1] == 4 and originalTmpArray[i][j+1] == 2 )) and
       # none of N and S are no in polygon
       (gridArray[i-1][j] == 0 and gridArray[i+1][j] == 0 )
      ):
        res = 0

    return res
