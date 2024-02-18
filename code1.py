import tkinter as tk

window = tk.Tk()

defual_setting_dict = {
    "UpperCase" : True,
    "LowerCase" : False,
    "Number" : True,
    "Symbol" : True,
    "Space" : False
}

label_featurs_list = [
    {
        "text": "UpperCase: ",
    },
    
    {
        "text": "LowerCase: ",
    },
     
    {
        "text": "Number: ",
    },
      
    {
        "text": "Symbol: ",
    },
       
    {
        "text": "Space: ",
    },
    
    {
        "text": "Length: ",
    },
    
    {
        "text": "Random_Password: ",
    }
]

label_created_list = []

for lable_obj in label_featurs_list:
    lable_created = tk.Label(
        master=window,
        height=3,
        width=18,
        font=('calibre',10, 'bold'),
        text=lable_obj['text'],
    )
    label_created_list.append(lable_created)
    
row_num = 0
for lable_objcts in label_created_list:
    lable_objcts.grid(row=row_num, column=0, columnspan=5)
    row_num += 1
 
yes_btn_list = []
 
for i in range(5):  
    yes_btn = tk.Button(
        master = window,
        text= f'yes {i}',
        width= 8,
        height= 1,
        command= quit,
    )
    yes_btn_list.append(yes_btn)

row_num = 0
for yes_btn_objs in yes_btn_list:
    yes_btn_objs.grid(row=row_num, column=5, columnspan=15)
    row_num += 1
    

no_btn_list = []
 
for i in range(5):  
    no_btn = tk.Button(
        master = window,
        text= f'no {i}',
        width= 8,
        height= 1,
        command= quit,
    )
    no_btn_list.append(no_btn)

row_num = 0
for no_btn_objs in no_btn_list:
    no_btn_objs.grid(row=row_num, column=20, columnspan=5)
    row_num += 1
    
length_ent = tk.Entry(
    master=window,
    width=20,
)

length_ent.grid(row=row_num, column=5, columnspan=20)

random_password_lbl = tk.Label(
    master=window,
    text = 'answer',
    width= 15,
)

random_password_lbl.grid(row= row_num+1, column=5, columnspan=20)
default_label_featurs = [
    {
        "text": "Default --> Yes",
    },
    
    {
        "text": "Default --> Yes",
    },
        
    {
        "text": "Default --> Yes",
    },
    
    {
        "text": "Default --> Yes",
    },
        
    {
        "text": "Default --> Yes",
    },
            
    {
        "text": "Default --> 8",
    },
            
]

default_label_list = []

for label_obj in default_label_featurs:
    default_lbl = tk.Label(
        master=window,
        height=3,
        width=20,
        text=label_obj['text'],
        font=('calibre',10, 'bold')
    )
    default_label_list.append(default_lbl)
    
row_num = 0
for label_objs in default_label_list:
    label_objs.grid(row=row_num, column=30, columnspan=10, )
    row_num += 1
    
run_btn = tk.Button(
    master=window,
    width=4,
    height=1,
    text="Run",
    command=quit,
)
run_btn.grid(row=row_num, column=27, columnspan=10)

reset = tk.Button(
    master=window,
    width=4,
    height=1,
    text="Reset",
    command=quit,
)
reset.grid(row=row_num, column=32, columnspan=10)
window.mainloop()