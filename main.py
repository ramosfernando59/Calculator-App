import tkinter as tk
import customtkinter as ctk

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator App")
        self.minsize(425, 600)  # Definindo largura mínima de 425 pixels

        self.result_var = tk.StringVar()

        # Create display
        self.display = ctk.CTkEntry(self, textvariable=self.result_var, font=("Arial", 24), justify='right', state='readonly')
        self.display.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky="nsew")

        # Create buttons
        buttons = [
            ["AC", "C", "+/-", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == "0":
                    btn = ctk.CTkButton(self, text=btn_text, font=("Arial", 20), command=lambda text=btn_text: self.on_button_click(text))
                    btn.grid(row=i+1, column=j, columnspan=2, padx=10, pady=10, sticky="nsew")
                elif btn_text in {".", "="}:
                    btn = ctk.CTkButton(self, text=btn_text, font=("Arial", 20), command=lambda text=btn_text: self.on_button_click(text))
                    btn.grid(row=i+1, column=j+1, padx=10, pady=10, sticky="nsew")
                else:
                    btn = ctk.CTkButton(self, text=btn_text, font=("Arial", 20), command=lambda text=btn_text: self.on_button_click(text))
                    btn.grid(row=i+1, column=j, padx=10, pady=10, sticky="nsew")

        # Configure grid weights
        for i in range(6):  # Update to 6 rows due to header row
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def on_button_click(self, text):
        if text == "AC":
            self.result_var.set("")
        elif text == "C":
            current_text = self.result_var.get()
            if current_text:
                self.result_var.set(current_text[:-1])
        elif text == "=":
            try:
                expression = self.result_var.get().replace('x', '*').replace('÷', '/')
                self.result_var.set(str(eval(expression)))
            except:
                self.result_var.set("Error")
        elif text in {"+", "-", "*", "/", "+/-"}:
            current_text = self.result_var.get()
            if text == "+/-":
                if current_text.startswith('-'):
                    self.result_var.set(current_text[1:])
                else:
                    self.result_var.set('-' + current_text)
            else:
                self.result_var.set(current_text + text)
        else:
            self.result_var.set(self.result_var.get() + text)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
