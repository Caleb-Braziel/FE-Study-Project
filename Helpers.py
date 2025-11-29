import tkinter as tk


def label_maker(question, frame):
    label = tk.Label(frame, bg = "white", text = question, font=("Arial", 10), wraplength=1100)
    label.pack()
    #pdf_list.append((label, "L")) # L for label


def table_maker(table, root):    
    
    table_frame = tk.Frame(root)
    table_frame.pack()   
    
    for idx, row in enumerate(table):
        for j, val in enumerate(row):
            label = tk.Label(table_frame, text = val, borderwidth=1, relief="solid", width=30)
            label.grid(row=idx, column=j, padx=2, pady=2)
    
    #pdf_list.append((table, "T")) # T for table      
    
def entry_maker(frame, answer): # MAYBE MAKE A SEPERATE FRAME TO REMOVE IT WHEN A NEW ANSWER IS TYPED
    entry = tk.Entry(frame, width=50)
    entry.pack(pady=5)
    
    def submit():
        user_answer =entry.get()
        entry.delete(0, tk.END)
        
        if user_answer == "":
            return
        elif user_answer.isdigit() or is_float(user_answer):
            if float(user_answer) < answer + (0.005 * answer) and float(user_answer) > answer - (0.005 * answer):
                correct(frame)
            else:
                incorrect(frame, answer)
        else:
            incorrect(frame, answer) # HANDLE NON-NUMERIC ANSWERS LATER      
    
    button = tk.Button(frame, text="Submit", command=submit)
    button.pack()
    
    
    return button.invoke()  # Waits for button press and returns the entry value as an integer

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def correct(frame):
    label = tk.Label(frame, text="Correct!", fg="green", font=("Arial", 24, "bold"), width = 200)
    label.pack()
    
def incorrect(frame, answer):    
    label = tk.Label(frame, text="Incorrect! The correct answer is " + str(answer), fg="red", font=("Arial", 12, "bold"), width = 200)
    label.pack()

def spacer(frame):
    label_maker("", frame)
    label_maker("", frame)

def frame_clear(frame):
    for widget in frame.winfo_children():
        widget.destroy()   
        