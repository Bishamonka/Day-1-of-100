import random
import tkinter as tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# —————————————————————————————————————————— PANDAS —————————————————————————————————————————— #

try:
    data = pd.read_csv("data/words_to_learn.csv")
    words_to_learn = data.to_dict(orient='records')
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    words_to_learn = data.to_dict(orient='records')
else:
    print(f"Data file successfully loaded!")
# —————————————————————————————————————————— NEXT CARD —————————————————————————————————————————— #

current_card = []


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(canvas_card_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="#555555")
    canvas.itemconfig(card_word, text=current_card["French"], fill="#222222")
    print(f"Words left: {len(words_to_learn)}")
    flip_timer = window.after(3000, func=card_flip)


def delete_word_and_next_card():
    words_to_learn.remove(current_card)
    df = pd.DataFrame(words_to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def card_flip():
    canvas.itemconfig(card_title, text="English", fill="#ffffff")
    canvas.itemconfig(card_word, text=current_card["English"], fill="#ffffff")
    canvas.itemconfig(canvas_card_image, image=card_back)


# —————————————————————————————————————————— UI SETUP —————————————————————————————————————————— #


window = tk.Tk()
window.title("Flash Card App")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)

card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
check_icon = tk.PhotoImage(file="images/right.png")
cross_icon = tk.PhotoImage(file="images/wrong.png")

canvas = tk.Canvas(width=800, height=560, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
canvas_card_image = canvas.create_image(400, 280, image=card_front)
card_title = canvas.create_text(400, 150, text="...", fill="#555555", font=("Arial", 32, 'italic'))
card_word = canvas.create_text(400, 280, text="...", fill="#222222", font=("Arial", 64, 'bold'))
canvas.grid(column=0, columnspan=2, row=0)

btn_cross = tk.Button(image=cross_icon, highlightthickness=0, borderwidth=0, command=next_card)
btn_cross.grid(column=0, row=1)
btn_check = tk.Button(image=check_icon, highlightthickness=0, borderwidth=0, command=delete_word_and_next_card)
btn_check.grid(column=1, row=1)

next_card()

window.mainloop()
