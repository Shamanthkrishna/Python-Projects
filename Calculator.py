import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.expression = ""
        
        self.display = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)
        
        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        
        for button in buttons:
            tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        tk.Button(self.root, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear).grid(row=row, column=col)
    
    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.update_display()
    
    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except Exception as e:
            self.expression = "Error"
        self.update_display()
    
    def clear(self):
        self.expression = ""
        self.update_display()
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
