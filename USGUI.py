import tkinter as tk
import tkinter.font as font


def convert_base():
    number = number_entry.get()
    from_base = from_base_var.get()
    to_base = to_base_var.get()

    if from_base == "binary":
        if to_base == "decimal":
            result = int(number, 2)
        elif to_base == "octal":
            result = oct(int(number, 2))[2:]
        elif to_base == "hexadecimal":
            result = hex(int(number, 2))[2:]
        elif to_base == "ascii":
            result = "hanya bisa dari string"
        else:
            result = number
    elif from_base == "decimal":
        if to_base == "binary":
            result = bin(int(number))[2:]
        elif to_base == "octal":
            result = oct(int(number))[2:]
        elif to_base == "hexadecimal":
            result = hex(int(number))[2:]
        elif to_base == "ascii":
            result = "hanya bisa dari string"
        else:
            result = number
    elif from_base == "octal":
        if to_base == "binary":
            result = bin(int(number, 8))[2:]
        elif to_base == "decimal":
            result = int(number, 8)
        elif to_base == "hexadecimal":
            result = hex(int(number, 8))[2:]
        elif to_base == "ascii":
            result = "hanya bisa dari string"
        else:
            result = number
    elif from_base == "hexadecimal":
        if to_base == "binary":
            result = bin(int(number, 16))[2:]
        elif to_base == "decimal":
            result = int(number, 16)
        elif to_base == "octal":
            result = oct(int(number, 16))[2:]
        elif to_base == "ascii":
            result = "hanya bisa dari string"
        else:
            result = number
    elif from_base == "string":
        if to_base == "ascii":
            result = ''.join(str(ord(c)) for c in number)
        else:
            result = number
    else:
        result = number

    result_label.configure(text=result)


root = tk.Tk()
root.title("Melvin Converter")
root.configure(bg="#121212")  # Set background color

# Set custom font
myFont = font.Font(family='Helvetica', size=12, weight='bold')

number_label = tk.Label(root, text="Masukan String/Number:",
                        fg="white", bg="#121212", font=myFont, padx=10, pady=10)
number_label.pack()

number_entry = tk.Entry(root, font=myFont)
number_entry.pack()

from_base_label = tk.Label(root, text="Dari Basis:",
                           fg="white", bg="#121212", font=myFont, padx=10, pady=10)
from_base_label.pack()

from_base_var = tk.StringVar(root)
from_base_var.set("binary")
from_base_menu = tk.OptionMenu(
    root, from_base_var, "binary", "decimal", "octal", "hexadecimal", "string")
from_base_menu.config(font=myFont)
from_base_menu.pack()

to_base_label = tk.Label(root, text="Ke Basis:", fg="white",
                         bg="#121212", font=myFont, padx=10, pady=10)
to_base_label.pack()

to_base_var = tk.StringVar(root)
to_base_var.set("decimal")
to_base_menu = tk.OptionMenu(
    root, to_base_var, "binary", "decimal", "octal", "hexadecimal", "ascii")
to_base_menu.config(font=myFont)
to_base_menu.pack()

convert_button = tk.Button(
    root, text="Convert", bg="#c2c2c2", font=myFont, command=convert_base)
convert_button.pack(padx=10, pady=10)

result_label = tk.Label(root, text="", bg="#121212",
                        fg="white", font=myFont, padx=10, pady=10)
result_label.pack()

root.mainloop()
