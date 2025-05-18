import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.title("Unit Converter")
window.geometry("500x500")

label = tk.Label(window, text="value", font=("Arial", 20))
label.pack(pady=10)
entry_value = tk.Entry(window, font=("Arial", 20))
entry_value.pack(pady=10)

label_from_unit = tk.Label(window, text="convert from", font=("Arial", 20))
label_from_unit.pack(pady=10)
unit_from_to_var = tk.StringVar()
combo_from = ttk.Combobox(window, textvariable=unit_from_to_var, font=("Helvetica", 10))
combo_from['values'] = ["cm to m", "m to cm", "inches to cm", "cm to inches", "inches to feet", "feet to inches"]
combo_from.pack(pady=10)


def convert(value, from_to_unit):
    from_to_unit
    try:
        value = float(value)
        if from_to_unit == "cm to m":
            converted_value = value / 100
        elif from_to_unit == "m to cm":
            converted_value = value * 100
        elif from_to_unit == "inches to cm":
            converted_value = value * 2.54
        elif from_to_unit == "cm to inches":
            converted_value = value / 2.54
        elif from_to_unit == "inches to feet":
            converted_value = value / 12
        elif from_to_unit == "feet to inches":
            converted_value = value * 12
        else:
            messagebox.showerror("Error", "Invalid conversion!")
            return
        messagebox.showinfo("Converted Value", f"{value} {from_to_unit.split()[0]} = {converted_value} {from_to_unit.split()[2]}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a number.")

button_convert = tk.Button(window, text="Convert", font=("Arial", 20), command=lambda: convert(entry_value.get(), unit_from_to_var.get()))
button_convert.pack(pady=10)

window.mainloop()