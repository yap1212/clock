import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Update every second

root = tk.Tk()
root.title("Digital Clock")

time_label = tk.Label(root, font=('Helvetica', 48), fg='blue')
time_label.pack()

update_time()  # Start the clock update loop
root.mainloop()
