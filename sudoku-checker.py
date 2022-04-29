def row_and_column_correct(sudoku: list, x_times_y: int) -> bool:
    for i in range(0, x_times_y):
        row = sudoku[i]
        column_list = []
        for k in range(1, x_times_y+1):
            column = sudoku[k-1]
            if row.count(k) > 1:
                return False
            if column[i] > 0 and column[i] in column_list:
                return False
            column_list.append(column[i])
    return True

def rectangle_correct(sudoku: list, x: int, y: int) -> bool:
    count = []
    for f in range(0, x):
        n = f*y
        for i in range(0, y):
            m = i*x
            count = []
            for j in range(0+n, y+n):
                for k in range(0+m,x+m):
                    if sudoku[j][k] > 0 and sudoku[j][k] in count:
                        return False
                    count.append(sudoku[j][k])
    return True

def sudoku_correct(sudoku: list, size_x: int, size_y: int, size_x_times_y: int) -> bool:
    return row_and_column_correct(sudoku, size_x_times_y) and rectangle_correct(sudoku, size_x, size_y)

def main():
    grid_size_str = input("\nSudoku size XxY (for example 3x2 or 4x4): ")
    grid_size_int = grid_size_str.split("x")
    x = int(grid_size_int[0])
    y = int(grid_size_int[1])
    x_times_y = x*y
    sudoku = []
    count = []
    print("\n\nManual input your sudoku (no spaces, enter starts a newline, zeroes represent blank spot)\n")
    for i in range(0,x_times_y):
        if i > 0:
            sudoku.append(count)
            count = []
        user_inp = input(":    ")
        for j in range(len(user_inp)):
            count.append(int(user_inp[j]))
    sudoku.append(count)
    if sudoku_correct(sudoku, x, y, x_times_y):
        print("\nThis sudoku is correct!")
    else:
        print("\nThis sudoku is uncorrect.")

main()