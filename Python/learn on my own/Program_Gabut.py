import tkinter as tk
from tkinter import messagebox
import math

class kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.current_input = ''
        self.result_var = tk.StringVar()
        self.result_var.set('0')

        self.bg_color = "#363636"
        self.button_color = "#404040"
        self.operator_color = "#FF9500"
        self.special_color = "#A6A6A6"
        self.text_color = "#FFFFFF"

        self.root.configure(bg=self.bg_color)
        self.create_widgets()

    def create_widgets(self):
        display_frame = tk.Frame(self.root, bg=self.bg_color)
        display_frame.pack(pady=20, padx=20, fill=tk.X)

        result_label = tk.Label(display_frame, textvariable=self.result_var, font=('Arial', 24), bg=self.bg_color, fg=self.text_color, anchor="e", padx=10)
        result_label.pack(fill=tk.X)

        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        button =  [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']
        ]

        for i, row in enumerate(button):
            for j, button_text in enumerate(row):
                if button_text == '':
                    continue

                if button_text in ['C', '±', '%']:
                    bg_color = self.special_color
                    text_color = "#000000"
                elif button_text in ['÷', '×', '-', '+', '=']:
                    bg_color = self.operator_color
                    text_color = "#FFFFFF"
                else:
                    bg_color = self.button_color
                    text_color = "#FFFFFF"

                if button_text == '0':
                    btn = tk.Button(button_frame, text=button_text, font=('Arial', 18),bg=bg_color, fg=text_color, border=0, command=lambda t=button_text: self.button_click(t))
                    btn.grid(row=i, column=j, columnspan=2,sticky='ew',  padx=2, pady=2)
                else:
                    btn = tk.Button(button_frame, text=button_text, font=('Arial', 18), bg=bg_color, fg=text_color, border=0, command=lambda t=button_text: self.button_click(t))
                    btn.grid(row=i, column=j, sticky='ew', padx=2, pady=2)

        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.columnconfigure(j, weight=1)
    
    def button_click(self, value):
        try:
            if value == 'C':
                self.current_input = ''
                self.result_var.set('0')
            
            elif value == '±':
                if self.current_input and self.current_input != "0":
                    if self.current_input[0] == '-':
                        self.current_input = self.current_input[1:]
                    else:
                        self.current_input = '-' + self.current_input
                    self.result_var.set(self.current_input)

            elif value == '%':
                if self.current_input:
                    try:
                        result = float(self.current_input) / 100
                        self.current_input = str(result)
                        self.result_var.set(self.current_input)
                    except:
                        self.result_var.set('Error')

            elif value == '=':
                if self.current_input:
                    expression = self.current_input.replace('×', '*').replace('÷', '/')
                    try:
                        result = eval(expression)
                        self.current_input = str(result)
                        self.result_var.set(self.current_input)
                    except:
                        self.result_var.set('Error')

            else:
                if self.current_input == '0' and value not in ['÷', '×', '-', '+', '.']:
                    self.current_input = value 
                else:
                    self.current_input += value
                self.result_var.set(self.current_input)

        except Exception as e:
            self.result_var.set('Error')
            self.current_input = ''
def main():
    root = tk.Tk()
    app = kalkulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()