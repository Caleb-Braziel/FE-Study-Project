import tkinter as tk
from tkinter import ttk
from Question_Sheet_Maker import pdf_list, save_pdf
from Engr_Econ import buttons as econ_btns
from Heat_Transfer import buttons as ht_btns
from Helpers import frame_clear


########################### Global Variables #########################

BTN_PAD = 12 # padding for buttons 
BTN_WIDTH = 25 # width for buttons
CLEAR = False


######################### Basic Frames ##########################

root = tk.Tk()
root.geometry("1600x900")
root.title("FE Adlibs Worksheet Maker")

bottom_frame = tk.Frame(root, bg = "gray", padx = 300, pady = 20)
bottom_frame.pack(side = "bottom", fill = "x")

left_frame = tk.Frame(root, bg = "gray", padx = 20, pady = 20)
left_frame.pack(side = "left", fill = "y")

outer_frame = tk.Frame(root, bg = "lightgray", padx = 20, pady = 20)
outer_frame.pack(side="right", expand=True, fill="both", padx = 10, pady = 10)


############################# Scrollbar Functionality ##############################

canvas = tk.Canvas(outer_frame)
scrollbar = ttk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

frame = tk.Frame(canvas, bg="white", padx=10, pady=20)
scrolled_window = canvas.create_window((0, 0), window=frame, anchor="nw")

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfig(scrolled_window, width=canvas.winfo_width())
    
frame.bind("<Configure>", on_configure)     


################################ Buttons #######################################

def toggle():
    global CLEAR # Need to declare the variable as global to modify it
    
    if sheet_mode_btn.config('text')[-1] == "PDF Mode":
        sheet_mode_btn.config(text="Single Question", bg="red")
        CLEAR = True
        # Add a call to update on each click
    else:
        sheet_mode_btn.config(text="PDF Mode", bg="green")
        CLEAR = False
        # Add a call to update on each click


clear_btn = tk.Button(bottom_frame, text="Clear Screen", command=lambda: frame_clear(frame), width = 30)
clear_btn.pack(side="right", padx=10)

save_btn = tk.Button(bottom_frame, text="Save as PDF", command=lambda: save_pdf(), width = 30)
save_btn.pack(side="right", padx=10)

home_btn = tk.Button(bottom_frame, text="Home", command=lambda: home_buttons(), width = 30)
home_btn.pack(side="right", padx=10)

sheet_mode_btn = tk.Button(bottom_frame, text="PDF Mode", command=toggle, width= 30, bg="green")
sheet_mode_btn.pack(side= "right", padx=20)



def home_buttons():
    frame_clear(left_frame)
    
    math_btn = tk.Button(left_frame, text="Math", width = BTN_WIDTH, command=lambda: "")
    math_btn.pack(pady = BTN_PAD)

    stats_btn = tk.Button(left_frame, text="Probability and Statistics", width = BTN_WIDTH, command=lambda: "")
    stats_btn.pack(pady = BTN_PAD)

    econ_btn = tk.Button(left_frame, text="Economics", width = BTN_WIDTH, command=lambda: econ_btns(frame, left_frame, globals()["CLEAR"])) # globals() to access CLEAR variable
    econ_btn.pack(pady = BTN_PAD)

    electric_btn = tk.Button(left_frame, text="Electricity and Magnetism", width = BTN_WIDTH, command=lambda: "")
    electric_btn.pack(pady = BTN_PAD)

    statics_btn = tk.Button(left_frame, text="Statics", width = BTN_WIDTH, command=lambda: "")
    statics_btn.pack(pady = BTN_PAD)

    dynamics_btn = tk.Button(left_frame, text="Dynamics", width = BTN_WIDTH, command=lambda: "")
    dynamics_btn.pack(pady = BTN_PAD)

    Mech_O_Mats_btn = tk.Button(left_frame, text="Mechanics of Materials", width = BTN_WIDTH, command=lambda: "")
    Mech_O_Mats_btn.pack(pady = BTN_PAD)

    materials_btn = tk.Button(left_frame, text="Materials Science", width = BTN_WIDTH, command=lambda: "")
    materials_btn.pack(pady = BTN_PAD)

    fluids_btn = tk.Button(left_frame, text="Fluid Mechanics", width = BTN_WIDTH, command=lambda: "")
    fluids_btn.pack(pady = BTN_PAD)

    thermo_btn = tk.Button(left_frame, text="Thermodynamics", width = BTN_WIDTH, command=lambda: "")
    thermo_btn.pack(pady = BTN_PAD)

    heat_transfer_btn = tk.Button(left_frame, text="Heat Transfer", width = BTN_WIDTH, command=lambda: ht_btns(frame, left_frame, CLEAR))
    heat_transfer_btn.pack(pady = BTN_PAD)

    ctrls_btn = tk.Button(left_frame, text="Measurements and Controls", width = BTN_WIDTH, command=lambda: "")
    ctrls_btn.pack(pady = BTN_PAD)

    mech_design_btn = tk.Button(left_frame, text="Mechanical Design", width = BTN_WIDTH, command=lambda: "")
    mech_design_btn.pack(pady = BTN_PAD)    





home_buttons()

root.mainloop()  


# GUIDELINE: Try to make each file less than 500 lines of code
# Remember: gotta fix toggle section
# Maybe add answer sheet walkthrough maker later