
import Helpers
import random
import math
import tkinter as tk

BTN_WIDTH = 25
BTN_PAD = 12
MULTI_PART = True

########################## Conduction ##########################

def conduction(frame, func_choice, clear):
    
    # make sure there is a random option for func_choice if no question type is specified
    """
    Notes:
        - cylinder:    
            # Tf_i is hot and greater than Tinf
        
    """
    
    functions = ["plane_wall", "wall_convection", "composite_wall", "cylinder", "composite_cylinder"]
    
    if clear:
        Helpers.frame_clear(frame)
    
    k = random.randint(10, 200)  # W/mK
    A = random.randint(1, 10)    # m^2
    L = round(random.uniform(0.1, 1.0), 2)  # m (add this to notes later)
    T1 = random.randint(100, 500)  # °C
    T2 = random.randint(20, 100)   # °C
    
    
    
    def plane_wall(k, A, L, T1, T2):
        choices = ["flux", "rate"]
        selection = random.choice(choices)
        
        question = "A plane wall has a thermal conductivity of " + str(k) + " W/mK, an area of " + str(A) + " m^2, and a thickness of " + str(L) + " m. If the temperatures on either side of the wall are " + str(T1) + " °C and " + str(T2) + " °C respectively, "
        if selection == "flux":
            question += "what is the heat flux through the wall in W/m^2?"
        else:
            question += "what is the rate of heat transfer through the wall in watts?"
        Helpers.label_maker(question, frame)
        
        q = (k * A * (T1 - T2)) / L
        q_flux = q / A
        
        if selection== "flux":
            return q_flux
        
        return q
        
    def wall_convection(k, A, L, Tinf1, Tinf2, h1, h2):
        question = "A metal plate has a thickness of " + str(L) + " m, an area of " + str(A) + " m^2, and a thermal conductivity of " + str(k) + " W/mK."
        question += " The temperature of the fluid on one side of the plate is " + str(Tinf1) + " °C with a convective heat transfer coefficient of " + str(h1) + " W/m^2K, while the temperature of the fluid on the other side is " + str(Tinf2) + " °C with a convective heat transfer coefficient of " + str(h2) + " W/m^2K."
        Helpers.label_maker(question, frame)
        question = "Find the rate of heat transfer through the plate."
        Helpers.label_maker(question, frame)
        
        
        R1 = 1 / (h1 * A)
        Rcond = L / (k * A)
        R2 = 1 / (h2 * A)
        
        R_total = R1 + Rcond + R2
        
        q = (Tinf1 - Tinf2) / R_total
        
        answer = [q]
        
        if MULTI_PART:
            question = "Find the temperature of the wall surfaces on both sides (Ts1 and Ts2)."
            Helpers.label_maker(question, frame)
            Ts1 = Tinf1 - (q * R1) # equation is delta T = q * R (think of the rate of heat transfer as current and Temp as voltage)
            Ts2 = Tinf2 + (q * R2) # Note that this is addition since heat is leaving the wall to the fluid (Think hot wall to cold fluid)
            answer.extend([Ts1, Ts2])

        
        return answer
    
    def composite_wall(A, L1, L2, L3, k1, k2, k3, T1, T2):
        
        choices = ["flux", "rate"]
        selection = random.choice(choices)
        answer = []
        
        question = "A composite wall of area " + str(A) + " m^2 consists of three layers in series:"
        Helpers.label_maker(question, frame)
        question = "Layer 1: Thickness = " + str(L1) + " m, Thermal Conductivity = " + str(k1) + " W/mK"
        Helpers.label_maker(question, frame)
        question = "Layer 2: Thickness = " + str(L2) + " m, Thermal Conductivity = " + str(k2) + " W/mK"            
        Helpers.label_maker(question, frame)
        question = "Layer 3: Thickness = " + str(L3) + " m, Thermal Conductivity = " + str(k3) + " W/mK"            
        Helpers.label_maker(question, frame)    
        
        question = "Temperature on the two faces of the composite wall are " + str(T1) + " °C and " + str(T2) + " °C respectively. "
        Helpers.label_maker(question, frame)
        Helpers.spacer()
        if selection == "rate":
            question = "Find the rate of heat transfer through the wall."
        else:
            question = "Find the heat flux through the wall."
        Helpers.label_maker(question, frame)  
        
        R1 = L1 / (k1 * A)
        R2 = L2 / (k2 * A)
        R3 = L3 / (k3 * A)
        
        R_total = R1 + R2 + R3
        
        q = (T1 - T2) / R_total
        q_flux = q / A
        
        if selection == "flux":
            answer.append(q_flux)
        else:
            answer.append(q)
        
        if MULTI_PART:    
            question = "Find the temperatures at the interfaces between the layers (T_12 and T_23)." # Maybe change to be symbols instead of T_12 / T_23
            Helpers.label_maker(question, frame)  
            T_12 = T1 - (q * R1) # q * R1 gives the temperature drop across the first layer (delta T = q * R)
            T_23 = T_12 - (q * R2)
            
            answer.extend([T_12, T_23])
        
        return answer    
                
    def cylinder(ri, ro, L, k, hi, ho, Tinf, Tf_i): 
        question = "Hot fluid at a temperature of " + str(Tf_i) + " °C flows inside a cylindrical pipe with an inner radius of " + str(ri) + " m and an outer radius of " + str(ro) + " m. "
        question += "The pipe has a length of " + str(L) + " m and a thermal conductivity of " + str(k) + " W/mK. "
        question += "The convective heat transfer coefficient on the inner surface is " + str(hi) + " W/m^2K, while the convective heat transfer coefficient on the outer surface is " + str(ho) + " W/m^2K. "
        question += "The ambient temperature of the fluid outside the pipe is " + str(Tinf) + " °C."
        Helpers.label_maker(question, frame)
        
        question = "Find the heat transfer rate q (W) from the hot fluid to the ambient."
        Helpers.label_maker(question, frame)
        
        Ai = 2 * (math.pi) * ri * L # inner surface area
        Ao = 2 * (math.pi) * ro * L # outer surface area 
        
        R_conv_i = 1 / (hi * Ai)
        R_conv_o = 1 / (ho * Ao)  
        
        R_cond = math.log(ro / ri) / (2 * (math.pi) * k * L)
        R_total = R_conv_i + R_conv_o + R_cond
        q = (Tf_i - Tinf) / R_total
        
        answer = [q]
        
        if MULTI_PART:
            question = "Also, find the inner and outer surface temperatures of the pipe (Ts_i and Ts_o)."
            Helpers.label_maker(question, frame)
            Ts_i = Tf_i - (q * R_conv_i) # q * R_conv_i gives the temperature drop from the fluid to the inner surface
            Ts_o = Tinf + (q * R_conv_o) 
            answer.extend([Ts_i, Ts_o])
        
        return answer    
        
    def composite_cylinder(Tf_i, hi, r1, r2, r3, k1, k2, L, ho, Tinf):
        question = "Hot fluid at a temperature of " + str(Tf_i) + " °C flows inside a composite cylindrical pipe consisting of two layers. "
        question += "The inner radius of the pipe is " + str(r1) + " m, the interface between the two layers is at a radius of " + str(r2) + " m, and the outer radius is " + str(r3) + " m. "
        question += "The pipe has a length of " + str(L) + " m. The thermal conductivity of the inner layer is " + str(k1) + " W/mK, while the thermal conductivity of the outer layer is " + str(k2) + " W/mK. "
        question += "The convective heat transfer coefficient on the inner surface is " + str(hi) + " W/m^2K, while the convective heat transfer coefficient on the outer surface is " + str(ho) + " W/m^2K. "
        question += "The ambient temperature of the fluid outside the pipe is " + str(Tinf) + " °C."
        Helpers.label_maker(question, frame)
        
        question = "Find the heat transfer rate q (W) from the hot fluid to the ambient."
        Helpers.label_maker(question, frame)
        
        Ai = 2 * (math.pi) * r1 * L # inner surface area
        Ao = 2 * (math.pi) * r3 * L # outer surface area
        
        R_conv_i = 1 / (hi * Ai)
        R_conv_o = 1 / (ho * Ao)
        
        R_cond1 = math.log(r2 / r1) / (2 * (math.pi) * k1 * L)
        R_cond2 = math.log(r3 / r2) / (2 * (math.pi) * k2 * L)
        R_total = R_conv_i + R_conv_o + R_cond1 + R_cond2
        q = (Tf_i - Tinf) / R_total
        
        answer = [q]
        
        if MULTI_PART:
            question = "Also, find the inner and outer surface temperatures of the pipe (Ts_i and Ts_o)."
            Helpers.label_maker(question, frame)
            Ts_i = Tf_i - (q * R_conv_i) # q * R_conv_i gives the temperature drop from the fluid to the inner surface
            Ts_o = Tinf + (q * R_conv_o) 
            answer.extend([Ts_i, Ts_o])
        
        return answer    
    
    if func_choice == "random" or func_choice is None:
        func_choice = random.choice(functions)
        
    if func_choice == "plane_wall":
        k = random.randint(10, 200)  # W/mK
        A = random.randint(1, 10)    # m^2
        L = round(random.uniform(0.1, 1.0), 2)  # m (add this to notes later)
        T1 = random.randint(100, 500)  # °C
        T2 = random.randint(20, 100)   # °C
        
        answer = plane_wall(k, A, L, T1, T2)
        print(answer) # For testing purposes only    
    elif func_choice == "wall_convection":
        k = random.randint(10, 200)  # W/mK
        A = random.randint(1, 10)    # m^2
        L = round(random.uniform(0.1, 1.0), 2)
        Tinf1 = random.randint(100, 500)  # °C
        Tinf2 = random.randint(20, 100)   # °C
        h1 = random.randint(10, 100)      # W/m^2K
        h2 = random.randint(10, 100)      # W/m^2K
        
        answer = wall_convection(k, A, L, Tinf1, Tinf2, h1, h2)
        print(answer) # For testing purposes only    
    elif func_choice == "composite_wall":
        A = random.randint(1, 10)    # m^2
        L1 = round(random.uniform(0.1, 0.5), 2)
        L2 = round(random.uniform(0.1, 0.5), 2)
        L3 = round(random.uniform(0.1, 0.5), 2)
        k1 = random.randint(10, 200)  # W/mK
        k2 = random.randint(10, 200)  # W/mK
        k3 = random.randint(10, 200)  # W/mK
        T1 = random.randint(100, 500)  # °C
        T2 = random.randint(20, 100)   # °C
        
        answer = composite_wall(A, L1, L2, L3, k1, k2, k3, T1, T2)
        print(answer) # For testing purposes only    
    elif func_choice == "cylinder":
        ri = round(random.uniform(0.01, 0.1), 3)  # m
        ro = round(ri + random.uniform(0.01, 0.1), 3)  # m
        L = round(random.uniform(0.5, 2.0), 2)  # m
        k = random.randint(10, 200)  # W/mK
        hi = random.randint(10, 100)      # W/m^2K
        ho = random.randint(10, 100)      # W/m^2K
        Tinf = random.randint(20, 100)   # °C
        Tf_i = random.randint(100, 500)  # °C
        
        answer = cylinder(ri, ro, L, k, hi, ho, Tinf, Tf_i)
        print(answer) # For testing purposes only    
    elif func_choice == "composite_cylinder":
        r1 = round(random.uniform(0.01, 0.1), 3)  # m
        r2 = round(r1 + random.uniform(0.01, 0.1), 3)  # m
        r3 = round(r2 + random.uniform(0.01, 0.1), 3)  # m
        L = round(random.uniform(0.5, 2.0), 2)  # m
        k1 = random.randint(10, 200)  # W/mK
        k2 = random.randint(10, 200)  # W/mK
        hi = random.randint(10, 100)      # W/m^2K
        ho = random.randint(10, 100)      # W/m^2K
        Tinf = random.randint(20, 100)   # °C
        Tf_i = random.randint(100, 500)  # °C
        
        answer = composite_cylinder(Tf_i, hi, r1, r2, r3, k1, k2, L, ho, Tinf)
    else:
        print("Invalid function choice for conduction.")
        return    

    print(answer) # For testing purposes only    
    if clear:
        Helpers.entry_maker(frame, answer)  # Do not want entries for multiple questions (may change later, currently there for sheet mode) 
             
    else:
        Helpers.spacer(frame)    
    
            
