import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN = "#66aa66"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
FONT_NAME = "Inter"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    checkmarks.config(text="")
    top_label.config(text='')
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        top_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        top_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        top_label.config(text="Work", fg=DARK_GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(2, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=64, pady=32, bg=GREEN)

top_label = tkinter.Label(text="", font=(FONT_NAME, 40, 'bold'), bg=GREEN)
top_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=240, height=240, bg=GREEN, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(120, 120, image=tomato_image)
timer_text = canvas.create_text(120, 145, text=f"", font=(FONT_NAME, 32, 'bold'))


btn_start = tkinter.Button(text="Start", command=start_timer)
btn_start.config(highlightbackground=GREEN)
btn_start.grid(column=0, row=2)

btn_reset = tkinter.Button(text="Reset")
btn_reset.config(highlightbackground=GREEN, command=reset_timer)
btn_reset.grid(column=3, row=2)

checkmarks = tkinter.Label(text="", font=(FONT_NAME, 24, 'bold'), bg=GREEN)
checkmarks.grid(column=1, row=3)

canvas.grid(column=1, row=1)


window.mainloop()
