import tkinter as tk

# =========================
# TASK LIST
# =========================

tasks = []


# =========================
# FUNCTIONS
# =========================

# Add Task
def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)


# Delete Task
def delete_task():
    selected = task_list.curselection()

    if selected:
        number = selected[0]

        deleted = tasks.pop(number)
        task_list.delete(number)

        status_label.config(text=deleted + " was deleted!")


# View Tasks
def view_tasks():
    task_list.delete(0, tk.END)

    if len(tasks) == 0:
        status_label.config(text="No tasks yet.")
    else:
        for i in range(len(tasks)):
            task_list.insert(
                tk.END,
                str(i + 1) + ". " + tasks[i]
            )

        status_label.config(
            text="Showing your tasks."
        )


# Exit
def exit_app():
    app.destroy()


# =========================
# CREATE THE APP
# =========================

app = tk.Tk()

app.title("TO DO LIST")
app.geometry("500x600")


# =========================
# TITLE
# =========================

label = tk.Label(
    app,
    text="WELCOME! YOU CAN ADD YOUR TASK!",
    font=("Arial", 14, "bold")
)

label.pack(pady=15)


# =========================
# TASK ENTRY
# =========================

task_entry = tk.Entry(
    app,
    width=35,
    font=("Arial", 14)
)

task_entry.pack(pady=10)


# =========================
# BUTTONS
# =========================

add_button = tk.Button(
    app,
    text="Add Task",
    command=add_task,
    width=15
)

add_button.pack(pady=5)


view_button = tk.Button(
    app,
    text="View Tasks",
    command=view_tasks,
    width=15
)

view_button.pack(pady=5)


delete_button = tk.Button(
    app,
    text="Delete Task",
    command=delete_task,
    width=15
)

delete_button.pack(pady=5)


# =========================
# TASK LIST
# =========================

task_list = tk.Listbox(
    app,
    width=40,
    height=15,
    font=("Arial", 13)
)

task_list.pack(pady=15)


# =========================
# STATUS MESSAGE
# =========================

status_label = tk.Label(
    app,
    text="",
    font=("Arial", 10)
)

status_label.pack(pady=5)


# =========================
# EXIT BUTTON
# =========================

exit_button = tk.Button(
    app,
    text="Exit",
    command=exit_app,
    width=15
)

exit_button.pack(pady=10)


# =========================
# RUN THE APP
# =========================

app.mainloop()
