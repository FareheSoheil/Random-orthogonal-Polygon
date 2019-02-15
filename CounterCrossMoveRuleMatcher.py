import copy

# O(GRID_DIME^2)
def gridCounterCrossRuleMatcher(gridArray,originalTmpArray,gridArrayDime):
    rowIndex=colIndex=1
    tmpArray = copy.deepcopy(originalTmpArray)
    for row in originalTmpArray[1:gridArrayDime+1]:
        colIndex=1
        for col in row[1:gridArrayDime+1]:
            # only cells in condition 1 can be matched with counter cross rules
            if(col == 1):
                tmpArray[rowIndex][colIndex] = cellRuleMatcher(rowIndex,colIndex,gridArray,originalTmpArray)
            colIndex=colIndex+1
        rowIndex = rowIndex+1
    return tmpArray

def cellRuleMatcher(i,j,gridArray,tmpArray):
    res=2
    if(tmpArray[i-1][j-1] == 1):
        if(gridArray[i-1][j] != 4 and gridArray[i][j-1] != 4): res = 0
    if(tmpArray[i-1][j+1] == 1):
        if(gridArray[i-1][j] != 4 and gridArray[i][j+1] != 4): res = 0
    if(tmpArray[i+1][j-1] == 1):
        if(gridArray[i][j-1] != 4 and gridArray[i+1][j] != 4): res = 0
    if(tmpArray[i+1][j+1] == 1):
        if(gridArray[i][j+1] != 4 and gridArray[i+1][j] != 4): res = 0
    return res
