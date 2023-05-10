
def is_valid(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return True
    found_solution = False
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 1
            if solve(board, row+1, n, solutions):
                found_solution = True
            board[row][col] = 0
    return found_solution


def print_solution(board):
    cell_size = 50
    img_size = cell_size * len(board)
    img = Image.new('RGB', (img_size, img_size), 'white')
    draw = ImageDraw.Draw(img)
    for i in range(len(board)):
        for j in range(len(board)):
            x0, y0 = i * cell_size, j * cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            if (i + j) % 2 == 0:
                draw.rectangle((x0, y0, x1, y1), fill='black')
            if board[i][j] == 1:
                draw.ellipse((x0 + 5, y0 + 5, x1 - 5, y1 - 5), fill='red')
    img.show()

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(board, 0, n, solutions)
    if solutions:
        for i, solution in enumerate(solutions):
            print("Solution", i+1)
            print_solution(solution)
    else:
        print("No solutions found")

