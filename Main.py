import tkinter as tk
from tkinter import *




def open_tasks():
    #tasks winddow
    new_window = tk.Toplevel(root)
    new_window.title("Tasks")
    new_window.geometry("600x600")
    

    label = tk.Label(new_window, text="Tasks")
    label.pack(pady=20)
    

    new_button = tk.Button(new_window, text="New Button", command=lambda: print("New button clicked!"))
    new_button.pack(pady=20)



def on_button_clicked():
    open_tasks()

# Create the main window
root = tk.Tk()
root.title("Software-window")
root.geometry("1000x1000")





# Canvas widget -- rectangle is the navigation bar 
canvas = tk.Canvas(root, width=1000, height=1000)
rectangle = canvas.create_rectangle(0, 0, 150, 1000, fill="white", outline="black")
canvas.pack()

# all buttons for sidebar are defined here ->

# Tasks button 
task_button = tk.Button(root, text="Tasks",width=20, command=on_button_clicked)
task_button .pack()  # Corrected this line by adding parentheses
task_button .place(x=0,y=0)




root.mainloop()
