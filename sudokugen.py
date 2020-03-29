from random import shuffle,sample,randint

def in_square(row,col):
    if row<3 and col<3:
        return 1
    elif col>=3 and col<6 and row<3:
        return 2
    elif col>=6 and col<9 and row<3:
        return 3
    elif col<3 and row>=3 and row<6:
        return 4
    elif col>=3 and col<6 and row>=3 and row<6:
        return 5
    elif col>=6 and col<9 and row>=3 and row<6:
        return 6
    elif col<3 and row>=6 and row<9:
        return 7
    elif col>=3 and col<6 and row>=6 and row<9:
        return 8
    elif col>=6 and col<9 and row>=6 and row<9:
        return 9
    else:
        return 0
def ite_square(board,row,col):
    squ=[]
    sub_square=in_square(row,col)
    if sub_square==1:
        for i in range(0,3):
            for j in range(0,3):
                squ.append((board[i][j],i,j))
        return squ
    elif sub_square==2:
        for i in range(0,3):
            for j in range(3,6):
                squ.append((board[i][j],i,j))
        return squ 
    elif sub_square==3:
        for i in range(0,3):
            for j in range(6,9):
                squ.append((board[i][j],i,j))
        return squ 
    elif sub_square==4:
        for i in range(3,6):
            for j in range(0,3):
                squ.append((board[i][j],i,j))
        return squ 
    elif sub_square==5:
        for i in range(3,6):
            for j in range(3,6):
                squ.append((board[i][j],i,j))
        return squ 
    elif sub_square==6:
        for i in range(3,6):
            for j in range(6,9):
                squ.append((board[i][j],i,j))
        return squ 
    elif sub_square==7:
        for i in range(6,9):
            for j in range(0,3):
                squ.append((board[i][j],i,j))
        return squ 
    elif sub_square==8:
        for i in range(6,9):
            for j in range(3,6):
                squ.append((board[i][j],i,j))
        return squ 
    elif sub_square==9:
        for i in range(6,9):
            for j in range(6,9):
                squ.append((board[i][j],i,j))
        return squ 
    elif sub_square==0:
        return 0
def valid_sudoku(board,row,col):
    toggle=0
    for i in range(0,9):
        if board[i][col]==board[row][col]:
            if i==row:
                continue
            toggle+=1
            break
    for i in range(0,9):
        if board[row][i]==board[row][col]:
            if i==col:
                continue
            toggle+=1
            break
    for k,i,j in ite_square(board,row,col):
        if board[row][col]==k:
            if i==row and j==col:
                continue
            toggle+=1
            break
    if toggle==0:
        return True
    else:
        return False
def sudoku_gen(board=[["-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-","-"]]):
   #board size is 9x9 by default
    nlist=[1,2,3,4,5,6,7,8,9]
    shuffle(nlist)
    solve_sudoku(board,0,0,nlist)
    for row in range(0,9):
        space=sample(range(0,9),randint(5,6))
        for col in range(0,9):
            if col in space:
                board[row][col]='-'
    return board
def locked_tab(board):
    const=[]
    for i in range (0,9):
        for j in range(9):
            if board[i][j]!='-':
                const.append((i,j))
    return const
def solve_sudoku(board,row,col,listt=[1,2,3,4,5,6,7,8,9]):
    if (row,col) in locked_tab(board):
        return solve_sudoku(board,row,col+1,listt)
    if col>8:
        return solve_sudoku(board,row+1,0,listt)
    if row>8 :
        return True
    else:
        for k in listt:
            board[row][col]=k
            if valid_sudoku(board,row,col):
                if solve_sudoku(board,row,col+1,listt):
                    return True
        board[row][col]='-'
        return False

            
if __name__=="__main__":

    const=[]
    board=sudoku_gen()
    for i in board:
        print(i)
