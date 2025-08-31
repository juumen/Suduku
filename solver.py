

def isSafe(mat, i, j, num, row, col, box):
    if (row[i] & (1 << num)) or (col[j] & (1 << num)) or (box[i // 3 * 3 + j // 3] & (1 << num)):
        return False
    return True

def sudokuSolverRec(mat, i, j, row, col, box):
    n = len(mat)
    if i == n - 1 and j == n:
        return True
    if j == n:
        i += 1
        j = 0
    if mat[i][j] != 0:
        return sudokuSolverRec(mat, i, j + 1, row, col, box)

    for num in range(1, n + 1):
        if isSafe(mat, i, j, num, row, col, box):
            mat[i][j] = num
            row[i] |= (1 << num)
            col[j] |= (1 << num)
            box[i // 3 * 3 + j // 3] |= (1 << num)

            if sudokuSolverRec(mat, i, j + 1, row, col, box):
                return True

            mat[i][j] = 0
            row[i] &= ~(1 << num)
            col[j] &= ~(1 << num)
            box[i // 3 * 3 + j // 3] &= ~(1 << num)
    return False

def solve_sudoku(grid):
    """Takes a 9x9 grid with 0 or '?' as blanks, returns solved grid."""
    n = len(grid)
    mat = [[0 if val == '?' else val for val in row] for row in grid]

    row = [0] * n
    col = [0] * n
    box = [0] * n

    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                row[i] |= (1 << mat[i][j])
                col[j] |= (1 << mat[i][j])
                box[(i // 3) * 3 + j // 3] |= (1 << mat[i][j])

    sudokuSolverRec(mat, 0, 0, row, col, box)
    return mat
