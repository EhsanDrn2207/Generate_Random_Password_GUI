import tkinter as tk
import os
import sys

from generate_password import *
from errors import LengthLimitError

window = tk.Tk()

window.title("Password Generation")

defual_setting_dict = {
    "UpperCase" : True,
    "LowerCase" : False,
    "Number" : True,
    "Symbol" : True,
    "Space" : False
}

        
label_featurs_list = [
    {
        "text": "UpperCase:",
    },
    
    {
        "text": "LowerCase:",
    },
     
    {
        "text": "Number:",
    },
      
    {
        "text": "Symbol:",
    },
       
    {
        "text": "Space:",
    },
    
    {
        "text": "Length:",
    },
    
    {
        "text": "Random_Password:",
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
    
yes_button_commands = [
    {
        "command" : lambda: defual_setting_dict.update({"UpperCase": True}),
    },
    
    {
        "command" : lambda: defual_setting_dict.update({"LowerCase": True}),
    },
        
    {
        "command" :lambda: defual_setting_dict.update({"Number": True}),
    },
            
    {
        "command" :lambda: defual_setting_dict.update({"Symbol": True}),
    },
                
    {
        "command" :lambda: defual_setting_dict.update({"Space": True}),
    },
                    
]
 
yes_btn_list = []
 
for yes_btn in yes_button_commands:  
    yes_btn = tk.Button(
        master = window,
        text= 'yes',
        width= 8,
        height= 1,
        fg="blue",
        command= yes_btn["command"],
    )
    yes_btn_list.append(yes_btn)

row_num = 0
for yes_btn_objs in yes_btn_list:
    yes_btn_objs.grid(row=row_num, column=5, columnspan=15)
    row_num += 1
  
no_button_commands = [
    {
        "command" : lambda: defual_setting_dict.update({"UpperCase": False}),
    },
    
    {
        "command" : lambda: defual_setting_dict.update({"LowerCase": False}),
    },
        
    {
        "command" :lambda: defual_setting_dict.update({"Number": False}),
    },
            
    {
        "command" :lambda: defual_setting_dict.update({"Symbol": False}),
    },
                
    {
        "command" :lambda: defual_setting_dict.update({"Space": False}),
    },
                    
]  

no_btn_list = []
 
for no_btn in no_button_commands:  
    no_btn = tk.Button(
        master = window,
        text= 'no',
        width= 8,
        height= 1,
        fg="blue",
        command= no_btn['command'],
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
    text = 'result',
    width= 20,
)

random_password_lbl.grid(row= row_num+1, column=5, columnspan=20)
default_label_featurs = [
    {
        "text": "Default ==> Yes",
    },
    
    {
        "text": "Default ==> No",
    },
        
    {
        "text": "Default ==> Yes",
    },
    
    {
        "text": "Default ==> Yes",
    },
        
    {
        "text": "Default ==> No",
    },
            
    {
        "text": "Default ==> 8",
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
    label_objs.grid(row=row_num, column=30, columnspan=10,)
    row_num += 1
    
def generate_random_password_gui(event = "<Return>"):
    on_options = []
    for option in defual_setting_dict:
        if defual_setting_dict[option] == True:
            on_options.append(option)
    try:
        length = length_ent.get()
        if  int(length) > 20 or int(length) < 4:
            raise LengthLimitError
        result = generate_random_password(on_options, int(length))
        
    except ValueError:
        result = generate_random_password(on_options, 8)
    
    except LengthLimitError:
        random_password_lbl['text'] = "length between 4 to 20."
    
    for label in label_created_list:
        if (label['text'][:-1])in on_options:
            label['fg'] = 'green'
        else:
            if label['text'] == "Random_Password:" or label['text'] == "Length:":
                label['fg'] = 'black'
            else:
                label['fg'] = 'red'
    
    with open("passwords.txt", 'a') as file:
        file.write(f"\n{result}\n")
        file.write("\n--------------------------------------------\n")     
        random_password_lbl['text'] = result
    
def restart_program(*args):
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
run_btn = tk.Button(
    master=window,
    width=4,
    height=1,
    text="Run",
    fg="#009ACD",
    command=generate_random_password_gui,
)
run_btn.grid(row=row_num, column=27, columnspan=10)

quit_btn = tk.Button(
    master=window,
    width=4,
    height=1,
    text="Quit",
    fg= 'red',
    command=quit,
)
quit_btn.grid(row=row_num, column=32, columnspan=10)


    
restart_btn = tk.Button(
    master=window,
    width=4,
    height=1,
    fg = "blue",
    text = "reset",
    command= restart_program
)

restart_btn.grid(row=row_num, column=37, columnspan=10)

window.bind("<Return>", generate_random_password_gui)
window.bind("<q>", quit)
window.bind("<r>", restart_program)

window.mainloop()