from tkinter import *
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 35
reps=0
runs=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps,runs
    global ticks
    button_start.config(state=NORMAL)
    window.after_cancel(timer)
    label.config(text='Timer',fg=GREEN)
    ticks=''
    reps=0
    runs=0
    chk_mark_label.config(text=ticks)
    canvas.itemconfig(time_text,text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps,runs
    global ticks
    button_start.config(state=DISABLED)
    reps+=1
    if reps<8:
        winsound.Beep(500, 500)
        if reps%2!=0:
            label.config(text='WORK HARD!',fg=RED)
            label2.config(text=f'Runs Ongoing={runs+1}')
            count_down(int(WORK_MIN*60))
        else:
            ticks+='✔\n'
            chk_mark_label.config(text=ticks)
            label.config(text='Small break!',fg=PINK)
            label2.config(text=f'Runs Ongoing={runs + 1}')
            count_down(int(SHORT_BREAK_MIN*60))
    else:
        label.config(text='Long Break!',fg=GREEN)
        label2.config(text=f'Runs Ongoing={runs + 1}')
        winsound.Beep(1000,500)
        count_down(int(LONG_BREAK_MIN*60))
        ticks = ''
        reps = 0
        chk_mark_label.config(text=ticks)
        runs+=1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(t):
    global timer
    t_in_min=t//60
    if t_in_min<=9:
        tm_text=f"0{t_in_min}"
    else:
        tm_text=t_in_min
    t_in_sec=t%60
    if t_in_sec<=9:
        ts_text=f"0{t_in_sec}"
    else:
        ts_text=t_in_sec
    canvas.itemconfig(time_text,text=f"{tm_text}:{ts_text}")
    if t>0:
       timer=window.after(1000,count_down,t-1)
    else:
        start_timer()

def just_a_min(t_in_sec=60):
    if t_in_sec<=9:
        ts_text=f"0{t_in_sec}"
    else:
        ts_text=t_in_sec
    canvas.itemconfig(time_text,text=f"00:{ts_text}")
    if t_in_sec>0:
        timer=window.after(1000,just_a_min,t_in_sec-1)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Pomodoro')
window.config(bg=YELLOW,padx=100,pady=50)
for i in range(3):
    window.columnconfigure(i)
for j in range(4):
    if j>=2:
        window.rowconfigure(j,weight=3)
    else:
        window.rowconfigure(j)
ticks=''
label=Label(window,text='Timer',fg=GREEN,font=(FONT_NAME,40,'italic'),bg=YELLOW)
label2=Label(window,text='',font=(FONT_NAME,20,'bold italic'),fg='#0998E6',bg=YELLOW)
button_start=Button(window,text='Start',command=start_timer)
button_reset=Button(window,text='Reset',command=reset_timer)
canvas=Canvas(window,highlightthickness=0,bg=YELLOW,width=200,height=226)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
time_text=canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
chk_mark_label=Label(text=ticks,fg='green',font=(FONT_NAME,15),bg=YELLOW)
canvas.grid(column=1,row=2)
button_start.grid(column=0,row=3)
button_reset.grid(column=2,row=3)
label.grid(column=1,row=0)
label2.grid(column=1,row=1)
chk_mark_label.grid(column=1,row=4)
window.mainloop()