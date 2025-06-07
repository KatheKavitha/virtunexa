import tkinter as tk
from assistant import handle_command

def on_submit():
    command = entry.get()
    response = handle_command(command)
    result_label.config(text=response)

root = tk.Tk()
root.title("Virtual Assistant")

entry = tk.Entry(root, width=40)
entry.pack()

submit_btn = tk.Button(root, text="Submit", command=on_submit)
submit_btn.pack()

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack()

root.mainloop()