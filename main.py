from sudokugen import *
from tkinter import *
import time

if __name__ == "__main__":
    root = Tk()
    root.title("Sudoku")
    board, winboard = sudoku_gen()
    label1 = Label(root, text="Sudoku", font="Arial 20 italic", pady=7)
    label1.pack()
    frame = Frame(root)
    frame2 = Frame(root)
    frame.pack(pady=(35, 0))
    frame2.pack()
    cell = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            e = Entry(frame, width=3, fg="black", justify="center",
                      relief="sunken", selectbackground="yellow")
            e.grid(row=i, column=j, ipady=10, ipadx=10)
            if i % 3 == 2:
                e.grid(pady=(0, 5))
            if j % 3 == 2:
                e.grid(padx=(0, 5))
            if board[i][j] != "-":
                e.insert(0, board[i][j])
                e.configure(state="readonly")
                e["fg"] = "blue"
            else:
                cell[(i, j)] = e
    toggle = False

    def popup():
        win_pop = Tk()
        win_pop.title("Victory")
        win_label = Label(win_pop, text="You Win !!")
        win_label.pack(side=TOP)
        win_button = Button(win_pop, text="Done", command=win_pop.destroy)
        win_button.pack(side=BOTTOM)

    def check():
        global toggle
        if board == winboard:
            popup()
            root.destroy()
            exit
        for i, j in cell:
            if cell[(i, j)].get() != '':
                board[i][j] = int(cell[(i, j)].get())
        wrong = check_board(board, winboard)
        if toggle == False:
            for i in wrong:
                cell[(i[1], i[2])]["bg"] = "red"
            toggle = True
            frame.after(1000, check)
        else:
            for i in wrong:
                cell[(i[1], i[2])]["bg"] = "white"
            toggle = False

    def solve():
        wrong = check_board(board, winboard)
        for i in wrong:
            cell[(i[1], i[2])].delete(0)
            cell[(i[1], i[2])].insert(0, winboard[i[1]][i[2]])
    b1 = Button(frame2, text="Check", width=10, height=10, command=check)
    b1.pack(padx=45, pady=(5, 15), side=LEFT)
    b2 = Button(frame2, text="Solve", width=10, height=10, command=solve)
    b2.pack(padx=45, pady=(5, 15), side=RIGHT)
    root.geometry("600x500+150+145")
    mainloop()
