import tkinter as tk

root = tk.Tk()
root.title("Sudoku Builder")


sudoku_grid = []


current_row = []

# Entry field
entry_field = tk.Entry(root, width=20, font=('Arial', 16))
entry_field.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout
keys = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('?', 4, 0), ('Clear', 4, 1),('Enter', 4, 2)
   
]

def on_button_click(value):
    global current_row, sudoku_grid
    
    current_text = entry_field.get()
    
    if value == 'Clear':
        entry_field.delete(0, tk.END)
        
    elif value == 'Enter':
        if (current_text.isdigit() and 0 <= int(current_text) <= 9) or current_text == '?':
           
            if current_text == '?':
                current_row.append('?')
            else:
                current_row.append(int(current_text))
            
            entry_field.delete(0, tk.END)
            
            # If row has 9 entries, save it
            if len(current_row) == 9:
                sudoku_grid.append(current_row)
                print("Row saved:", current_row)
                current_row = []  # reset for next row
            
            
            if len(sudoku_grid) == 9:
                print("\nSudoku Grid Completed:")
                for row in sudoku_grid:
                    print(row)
                
               
                
        else:
            print("Invalid input. Enter 0–9 or ?")
    
    else:
        entry_field.insert(tk.END, value)


for (text, row, col) in keys:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 12),
                       command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