def convection():
    pass
def radiation():
    pass
def combination():
    pass
def overall_HT():
    pass
def nrg_balance():
    pass    
def lumped_system():
    pass    
def properties(): # Things like biot number, nusselt number, etc
    pass




############################## Math Helper Functions ##############################

def heat_transfer_rate(info):
    # maybe make info a dictionary to make it easier to read
    # have there be a type in the dictionary that specifies what kind of heat transfer it is
    pass

def temperature(info):
    # find the temperature at a certain point based on the info given
    # likely just a rearrangement of the heat_transfer_rate function
    pass

def resistance(info):
    # find the thermal resistance based on the info given
    pass



############################### MISCELLANEOUS FUNCTIONS ###############################

def multi_part(choice):
    # Maybe add a random option so that there can be multiple parts but it isnt guaranteed
    if choice: 
        MULTI_PART = True
    else:
        MULTI_PART = False
    

############################# Main Program Functions #############################

def buttons(frame, left_frame, clear):
    Helpers.frame_clear(left_frame)
    conduction_btn = tk.Button(left_frame, text="Conduction", width = BTN_WIDTH, command=lambda: conduction(frame, None, clear))
    conduction_btn.pack(pady = BTN_PAD)
    
    convection_btn = tk.Button(left_frame, text="Convection", width = BTN_WIDTH, command=lambda: convection())
    convection_btn.pack(pady = BTN_PAD)
    
    radiation_btn = tk.Button(left_frame, text="Radiation", width = BTN_WIDTH, command=lambda: radiation())
    radiation_btn.pack(pady = BTN_PAD)
    
    combination_btn = tk.Button(left_frame, text="Combination Heat Transfer", width = BTN_WIDTH, command=lambda: combination())
    combination_btn.pack(pady = BTN_PAD)
    
    overall_HT_btn = tk.Button(left_frame, text="Overall Heat Transfer Coefficient", width = BTN_WIDTH, command=lambda: overall_HT())
    overall_HT_btn.pack(pady = BTN_PAD)
    
    nrg_balance_btn = tk.Button(left_frame, text="Heat Transfer Energy Balance", width = BTN_WIDTH, command=lambda: nrg_balance())
    nrg_balance_btn.pack(pady = BTN_PAD)
    
    lumped_system_btn = tk.Button(left_frame, text="Lumped System Analysis", width = BTN_WIDTH, command=lambda: lumped_system())
    lumped_system_btn.pack(pady = BTN_PAD)
    
    properties_btn = tk.Button(left_frame, text="Heat Transfer Properties", width = BTN_WIDTH, command=lambda: properties())
    properties_btn.pack(pady = BTN_PAD)
    
    random_btn = tk.Button(left_frame, text="Random Heat Transfer Question", width = BTN_WIDTH, command=lambda: conduction(frame, "random"))
    random_btn.pack(pady = BTN_PAD)
    