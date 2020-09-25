# Tiffany McBrayer

# Reduced Echelon modified 
def reducedEchelon(A):
##    howManyRows = eval(input("How many rows do you want your matrix to be?"))
##    total = 1
##    A = []
##    for _ in range (howManyRows):
##        row = eval(input("Fill in the entries for Row {}:".format(total)))
##        A.append(row)
##        total = total + 1
##    print("A = ")
##    printGrid(A)

    howManyRows = len(A)
    
    # left to right
    rowsCount = 0
    columnCount = 0
    while rowsCount != howManyRows:
        newA = takeOut(A, rowsCount, columnCount)
        numList = []
        zeroList = []
        for row in newA:
            if row[0] == 0:
                zeroList.append(row)
            else:
                numList.append(row)
        if len(numList) == 0:
            rowsCount = howManyRows
        elif len(newA[0]) == 1:
            rowsCount = howManyRows
        else:
            AwithPivot = createPivot(newA)
            A = putBack(A, AwithPivot, rowsCount, columnCount)
            rowsCount = rowsCount + 1
            columnCount = columnCount + 1
##    print("Clear from left to right")
##    print("A = ")
##    printGrid(A)

    # right to left
##    print("Clear from right to left")
    clearLeft_Right(A)
    putZeros(A)
##    print("A = ")
    printGrid(A)
#------------------------------------------------------------------------------
# How to swap a matrix
def swap(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]
    return matrix

# How to scale a matrix
def scale(matrix, i, r):
    newRow = []
    rowi = matrix[i]
    for number in rowi:
        number = number * r
        newRow.append(number)
    matrix[i] = newRow
    return matrix

# How to add one matrix to another
def AddMult(matrix, i, j, r):
    matrixNewJ = scale(matrix, j, r)
    rowj = matrixNewJ[j]
    total = 0
    newRow = []
    for row in matrixNewJ:
        if row == matrixNewJ[i]:
            for number in row:
                number = number + rowj[total]
                newRow.append(number)
                total = total + 1
        else:
            pass
    matrixNewJ[i] = newRow
    if r == 0:
        matrixNewJ = scale(matrix, j, r)
    else:
        matrixNewJ = scale(matrix, j, 1/r)
    matrix = matrixNewJ
    return matrix
#-------------------------------------------------------------------------------
# Helper functions to do the first half
def createPivot(matrix):
    # put all zeros to the bottom 
    numList = []
    zeroList = []
    for row in matrix:
        if row[0] == 0:
            zeroList.append(row)
        else:
            numList.append(row)
    matrix = numList+zeroList
    
    # find min number in column and put at the top for pivot of column
    r1 = matrix[0]
    y = r1[0]
    total = 1
    for row in matrix:
        x = row[0]
        if x == 0:
            pass
        if 0 < x < y:
            y = x
            whichRow = total #row with min number in column 1
            matrix = swap(matrix, 0, whichRow-1)
        else:
            pass
        total = total + 1
        
    # if all numbers are negative
    if y < 0:
        scale(matrix, 0, -1)
    else:
        pass
    r1 = matrix[0]
    y = r1[0]
    pivot = y

    # If the pivot is greater than one divide row by the pivot number
    if pivot > 1 or pivot < 0:
        scale(matrix, 0, 1/pivot)
    else:
        pass
    
    # create a pivot in the first column 
    rowNum = 0
    for row in matrix[1:]:
        r = row[0]
        if r == 0:
            pass
        else:
            rowNum = rowNum + 1
            AddMult(matrix, rowNum, 0, -r)
    return matrix

#-------------------------------------------------------------------------------
# Manipulate seperate parts of the matrix 
def takeOut(matrix, i, j):
    takeRows = matrix[i:]
    matrix =[]
    for row in takeRows:
        newRow = row[j:]
        matrix.append(newRow)
    return matrix

def putBack(originalMatrix, matrix, i, j):
    putRows = originalMatrix
    total = 0 
    for row in putRows[i:]:
        row[j:] = matrix[total]
        total = total + 1
    return originalMatrix
#-------------------------------------------------------------------------------
# Helper functions to do the second half
def clearHelper(matrix, pivot, rowNums, pivotColumn):
    scale(matrix,-1, (1/pivot))
    pivot = pivot/1
    for R in range(0,rowNums):
        if matrix[R][pivotColumn] == 0:
            pass
        else:
            AddMult(matrix, R, rowNums, -(matrix[R][pivotColumn]))
    return matrix

def clearLeft_Right(matrix):
    rowNum = len(matrix)
    colNum = len(matrix[0])
    trackRow = rowNum -1
    pivot = 0
    for _ in range(rowNum):
        pivotNext = None
        pivotColumn = None
        # if on last row
        if trackRow == 0:
            pivotColumn = 0
            scale(matrix, 0, (1/matrix[0][0]))
        else:
            c = colNum
            for _ in range(colNum):
                c = c - 1
                if matrix[trackRow][c] != 0:
                    pivotColumn = c
                    pivot = matrix[trackRow][c]
                else:
                    pass
            pivotNext = pivotColumn
            # use the infor from loop
            if pivotColumn != None:
                clearHelper(matrix, pivot, trackRow, pivotColumn)
                #print(matrix)
            else:
                pass
        trackRow = trackRow -1
        #print(matrix)
    return matrix   

    # put all zeros to the bottom
def putZeros(matrix):
    colNum = len(matrix[0])
    numList = []
    zeroList = []
    for row in matrix:
        total = 0 
        for number in row:
            if number == 0:
                total = total + 1
            else:
                pass
        if total == colNum:
            zeroList.append(row)
        else:
            numList.append(row)
    matrix = numList+zeroList
    return matrix

# Show matrix in nice format
def printGrid(matrix):
    for row in matrix:
        print(row)
    print()
