#Import moduls:
import tkinter as tk
import math
from operation import fact
from operation import sqr
from operation import logar
from operation import rad
from operation import cosin
from operation import sin
from operation import tangens

#Create a window. Add some color, font, etc.:
root = tk.Tk()
root.title("Calculator")
root.configure(bg="lightyellow")
root.geometry("1000x800")

#Clear button:
def clear_button_click():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    result_label.config(text="")

clear_button = tk.Button(root, text="Clear", command=clear_button_click,
                         font=("Times New Roman", 18), bg="#FFFFFF")
clear_button.place(x=100, y=350)


# Fields for entering numbers:
entry_1 = tk.Entry(root, font=("Times New Roman", 20))
entry_1.place(x=65, y=100)
entry_2 = tk.Entry(root, font=("Times New Roman", 20))
entry_2.place(x=65, y=200)

# A label for the result:
result_label = tk.Label(root, text="", font=("Times New Roman", 20), bg="lightyellow")
result_label.place(x=50, y=300)

# Create function for addition:
def add_button_click():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())
        add_result = num_1.__add__(num_2)
        result_label.config(text=f"Result: {add_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

# Create button for addition:
add_button = tk.Button(root, text="Addition", command=add_button_click, font=("Times New Roman", 18),  bg="#F8B78F")
add_button.place(x=400, y=100)

# Create a subtraction function:
def sub_button_click():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())
        sub_result = num_1.__sub__(num_2)
        result_label.config(text=f"Result: {sub_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

# Create a subtraction button:
sub_button = tk.Button(root, text="Subtraction", command=sub_button_click, font=("Times New Roman", 18),  bg="#F8B78F")
sub_button.place(x=525, y=100)

# Create a multiplication function:
def mult_button_click():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())
        mult_result = num_1 * num_2

        if abs(mult_result) >= 1e8:
            formatted_result = f"{mult_result:.3e}"
        else:
            formatted_result = str(mult_result)

        result_label.config(text=f"Result: {formatted_result}", bg="#FFF8BC")

    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

# Create a multiplication button:
mult_button = tk.Button(root, text="Multiplication", command=mult_button_click, font=("Times New Roman", 18),  bg="#F8B78F")
mult_button.place(x=670, y=100)

# Create a division function:
def div_button_click():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())
        div_result = num_1.__truediv__(num_2)
        result_label.config(text=f"Result: {div_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Enter number and do not divide by 0!", bg="#FFC0CB")

# Create a division button:
div_button = tk.Button(root, text="Division", command=div_button_click, font=("Times New Roman", 18),  bg="#F8B78F")
div_button.place(x=840, y=100)

# Create a factorial function:
def fact_button_click():
    try:
        num_1 = float(entry_1.get())
        if num_1 < 0:
            result_label.config(text="Factorial only for non-negative numbers!", bg="#FFC0CB")
            return
        if num_1 > 500:
            result_label.config(text="Too big a number for a factorial!", bg="#FFC0CB")
            return

        fact_result = math.factorial(num_1)

        if fact_result >= 1e8:
            formatted_result = f"{fact_result:.3e}"
        else:
            formatted_result = str(fact_result)

        result_label.config(text=f"Result: {formatted_result}", bg="#FFF8BC")

    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")


# Create a factorial button:
fact_button = tk.Button(root, text="Factorial", command=fact_button_click, font=("Times New Roman", 18),  bg="#F8B78F")
fact_button.place(x=400, y=200)

# Create a function for calculating the square root:
def sqr_button_click():
    try:
        num_1 = float(entry_1.get())
        if num_1 < 0:
            result_label.config(text="You cannot calculate the square root of a negative number", bg="#FFC0CB")
            return
        sqr_result = sqr(num_1)
        result_label.config(text=f"Result: {sqr_result}", bg="#FFF8BC")
    except ValueError:
         result_label.config(text="Print number!",bg="#FFC0CB")

# Create a button for calculating the square root:
sqr_button = tk.Button(root, text="Square root", command=sqr_button_click, font=("Times New Roman", 18),  bg="#F8B78F")
sqr_button.place(x=525, y=200)

# Create a function for logarithm:
def log_button_click():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())
        if num_1 < 1:
            result_label.config(text="Basic of logarithm can`t be less than 1!", bg="#FFC0CB")
        elif num_2 < 0:
            result_label.config(text="Number of logarithm can`t be less than 0!", bg="#FFC0CB")
            return
        log_result = logar(num_1, num_2)
        result_label.config(text=f"Result: {log_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!",bg="#FFC0CB")

# Create a button for logarithm:
log_button = tk.Button(root, text="Logarithm", command=log_button_click, font=("Times New Roman", 18),  bg="#F8B78F")
log_button.place(x=670, y=200)

