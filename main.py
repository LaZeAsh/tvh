import tkinter as tk

def submit_prompt():
    prompt = prompt_entry.get()
    print("Prompt:", prompt)

root = tk.Tk()

prompt_label = tk.Label(root, text="Enter a text prompt:")
prompt_label.pack()

prompt_entry = tk.Entry(root)
prompt_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_prompt)
submit_button.pack()

root.mainloop()
