from tkinter import ttk
import tkinter as tk
import math

from reproducir_sonido import *

#Define las fuente de texto
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
GYLPHS_FONT_STYLE = ("Arial", 28, "bold")

# Define colores
BLACK = "#000000"
PSEUDOBLACK = "#28292b"
WHITE = "#FFFFFF"
RED = "#FF4971"
GREEN = "#61C766"
CYAN = "#79E6F3"
TEAL = "#00B19F"
AMBER = "#F2A272"
ORANGE = "#E5946A"

#PI = 3.1415   # Define valor de pi para el boton PI
resultado_anterior = 0   # Define la variable que sera usada por el boton ans
resultado = 0  # Define la variable que sera usada para reproducir el sonido

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(True, True)
        self.window.title("Calculadora Musical")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "*", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        # Crea la barra de progresso
        self.pb = ttk.Progressbar(self.buttons_frame, orient='horizontal', mode='determinate', maximum=10,length=260)
        self.pb.grid(row=5, column=2, columnspan=4, padx=0, pady=0)
        self.estado_sonido = "喇"  # Define el estado del sonido

        # Configura las columnas y las filas 
        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 6):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        # Crea los botones y los atajos de teclado
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())

        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def update_label(self):
        self.label.config(text=self.current_expression)

    def update_total_label(self):
        expression = self.total_expression

        for operator, symbol in self.operations.items():
            if symbol == '*':
                expression = expression.replace(operator, f'{symbol}')
            else:
                expression = expression.replace(operator, f' {symbol} ')

        self.total_label.config(text=expression)

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_open_parenthesis_button()
        self.create_close_parenthesis_button()
        self.create_delete_button()
        self.create_module_button()
        self.create_ans_button()
        self.create_play_button()
        #self.create_PI_button()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=WHITE)
        frame.pack(expand=True, fill='both')
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=BLACK, fg=WHITE, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=BLACK, fg=WHITE, padx=24, font=GYLPHS_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_operator_buttons(self):
        i = 0

        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=ORANGE, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=5, sticky=tk.NSEW)
            i += 1

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=PSEUDOBLACK, fg=CYAN, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def ans(self):
        self.current_expression += self.resultado_anterior
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()

    def sqrt(self):
        self.current_expression = str(math.sqrt(float(self.current_expression)))
        self.update_label()
        self.update_total_label()

    def square(self):
        self.current_expression += str(2*"*")
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_label()
        self.update_total_label()

    def delete(self):
        self.current_expression = self.current_expression[0:-1]
        self.total_expression = self.total_expression

        if len(self.current_expression) == 0:
            self.total_expression = self.total_expression[0:-1]
        else:
            pass

        self.update_label()
        self.update_total_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def reducir_numero(self):
        # Comprueba si es entero y si no lo es lo convierte
        try:
            val = int(self.resultado)
        except ValueError:
            try:
                float(self.resultado)
                self.resultado = self.resultado[-1::-4]
                self.reducir_numero()
            except ValueError:
                self.resultado = float(self.resultado)
                print(f"No.. input is not a number. It's a string: {self.resultado}")

        # Si el resultado es menor a 0 o mayor 84 y
        # entonces convierte el resultado en un numero dentro de ese rango.
        if int(self.resultado) < 0:
            self.resultado = int(self.resultado) * -1
            self.reducir_numero()

        while int(self.resultado) > 84:
            self.resultado = int(self.resultado)-(int(self.resultado)//2)
            self.reducir_numero()

    def play_and_stop(self):
        if self.estado_sonido == "喇":
            self.estado_sonido = ""
            self.create_play_button()

            self.total_expression += self.current_expression
            self.resultado = str(eval(self.total_expression))

            self.reducir_numero()
            pianoSonido(self.resultado)
            self.pb.start()
        else:
            self.estado_sonido = "喇"
            self.create_play_button()

            para_sonido()
            self.pb.stop()

    def module_operator(self):
        self.current_expression += str('%')
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_label()
        self.update_total_label()

    def open_parenthesis(self):
        self.current_expression += str('(')
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_label()
        self.update_total_label()

    def close_parenthesis(self):
        self.current_expression += str(')')
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_label()
        self.update_total_label()

    def create_ans_button(self):
        button = tk.Button(self.buttons_frame, text="ans", bg=PSEUDOBLACK, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.ans)
        button.grid(row=4, column=3, sticky=tk.NSEW)

    def create_play_button(self):
        button = tk.Button(self.buttons_frame, text=self.estado_sonido, bg=PSEUDOBLACK, fg=WHITE, font=GYLPHS_FONT_STYLE, height=0, width=0, borderwidth=0, command=self.play_and_stop)
        button.grid(row=5, column=1, columnspan=1, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=PSEUDOBLACK, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_module_button(self):
        button = tk.Button(self.buttons_frame, text="%", bg=PSEUDOBLACK, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.module_operator)
        button.grid(row=0, column=4, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=PSEUDOBLACK, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text="", bg=GREEN, fg=WHITE, font=GYLPHS_FONT_STYLE, borderwidth=0, command=self.delete)
        button.grid(row=3, column=4, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="﯊", bg=TEAL, fg=WHITE, font=GYLPHS_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_open_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text="(", bg=PSEUDOBLACK, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.open_parenthesis)
        button.grid(row=1, column=4, sticky=tk.NSEW)

    def create_close_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text=")", bg=PSEUDOBLACK, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.close_parenthesis)
        button.grid(row=2, column=4, sticky=tk.NSEW)
        self.update_label()

    #def PI(self):
        #self.current_expression += str(PI)
        #self.total_expression += self.current_expression
        #self.current_expression = ""
        #self.update_total_label()
        #self.update_label()

    #def create_PI_button(self):
        #button = tk.Button(self.buttons_frame, text="π", bg=PSEUDOBLACK, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.PI)
        #button.grid(row=5, column=5, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        try:
            self.resultado_anterior = str(eval(self.total_expression))

            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
            self.pb.start()
        except Exception as e:
            self.current_expression = "Syntax Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=RED, fg=WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=4, columnspan=2, sticky=tk.NSEW)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
