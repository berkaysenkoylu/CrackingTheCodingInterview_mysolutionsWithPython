## Chapter 1 - 1.8) Zero Matrix

from random import randint

def form_matrix(n, m):
    """Creates an n x m matrix from random numbers."""
    matrix = []
    for _ in range(n):
        row = []
        for i in range(m):
            new_int = randint(0, 9)
            row.append(new_int)
        matrix.append(row)

    return matrix

def zero_detector(mtrx):
    """
    This is a function that detects the zeros in a matrix
    and store the coordinates in a dictionary!
    """
    zero = []

    if len(mtrx) == 0:
        return None
    
    ## Number of rows
    row = len(mtrx)

    ## Number of columns
    col = len(mtrx[0]) ## mtrx[0] can be mtrx[1], mtrx[2] etc. To be sure, use mtrx[0]

    zero_n = 0
    zero_m = 0
       
    for i in range(row):
        for j in range(col):
            if mtrx[i][j] == 0:
                zero_n = i
                zero_m = j
                coord = (i, j)
                zero.append(coord)
    return zero

def replace_row_col_with_zero(mtrx):
    row = len(mtrx)
    col = len(mtrx[0])

    zero_coord = zero_detector(mtrx)

    for i in range(len(zero_coord)):
        zero_n = zero_coord[i][0]
        zero_m = zero_coord[i][1]
        
        ## Replace row
        mtrx[zero_n] = [0] * col

        ## Replace column
        for n in range(row):
            mtrx[n][zero_m] = 0

    return mtrx


def zero_matrix(mtrx):
    mtrx = replace_row_col_with_zero(mtrx)

    for row in range(len(mtrx)):
        print mtrx[row]
    


matrix = form_matrix(8, 8)

print matrix

print zero_matrix(matrix)
