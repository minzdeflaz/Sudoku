import sudokugen
if __name__=="__main__":
    
    board=sudokugen.sudoku_gen()
    for i in board:
        print(i)
    sudokugen.solve_sudoku(board,0,0)
    print('\n')
    for i in board:
        print(i)
