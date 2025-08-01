#Import moduls
import tkinter as tk
import math
from operation import fact
from operation import sqr
from operation import logar
from operation import rad
from operation import cosin
from operation import sin
from operation import tangens

#Create a window. Add some color, font, etc.
root = tk.Tk()
root.title("Calculator")
root.configure(bg="lightyellow")
root.geometry("1000x800")

# Поля для вводу чисел
entry_1 = tk.Entry(root, font=("Times New Roman", 20))
entry_1.place(x=65, y=100)
entry_2 = tk.Entry(root, font=("Times New Roman", 20))
entry_2.place(x=65, y=200)

# Мітка для результату
result_label = tk.Label(root, text="", font=("Times New Roman", 20), bg="lightyellow")
result_label.place(x=50, y=300)

# Create function for addition
def add_button_click():
    try:
        num_1 = int(entry_1.get())
        num_2 = int(entry_2.get())
        add_result = num_1.__add__(num_2)
        result_label.config(text=f"Result: {add_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

add_button = tk.Button(root, text="Addition", command=add_button_click, font=("Times New Roman", 18),  bg="lightyellow")
add_button.place(x=400, y=100)

#Create a subtraction function
def sub_button_click():
    try:
        num_1 = int(entry_1.get())
        num_2 = int(entry_2.get())
        sub_result = num_1.__sub__(num_2)
        result_label.config(text=f"Result: {sub_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

sub_button = tk.Button(root, text="Subtraction", command=sub_button_click, font=("Times New Roman", 18),  bg="lightyellow")
sub_button.place(x=525, y=100)

# Create a multiplication function
def mult_button_click():
    try:
        num_1 = int(entry_1.get())
        num_2 = int(entry_2.get())
        mult_result = num_1.__mul__(num_2)
        result_label.config(text=f"Result: {mult_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

mult_button = tk.Button(root, text="Multiplication", command=mult_button_click, font=("Times New Roman", 18),  bg="lightyellow")
mult_button.place(x=670, y=100)

# Create a division function
def div_button_click():
    try:
        num_1 = int(entry_1.get())
        num_2 = int(entry_2.get())
        div_result = num_1.__truediv__(num_2)
        result_label.config(text=f"Result: {div_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number and does not sivision by 0!", bg="#FFC0CB")

div_button = tk.Button(root, text="Division", command=div_button_click, font=("Times New Roman", 18),  bg="lightyellow")
div_button.place(x=840, y=100)

# Create a factorial function
def fact_button_click():
    try:
        num_1 = int(entry_1.get())
        if num_1 < 0:
            result_label.config(text="Факторіал тільки для невід’ємних чисел!", bg="#FFC0CB")
            return
        fact_result = fact(num_1)
        result_label.config(text=f"Result: {fact_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!",bg="#FFC0CB")
    except OverflowError:
        result_label.config(text="Number is too large for factorial!", bg="#FFC0CB")


fact_button = tk.Button(root, text="Factorial", command=fact_button_click, font=("Times New Roman", 18),  bg="lightyellow")
fact_button.place(x=400, y=200)

# Create a function for calculating the square root
def sqr_button_click():
    try:
        num_1 = int(entry_1.get())
        if num_1 < 0:
            result_label.config(text="You cannot calculate the square root of a negative number", bg="#FFC0CB")
            return
        sqr_result = sqr(num_1)
        result_label.config(text=f"Result: {sqr_result}", bg="#FFF8BC")
    except ValueError:
         result_label.config(text="Print number!",bg="#FFC0CB")

sqr_button = tk.Button(root, text="Square root", command=sqr_button_click, font=("Times New Roman", 18),  bg="lightyellow")
sqr_button.place(x=525, y=200)

# Create a function for logarithm
def log_button_click():
    try:
        num_1 = int(entry_1.get())
        num_2 = int(entry_2.get())
        if num_1 < 1:
            result_label.config(text="Basic of logarithm can`t be less than 1!", bg="#FFC0CB")
        elif num_2 < 0:
            result_label.config(text="Number of logarithm can`t be less than 0!", bg="#FFC0CB")
            return
        log_result = logar(num_1, num_2)
        result_label.config(text=f"Result: {log_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!",bg="#FFC0CB")

log_button = tk.Button(root, text="Logarithm", command=log_button_click, font=("Times New Roman", 18),  bg="lightyellow")
log_button.place(x=670, y=200)

#Create a function for a exponentiation
def exp_button_click():
    try:
        num_1 = int(entry_1.get())
        num_2 = int(entry_2.get())
        exp_result = num_1.__pow__(num_2)
        result_label.config(text=f"Result: {exp_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!",bg="#FFC0CB")

exp_button = tk.Button(root, text="Exponentiation", command=exp_button_click, font=("Times New Roman", 18),  bg="lightyellow")
exp_button.place(x=800, y=200)

# Create a function to convert radians to degrees
def rad_button_click():
    try:
        num_1 = int(entry_1.get())
        rad_result = rad(num_1)
        result_label.config(text=f"Result: {rad_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!",bg="#FFC0CB")

rad_button = tk.Button(root, text="Degrees in radians", command=rad_button_click, font=("Times New Roman", 18),  bg="lightyellow")
rad_button.place(x=400, y=300)

#Create a cosine function
def cos_button_click():
    try:
        num_1 = float(entry_1.get())
        rad = math.radians(num_1)
        cos_result = math.cos(rad)
        result_label.config(text=f"Result: {cos_result}", bg="#8AF1AD")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")


cos_button = tk.Button(root, text="Cosine", command=cos_button_click, font=("Times New Roman", 18),  bg="#A5FDC2")
cos_button.place(x=610, y=300)

# Create a sine function
def sin_button_click():
    try:
        num_1 = float(entry_1.get())
        rad = math.radians(num_1)
        sin_result = math.sin(rad)
        result_label.config(text=f"Result: {sin_result}", bg="#8AF1AD")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

sin_button = tk.Button(root, text="Sine", command=sin_button_click, font=("Times New Roman", 18),  bg="#A5FDC2")
sin_button.place(x=711, y=300)

#Create a tangens function:
def tang_button_click():
    try:
        num_1 = int(entry_1.get())
        rad = math.radians(num_1)
        tang_result = math.sin(rad)
        result_label.config(text=f"Result: {tang_result}", bg="#8AF1AD")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

tang_button = tk.Button(root, text="Tangens", command=tang_button_click, font=("Times New Roman", 18),  bg="#A5FDC2")
tang_button.place(x=787, y=300)

#Create a arccosine funtion:
def arccos_button_click():
    try:
        num_1 = int(entry_1.get())
        rad = math.radians(num_1)
        arccos_result = math.acos(rad)
        result_label.config(text=f"Result: {arccos_result}", bg="#8AF1AD")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

arccos_button = tk.Button(root, text="Arccosine", command=arccos_button_click, font=("Times New Roman", 18),  bg="#A5FDC2")
arccos_button.place(x=400, y=400)

root.mainloop()