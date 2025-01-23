import tkinter as tk
from tkinter import simpledialog, scrolledtext
import CHATBOT


root = tk.Tk()
root.title("Chatbot")


root.geometry("500x500")


history_text = scrolledtext.ScrolledText(root, state='disabled', height=30, width=40)
history_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


def send():
    user_input = user_input_entry.get()
    if user_input:
        
        history_text.config(state='normal')
        history_text.insert(tk.END, "User: " + user_input + "\n")
        history_text.config(state='disabled')
        
       
        response = CHATBOT.get_GPT_response(user_input)
        history_text.config(state='normal')
        history_text.insert(tk.END, "GPT: " + response + "\n")
        history_text.config(state='disabled')
        
        
        user_input_entry.delete(0, tk.END)


user_input_entry = tk.Entry(root, width=52)
user_input_entry.grid(row=1, column=0, pady=10)


send_button = tk.Button(root, text="Ask GPT", command=send)
send_button.grid(row=1, column=1)


root.mainloop()
