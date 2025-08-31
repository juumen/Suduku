
# driver.py
import tkinter as tk
from builder import SudokuBuilder
from solver import solve_sudoku


BOX_COLORS = [
    "#f8f9fa", "#e9ecef", "#f8f9fa",
    "#e9ecef", "#f8f9fa", "#e9ecef",
    "#f8f9fa", "#e9ecef", "#f8f9fa"
]

def show_solution_window(root, grid):
    solution_win = tk.Toplevel(root)
    solution_win.title("Sudoku Solution")

    solved = solve_sudoku(grid)

    for i in range(9):
        for j in range(9):
            # determine which 3x3 box this cell belongs to
            box_index = (i // 3) * 3 + (j // 3)
            bg_color = BOX_COLORS[box_index]

            cell = tk.Label(
                solution_win,
                text=str(solved[i][j]),
                width=4, height=2,
                borderwidth=1, relief="solid",
                font=('Arial', 14),
                bg=bg_color
            )
            cell.grid(row=i, column=j, padx=1, pady=1)

def main():
    root = tk.Tk()
    root.title("Sudoku Builder")

    SudokuBuilder(root, on_complete=lambda grid: show_solution_window(root, grid))

    root.mainloop()

if __name__ == "__main__":
    main()
