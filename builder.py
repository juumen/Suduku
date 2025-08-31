import tkinter as tk

class SudokuBuilder:
    def __init__(self, root, on_complete):
        self.root = root
        self.on_complete = on_complete
        self.sudoku_grid = []

        #
        vcmd = (root.register(self.validate_input), "%P")
        self.entry_field = tk.Entry(root, width=20, font=('Arial', 16),
                                    validate="key", validatecommand=vcmd)
        self.entry_field.grid(row=0, column=0, columnspan=4, pady=10)

        self.keys = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('?', 4, 0), ('Clear', 4, 1), ('Enter', 4, 2)
            
        ]

        
        self.buttons = {}

        for (text, row, col) in self.keys:
            button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 12),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons[text] = button

    def validate_input(self, new_value):
        """Allow only up to 9 characters (digits or '?')"""
        if len(new_value) > 9:
            return False
        
        if len(new_value) == 9:
            self.disable_number_buttons()
        else:
            self.enable_number_buttons()
        return all(ch.isdigit() or ch == '?' for ch in new_value)

    def disable_number_buttons(self):
        for key in ['0','1','2','3','4','5','6','7','8','9','?']:
            self.buttons[key]['state'] = 'disabled'

    def enable_number_buttons(self):
        for key in ['0','1','2','3','4','5','6','7','8','9','?']:
            self.buttons[key]['state'] = 'normal'

    def on_button_click(self, value):
        current_text = self.entry_field.get()

        if value == 'Clear':
            self.entry_field.delete(0, tk.END)
            self.enable_number_buttons()

        elif value == 'Enter':
            if len(current_text) == 9 and all(ch.isdigit() or ch == '?' for ch in current_text):
                row = [int(ch) if ch.isdigit() else '?' for ch in current_text]
                self.sudoku_grid.append(row)
                row_number = len(self.sudoku_grid)
                print(f"Row {row_number} saved:", row)
                self.entry_field.delete(0, tk.END)
                self.enable_number_buttons()

                if len(self.sudoku_grid) == 9:
                    print("\nSudoku Puzzle Entered:")
                    for idx, r in enumerate(self.sudoku_grid, start=1):
                        print(f"Row {idx}: {r}")
                    self.on_complete(self.sudoku_grid)
            else:
                print("Invalid row. Enter exactly 9 values (0–9 or ?).")

        else:
            if len(current_text) < 9:
                self.entry_field.insert(tk.END, value)
                if len(current_text) + 1 == 9:
                    self.disable_number_buttons()

