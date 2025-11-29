import tkinter as tk
import random
import inspect
import Helpers


rates = [0.5, 1, 1.5, 2, 4, 6, 8, 10, 12, 18]
label_list = []

BTN_WIDTH = 25
BTN_PAD = 12



################################################# Single Payment #################################################


def single_future_payment(F, n, i, frame): # AKA Single Payment Present Worth
    
    question = "What is the present worth of $" + str(F) + " received " + str(n) + " years from now at an interest rate of " + str(i) + "% compounded annually?" 
    
    Helpers.label_maker(question, frame)
    
    P = F / ((1 + (i / 100))**n)
    
    return P

def single_present_compound(P, n, i, frame):
    question = "You invest $" + str(P) + " today in an account that earns "  + str(i) + "% annual interest compounded annually. What will be the future worth of this investment after " + str(n) + " years?" 
    
    Helpers.label_maker(question, frame)
    
    F = P * ((1 + (i / 100))**n)
    
    return P



################################################# Uniform #################################################

def uni_A_F(A, n, i, frame):
    
    question = "A piece of equipment requires uniform annual maintenance costs of $" + str(A) + " each year for " + str(n) + " years. If the interest rate is " + str(i) + "% per year, what is the future worth (F) of these costs at the end of year" + str(n) + "?"
    Helpers.label_maker(question, frame)
    
    i = i / 100
    F = A * (((1 + i)**n - 1) / i)
    return F


def uni_P_A(P, n, i, frame):
    
    question = "A machine costs $" + str(P) + " and has no salvage value at the end of its " + str(n) + "-year life. If the interest rate is " + str(i) + "% per year, determine the uniform annual worth (A) of the initial investment."
    Helpers.label_maker(question, frame)
    
    i = i / 100
    A = P * ((i * (1 + i)**n ) / ((1+i)**n - 1))
    return A
    

def uni_F_A(F, n, i, frame):
    
    question = "An investment is expected to yield a future amount of $" + str(F) + " after " + str(n) + " years. If the interest rate is " + str(i) + "% per year, what is the equivalent uniform annual amount (A) over the " + str(n) + " years?"
    Helpers.label_maker(question, frame)
    
    i = i / 100
    A =  F * (i /((1 + i)**n - 1))
    return A

def uni_A_P(A, n, i, frame):
    
    question = "A maintenance contract requires annual payments of $" + str(A) + " for " + str(n) + " years. If the interest rate is " + str(i) + "% per year, what is the present worth (P) of these payments?"
    Helpers.label_maker(question, frame)
    
    i = i / 100
    P = A * (((1 + i)**n - 1) / (i * (1 + i)**n))
    return P
    
    
################################################# Salvage Value #################################################


