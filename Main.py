import tkinter as tk

root = tk.Tk()
root.title("Software-window")
root.geometry("1000x1000")

task0_name = ""
task1_name = ""
task2_name = ""
task3_name = ""
task4_name = ""
task5_name = ""

tasks_status = [0, 0, 0, 0, 0]

def open_tasks():
    new_window = tk.Toplevel(root)
    new_window.title("Tasks")
    new_window.geometry("1800x800")

    label = tk.Label(new_window, text="Tasks")
    label.pack(pady=20)

    canvas = tk.Canvas(new_window, width=1800, height=800, bg="white")
    canvas.pack()

    # Create a rectangle on the canvas
    taskboxes = [
        canvas.create_rectangle(50, 50, 300, 500, fill="white", outline="black"),
        canvas.create_rectangle(350, 50, 600, 500, fill="white", outline="black"),
        canvas.create_rectangle(650, 50, 900, 500, fill="white", outline="black"),
        canvas.create_rectangle(950, 50, 1200, 500, fill="white", outline="black"),
        canvas.create_rectangle(1250, 50, 1500, 500, fill="white", outline="black")
    ]

    task_texts = [
        canvas.create_text(175, 90, text="", fill="black"),
        canvas.create_text(475, 90, text="", fill="black"),
        canvas.create_text(775, 90, text="", fill="black"),
        canvas.create_text(1075, 90, text="", fill="black"),
        canvas.create_text(1375, 90, text="", fill="black")
    ]

    def update_task_boxes():
        for i, status in enumerate(tasks_status):
            if status == 0:
                canvas.itemconfig(task_texts[i], text="empty")
            else:
                canvas.itemconfig(task_texts[i], text="task name")

    update_task_boxes()

    new_button = tk.Button(new_window, text="New Button", command=lambda: print("New button clicked!"))
    new_button.pack(pady=20)

def open_new_task():
    new_window = tk.Toplevel(root)
    new_window.title("New Task")
    new_window.geometry("400x500")

    label = tk.Label(new_window, text="Enter Task Name")
    label.pack(pady=20)

    new_task_title = tk.StringVar()
    entry = tk.Entry(new_window, textvariable=new_task_title, width=30)
    entry.pack(pady=20)

    label_description = tk.Label(new_window, text="Enter Description")
    label_description.pack(pady=40)
    
    new_task_description = tk.StringVar()
    entry2 = tk.Entry(new_window, textvariable=new_task_description, width=30)
    entry2.pack(pady=20)

    def get_input():
        user_input = new_task_title.get()
        user_input2 = new_task_description.get()
        print("User input:", user_input, user_input2)
        # Update the task status (for demonstration purposes, we'll just update the first available spot)
        for i in range(len(tasks_status)):
            if tasks_status[i] == 0:
                tasks_status[i] = 1  # Mark the task as occupied
                break

    button = tk.Button(new_window, text="Create Task", command=get_input)
    button.pack(pady=20)

def on_task_clicked():
    open_tasks()

def on_new_task_clicked():
    open_new_task()

canvas = tk.Canvas(root, width=1000, height=1000)
rectangle = canvas.create_rectangle(0, 0, 150, 1000, fill="white", outline="black")
canvas.pack()

task_button = tk.Button(root, text="Tasks", width=20, command=on_task_clicked)
task_button.pack()
task_button.place(x=0, y=0)

new_task_button = tk.Button(root, text="Create New Task", width=20, command=on_new_task_clicked)
new_task_button.pack()
new_task_button.place(x=0, y=25)

login_button = tk.Button(root, text="Login", width=20, command=on_new_task_clicked)
login_button.pack()
login_button.place(x=0, y=50)

root.mainloop()
