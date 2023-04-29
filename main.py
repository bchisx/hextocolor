import tkinter as tk

window = tk.Tk()
window.title("Hex Color App")

label = tk.Label(window, text="Enter a hex value (e.g. #FF0000) and press Enter:")
label.pack()

entry = tk.Entry(window)
entry.pack()

def change_color(event):
    hex_value = entry.get()
    if len(hex_value) == 7 and hex_value[0] == "#":
        try:
            int(hex_value[1:], 16)
            window.config(bg=hex_value)
        except ValueError:
            label.config(text="Invalid hex value. Please try again.")
    else:
            label.config(text="Invalid hex value. Please try again.")

entry.bind("<Return>", change_color)

window.mainloop()
