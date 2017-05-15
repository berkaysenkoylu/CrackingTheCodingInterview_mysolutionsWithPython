## Chapter 1 - 1.7) Rotate Matrix


def matrix2list(matrix):
    """A function to transform the given matrix to a list!"""
    newList = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newList.append(matrix[i][j])
    return newList


def matrixrotor(matrix):
    """A function that rotates the matrix by 90 degrees clockwise!"""
    newList = matrix2list(matrix)
    matrix_to_return = []
    n = int(len(newList) - (len(newList))**(0.5))
    while(n < len(newList)):
        row = []
        i = n
        while(i >= 0):
            row.append(newList[i])
            i -= int((len(newList))**(0.5))
        matrix_to_return.append(row)
        n += 1
    return matrix_to_return
        
            


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print matrixrotor(matrix)