def salvage_value(P, n, i, frame): # AKA Capital Recovery problem
    min = P // 10
    max = P // 2
    
    sal_val = (random.randint(min, max) // 100) * 100
    
    question = "A machine costs $" + str(P) + " and has an estimated salvage value of $" + str(sal_val) + " at the end of " + str(n) + " years. If the interest rate is " + str(i) + "% per year, what is the equivalent uniform annual cost (A) of the machine?"
    i = i / 100
    Helpers.label_maker(question, frame)
    
    cap_factor = ( i * (1 + i)**n ) / ((1 + i)**n -1) # Capital recovery factor
    salvage_factor = (i / ((1 + i)**n - 1 ))      
    
    print(cap_factor)
    print(salvage_factor)       
    
    A = (P * cap_factor) - (sal_val * salvage_factor)
    
    return A



################################################# Cost Benefit #################################################

def BC_one(P, n, i, frame):
    if n < 5:
        n = 5 
        
        
    
    A_cost = random.randint(P // 20, 3 * (P // 20))
    A_benefit = random.randint(3 * (P // 20), 3 * (P // 10))
    
    question = "A highway improvement project requires an initial investment of $" + str(P) + " and annual maintenance costs of $" + str(A_cost) + " for " + str(n) + " years. "
    question += "The project is expected to generate annual benefits of $" + str(A_benefit) + " per year over the same period. " 
    question += "If the interest rate is " + str(i) + "% per year, determine the benefit–cost ratio (B/C) and decide whether the project is economically justified."
    
    Helpers.label_maker(question, frame)
    
    PW_factor = (( (1 + i)**n - 1) / (i * (1 + i)**n)) 
    
    PW_benefit = A_benefit * PW_factor
    PW_cost = P + (A_cost * PW_factor)
    
    BC = PW_benefit / PW_cost
    
    if BC < 1:
        answer = "Not economically justified" 
    else: # Includes BC = 1 case
        answer = "Economically justified"
        
    return answer    
    
def BC_two(P_A, n, i, frame):    
    if n < 5:
        n = 5  
        
    AA_cost = random.randint(P_A // 20, 3 * (P_A // 20))
    AA_benefit = random.randint(3 * (P_A // 20), 3 * (P_A // 10))    
    
    P_B = random.randint(int(0.8 * P_A), int(1.5 * P_A))
    
    if P_B < P_A:
        AB_cost = random.randint(3 * (P_A // 20), 4 * (P_A // 20))
        AB_benefit = random.randint(5 * (P_A // 20), 6 * (P_A // 10))
    else:
        AB_cost = random.randint(P_B // 20, 3 * (P_B // 20))
        AB_benefit = random.randint(3 * (P_B // 20), 3 * (P_B// 10)) 
        
        
        
    table = [
        ["Project", "Initial Cost ($)", "Annual Cost ($)"," Annual Benefit ($)"],
        ["A", str(P_A), str(AA_cost), str(AA_benefit)],
        ["B", str(P_B), str(AB_cost), str(AB_benefit)],
    ]    
        
    question = "Two road improvement alternatives, A and B, are being considered. Their costs and annual benefits are shown below."
    Helpers.label_maker(question, frame)
    
    question = "The interest rate is " + str(i) + "% per year, and both projects have a " + str(n) + "-year life. Which project should be selected based on an incremental B/C analysis?"
    Helpers.label_maker(question, frame)
    
    Helpers.table_maker(table, frame)
    
    
    
    i = i / 100   
    
    PW_factor = (((1 + i)**n - 1) / (i * (1 + i)**n)) 
    
    PWA_benefit = AA_benefit * PW_factor
    PWA_cost = P_A + (AA_cost * PW_factor)
    
    PWB_benefit = AB_benefit * PW_factor
    PWB_cost = P_B + (AB_cost * PW_factor)
    
    PW_benefit = PWB_benefit - PWA_benefit
    PW_cost = PWB_cost - PWA_cost
        
    BC = PW_benefit / PW_cost
    
    print("B / C = " + str(BC)) # Checking logic for negatives  
    
    if BC < 1:
        if P_A < P_B:
            answer = "Select Alternative A"
        else:
            answer = "Select Alternative B"    
    else: # Includes BC = 1 case
        if P_A < P_B:
            answer = "Select Alternative B"   
        else:
            answer = "Select Alternative A"     
        
    return answer    
      
        



################################################# Payback Period / Breakeven #################################################

def payback_equal(P, frame):
    
    A = random.randint(P // 20, P // 3)

    question = "A company purchases a machine for $" + str(P) + ". It generates annual net cash inflows of $" + str(A)
    Helpers.label_maker(question, frame)
    question = "What is the payback period for the machine?"
    Helpers.label_maker(question, frame)
    
    n = P / A
    
    return n

def payback_unequal(P, frame):
    
    A = []
    
    n = 0
    stay = True
    greater_year = 0
    greater_sum = 0
    
    A1 = random.randint(P // 8, P // 5)
    A.append(A1)
    sum = A1
    
    while stay != 0:
        
        A_next = A[n] + random.randint(A[n] // 6, A[n])
        sum += A_next
        A.append(A_next)
        n += 1
        
        if sum < P:
            stay = 1
        else:
            if greater_year == 0:
                greater_year = n # year where the sum is greater than P
                greater_sum = sum - A_next
                 
            if n < 6: # setting max table values to 6
                stay = random.randint(0, 3) # 50 / 50 if n continues when sum > P
            else:
                stay = 0   
    
    table = [
        ["Year", "Net Cash Inflow ($)"] 
    ]
    
    for idx in range(len(A)):
        row = [str(idx + 1), str(A[idx])]
        table.append(row)    
    
    question = "A company is considering purchasing a new machine for $" + str(P) + ". The machine is expected to generate the following net cash inflows over the next " + str(len(A)) + "years:"
    
    Helpers.label_maker(question, frame)
    Helpers.table_maker(table, frame)  
    
    question = "Calculate the payback period for the machine."
    Helpers.label_maker(question, frame)  
    exact_year = greater_year - 1 + ((P - greater_sum + A[greater_year]) / A[greater_year])
    
    return exact_year
                  
def breakeven(frame):
    
    A = random.randint(20, 100) * 100
    var_cost = random.randint(15, 60)
    sell_price = var_cost + random.randint(var_cost // 10, 2 * var_cost)
    
    question = "A company manufactures small electric fans. The company’s cost structure and selling price are as follows:"
    Helpers.label_maker(question, frame)
    
    table = [
        ["Parameter", "Value"],
        ["Fixed Costs", "$" + str(A) + " per year"],
        ["Variable Cost", "$" + str(var_cost) + " per fan"],
        ["Selling Price", "$" + str(sell_price) + " per fan"]
    ]
    
    Q_BE = A / (sell_price - var_cost) # Break-Even Quantity
    
    units = random.choice([True, False]) # variable to determine whether answer is in dollars or units
    
    if units == True:
        question = "Determine the break-even quantity:"
        answer = Q_BE
    else:
        question = "Determine the break-even revenue:"
        answer = Q_BE * sell_price
            
    Helpers.table_maker(table, frame)
    Helpers.label_maker(question, frame)
    
    return answer


################################################# ROR / IRR #################################################

def single_ROR(P, n, frame):
    
    F = P + random.randint(P // 10, 4 * P)
    
    question = "An engineer invests $" + str(P) + " and receives $" + str(F) + " after " + str(n) + " years. What is the rate of return?"
    Helpers.label_maker(question, frame)
    
    i = (F / P)**(1 / n) - 1
    
    return i * 100
    
def uniform_ROR():
    pass

def increment_ROR():
    pass

def mixed_ROR():
    pass


################################################# Inflation / Real vs Nominal Interest Rates #################################################

def real_rate(frame):
    d = random.randint(5, 11) # Nominal interest rate
    f = random.randint(1, 7) # inflation rate
    
    question = "If the nominal interest rate is " + str(d) + "% per year and the inflation rate is " + str(f) + "% per year, what is the real interest rate?"
    Helpers.label_maker(question, frame)
    
    d = d / 100
    f = f / 100 
    
    i = ((d - f) / (1 + f)) * 100
    
    return i * 100

def nom_rate(frame):
    i = random.randint(1, 14) / 2 # Real interest rate
    f = random.randint(1, 7) # Inflation rate
    
    question = "An investment offers a real rate of return of " + str(i) + "% per year when inflation is " + str(f) + "%. Find the nominal interest rate."
    Helpers.label_maker(question, frame)
    
    i = i / 100
    f = f / 100 
    
    d = i + f + (i * f)
    
    return d * 100

def inflation(P, n, frame):
    
    d = random.randint(5, 11) # Nominal interest rate
    f = random.randint(1, 7) # inflation rate
    
    d = 8
    f = 3
    P = 10000
    n = 4
    
    question = "You invest $" + str(P) + " for " + str(n) + " years at a nominal rate of " + str(d) + "%, while inflation averages " + str(f) + "% per year. Find the real future value in today’s dollars."
    Helpers.label_maker(question, frame)
    
    d = d / 100
    f = f / 100
    
    F = P * (d + 1)**n
    print(F)
    
    F_real = F / ((1 + f)**n)
    
    return F_real
    


################################################# Loan / Sinking Fund / Mortgage Calculations #################################################

def loan(P, n, i, frame):
    question = "A $" +  str(P) + " loan is to be repaid in equal annual payments over " + str(n) + " years at " + str(i) + "% interest."
    Helpers.label_maker(question, frame)
    question = "What is the annual payment?"
    Helpers.label_maker(question, frame)
    
    i = i / 100
    
    A = P * ((i * (1 + i)**n ) / ((1+i)**n - 1))
    return A

def mortgage(P, n, i, frame):
    question = "A $" + str(P) + " mortgage is issued at " + str(i) + "% annual interest, compounded monthly, for " + str(n) + " years."
    Helpers.label_maker(question, frame)
    question = "Find the monthly payment."
    Helpers.label_maker(question, frame)
    
    i = i / 100
    
    i_m = i / 12 # monthly interest
    
    N = n * 12
    
    A = P * ((i_m * (1 + i_m)**N ) / ((1+i_m)**N - 1))
    return A
    
def sink_fund(F, n, i, frame):
    question = "You want $" + str(F) + " in " + str(n) + " years and can earn " + str(i) + "% interest per year."
    Helpers.label_maker(question, frame)
    question = "How much must you deposit annually?"
    Helpers.label_maker(question, frame)
    
    i = i / 100
    
    A = F * (i /((1 + i)**n - 1))
    return A


################################################# Straight Line Depreciation #################################################

def SLD(P, n, frame):
    
    min = P // 10
    max = P // 2
    
    sal_val = (random.randint(min, max) // 100) * 100
    
    year = random.randint(1, n)
    
    question = "A machine costs $" + str(P) + " , has an estimated salvage value of $" + str(sal_val) + ", and a useful life of " + str(n) + " years."
    Helpers.label_maker(question, frame)
    question = "Using the straight-line method, determine: "
    Helpers.label_maker(question, frame)
    question = "1. The annual depreciation "
    Helpers.label_maker(question, frame)
    question = "2. The book value at the end of year " + str(year)
    Helpers.label_maker(question, frame)
    
    D = (P - sal_val) / n
    BV = P - (D * year)
    
    answer = "Annual Depreciation: " + str(D) + "Book Value: " + str(BV)
    
    return answer


################################################# Main For Questions #################################################

def question_maker(num, frame, clear):
    function_names = [
        # Single Payment
        single_future_payment,
        single_present_compound,

        # Uniform
        uni_A_F,
        uni_P_A,
        uni_F_A,
        uni_A_P,

        # Salvage Value
        salvage_value,

        # Cost Benefit
        BC_one,
        BC_two,

        # Payback Period / Breakeven
        payback_equal,
        payback_unequal,
        breakeven,

        # ROR / IRR
        single_ROR,
        # uniform_ROR,
        # increment_ROR,
        # mixed_ROR,

        # Inflation / Real vs Nominal Interest Rates
        real_rate,
        nom_rate,
        inflation,

        # Loan / Sinking Fund / Mortgage Calculations
        loan,
        mortgage,
        sink_fund,

        # Straight Line Depreciation
        SLD
    ]
    

    amount = (random.randint(100, 100001) // 100) * 100
    years = random.randint(1, 21)
    interest = random.choice(rates)
        
    func = function_names[num]
        
    param_num = len((inspect.signature(func)).parameters)
    if clear == True:
        Helpers.frame_clear(frame)
        
    if param_num == 4:
        answer = func(amount, years, interest, frame)
    elif param_num  == 3:
        answer = func(amount, years, frame)
    elif param_num  == 2:
        answer = func(amount, frame)
    elif param_num == 1: 
        answer = func(frame)
    else:
        print("Error: Function has incorrect number of parameters.")    
    
    print(answer) # For testing purposes only    
    if clear:
        Helpers.entry_maker(frame, answer)  # Do not want entries for multiple questions (may change later, currently there for sheet mode)      
    else:
        Helpers.spacer(frame)
           

############################ Button functions ############################

def buttons(frame, left_frame, clear):
    Helpers.frame_clear(left_frame)
    SFP_btn = tk.Button(left_frame, text="Single Future Payment", width = BTN_WIDTH, command=lambda: question_maker(0, frame, clear))
    SFP_btn.pack(pady = BTN_PAD)
    
    SPC_btn = tk.Button(left_frame, text="Single Present Compound", width = BTN_WIDTH, command=lambda: question_maker(1, frame, clear))
    SPC_btn.pack(pady = BTN_PAD)
    
    UNI_btn = tk.Button(left_frame, text="Uniform Questions", width = BTN_WIDTH, command=lambda: question_maker(random.randint(2, 5), frame, clear))
    UNI_btn.pack(pady = BTN_PAD)
    
    SAL_btn = tk.Button(left_frame, text="Salvage Value", width = BTN_WIDTH, command=lambda: question_maker(6, frame, clear))
    SAL_btn.pack(pady = BTN_PAD)
    
    CB_btn = tk.Button(left_frame, text="Cost Benefit Analysis", width = BTN_WIDTH, command=lambda: question_maker(random.randint(7, 8), frame, clear))
    CB_btn.pack(pady = BTN_PAD)
    
    PB_btn = tk.Button(left_frame, text="Payback Period / Breakeven", width = BTN_WIDTH, command=lambda: question_maker(random.randint(9, 11), frame, clear))
    PB_btn.pack(pady = BTN_PAD)
    
    ROR_btn = tk.Button(left_frame, text="Rate of Return", width = BTN_WIDTH, command=lambda: question_maker(12, frame, clear)) #change this later when more ROR functions are added
    ROR_btn.pack(pady = BTN_PAD)
    
    INF_btn = tk.Button(left_frame, text="Inflation / Interest Rates", width = BTN_WIDTH, command=lambda: question_maker(random.randint(13, 15), frame, clear))
    INF_btn.pack(pady = BTN_PAD)
    
    LSM_btn = tk.Button(left_frame, text="Loan / Sinking Fund / Mortgage", width = BTN_WIDTH, command=lambda: question_maker(random.randint(16, 18), frame, clear))
    LSM_btn.pack(pady = BTN_PAD)
    
    SLD_btn = tk.Button(left_frame, text="Straight Line Depreciation", width = BTN_WIDTH, command=lambda: question_maker(19, frame, clear))
    SLD_btn.pack(pady = BTN_PAD)
    
    random_btn = tk.Button(left_frame, text="Random Question", width = BTN_WIDTH, command=lambda: question_maker(random.randint(0, 19), frame, clear))
    random_btn.pack(pady = BTN_PAD)
    







