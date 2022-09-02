import tkinter as tk

window = tk.Tk()
window.title("Kilometers to Miles Converter")
window.minsize(width=320, height=160)
window.config(padx=40, pady=40)

user_input = tk.Entry(width=10)
user_input.grid(column=1, row=0)

miles = tk.Label(text="Miles", font=("Arial", 16))
miles.grid(column=2, row=0)

meta_label = tk.Label(text="is equal to", font=("Arial", 16))
meta_label.grid(column=0, row=1)

result_label = tk.Label(text="?", font=("Arial", 16))
result_label.grid(column=1, row=1)
result_label['text'] = 0

km_label = tk.Label(text="Km", font=("Arial", 16))
km_label.grid(column=2, row=1)


def button_got_clicked():
    ui = float(user_input.get())
    new_result = ui * 1.609344
    result_label['text'] = round(new_result, 2)


button = tk.Button(text='Calculate', command=button_got_clicked)
button.grid(column=1, row=2)

window.mainloop()
