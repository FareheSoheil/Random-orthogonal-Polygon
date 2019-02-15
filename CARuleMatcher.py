# O(GRID_DIME^2)
def gridCARuleMatcher(gridArray,tmpArray,gridArrayDime):
    rowIndex=colIndex=1
    for row in gridArray[1:gridArrayDime+1]:
        colIndex=1
        for col in row[1:gridArrayDime+1]:
            # only cells in condition 0 can be matched with ca rules
            if(col == 0):
                tmpArray[rowIndex][colIndex] = cellRuleMatcher(rowIndex,colIndex,gridArray)
            colIndex=colIndex+1
        rowIndex = rowIndex+1

# checked twice
def oneNeighbourRuleMatcher(i,j,grid):
    res = 0
    if(grid[i-1][j] == 4 or grid[i+1][j] == 4 or grid[i][j-1] == 4 or grid[i][j+1] == 4):
        res = 1
    return res
# checked twice
def twoNeighboursRuleMatcher(i,j,grid):
        res = 0
        if((grid[i][j-1] == 4 and grid[i+1][j-1] == 4) or
           (grid[i+1][j] == 4 and grid[i+1][j-1] == 4) or
           (grid[i+1][j] == 4 and grid[i+1][j+1] == 4) or
           (grid[i][j+1] == 4 and grid[i+1][j+1] == 4) or
           (grid[i][j+1] == 4 and grid[i-1][j+1] == 4) or
           (grid[i-1][j] == 4 and grid[i-1][j-1] == 4) or
           (grid[i-1][j] == 4 and grid[i-1][j+1] == 4) or
           (grid[i-1][j-1] == 4 and grid[i][j-1] == 4)
           ):
            res = 1
        return res
# checked twice
def threeNeighboursRuleMatcher(i,j,grid):
        res = 0
        if((grid[i][j-1] == 4 and grid[i-1][j-1] == 4 and grid[i-1][j] == 4) or
           (grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4) or
           (grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and grid[i][j+1] == 4) or
           (grid[i-1][j+1] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4) or
           (grid[i-1][j-1] == 4 and grid[i][j-1] == 4 and grid[i+1][j-1] == 4) or
           (grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4) or
           (grid[i+1][j-1] == 4 and grid[i+1][j] == 4 and grid[i+1][j+1] == 4) or
           (grid[i+1][j] == 4 and grid[i+1][j+1] == 4 and grid[i][j+1] == 4)
           ):
            res = 1
        return res
# checked twice
def fourNeighboursRuleMatcher(i,j,grid):
        res = 0
        if((grid[i-1][j-1] == 4 and grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4) or
           (grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4 and grid[i+1][j+1] == 4) or
           (grid[i][j+1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4 and grid[i+1][j+1] == 4) or
           (grid[i][j-1] == 4 and grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4) or
           (grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4) or
           (grid[i][j+1] == 4 and grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4) or
           (grid[i+1][j] == 4 and grid[i-1][j+1] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4)
           ):
            res = 1
        return res
# checked twice
def fiveNeighboursRuleMatcher(i,j,grid):
        res = 0
        if((grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and grid[i][j-1] == 4 and grid[i+1][j-1] == 4) or
           (grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4) or
           (grid[i-1][j-1] == 4 and grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4 and grid[i+1][j+1] == 4) or
           (grid[i][j-1] == 4 and grid[i][j+1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4 and grid[i+1][j+1] == 4) or
           (grid[i-1][j+1] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4 and grid[i+1][j] == 4 and grid[i+1][j-1] == 4) or
           (grid[i][j-1] == 4 and grid[i][j+1] == 4 and grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4) or
           (grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4) or
           (grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4 and grid[i+1][j] == 4)
           ):
            res = 1
        return res
# checked twice
def sixNeighboursRuleMatcher(i,j,grid):
    res = 0
    if((grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and
        grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i][j+1] == 4) or

        (grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and
        grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4) or

        (grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i][j-1] == 4 and
        grid[i+1][j-1] == 4 and grid[i+1][j] == 4 and grid[i+1][j+1] == 4) or

        (grid[i-1][j-1] == 4 and grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and
        grid[i+1][j] == 4 and grid[i+1][j+1] == 4 and grid[i][j+1] == 4) or

        (grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4 and
        grid[i+1][j+1] == 4 and grid[i][j+1] == 4 and grid[i-1][j+1] == 4) or

        (grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and grid[i][j+1] == 4 and
        grid[i+1][j+1] == 4 and grid[i+1][j] == 4 and grid[i+1][j-1] == 4) or


        (grid[i][j-1] == 4 and grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and
        grid[i-1][j+1] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4) or

        (grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and
        grid[i][j+1] == 4 and grid[i+1][j+1] == 4 and grid[i+1][j] == 4)

       ):
        res = 1
    return res

# checked twice
def sevenNeighboursRuleMatcher(i,j,grid):
    res = 0
    if((grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and
        grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4 ) or

        (grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and
        grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and grid[i+1][j] == 4 and grid[i+1][j+1] == 4) or

        (grid[i-1][j-1] == 4 and grid[i][j-1] == 4 and grid[i+1][j-1] == 4 and
        grid[i+1][j] == 4 and grid[i-1][j+1] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4) or

        (grid[i-1][j-1] == 4 and grid[i-1][j] == 4 and grid[i-1][j+1] == 4 and
        grid[i+1][j-1] == 4 and grid[i+1][j] == 4 and grid[i][j+1] == 4 and grid[i+1][j+1] == 4)
       ):
        res = 1
    return res

# O(1)
def cellRuleMatcher(rowIndex,colIndex,neighbourhood):
    numOfActiveNeighbours = 0
    res=0
    # O(1)
    for i in range(rowIndex-1,rowIndex+2):
        for j in range(colIndex-1,colIndex+2):
            if(neighbourhood[i][j]== 4):
                numOfActiveNeighbours=numOfActiveNeighbours+1
    # O(1)
    if(numOfActiveNeighbours==1):
        res = oneNeighbourRuleMatcher(rowIndex,colIndex,neighbourhood)
    elif(numOfActiveNeighbours==2):
        res = twoNeighboursRuleMatcher(rowIndex,colIndex,neighbourhood)
    elif(numOfActiveNeighbours==3):
        res = threeNeighboursRuleMatcher(rowIndex,colIndex,neighbourhood)
    elif(numOfActiveNeighbours==4):
        res = fourNeighboursRuleMatcher(rowIndex,colIndex,neighbourhood)
    elif(numOfActiveNeighbours==5):
        res = fiveNeighboursRuleMatcher(rowIndex,colIndex,neighbourhood)
    elif(numOfActiveNeighbours==6):
        res = sixNeighboursRuleMatcher(rowIndex,colIndex,neighbourhood)
    elif(numOfActiveNeighbours==7):
        res = sevenNeighboursRuleMatcher(rowIndex,colIndex,neighbourhood)
    return res
