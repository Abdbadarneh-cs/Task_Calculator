import tkinter as tk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.calculator = Calculator()
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("570x600+100+200")
        self.root.resizable(False, False)
        self.root.configure(bg="#17161b")

        self.equation = ""

        self.label_result = tk.Label(root, width=25, height=2, text="", font=("arial", 30),
                                     bg="#1e1e1e", fg="white", anchor="e")
        self.label_result.pack()

        self.create_buttons()

    def show(self, value):
        self.equation += value
        self.label_result.config(text=self.equation)

    def clear(self):
        self.equation = ""
        self.label_result.config(text="")

    def calculate(self):
        result = self.calculator.evaluate(self.equation)
        self.label_result.config(text=result)
        self.equation = result if result != "Error" else ""

    def create_buttons(self):
        button_specs = [
            ("C", 10, 100, "#3697f5", lambda: self.clear()),
            ("/", 150, 100, "#ff9500", lambda: self.show("/")),
            ("%", 290, 100, "#ff9500", lambda: self.show("%")),
            ("*", 430, 100, "#ff9500", lambda: self.show("*")),

            ("7", 10, 200, "#2a2d36", lambda: self.show("7")),
            ("8", 150, 200, "#2a2d36", lambda: self.show("8")),
            ("9", 290, 200, "#2a2d36", lambda: self.show("9")),
            ("-", 430, 200, "#ff9500", lambda: self.show("-")),

            ("4", 10, 300, "#2a2d36", lambda: self.show("4")),
            ("5", 150, 300, "#2a2d36", lambda: self.show("5")),
            ("6", 290, 300, "#2a2d36", lambda: self.show("6")),
            ("+", 430, 300, "#ff9500", lambda: self.show("+")),

            ("1", 10, 400, "#2a2d36", lambda: self.show("1")),
            ("2", 150, 400, "#2a2d36", lambda: self.show("2")),
            ("3", 290, 400, "#2a2d36", lambda: self.show("3")),
            (".", 430, 400, "#ff9500", lambda: self.show(".")),

            ("(", 10, 500, "#2a2d36", lambda: self.show("(")),
            ("0", 150, 500, "#2a2d36", lambda: self.show("0")),
            (")", 290, 500, "#2a2d36", lambda: self.show(")")),
            ("=", 430, 500, "#ff9500", lambda: self.calculate()),
        ]

        for spec in button_specs:
            text, x, y, color, cmd = spec[:5]
            width = spec[5] if len(spec) > 5 else 5
            height = spec[6] if len(spec) > 6 else 1

            tk.Button(self.root, text=text, width=width, height=height,
                      font=("arial", 30, "bold"), bd=1, fg="#fff", bg=color,
                      command=cmd).place(x=x, y=y)
