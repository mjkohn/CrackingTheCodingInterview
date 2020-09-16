# Cracking the Code interview
# Interview question 1.7
# zero row,col of MxN matrix

def find_zero_row(matrix):
    return [i for i, row in enumerate(matrix) if not all(row)]

def find_zero_column(matrix):
    # this will transpose the matrix and send it to find rows
    return find_zero_row(zip(*matrix))

def zero(matrix):
    rows = find_zero_row(matrix)
    cols = find_zero_column(matrix)

    # Zero out rows
    for row in rows:
        rows[row] = [0] * len(matrix[0])

    # Zero Cols, access column needed to zero
    for col in cols:
        # access row, and zero out column
        for row in matrix:
            row[col] = 0

    return matrix
