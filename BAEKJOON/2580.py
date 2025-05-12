import sys
input = sys.stdin.readline

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

def check_box(x,y):
    temp = 0
    box_x = x//3
    box_y = y//3
    cnt = 0
    sum = 0
    for i in range(3):
        for j in range(3):
            if sudoku[3*box_x + i][3*box_y + j] != 0:
                temp+= 1
                sum+=sudoku[3*box_x + i][3*box_y + j]
            cnt+=1
        if temp == 8:
            sudoku[x][y] = 45-sum

def check_row(x,y):
    temp = 0
    sum = 0
    for i in range(9):
        if sudoku[x][i] != 0:
            temp+=1
            sum+=sudoku[x][i]
    if temp == 8:
        sudoku[x][y] = 45-sum
        return False
    return True
def check_col(x,y):
    temp = 0
    sum = 0
    for i in range(9):
        if sudoku[i][y] != 0:
            temp+=1
            sum+=sudoku[i][y]
    if temp == 8:
        sudoku[x][y] = 45-sum
        return False
    return True

for i in range(9):
    for j in range(9):
        if sudoku[i][j]!=0:
            print(sudoku[i][j], end=' ')
            continue
        if(check_row(i,j)):
            if(check_col(i,j)):
                check_box(i,j)
        print(sudoku[i][j], end=' ')
    print()

