import tkinter as tk
from calculator import addition, subtraction, multiplication, division

class Calculator:
    def __init__(self):
        self. window = tk.Tk()
        self.window.title("CALCULADORA")
        self.window.configure(bg="gray")
        self.icon_path="D:\CODE\PYTHON\Calculadora\images\Calculator.ico"
        self.window.iconbitmap(self.icon_path)
        self.current_input=""
        self.total=0
        self.operator=None

        

        self.add_input()
        self.add_buttons()


        self.window.mainloop()

    def add_input(self):
        self.text_input = tk.Entry(self.window, font=("Arial", 16))
        self.text_input.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.text_input.configure(bg="green")  # Establece el color de fondo del campo de entrada
        self.text_input.configure(fg="black")  # Establece el color del texto del campo de entrada
    
    def add_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text_b, row_b, column_b) in buttons:
            button = tk.Button(self.window, text=text_b, padx=20, pady=20, command=lambda t=text_b: self.click_button(t))
            button.grid(row=row_b, column=column_b, sticky='nsew', padx=5, pady=5)
            button.configure(bg="#CCCCCC")
            button.configure(fg="black")
            button.config(relief="raised") 
        
        # Configuración de columnas para centrar botones
        for col in range(4):
            self.window.grid_columnconfigure(col, weight=1)

        # Configuración de filas para centrar botones verticalmente
        for row in range(5):
            self.window.grid_rowconfigure(row, weight=1)

    def click_button(self, value):
        if value.isdigit() or value == ".":
            self.current_input += value
            self.update_display(self.current_input)
        elif value in "+-*/":
            if self.current_input:
                self.total = float(self.current_input)
            self.operator = value
            self.current_input = ""
        elif value == "=":
            self.perform_calculation()

    def perform_calculation(self):
        if self.operator and self.current_input:
            operand = float(self.current_input)
            if self.operator == "+":
                self.total = addition(self.total, operand)
            elif self.operator == "-":
                self.total = subtraction(self.total, operand)
            elif self.operator == "*":
                self.total = multiplication(self.total, operand)
            elif self.operator == "/":
                self.total = division(self.total, operand)
            self.update_display(str(self.total))
            self.current_input = ""
            self.operator = None
    
    def update_display(self, value):
        self.text_input.delete(0, tk.END)
        self.text_input.insert(0, value)