# Create a function for a exponentiation:
def exp_button_click():
    try:
        num_1 = float(entry_1.get())
        num_2 = float(entry_2.get())

        if abs(num_1) > 1_000 or abs(num_2) > 500:
            result_label.config(text="Числа занадто великі!", bg="#FFC0CB")
            return

        exp_result = num_1 ** num_2

        if abs(exp_result) >= 1e8:
            formatted_result = f"{exp_result:.3e}"
        else:
            formatted_result = str(exp_result)

        result_label.config(text=f"Result: {formatted_result}", bg="#FFF8BC")

    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")
    except OverflowError:
        result_label.config(text="Result is too large!", bg="#FFC0CB")

# Create a button for a exponentiation:
exp_button = tk.Button(root, text="Exponentiation", command=exp_button_click, font=("Times New Roman", 18),  bg="#F8B78F")
exp_button.place(x=800, y=200)

# Create a function to convert radians to degrees:
def rad_button_click():
    try:
        num_1 = float(entry_1.get())
        rad_result = rad(num_1)
        result_label.config(text=f"Result: {rad_result}", bg="#FFF8BC")
    except ValueError:
        result_label.config(text="Print number!",bg="#FFC0CB")

# Create a button to convert radians to degrees:
rad_button = tk.Button(root, text="Radians to degrees", command=rad_button_click, font=("Times New Roman", 18),  bg="#F8B78F")
rad_button.place(x=400, y=300)

#Create a cosine function:
def cos_button_click():
    try:
        num_1 = float(entry_1.get())
        rad = math.radians(num_1)
        cos_result = math.cos(rad)
        result_label.config(text=f"Result: {cos_result}", bg="#8AF1AD")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

#Create a cosine button:
cos_button = tk.Button(root, text="Cosine", command=cos_button_click, font=("Times New Roman", 18),  bg="#A5FDC2")
cos_button.place(x=610, y=300)

# Create a sine function:
def sin_button_click():
    try:
        num_1 = float(entry_1.get())
        rad = math.radians(num_1)
        sin_result = math.sin(rad)
        result_label.config(text=f"Result: {sin_result}", bg="#8AF1AD")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

# Create a sine button:
sin_button = tk.Button(root, text="Sine", command=sin_button_click, font=("Times New Roman", 18),  bg="#A5FDC2")
sin_button.place(x=711, y=300)

#Create a tangen function:
def tang_button_click():
    try:
        num_1 = float(entry_1.get())
        rad = math.radians(num_1)
        tang_result = math.sin(rad)
        result_label.config(text=f"Result: {tang_result}", bg="#8AF1AD")
    except ValueError:
        result_label.config(text="Print number!", bg="#FFC0CB")

#Create a tangen button:
tang_button = tk.Button(root, text="Tangen", command=tang_button_click, font=("Times New Roman", 18),  bg="#A5FDC2")
tang_button.place(x=787, y=300)

#Create a arccosine funtion:
def arccos_button_click():
    try:
        num_1 = float(entry_1.get())
        if -1 <= num_1 <= 1:
            arccos_result = math.degrees(math.acos(num_1))
            result_label.config(text=f"Result: {arccos_result:.2f}°", bg="#8AF1AD")
        else:
            result_label.config(text="Input must be between -1 and 1!", bg="#FFC0CB")
    except ValueError:
        result_label.config(text="Print a valid number!", bg="#FFC0CB")

#Create a arccosine button:
arccos_button = tk.Button(root, text="Arccosine", command=arccos_button_click, font=("Times New Roman", 18),  bg="#9C9DF4")
arccos_button.place(x=400, y=400)

# Create a arcsin function:
def arcsin_button_click():
    try:
        num_1 = float(entry_1.get())
        if -1 <= num_1 <= 1:
            arcsin_result = math.degrees(math.asin(num_1))
            result_label.config(text=f"Result: {arcsin_result:.2f}°", bg="#8AF1AD")
        else:
            result_label.config(text="Input must be between -1 and 1!", bg="#FFC0CB")
    except ValueError:
        result_label.config(text="Print a valid number!", bg="#FFC0CB")

# Create a arcsin button:
arcsin_button = tk.Button(root, text="Arcsine", command=arcsin_button_click, font=("Times New Roman", 18),  bg="#9C9DF4")
arcsin_button.place(x=525, y=400)

# Create a acrtangent function:
def arctg_button_click():
    try:
        num_1 = float(entry_1.get())
        arctg_result = math.degrees(math.atan(num_1))
        result_label.config(text=f"Result: {arctg_result:.2f}°", bg="#8AF1AD")
    except ValueError:
        result_label.config(text="Print a valid number!", bg="#FFC0CB")

# Create a acrtanhens button:
arctg_button = tk.Button(root, text="Artangent", command=arctg_button_click, font=("Times New Roman", 18),  bg="#9C9DF4")
arctg_button.place(x=630, y=400)

root.mainloop()



